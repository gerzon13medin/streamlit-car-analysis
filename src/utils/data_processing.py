import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    """
    Limpia el dataset aplicando las siguientes transformaciones:
    1. Elimina filas con valores vacios en la columna Brand
    2. Elimina filas duplicadas
    3. Convierte los nombres de las columnas a minúsculas en formato snake_case

    param df: Dataframe de Pandas con los datos de vehiculos
    return: Dataframe limpio
    """

    # Eliminar valores vacíos en la columna Brand
    df = df.dropna(subset="Brand")

    # Elimina filas duplicadas
    df = df.drop_duplicates()


    # Convertir nombres de columnas a snake_case
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    return df