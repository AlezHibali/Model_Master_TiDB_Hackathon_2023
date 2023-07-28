from flask import Flask, jsonify, request
from prompt2data import main_process
import urllib.parse
from extract_model_name import process_input_string
from user_func import addUserInfo, deleteUserInfo, checkUserInfo

app = Flask(__name__)

def header_processing(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

# curl localhost:8080/api/prompt2data?prompt=top%205%20club%20that%20has%20the%20smallest%20average%20age
@app.route('/api/prompt2data', methods=['GET'])
def prompt2data():
    # Get the 'prompt' parameter from the HTTP GET request and decode it
    prompt_encoded = request.args.get('prompt')

    if not prompt_encoded:
        return jsonify({'error': 'No prompt provided'})

    prompt = urllib.parse.unquote(prompt_encoded)

    # Call the 'main_process' function with the decoded input prompt
    data = main_process(prompt)

    # Return the data as JSON
    if data[1] == 200:
        model_list = process_input_string(data[0])
        response_data = {
            "value1": data[0] if data[0] else "There is no result!",
            "value2": model_list
        }
        return header_processing(jsonify(response_data))
    else:
        return header_processing(jsonify({"message": f"Error with status code {data[1]}"}))

@app.route('/api/add_user', methods=['POST'])
def add_user():
    # Get the 'username' and 'password' parameters from the JSON request data
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid data format. Please provide both username and password in JSON format.'})

    username = data['username']
    password = data['password']

    # Call the 'addUserInfo' function to add the user to the database
    addUserInfo(username, password)

    return header_processing(jsonify({'message': 'User information added successfully.'}))

@app.route('/api/delete_user', methods=['POST'])
def delete_user():
    # Get the 'username' parameter from the JSON request data
    username = request.get_json()

    deleteUserInfo(username)

    return header_processing(jsonify({'message': 'User information deleted successfully.'}))

@app.route('/api/check_user_info', methods=['GET'])
def check_user_info():
    # Get the 'username' parameter from the HTTP GET request
    username = request.args.get('username')

    user_info = checkUserInfo(username)

    return header_processing(jsonify(user_info))

if __name__ == '__main__':
    # app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
