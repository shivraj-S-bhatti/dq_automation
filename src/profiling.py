import pandas as pd

def generate_profile(file_path):
    df = pd.read_csv(file_path)
    print(df.info())
    print(df.describe())
    return df
