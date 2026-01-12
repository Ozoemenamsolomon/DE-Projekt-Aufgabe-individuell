# --- Start of LLM-Generated Code ---

import pandas as pd

def apply_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtert Datensätze auf Bioabfall FFM mit einem Nettogewicht größer als 1000 KG.
    """
    filtered_df = df[
        (df["WASTE_TYPE_TXT"] == "Bioabfall FFM") &
        (df["NET_WEIGHT"] > 1000)
    ].copy()

    return filtered_df


TRANSFORM_DOCUMENTATION = """
## Filter: Bioabfall FFM mit Gewicht > 1000 KG

Diese Transformation filtert den Datensatz nach folgenden Kriterien:

- **Abfallart**: Es werden ausschließlich Einträge berücksichtigt, bei denen
  `WASTE_TYPE_TXT` exakt den Wert **"Bioabfall FFM"** hat.
- **Gewicht**: Zusätzlich muss das Nettogewicht (`NET_WEIGHT`) größer als **1000 KG** sein.

### Ergebnis
Der zurückgegebene DataFrame enthält nur die relevanten Datensätze, alle Spalten
des Originaldatensatzes bleiben erhalten.
"""
# --- End of LLM-Generated Code ---
