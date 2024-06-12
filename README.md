# Formula 1 Data Visualizer

## Overview
Welcome to the Formula 1 Data Visualizer! This application provides an engaging and insightful way to explore the vast and exciting world of Formula 1 racing. Designed with both casual fans and dedicated enthusiasts in mind, this tool harnesses the power of data visualization to bring the statistics and stories of Formula 1 to life.

This project aims to tell a compelling story through data visualizations. By leveraging various libraries and tools, we have created interactive and insightful visualizations that allow users to explore and understand the dataset in depth. The project is designed to meet specific requirements and demonstrate proficiency in data handling, visualization, and interactivity.

## Project Purpose

The purpose of this project is to showcase the power of data visualization in conveying complex information in an accessible and engaging way. We aim to provide users with an interactive experience that allows them to delve into the data, discover patterns, and draw meaningful insights.

## The main features include
- **Global Map of Drivers**: Explore a map that shows the geographical distribution of F1 drivers and their victories.
- **Total Wins by Driver**: Visualize the total number of wins by each Formula 1 driver.
- **Total Wins by Team**: See the total number of races won by each team in F1 history.
- **Top N Pilots by Total Victories**: Select and view the top pilots by total victories.


## Instructions

### How to Use and Interact with the Project

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/f1-data-visualizer.git
    cd f1-data-visualizer
    ```

2. **Set Up the Environment**:
    - Ensure you have Python installed.
    - Install the necessary dependencies:
        ```bash
        pip install flask pandas folium plotly
        ```

3. **Prepare the Data**:
    - Ensure `merged_results.csv` is in the `Sources` folder.

4. **Run the Application**:
    ```bash
    python app.py
    ```

5. **Access the Application**:
    - Open your web browser and go to `http://127.0.0.1:5000/`.

### Interacting with the Application

- **Global Map of Drivers**: Navigate to the 'Map' section to explore the global distribution of drivers. Click on any pin to see detailed information about drivers from that country and their total wins.
- **Total Wins by Driver**: Navigate to the 'Drivers' section to view a bar chart showing the total wins by each driver.
- **Total Wins by Team**: Navigate to the 'Teams' section to view a bar chart of the total races won by each team.
- **Top N Pilots by Total Victories**: Navigate to the 'Top Pilots' section to select the number of top pilots you want to see and view a ranked list of drivers by their total victories.

## Ethical Considerations
In developing the Formula 1 Data Visualizer, several efforts were made to address ethical considerations:
- **Data Accuracy and Integrity**: Ensuring the accuracy and integrity of the data presented is crucial. Misrepresenting statistics can lead to misinformation and potentially damage the reputations of drivers and teams. We commit to using reliable data sources and continuously verifying the accuracy of the information presented in our application.
- **Privacy and Consent**: Respecting the privacy of individuals whose data is being visualized is paramount. Although the data used is typically publicly available, it is essential to handle it responsibly. We only use publicly available data and ensure that our visualizations respect the privacy of the individuals involved.
- **Bias and Fair Representation**: Data visualizations should strive to be unbiased and represent the data fairly. It is easy to inadvertently introduce bias through the choice of metrics or presentation style. We aim for neutrality and objectivity in our visualizations, providing a balanced view of the data without favoritism or prejudice.
- **Impact on Stakeholders**: Understanding how the visualized data might impact stakeholders, including drivers, teams, fans, and sponsors, is essential. We design our visualizations to celebrate achievements and provide constructive insights, fostering a positive and respectful discourse around Formula 1.

### Data Sources
- The data used in this project is sourced from publicly available Formula 1 race results databases and repositories.

### Code References
- The visualizations were created using the [Plotly](https://plotly.com/python/) library.
- The interactive map was implemented using [Folium](https://python-visualization.github.io/folium/).
- The web framework used for this project is [Flask](https://flask.palletsprojects.com/).
- Parts of the code were generated with the assistance of [ChatGPT](https://openai.com/chatgpt), an AI language model developed by OpenAI.