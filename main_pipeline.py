import pandas as pd
import os
from etl.extract import extract_and_merge_data
from etl.load import load_data
from transforms.dynamic_transforms import apply_transform, TRANSFORM_DOCUMENTATION

# Define file paths
MERGED_DATA_PATH = 'data/merged_data.csv'
TRANSFORMED_DATA_PATH = 'data/transformed_output.csv'

def run_pipeline():
    """
    Orchestrates the entire ETL pipeline.
    """
    print("--- Starting ETL Pipeline ---")

    # --- EXTRACT ---
    # Check if the merged data file already exists. If not, run the extraction process.
    if not os.path.exists(MERGED_DATA_PATH):
        print(f"'{MERGED_DATA_PATH}' not found. Running the extraction and merge process now.")
        extract_and_merge_data(output_path=MERGED_DATA_PATH)
    
    # Load the clean, merged data
    print(f"Loading data from '{MERGED_DATA_PATH}'...")
    try:
        source_df = pd.read_csv(MERGED_DATA_PATH)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: Could not find '{MERGED_DATA_PATH}' even after attempting to create it.")
        return
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return

    # --- TRANSFORM ---
    print("\n--- Applying Dynamic Transformation ---")
    transformed_df = apply_transform(source_df)
    print("Transformation applied.")

    # Display the documentation for the applied transformation
    print("\n--- Transformation Documentation ---")
    print(TRANSFORM_DOCUMENTATION)
    print("------------------------------------")

    # --- LOAD ---
    print("\n--- Loading Transformed Data ---")
    load_data(transformed_df, TRANSFORMED_DATA_PATH)

    print("\n--- ETL Pipeline Completed Successfully ---")

if __name__ == '__main__':
    run_pipeline()
