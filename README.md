# GDP Analysis and Visualization Dashboard
This Software Design and Analysis Project is a Python-based data analysis and visualization system that processes World Bank GDP Data and generates multiple data representation visuals for both region-wise and country-wise data selection. The entire workflow is derived from a JSON configuration file which makes the system flexible and reusable.

## Project Objectives
- Load, Clean and FIlter GDP Data according to JSON file
- Transform GDP CSV file data into analysis-prepared data
- Apply statistical operations according to user preferences
- Visualize GDP Trends
    * Region-wise Representation (Bar Graph, Pie Chart, Heatmap)
    * Country-wise Representation (Line Plot, Scatter Plot, Histogram)
- Control execution using a validated JSON configuration file

## Project Structure
```text
SDA-Project/
│
├── maindata.py
├── load_data.py
├── cleaner.py
├── transform.py
├── load_json.py
├── validate_json.py
├── filter_by_region.py
├── filter_by_country.py
├── Process.py
├── visualize_regions.py
├── visualize_countries.py
├── config.json
├── requirements.txt
└── README.md
```
## Data Processing Workflow
### 1. Load Data
    - GDP is loaded from a CSV file 
### 2. Clean Data
    - Handles missing GDP values
    - Ensures numeric consistency
    - Prevents 
