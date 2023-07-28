import ast

def extract_model_names(input_list):
    model_names = []
    for item in input_list:
        if 'model_name' in item:
            model_names.append(item['model_name'])
        # else:
        #     model_names.append(item)
    return model_names

def process_input_string(input_str):
    # Split the input string into individual dictionary strings
    dict_strings = input_str.strip().split('\n')
    
    # Convert each dictionary string to a Python dictionary
    dicts = [ast.literal_eval(dict_str) for dict_str in dict_strings]
    
    # Use the extract_model_names function to get the model names
    return extract_model_names(dicts)

def main():
    input_data = "{'model_name': 'airoboros-65B-gpt4-1.4-GGML', 'model_size': '597196.8218'}\n{'model_name': 'airoboros-65B-gpt4-1.2-GGML', 'model_size': '597196.8147'}\n{'model_name': 'Upstage-Llama1-65B-Instruct-GGML', 'model_size': '597196.8141'}"

    output_list = process_input_string(input_data)
    print(output_list)

if __name__ == "__main__":
    main()