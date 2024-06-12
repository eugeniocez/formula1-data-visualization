from flask import Flask, render_template
import pandas as pd
import folium
import plotly.express as px

app = Flask(__name__, static_folder="static")

# Read the CSV data
data = pd.read_csv('static/Sources/merged_results.csv')

# Nationality to coordinates mapping
nationality_coordinates = {
    'United Kingdom': (54.5260, -3.7038),
    'France': (46.2276, 2.2137),
    'Germany': (51.1657, 10.4515),
    'Italy': (41.8719, 12.5674),
    'Brazil': (-14.2350, -51.9253),
    'Australia': (-25.2744, 133.7751),
    'New Zealand': (-40.9006, 174.8860),
    'Sweden': (60.1282, 18.6435),
    'United States': (37.0902, -95.7129),
    'Mexico': (23.6345, -102.5528),
    'Switzerland': (46.8182, 8.2275),
    'Belgium': (50.5039, 4.4699),
    'Austria': (47.5162, 14.5501),
    'South Africa': (-30.5595, 22.9375),
    'Argentina': (-38.4161, -63.6167),
    'Canada': (56.1304, -106.3468),
    'Finland': (61.9241, 25.7482),
    'Colombia': (4.5709, -74.2973),
    'Spain': (40.4637, -3.7492),
    'Poland': (51.9194, 19.1451),
    'Venezuela': (6.4238, -66.5897),
    'Netherlands': (52.1326, 5.2913),
    'Monaco': (43.7384, 7.4246)
}

# Country code to full name mapping
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map_view():
    f1_map = folium.Map(location=[0, 0], zoom_start=2)
    
    grouped = data.groupby(['Nationality', 'Driver']).agg({'Total_Victories_Driver': 'sum'}).reset_index()
    drivers_by_nationality = grouped.groupby('Nationality').apply(lambda x: x.to_dict(orient='records')).to_dict()

    def create_popup_content(drivers):
        total_wins = sum(driver['Total_Victories_Driver'] for driver in drivers)
        driver_details = "\n".join([f"{driver['Driver']}: {driver['Total_Victories_Driver']} wins" for driver in drivers])
        return f"Total Wins for {drivers[0]['Nationality']}:\n{total_wins}\n{driver_details}"

    for nationality, drivers in drivers_by_nationality.items():
        if nationality in nationality_coordinates:
            lat, lon = nationality_coordinates[nationality]
            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(create_popup_content(drivers), parse_html=False, max_width=450)
            ).add_to(f1_map)

    map_html = f1_map._repr_html_()
    return render_template('map.html', map_html=map_html)

@app.route('/drivers')
def drivers_view():
    fig = px.bar(data, x='Driver', y='Total_Victories_Driver', title='Total Wins by Driver')
    graph_html = fig.to_html(full_html=False)
    return render_template('drivers.html', graph_html=graph_html)

@app.route('/teams')
def teams_view():
    # Group by 'Team' and mean the 'Total Races won by team' to ensure unique values
    team_victories_df = data.groupby('Team', as_index=False)['Total Races won by team'].mean()
    
    # Create the bar chart with the grouped data
    fig = px.bar(team_victories_df, x='Team', y='Total Races won by team', title='Total Wins by Team')
    
    # Convert the figure to HTML
    graph_html = fig.to_html(full_html=False)
    
    # Render the template with the graph
    return render_template('teams.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
