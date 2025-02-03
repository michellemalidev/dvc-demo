import pandas as pd
from dvc.api import DVCFileSystem

def process_large_csv():
    # Initialize DVCFileSystem with GCS URL
    fs = DVCFileSystem(remote="myremote")

    # Open the large CSV file using DVCFileSystem
    with fs.open('large_file.csv', 'rb') as f:
        # Read the CSV file in chunks to handle large files
        chunk_size = 100000  # Number of rows per chunk
        total_value = 0
        total_count = 0

        # Use pandas to read the CSV in chunks
        for chunk in pd.read_csv(f, chunksize=chunk_size):
            total_value += chunk['value'].sum()
            total_count += chunk['value'].count()

        average_value = total_value / total_count if total_count > 0 else 0
        print(f'Average value: {average_value}')

# Call the function to process the large CSV file
process_large_csv()