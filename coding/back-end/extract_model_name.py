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
    # Check if the input string is empty
    if not input_str:
        return []  # Return an empty list as there are no dictionaries to process
    
    # Split the input string into individual dictionary strings
    dict_strings = input_str.strip().split('\n')
    
    # Convert each dictionary string to a Python dictionary
    dicts = [ast.literal_eval(dict_str) for dict_str in dict_strings]
    
    # Use the extract_model_names function to get the model names
    return extract_model_names(dicts)
