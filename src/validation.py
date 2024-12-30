def validate_nulls(df):
    null_counts = df.isnull().sum()
    return null_counts

def validate_uniqueness(df, column_name):
    return df[column_name].is_unique
