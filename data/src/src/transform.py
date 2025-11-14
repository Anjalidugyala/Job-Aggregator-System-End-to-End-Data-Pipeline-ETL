import pandas as pd

def clean_jobs(jobs):
    df = pd.DataFrame(jobs)

    # Remove rows with missing titles
    df = df[df["title"] != "N/A"]

    # Remove duplicates
    df = df.drop_duplicates()

    # Reset index
    df = df.reset_index(drop=True)

    return df
