import os
from src.profiling import profiling
from src.validation import validate_data

# Define paths
RAW_DATA_PATH = "../data/raw/Airbnb_Open_Data.csv"
PROCESSED_DATA_PATH = "../data/processed/processed_airbnb_data.csv"

def main():
    print("Starting the data quality automation process...")
    
    # Step 1: Perform data profiling
    profiling(RAW_DATA_PATH)

    # Step 2: Perform data validation and cleaning
    validate_data(RAW_DATA_PATH, PROCESSED_DATA_PATH)

    print(f"Data processing complete. Cleaned data saved at: {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    main()
