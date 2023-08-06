from flask import Flask, jsonify, request
from flask_cors import CORS
from prompt2data import main_process
import urllib.parse
from extract_model_name import process_input_string
from user_func import addUserInfo, checkUserInfo, getUserFavModels, modifyUserFavModels, checkUserFavModels

app = Flask(__name__)
CORS(app)

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

# curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"ali.daixin.tian@gmail.com\", \"password\":\"12345678\"}" http://localhost:8080/api/add_user
@app.route('/api/add_user', methods=['POST'])
def add_user():
    # Get the 'username' and 'password' parameters from the JSON request data
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid data format. Please provide both username and password in JSON format.'})

    username = data['username']
    password = data['password']

    # Call the 'addUserInfo' function to add the user to the database
    if (addUserInfo(username, password)):
        return header_processing(jsonify({'message': 'User information added successfully.'}))
    else:
        return header_processing(jsonify({'message': 'Error: addUserInfo failed.'}))

# not implemented yet
@app.route('/api/check_user_info', methods=['GET'])
def check_user_info():
    # Get the 'username' parameter from the HTTP GET request
    username = request.args.get('username')

    user_info = checkUserInfo(username)

    return header_processing(jsonify(user_info))

# curl "http://localhost:8080/api/get_user_fav?username=admin"
@app.route('/api/get_user_fav', methods=['GET'])
def get_user_fav():
    # Get the 'username' parameter from the HTTP GET request
    username = request.args.get('username')

    info = getUserFavModels(username)

    return header_processing(jsonify(info))

# curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"admin_api_trial\", \"model\":\"gpt2\"}" http://localhost:8080/api/modify_user_fav
@app.route('/api/modify_user_fav', methods=['POST'])
def modify_user_fav():
    # Get the 'username' and 'password' parameters from the JSON request data
    data = request.get_json()

    if not data or 'username' not in data or 'model' not in data:
        return jsonify({'error': 'Invalid data format. Please provide both username and model name in JSON format.'})

    username = data['username']
    model = data['model']

    res = modifyUserFavModels(username, model)

    if res == 1:
        return header_processing(jsonify({'message': 'Model Added to Favorite.'}))
    elif res == -1:
        return header_processing(jsonify({'message': 'Model Removed from Favorite.'}))
    else:
        return header_processing(jsonify({'message': 'Error: modify_user_fav failed.'}))
    
# curl "http://localhost:8080/api/check_user_fav?model=gpt2"
@app.route('/api/check_user_fav', methods=['GET'])
def check_user_fav():
    # Get the 'model' parameter from the HTTP GET request
    model = request.args.get('model')
    username = 'ali.daixin.tian@gmail.com'

    res = checkUserFavModels(username, model)

    if res:
        return header_processing(jsonify({'message': 'True.'}))
    else:
        return header_processing(jsonify({'message': 'False.'}))
    

if __name__ == '__main__':
    # app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
