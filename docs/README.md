# Data Quality Automation Project

## Project Overview
This project focuses on automating data quality management for tabular datasets using Python. It leverages profiling, validation, and cleaning techniques to improve the reliability and usability of structured data.

Our primary dataset for exploration and experimentation is the Airbnb Open Data, which includes information on New York City homestays.

## Current Features
1. **Data Profiling**:
   - Summarize data statistics.
   - Identify missing values and outliers.
2. **Validation**:
   - Verify data integrity.
   - Apply basic cleaning strategies.
3. **Processing**:
   - Transform raw data into a clean and structured format for downstream use.

## Directory Structure

dq_automation/ ├── data/ │ ├── raw/ │ │ ├── Airbnb_Open_Data.csv │ │ ├── Airbnb_Open_Data_Dictionary.xlsx │ ├── processed/ ├── notebooks/ │ ├── exploratory.ipynb ├── src/ │ ├── main.py │ ├── profiling.py │ ├── validation.py │ ├── utils.py ├── tests/ │ ├── test_validation.py ├── docs/ │ ├── README.md │ ├── references.md │ ├── slides/ │ │ ├── rekatsinas_lecture.pdf │ ├── paper/ │ │ ├── draft.pdf ├── .gitignore ├── LICENSE ├── requirements.txt