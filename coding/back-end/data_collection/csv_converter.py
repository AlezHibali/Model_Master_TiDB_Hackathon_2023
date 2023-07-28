# import pandas as pd

# # Load the CSV file
# df = pd.read_csv('models.csv')

# # Assume 'size_in_MB' is the column with numbers in units of MB
# def convert_units(val):
#     num_int_digits = len(str(int(val))) if val > 0 else 0
#     # Calculate the number of decimal places needed for 3 significant figures
#     decimal_places = 3 - num_int_digits if num_int_digits <= 3 else 0
#     # Convert MB to GB
#     if pd.isnull(val) or val == 0:
#         return 'N/A'
#     # Convert MB to KB
#     elif val >= 1024:
#         return f'model size {round(val / 1024, decimal_places)}GB'
#     elif val < 1:
#         return f'model size {round(val * 1024, decimal_places)}KB'
#     # Keep as MB
#     else:
#         return f'model size {round(val, decimal_places)}MB'

# # Apply the function to the column and replace it
# df['model_size'] = df['model_size'].apply(convert_units)

# # Save the modified dataframe back to a CSV file
# df.to_csv('hopefully_final_version_model_info.csv', index=False)

import csv
import math

# Function to convert units and round to 3 significant figures
def convert_units(val):
    if val == '' or float(val) == 0:
        return 'model size N/A'
    else:
        val = float(val)
        num_int_digits = len(str(int(val))) if val > 0 else 0
        decimal_places = 3 - num_int_digits if num_int_digits <= 3 else 0
        if val >= 1024:
            return f'model size {round(val / 1024, decimal_places)}GB'
        elif val < 1:
            return f'model size {round(val * 1024, decimal_places)}KB'
        else:
            return f'model size {round(val, decimal_places)}MB'

# Read the CSV file and apply the function to the column
with open('models.csv', 'r') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    data = []
    for i, row in enumerate(reader):
        if i >= 1452-2:
            break
        row[header.index('model_size')] = convert_units(row[header.index('model_size')])
        data.append(row)

# Write the modified data back to a CSV file
with open('hopefully_final_version_model_info.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(data)
