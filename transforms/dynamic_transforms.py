# --- Start of LLM-Generated Code ---

import pandas as pd

def apply_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters the DataFrame for 'Bioabfall FFM' waste type with a net weight greater than 1000 KG.
    """
    # Filter for waste type 'Bioabfall FFM'
    waste_type_filter = df['WASTE_TYPE_TXT'] == 'Bioabfall FFM'
    
    # Filter for net weight greater than 1000 KG
    weight_filter = df['NET_WEIGHT'] > 1000
    
    # Apply both filters
    transformed_df = df[waste_type_filter & weight_filter].copy()
    
    return transformed_df

TRANSFORM_DOCUMENTATION = """
## Bio-waste and Weight Filter Transformation

This transformation filters the dataset to isolate specific records based on two criteria:

1.  **Waste Type**: It selects only the records where the `WASTE_TYPE_TXT` is exactly 'Bioabfall FFM'.
2.  **Net Weight**: It further filters these records to include only those where the `NET_WEIGHT` is greater than 1000 KG.

The resulting dataset contains only high-volume collections of 'Bioabfall FFM'.
"""
