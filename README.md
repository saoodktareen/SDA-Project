# GDP Analysis and Visualization Dashboard
This Software Design and Analysis Project is a Python-based data analysis and visualization system that processes World Bank GDP Data and generates multiple data representation visuals for both region-wise and country-wise data selection. The entire workflow is derived from a JSON configuration file which makes the system flexible and reusable.

# Project Objectives
- Load, Clean and FIlter GDP Data according to JSON file
- Transform GDP csv file data into analysis-prepared data
- Apply statistical operations according to user preferences
- Visualize GDP Trends
    * Region-wise Representation (Bar Graph, Pie Chart, Heatmap)
    * Country-wise Representation (Line Plot, Scatter Plot, Histogram)
- Control execution using a validated JSON configuration file

# Project Structure
SDA-Project/
│
├── maindata.py # Main entry point of the project
├── load_data.py # Loads GDP CSV data
├── cleaner.py # Cleans and validates raw data
├── transform.py # Converts data to long format
├── load_json.py # Loads JSON configuration
├── validate_json.py # Validates JSON keys & values
├── filter_by_region.py # Filters data for selected regions
├── filter_by_country.py # Filters data for selected countries
├── Process.py # Handles GDP aggregation logic
│
├── visualize_regions.py # Region-wise visualizations
├── visualize_countries.py # Country-wise visualizations
│
├── config.json # User-defined configuration file
├── requirements.txt # Required Python libraries
└── README.md # Project documentation