import csv

# Function to convert units and round to 3 significant figures
def convert_units(val):
    if val == '' or float(val) == 0:
        return 'N/A'
    else:
        val = float(val)
        num_int_digits = len(str(int(val))) if val > 0 else 0
        decimal_places = 3 - num_int_digits if num_int_digits <= 3 else 0
        if val >= 1024:
            return f'{round(val / 1024, decimal_places)}GB'
        elif val < 1:
            return f'{round(val * 1024, decimal_places)}KB'
        else:
            return f'{round(val, decimal_places)}MB'

def main():
    input_file = 'models.csv'
    output_file = 'hopefully_final_version_model_info.csv'

    # Read the CSV file and apply the function to the column
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        data = []
        for i, row in enumerate(reader):
            if i >= 1452-2:
                break
            row[header.index('model_size')] = convert_units(row[header.index('model_size')])
            data.append(row)

    # Write the modified data back to a CSV file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(data)

if __name__ == "__main__":
    main()