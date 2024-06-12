from flask import Flask, render_template, request
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import plotly.express as px

app = Flask(__name__)

# Load data from CSV file.
data = pd.read_csv('static/Sources/merged_results.csv')

# Conversion from country codes to full names for clarity in the map and other visualizations.
country_conversion = {
    'ARG': 'Argentina',
    'AUS': 'Australia',
    'AUT': 'Austria',
    'BEL': 'Belgium',
    'BRA': 'Brazil',
    'CAN': 'Canada',
    'COL': 'Colombia',
    'ESP': 'Spain',
    'FIN': 'Finland',
    'FRA': 'France',
    'GBR': 'United Kingdom',
    'GER': 'Germany',
    'ITA': 'Italy',
    'MEX': 'Mexico',
    'MON': 'Monaco',
    'NED': 'Netherlands',
    'NZL': 'New Zealand',
    'POL': 'Poland',
    'RSA': 'South Africa',
    'SUI': 'Switzerland',
    'SWE': 'Sweden',
    'USA': 'United States',
    'VEN': 'Venezuela'
}
data['Nationality'] = data['Nationality'].map(country_conversion)

# Geographic coordinates for the countries involved, used in the map pins.
nationality_coordinates = {
    'Argentina': (-38.4161, -63.6167),
    'Australia': (-25.2744, 133.7751),
    'Austria': (47.5162, 14.5501),
    'Belgium': (50.5039, 4.4699),
    'Brazil': (-14.2350, -51.9253),
    'Canada': (56.1304, -106.3468),
    'Colombia': (4.5709, -74.2973),
    'France': (46.2276, 2.2137),
    'Germany': (51.1657, 10.4515),
    'Italy': (41.8719, 12.5674),
    'Mexico': (23.6345, -102.5528),
    'Monaco': (43.7384, 7.4246),
    'Netherlands': (52.1326, 5.2913),
    'New Zealand': (-40.9006, 174.8860),
    'Poland': (51.9194, 19.1451),
    'South Africa': (-30.5595, 22.9375),
    'Spain': (40.4637, -3.7492),
    'Sweden': (60.1282, 18.6435),
    'Switzerland': (46.8182, 8.2275),
    'United Kingdom': (54.5260, -3.4350),
    'United States': (37.0902, -95.7129),
    'Venezuela': (6.4238, -66.5897)
}

def create_popup_content(nationality, drivers):
    total_wins = drivers['Total_Victories_Driver'].sum()
    driver_list = "<br>".join([f"{row['Driver']}: {row['Total_Victories_Driver']}" for _, row in drivers.iterrows()])
    return f"<strong>{nationality}</strong><br>Total Wins: {total_wins}<br>{driver_list}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def map_view():
    f1_map = folium.Map(location=[0, 0], zoom_start=2)
    marker_cluster = MarkerCluster().add_to(f1_map)

    for nationality, group in data.groupby('Nationality'):
        if nationality in nationality_coordinates:
            lat, lon = nationality_coordinates[nationality]
            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(create_popup_content(nationality, group), max_width=450)
            ).add_to(marker_cluster)

    map_html = f1_map._repr_html_()
    return render_template('map.html', map_html=map_html)

@app.route('/drivers')
def drivers_view():
    fig = px.bar(data, x='Driver', y='Total_Victories_Driver', 
                 title='Total Wins by Driver', 
                 color='Total_Victories_Driver', 
                 color_continuous_scale='Viridis',
                 labels={'Total_Victories_Driver': 'Total Wins', 'Driver': 'Driver'},
                 template='plotly_white')
    fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGrey')))
    fig.update_layout(title_font_size=22, title_x=0.5, 
                      xaxis_title='', yaxis_title='Total Wins',
                      plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    graph_html = fig.to_html(full_html=False)
    return render_template('drivers.html', graph_html=graph_html)

@app.route('/teams')
def teams_view():
    team_victories_df = data.groupby('Team', as_index=False)['Total_Victories_Team'].mean()
    fig = px.bar(team_victories_df, x='Team', y='Total_Victories_Team',
                 title='Total Wins by Team', 
                 color='Total_Victories_Team', 
                 color_continuous_scale='Bluered',
                 labels={'Total_Victories_Team': 'Total Wins', 'Team': 'Team'},
                 template='plotly_white')
    fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGrey')))
    fig.update_layout(title_font_size=22, title_x=0.5, 
                      xaxis_title='', yaxis_title='Total Wins',
                      plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    graph_html = fig.to_html(full_html=False)
    return render_template('teams.html', graph_html=graph_html)

@app.route('/top_pilots', methods=['GET', 'POST'])
def top_pilots_view():
    N = 10
    if request.method == 'POST':
        N = int(request.form['topN'])

    top_pilots = data.groupby('Driver').agg({'Total_Victories_Driver': 'sum'}).reset_index().sort_values(by='Total_Victories_Driver', ascending=False).head(N)
    fig = px.bar(top_pilots, x='Driver', y='Total_Victories_Driver', 
                 title=f'Top {N} Pilots by Total Victories', 
                 color='Total_Victories_Driver', 
                 color_continuous_scale='Cividis',
                 labels={'Total_Victories_Driver': 'Total Wins', 'Driver': 'Driver'},
                 template='plotly_white')
    fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGrey')))
    fig.update_layout(
        title_font_size=22, title_x=0.5, 
        xaxis_title='', yaxis_title='Total Wins',
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='black')
    )
    graph_html = fig.to_html(full_html=False)
    return render_template('top_pilots.html', graph_html=graph_html, topN=N)

if __name__ == '__main__':
    app.run(debug=True)
