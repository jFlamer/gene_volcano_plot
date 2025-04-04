# Gene Volcano Plot Web App

This Flask-based web application generates an interactive volcano plot and box plots using data from an Excel file.

## Prerequisites

Requirements:
- Python (>=3.8)
- pip
- Miniconda or Anaconda (optional, for virtual environment management)

### Required Python Packages

In your conda virtual environment(suggested):
```sh
conda create -n flEnv
conda activate flEnv
```
Install dependencies by running:

```sh
pip install flask pandas numpy matplotlib plotly openpyxl
```

or if using conda:

```sh
conda install -c conda-forge flask pandas numpy matplotlib plotly openpyxl
```

## Running the Application

1. Clone or download the repository containing this project.
2. Navigate to the project directory:

```sh
cd /path/to/project
```

3. Start the Flask app:

```sh
python app.py
```

Alternatively (from *app.py* level):
```sh
flask run
```

4. Open your browser and go to:

```
http://127.0.0.1:5000/plot
```

## Features

- **Volcano Plot**: Displays a scatter plot of log fold change vs. adjusted p-value.
- **Box Plot**: Allows visual comparison of protein concentrations for specific genes across young and old donors.
- **Interactive UI**: Hovering over points reveals gene information.


