import os
import pandas as pd
import glob

def load_and_merge_data(data_path='Daten'):
    """
    Loads, merges, and preprocesses data from the specified data path.

    Args:
        data_path (str): The path to the root data directory.

    Returns:
        pandas.DataFrame: A merged and preprocessed DataFrame.
    """
    # Find all daily data folders
    daily_folders = [d for d in glob.glob(os.path.join(data_path, '*')) if os.path.isdir(d)]

    all_data_dfs = []

    for folder in daily_folders:
        try:
            # Load data from each CSV file
            stammdaten_df = pd.read_csv(os.path.join(folder, '01_Stammdaten.csv'), sep=';', on_bad_lines='skip', low_memory=False)
            auftragsdaten_df = pd.read_csv(os.path.join(folder, '02_Auftragsdaten.csv'), sep=';', on_bad_lines='skip', low_memory=False)
            waage_df = pd.read_csv(os.path.join(folder, '03_Waage.csv'), sep=';', on_bad_lines='skip', low_memory=False)
            kippsignale_df = pd.read_csv(os.path.join(folder, '04_Kippsignale.csv'), sep=';', on_bad_lines='skip', low_memory=False)

            # Merge the dataframes
            # 1. Merge auftragsdaten with waage on ORDERNR
            auftrag_waage_df = pd.merge(auftragsdaten_df, waage_df, on='ORDERNR', how='inner')

            # 2. Merge the result with kippsignale on ORDERNR
            auftrag_waage_kipp_df = pd.merge(auftrag_waage_df, kippsignale_df, on='ORDERNR', how='inner', suffixes=('_auftrag', '_kipp'))
            
            # After the merge, pandas adds suffixes to columns with the same name.
            # We need to restore the 'ROUTE' column for the next merge.
            # We'll use the route from auftragsdaten as the source of truth.
            if 'ROUTE_auftrag' in auftrag_waage_kipp_df.columns:
                auftrag_waage_kipp_df['ROUTE'] = auftrag_waage_kipp_df['ROUTE_auftrag']

            # 3. Merge the result with stammdaten on ROUTE
            # To avoid issues with many-to-many joins, we'll drop duplicates from stammdaten based on ROUTE
            stammdaten_unique_route_df = stammdaten_df.drop_duplicates(subset=['ROUTE'])
            merged_df = pd.merge(auftrag_waage_kipp_df, stammdaten_unique_route_df, on='ROUTE', how='left')

            all_data_dfs.append(merged_df)
        except FileNotFoundError as e:
            print(f"Warning: Skipping folder {folder} due to missing file: {e.filename}")
        except Exception as e:
            print(f"An error occurred while processing folder {folder}: {e}")


    if not all_data_dfs:
        print("No data was loaded. Please check the data path and file structure.")
        return pd.DataFrame()

    # Concatenate data from all days
    final_df = pd.concat(all_data_dfs, ignore_index=True)

    # Basic data cleaning
    final_df['NET_WEIGHT'] = pd.to_numeric(final_df['NET_WEIGHT'], errors='coerce')
    final_df['GROSS_WDATE'] = pd.to_datetime(final_df['GROSS_WDATE'], format='%Y%m%d', errors='coerce')


    return final_df

def get_total_waste_weight_per_day(merged_df: pd.DataFrame):
    """
    Calculates the total weight of waste collected per day.

    Args:
        merged_df (pd.DataFrame): The merged and preprocessed DataFrame.

    Returns:
        pandas.Series: A Series with the total waste weight per day.
    """
    if 'GROSS_WDATE' not in merged_df.columns or 'NET_WEIGHT' not in merged_df.columns:
        return "Required columns ('GROSS_WDATE', 'NET_WEIGHT') not found."
    
    daily_weight = merged_df.groupby('GROSS_WDATE')['NET_WEIGHT'].sum().reset_index()
    daily_weight = daily_weight.rename(columns={'GROSS_WDATE': 'Date', 'NET_WEIGHT': 'TotalWeight'})

    return daily_weight

def get_most_common_waste_type(merged_df: pd.DataFrame):
    """
    Finds the most common waste type.

    Args:
        merged_df (pd.DataFrame): The merged and preprocessed DataFrame.

    Returns:
        pandas.Series: A Series with the counts of each waste type.
    """
    if 'WASTE_TYPE_TXT' not in merged_df.columns:
        return "Required column 'WASTE_TYPE_TXT' not found."
    return merged_df['WASTE_TYPE_TXT'].value_counts()

def get_tipping_signals_per_route(merged_df: pd.DataFrame):
    """
    Counts the number of tipping signals per route.

    Args:
        merged_df (pd.DataFrame): The merged and preprocessed DataFrame.

    Returns:
        pandas.Series: A Series with the number of tipping signals per route.
    """
    if 'ROUTE' not in merged_df.columns:
        return "Required column 'ROUTE' not found."
    return merged_df['ROUTE'].value_counts()

if __name__ == "__main__":
    # Load and merge data
    print("Starting ETL pipeline...")
    merged_data = load_and_merge_data()

    if not merged_data.empty:
        print("ETL pipeline completed successfully.")
        
        # Answer the three questions
        print("\n1. What is the total weight of waste collected per day?")
        total_weight_per_day = get_total_waste_weight_per_day(merged_data)
        print(total_weight_per_day)

        print("\n2. What is the most common waste type?")
        most_common_waste = get_most_common_waste_type(merged_data)
        print(most_common_waste)

        print("\n3. How many tipping signals are there per route?")
        signals_per_route = get_tipping_signals_per_route(merged_data)
        print(signals_per_route)
    else:
        print("Could not generate insights because no data was loaded.")
