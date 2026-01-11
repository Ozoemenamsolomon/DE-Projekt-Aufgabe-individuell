import os
import pandas as pd
import glob
import sys

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def extract_and_merge_data(raw_data_path='Daten', output_path='data/merged_data.csv'):
    """
    Loads all daily raw CSVs, merges them into a single DataFrame,
    performs necessary cleaning and data type conversion, and saves it
    to a specified location.

    Args:
        raw_data_path (str): The path to the directory containing the daily data folders.
        output_path (str): The path to save the merged CSV file.

    Returns:
        pd.DataFrame: The fully merged and cleaned DataFrame.
    """
    print("Starting data extraction and merging...")
    daily_folders = [d for d in glob.glob(os.path.join(raw_data_path, '*')) if os.path.isdir(d)]

    if not daily_folders:
        print(f"Error: No data folders found in '{raw_data_path}'. Please check the path.")
        return pd.DataFrame()

    all_data_dfs = []
    for folder in daily_folders:
        try:
            stammdaten_df = pd.read_csv(os.path.join(folder, '01_Stammdaten.csv'), sep=';', on_bad_lines='skip', low_memory=False)
            auftragsdaten_df = pd.read_csv(os.path.join(folder, '02_Auftragsdaten.csv'), sep=';', on_bad_lines='skip', low_memory=False)
            waage_df = pd.read_csv(os.path.join(folder, '03_Waage.csv'), sep=';', on_bad_lines='skip', low_memory=False)
            kippsignale_df = pd.read_csv(os.path.join(folder, '04_Kippsignale.csv'), sep=';', on_bad_lines='skip', low_memory=False)

            # Perform merges
            auftrag_waage_df = pd.merge(auftragsdaten_df, waage_df, on='ORDERNR', how='inner')
            auftrag_waage_kipp_df = pd.merge(auftrag_waage_df, kippsignale_df, on='ORDERNR', how='inner', suffixes=('_auftrag', '_kipp'))
            
            if 'ROUTE_auftrag' in auftrag_waage_kipp_df.columns:
                auftrag_waage_kipp_df['ROUTE'] = auftrag_waage_kipp_df['ROUTE_auftrag']

            stammdaten_unique_route_df = stammdaten_df.drop_duplicates(subset=['ROUTE'])
            merged_df = pd.merge(auftrag_waage_kipp_df, stammdaten_unique_route_df, on='ROUTE', how='left')
            all_data_dfs.append(merged_df)
        except FileNotFoundError as e:
            print(f"Warning: Skipping folder {folder} due to missing file: {e.filename}")
        except Exception as e:
            print(f"An error occurred while processing folder {folder}: {e}")

    if not all_data_dfs:
        print("Error: No data could be loaded. Merged DataFrame is empty.")
        return pd.DataFrame()

    final_df = pd.concat(all_data_dfs, ignore_index=True)

    # --- Static Data Cleaning and Type Conversion ---
    final_df['NET_WEIGHT'] = pd.to_numeric(final_df['NET_WEIGHT'], errors='coerce')
    final_df['GROSS_WDATE'] = pd.to_datetime(final_df['GROSS_WDATE'], format='%Y%m%d', errors='coerce')
    final_df['DATE_CREATE'] = pd.to_datetime(final_df['DATE_CREATE'], format='%Y%m%d', errors='coerce')
    
    # Coalesce date columns if necessary
    final_df['EVENT_DATE'] = final_df['GROSS_WDATE'].fillna(final_df['DATE_CREATE'])
    
    # Drop original date columns if they are no longer needed
    final_df = final_df.drop(columns=['GROSS_WDATE', 'DATE_CREATE'])

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Save the merged data
    final_df.to_csv(output_path, index=False)
    print(f"Successfully extracted and merged data to '{output_path}'")

    return final_df

if __name__ == '__main__':
    # This allows the script to be run directly to generate the merged data file.
    extract_and_merge_data()
