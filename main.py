from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

TOKEN = "secret-key"

books={
    'id': [],
    'title': [],
    'author': [],
    'isbn': [],
    'available': []
}

members={
    'id':[],
    'name':[],
    'email':[]
}

book_id_counter=0
member_id_counter=0

def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token != f"Bearer {TOKEN}":
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

def find_by_id(collection, item_id):
    ids=collection['id']
    ind=[ids.index(item) for item in ids if item == item_id]
    if len(ind)==0:
        return None
    ind=ind[0]
    return {key:books[key][ind] for key in books.keys()}

@app.route('/books', methods=['GET'])
@require_auth
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
@require_auth
def add_book():
    global book_id_counter
    data = request.json
    new_book = {
        'id': book_id_counter,
        'title': data.get('title'),
        'author': data.get('author'),
        'isbn': data.get('isbn'),
        'available': data.get('available', True)
    }
    books['id'].append(new_book['id'])
    books['title'].append(new_book['title'])
    books['author'].append(new_book['author'])
    books['isbn'].append(new_book['isbn'])
    books['available'].append(new_book['available'])
    book_id_counter += 1
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['GET'])
@require_auth
def get_book(book_id):
    book = find_by_id(books, book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['PUT'])
@require_auth
def update_book(book_id):
    book = find_by_id(books, book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    data = request.json
    # book.update({
    #     'title': data.get('title', book['title']),
    #     'author': data.get('author', book['author']),
    #     'isbn': data.get('isbn', book['isbn']),
    #     'available': data.get('available', book['available'])
    # })
    ind=books['id'].index(book_id)
    books['title'][ind]=data.get('title', book['title'])
    books['author'][ind]=data.get('author', book['author'])
    books['isbn'][ind]=data.get('isbn', book['isbn'])
    books['available'][ind]=data.get('available', book['available'])
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
@require_auth
def delete_book(book_id):
    global books
    book = find_by_id(books, book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    books['id'].remove(book['id'])
    books['title'].remove(book['title'])
    books['author'].remove(book['author'])
    books['isbn'].remove(book['isbn'])
    books['available'].remove(book['available'])
    return '', 204

@app.route('/books/<book_title>', methods=['GET'])
@require_auth
def find_by_title(book_title):
    title=books['title']
    ind=[title.index(item) for item in title if item == book_title]
    if len(ind)==0:
        return jsonify({'error': 'Book not found'}), 404
    ind=ind[0]
    return jsonify({key:books[key][ind] for key in books.keys()})

@app.route('/books/<book_author>', methods=['GET'])
@require_auth
def find_by_author(book_author):
    author=books['author']
    inds=[author.index(item) for item in author if item == book_author]
    if len(inds)==0:
        return jsonify({'error': 'Book not found'}), 404
    book_found=[]
    for ind in inds:
        book_found.append({key:books[key][ind] for key in books.keys()})
    return jsonify(book_found)

# Members

@app.route('/members', methods=['GET'])
@require_auth
def get_members():
    return jsonify(members)

@app.route('/members', methods=['POST'])
@require_auth
def add_member():
    global member_id_counter
    data = request.json
    new_member = {
        'id': member_id_counter,
        'name': data.get('name'),
        'email': data.get('email')
    }
    members['id'].append(new_member['id'])
    members['name'].append(new_member['name'])
    members['email'].append(new_member['email'])
    member_id_counter += 1
    return jsonify(new_member), 201

@app.route('/members/<int:member_id>', methods=['GET'])
@require_auth
def get_member(member_id):
    member = find_by_id(members, member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['PUT'])
@require_auth
def update_member(member_id):
    member = find_by_id(members, member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    data = request.json
    ind=members['id'].index(member_id)
    members['name'][ind]=data.get('name', member['name'])
    members['email'][ind]=data.get('email', member['email'])
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['DELETE'])
@require_auth
def delete_member(member_id):
    global members
    member = find_by_id(members, member_id)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    members['id'].remove(member['id'])
    members['name'].remove(member['name'])
    members['email'].remove(member['email'])
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)