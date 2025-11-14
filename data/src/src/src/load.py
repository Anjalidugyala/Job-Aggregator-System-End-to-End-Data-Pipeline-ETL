import pandas as pd

def save_to_csv(df):
    output_path = "data/processed_jobs.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved file to {output_path}")
