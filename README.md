# Automated Competition Analysis Pipeline

## Overview
This project collects competitor data, stores it in SQLite, analyzes it, and displays it in a Streamlit dashboard.

## Current MVP
- Stock scraper
- SQLite ETL pipeline
- KPI calculations
- Streamlit dashboard

## Setup
1. Clone the repository
2. Create a virtual environment
3. Install requirements
4. Add your API key to `.env`
5. Run ETL
6. Launch Streamlit

## Install
```bash
pip install -r requirements.txt
```

## Run ETL
```bash
python -m etl.pipeline_runner
```

## Run dashboard
```bash
streamlit run dashboard/app.py
```