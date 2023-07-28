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

def get_category(task):
    category_mapping = {
        # -- Audio
        'Audio Classification': 'Audio',
        'Audio-to-Audio': 'Audio',
        'Automatic Speech Recognition': 'Audio',
        'Text-to-Speech': 'Audio',
        'Voice Activity Detection': 'Audio',
        
        # -- Computer Vision
        'Depth Estimation': 'Computer Vision',
        'Image Classification': 'Computer Vision',
        'Image Segmentation': 'Computer Vision',
        'Image-to-Image': 'Computer Vision',
        'Object Detection': 'Computer Vision',
        'Unconditional Image Generation': 'Computer Vision',
        'Video Classification': 'Computer Vision',
        'Zero-Shot Image Classification': 'Computer Vision',
        
        # -- Multimodel
        'Document Question Answering': 'Multimodel',
        'Feature Extraction': 'Multimodel',
        'Graph Machine Learning': 'Multimodel',
        'Image-to-Text': 'Multimodel',
        'Text-to-Image': 'Multimodel',
        'Text-to-Video': 'Multimodel',
        'Visual Question Answering': 'Multimodel',
        
        # -- Natural Language Processing
        'Conversational': 'Natural Language Processing',
        'Fill-Mask': 'Natural Language Processing',
        'Question Answering': 'Natural Language Processing',
        'Sentence Similarity': 'Natural Language Processing',
        'Summarization': 'Natural Language Processing',
        'Table Question Answering': 'Natural Language Processing',
        'Text Classification': 'Natural Language Processing',
        'Text Generation': 'Natural Language Processing',
        'Text2Text Generation': 'Natural Language Processing',
        'Token Classification': 'Natural Language Processing',
        'Translation': 'Natural Language Processing',
        'Zero-Shot Classification': 'Natural Language Processing',
        
        # -- Reinforcement Learning
        'Reinforcement Learning': 'Reinforcement Learning',
        'Robotics': 'Reinforcement Learning',
        
        # -- Tabular
        'Tabular Classification': 'Tabular',
        'Tabular Regression': 'Tabular'
    }

    return category_mapping.get(task, '')

def main(input_file):
    output_file = 'output.csv'

    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['category']

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            row_count = 0
            for row in reader:
                # Modify the 'downloads_last_month', 'model_size', and 'likes' columns
                row['downloads_last_month'] = convert_downloads(row['downloads_last_month'])
                # row['model_size'] = convert_model_size(row['model_size'])
                row['likes'] = convert_likes(row['likes'])
                # Add the 'category' column based on the 'task' value
                row['category'] = get_category(row['task'])

                # Write the modified row to the output CSV file
                writer.writerow(row)

                row_count += 1
                if row_count >= 1450:
                    break

    print("CSV modification complete. Output file: 'output.csv'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_data.csv>")
    else:
        input_data_file = sys.argv[1]
        main(input_data_file)