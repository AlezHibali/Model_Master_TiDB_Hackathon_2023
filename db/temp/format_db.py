import csv
import re
import sys

def convert_downloads(downloads_str):
    return downloads_str.replace(',', '')

def convert_model_size(size_str):
    size_str = size_str.lower()
    size_units = {'kb': 1 / 1024, 'mb': 1, 'gb': 1024, 'b': 1 / (1024 * 1024)}
    for unit, multiplier in size_units.items():
        if unit in size_str:
            size = float(re.findall(r'[0-9.]+', size_str)[0])
            return str(int(size * multiplier))  # Convert to MB
    return "0"  # Return 0 if the format is unknown

def convert_likes(likes_str):
    likes_str = likes_str.lower()
    likes_units = {'k': 1000, 'm': 1000000, 'b': 1000000000}
    for unit, multiplier in likes_units.items():
        if unit in likes_str:
            return str(int(float(likes_str.replace(unit, '')) * multiplier))
    return likes_str.replace(',', '')

def main(input_file):
    output_file = 'output.csv'

    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                # Modify the 'downloads_last_month', 'model_size', and 'likes' columns
                row['downloads_last_month'] = convert_downloads(row['downloads_last_month'])
                row['model_size'] = convert_model_size(row['model_size'])
                row['likes'] = convert_likes(row['likes'])

                # Write the modified row to the output CSV file
                writer.writerow(row)

    print("CSV modification complete. Output file: 'output.csv'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_data.csv>")
    else:
        input_data_file = sys.argv[1]
        main(input_data_file)