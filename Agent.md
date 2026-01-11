## Data Description and Usage Guide for LLMs

This document provides a detailed description of the waste management dataset, designed to be used by a Large Language Model (LLM) to understand the data and generate analytical functions.

### Goal

The dataset contains logistical data for a waste management company. The goal is to analyze waste collection operations, including orders, routes, weights, and collection events (tipping).

### File Structure

The data is organized by day into separate folders. Each folder contains four CSV files with a semicolon (`;`) as a separator.

```
Daten/
└── yyyymmdd/
    ├── 01_Stammdaten.csv
    ├── 02_Auftragsdaten.csv
    ├── 03_Waage.csv
    └── 04_Kippsignale.csv
```

---

### Data Dictionary

Below is a detailed description of each file and its columns.

#### 1. `01_Stammdaten.csv` (Master Data)

This file contains master data about objects, containers, routes, and locations.

| Column | Description | Data Type | Example |
| :--- | :--- | :--- | :--- |
| **ROUTE** | **Unique identifier for a collection route.** (Primary Key for joining) | `string` | `EW1403` |
| **TIDNR** | Unique identifier for a container (Tonne). | `string` | `12345678` |
| **EQUNR** | Unique identifier for a piece of equipment. | `string` | `87654321` |
| WASTE_TYPE_TXT | Text description of the waste type. | `string` | `gemischte Siedlungsabfälle` |
| BEH_TYPE_TXT | Text description of the container type. | `string` | `1100L` |
| STPL_STREET | Street name of the container's location. | `string` | `Musterstraße` |
| STPL_CITY1 | City of the container's location. | `string` | `Frankfurt am Main` |
| ... | (Other semi-static master data columns) | | |

#### 2. `02_Auftragsdaten.csv` (Order Data)

This file contains information about collection orders.

| Column | Description | Data Type | Example |
| :--- | :--- | :--- | :--- |
| **ORDERNR** | **Unique identifier for a collection order.** (Primary Key for joining) | `string` | `00000000000002629397` |
| **ROUTE** | Identifier for the route this order belongs to. (Foreign Key to `Stammdaten`) | `string` | `EN0132` |
| ORDER_DATE | The date the order was created. | `Date (YYYYMMDD)` | `20250409` |

#### 3. `03_Waage.csv` (Weight Data)

This file contains weight measurements associated with orders.

| Column | Description | Data Type | Example |
| :--- | :--- | :--- | :--- |
| **ORDERNR** | Identifier for the order being weighed. (Foreign Key to `Auftragsdaten`) | `string` | `00000000000002629397` |
| NET_WEIGHT | The net weight of the collected waste. | `float` | `10920` |
| WEIGHT_UNIT | The unit of the weight measurement. | `string` | `KG` |
| GROSS_WDATE | The date of the gross weighing. | `Date (YYYYMMDD)` | `20250408` |
| ENTSORGER | The disposal company. | `string` | `RMB` |

#### 4. `04_Kippsignale.csv` (Tipping Signal Data)

This file logs the actual collection events (tipping of containers).

| Column | Description | Data Type | Example |
| :--- | :--- | :--- | :--- |
| **ORDERNR** | Identifier for the order associated with the tip. (Foreign Key to `Auftragsdaten`) | `string` | `00000000000002629397` |
| **ROUTE** | The route on which the tipping occurred. (Foreign Key to `Stammdaten`) | `string` | `EN0132` |
| **TIDNR** | Identifier for the container that was tipped. (Foreign Key to `Stammdaten`) | `string` | `5689421` |
| KIPPE | A signal indicating a tipping event (likely `1` or `true`). | `integer` | `1` |
| LONGITUDE | GPS longitude of the tipping event. | `float` | `8.682127` |
| LATITUDE | GPS latitude of the tipping event. | `float` | `50.110924` |
| DATE_CREATE | Date the tipping signal was created. | `Date (YYYYMMDD)` | `20250409` |
| TIME_CREATE | Time the tipping signal was created. | `Time (HHMMSS)` | `140331` |

---

### Entity-Relationship Model (Join Logic)

To create a comprehensive dataset for analysis, the files should be merged (joined) as follows:

1.  **Orders and Weights**: Join `02_Auftragsdaten.csv` with `03_Waage.csv` on the `ORDERNR` column.
2.  **Add Tipping Signals**: Join the result with `04_Kippsignale.csv`, also on `ORDERNR`.
3.  **Add Master Data**: Join the result with `01_Stammdaten.csv` on the `ROUTE` column. This adds rich descriptive data like waste type text and location details.

**Note on Joins:** When merging, be aware that `ROUTE` exists in `Auftragsdaten` and `Kippsignale`. Use the `ROUTE` from `Auftragsdaten` as the primary key (`ROUTE_auftrag` if suffixes are added by pandas).

