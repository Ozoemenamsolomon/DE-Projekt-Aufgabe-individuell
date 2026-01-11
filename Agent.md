# LLM Context: Data Schema for `merged_data.csv`

This document describes the schema for the `merged_data.csv` file. This file is the primary data source for all dynamic transformations and analyses. An LLM should use this schema as the ground truth for the data it will be processing.

**File Location:** `data/merged_data.csv`

**Description:** A comprehensive, merged, and cleaned dataset from all raw daily waste management sources. It contains information on orders, routes, weights, and tipping events.

---

### **Data Schema**

| Column             | Data Type        | Description                                                                        | Example                      |
| :----------------- | :--------------- | :--------------------------------------------------------------------------------- | :--------------------------- |
| **ORDERNR**        | `string`         | Unique identifier for a collection order.                                          | `00000000000002629397`       |
| **ROUTE**          | `string`         | Unique identifier for the collection route the order belongs to.                   | `EW1403`                     |
| **TIDNR**          | `string`         | Unique identifier for a specific container (Tonne).                                | `12345678`                   |
| **NET_WEIGHT**     | `float`          | The net weight of the collected waste in kilograms (KG).                           | `10920.0`                    |
| **WASTE_TYPE_TXT** | `string`         | The full text description of the waste type.                                       | `gemischte Siedlungsabfälle` |
| **BEH_TYPE_TXT**   | `string`         | The full text description of the container type.                                   | `1100L`                      |
| **ENTSORGER**      | `string`         | The name of the disposal company responsible for the weighing.                     | `RMB`                        |
| **STPL_STREET**    | `string`         | The street name for the container's registered location.                           | `Musterstraße`               |
| **STPL_CITY1**     | `string`         | The city for the container's registered location.                                  | `Frankfurt am Main`          |
| **KIPPE**          | `integer`        | A signal indicating a tipping event has occurred (usually `1`).                    | `1`                          |
| **LONGITUDE**      | `float`          | The GPS longitude coordinate of the tipping event.                                 | `8.682127`                   |
| **LATITUDE**       | `float`          | The GPS latitude coordinate of the tipping event.                                  | `50.110924`                  |
| **EVENT_DATE**     | `datetime64[ns]` | The primary date for the event, coalesced from weighing and signal creation dates. | `2025-04-08`                 |
| ORDER_DATE         | `int64`          | The original date the order was created in `YYYYMMDD` format.                      | `20250409`                   |
| LICENSE_NUM        | `string`         | The license plate number of the vehicle involved in the weighing.                  | `F-ES3054`                   |
| FRZG               | `string`         | The vehicle identifier from the tipping signal data.                               | `F-ES3054`                   |
| TIME_CREATE        | `int64`          | The original time the tipping signal was created in `HHMMSS` format.               | `140331`                     |
| ...                |                  | _Other columns from the original source files exist but are less commonly used._   |                              |

---

## LLM Prompt Template for Dynamic ETL Transformation

You are an expert Python data engineer. Your task is to generate a Python function and its documentation based on a user's request.

**IMPORTANT RULES:**

1. You MUST generate a single Python function named `apply_transform`.
2. This function MUST accept a pandas DataFrame as its only argument and MUST return a transformed pandas DataFrame.
3. You MUST also generate a Markdown-formatted string variable named `TRANSFORM_DOCUMENTATION` that clearly explains the transformation logic.
4. The generated code should be self-contained within the `transforms/dynamic_transforms.py` file, requiring only `pandas`.
5. The function should operate on the `merged_data.csv` file, whose schema is described in detail above.

---

### User's Transformation Request

```
{user_prompt}
```

---

### Your Task

Based on the data schema and the user's request above, generate the Python code for the `apply_transform` function and the `TRANSFORM_DOCUMENTATION` variable. Place your generated code inside the `transforms/dynamic_transforms.py` file, replacing the placeholder content.

**Example Output Structure:**

```python
# --- Start of LLM-Generated Code ---

import pandas as pd

def apply_transform(df: pd.DataFrame) -> pd.DataFrame:
	"""
	(Your function description here)
	"""
	# Your transformation logic here

	return df

TRANSFORM_DOCUMENTATION = """
## (Your Documentation Title)

(Your Markdown-formatted documentation here)
"""
```
