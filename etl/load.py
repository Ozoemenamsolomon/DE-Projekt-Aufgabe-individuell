import pandas as pd
import os

def load_data(dataframe: pd.DataFrame, destination_path: str):
    """
    Saves a DataFrame to a specified destination CSV file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to save.
        destination_path (str): The path to the output CSV file.
    """
    if not isinstance(dataframe, pd.DataFrame):
        print("Error: Input is not a pandas DataFrame.")
        return

    try:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        dataframe.to_csv(destination_path, index=False)
        print(f"Successfully loaded data to '{destination_path}'")
    except Exception as e:
        print(f"An error occurred while loading data to '{destination_path}': {e}")

if __name__ == '__main__':
    # Example usage:
    # This part will not run in the main pipeline but can be used for testing.
    print("Running load.py example...")
    example_df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': ['A', 'B', 'C']
    })
    load_data(example_df, 'data/example_output.csv')