---

### Example Questions and Python Functions

Here are examples of how to answer common questions about the data using Python and Pandas. An LLM should use these as a template for generating new functions.

#### ETL Base Function

First, all data should be loaded and merged using a function like this. This merged DataFrame is the input to all analysis functions.

```python
import pandas as pd
import os
import glob

def load_and_merge_data(data_path='Daten'):
    """
    Loads and merges all daily CSVs into a single, cleaned pandas DataFrame.
    """
    daily_folders = [d for d in glob.glob(os.path.join(data_path, '*')) if os.path.isdir(d)]
    all_data_dfs = []

    for folder in daily_folders:
        try:
            stammdaten_df = pd.read_csv(os.path.join(folder, '01_Stammdaten.csv'), sep=';', on_bad_lines='skip', low_memory=False)
            auftragsdaten_df = pd.read_csv(os.path.join(folder, '02_Auftragsdaten.csv'), sep=';', on_bad_lines='skip', low_memory=False)
            waage_df = pd.read_csv(os.path.join(folder, '03_Waage.csv'), sep=';', on_bad_lines='skip', low_memory=False)
            kippsignale_df = pd.read_csv(os.path.join(folder, '04_Kippsignale.csv'), sep=';', on_bad_lines='skip', low_memory=False)

            auftrag_waage_df = pd.merge(auftragsdaten_df, waage_df, on='ORDERNR', how='inner')
            auftrag_waage_kipp_df = pd.merge(auftrag_waage_df, kippsignale_df, on='ORDERNR', how='inner', suffixes=('_auftrag', '_kipp'))
            
            if 'ROUTE_auftrag' in auftrag_waage_kipp_df.columns:
                auftrag_waage_kipp_df['ROUTE'] = auftrag_waage_kipp_df['ROUTE_auftrag']

            stammdaten_unique_route_df = stammdaten_df.drop_duplicates(subset=['ROUTE'])
            merged_df = pd.merge(auftrag_waage_kipp_df, stammdaten_unique_route_df, on='ROUTE', how='left')
            all_data_dfs.append(merged_df)
        except Exception as e:
            print(f"Error processing folder {folder}: {e}")

    final_df = pd.concat(all_data_dfs, ignore_index=True)

    # Data type conversions
    final_df['NET_WEIGHT'] = pd.to_numeric(final_df['NET_WEIGHT'], errors='coerce')
    final_df['GROSS_WDATE'] = pd.to_datetime(final_df['GROSS_WDATE'], format='%Y%m%d', errors='coerce')
    return final_df

```

#### Example 1: Total Waste Weight Per Day

**User Question:** "What is the total weight of waste collected each day?"

**Generated Function:**
```python
def get_total_waste_weight_per_day(merged_df: pd.DataFrame):
    """
    Calculates the total net weight of waste collected per day.
    
    Args:
        merged_df (pd.DataFrame): The pre-merged and cleaned DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with 'Date' and 'TotalWeight' columns.
    """
    if 'GROSS_WDATE' not in merged_df.columns or 'NET_WEIGHT' not in merged_df.columns:
        return "Required columns ('GROSS_WDATE', 'NET_WEIGHT') not found."
    
    # Group by date and sum the net weights
    daily_weight = merged_df.groupby('GROSS_WDATE')['NET_WEIGHT'].sum().reset_index()
    daily_weight = daily_weight.rename(columns={'GROSS_WDATE': 'Date', 'NET_WEIGHT': 'TotalWeight'})
    
    return daily_weight
```

#### Example 2: Most Common Waste Type

**User Question:** "What are the most common types of waste?"

**Generated Function:**
```python
def get_most_common_waste_type(merged_df: pd.DataFrame):
    """
    Counts the occurrences of each waste type.
    
    Args:
        merged_df (pd.DataFrame): The pre-merged and cleaned DataFrame.

    Returns:
        pd.Series: A Series with waste types and their counts.
    """
    if 'WASTE_TYPE_TXT' not in merged_df.columns:
        return "Required column 'WASTE_TYPE_TXT' not found."
    
    return merged_df['WASTE_TYPE_TXT'].value_counts()
```

#### Example 3: Tipping Signals Per Route

**User Question:** "How many tipping signals were recorded for each route?"

**Generated Function:**
```python
def get_tipping_signals_per_route(merged_df: pd.DataFrame):
    """
    Counts the number of tipping signals per collection route.
    
    Args:
        merged_df (pd.DataFrame): The pre-merged and cleaned DataFrame.

    Returns:
        pd.Series: A Series with routes and their tipping signal counts.
    """
    if 'ROUTE' not in merged_df.columns:
        return "Required column 'ROUTE' not found."
        
    return merged_df['ROUTE'].value_counts()
```
