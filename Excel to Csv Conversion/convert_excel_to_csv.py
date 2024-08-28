import pandas as pd

try:
    xl_file = r"file\path\file_name.xlsx" 
    print(f"Reading Excel file from: {xl_file}")
    df = pd.read_excel(xl_file)
    print("Excel file read successfully!")
    print(df)

    csv_file = r"file\path\file_name.csv"
    print(f"Saving to CSV at: {csv_file}")
    df.to_csv(csv_file, index=False)
    print("CSV saved successfully!")
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

