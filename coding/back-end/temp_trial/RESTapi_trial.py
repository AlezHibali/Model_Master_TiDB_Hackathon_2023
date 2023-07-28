from flask import Flask, jsonify, request
from prompt2data import main_process
import urllib.parse

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
]

# Get all books
# curl localhost:8080/books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Add a new book
# curl -X POST localhost:8080/books
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {"id": len(books) + 1, "title": data["title"], "author": data["author"]}
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        book["title"] = data["title"]
        book["author"] = data["author"]
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [item for item in books if item["id"] != book_id]
    return jsonify({"message": "Book deleted successfully"}), 200

################################
# curl localhost:8080/api/prompt2data?prompt=top%205%20club%20that%20has%20the%20smallest%20average%20age
@app.route('/api/prompt2data', methods=['GET'])
def get_data():
    # Get the 'prompt' parameter from the HTTP GET request and decode it
    prompt_encoded = request.args.get('prompt')

    if not prompt_encoded:
        return jsonify({'error': 'No prompt provided'})

    prompt = urllib.parse.unquote(prompt_encoded)

    # Call the 'main_process' function with the decoded input prompt
    data = main_process(prompt)

    # Return the data as JSON
    if data[1] == 200:
        return jsonify(data[0])
    else:
        return jsonify({"message": f"Error with status code {data[1]}"})

if __name__ == '__main__':
    # app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
