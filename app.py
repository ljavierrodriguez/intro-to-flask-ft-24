from flask import Flask, jsonify, request, json

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    data = {
        "msg": "Hola Mundo desde Flask"
    }
    return jsonify(data), 200

@app.route('/test')
def test():
    status = {
        "msg": "Server running successfully"
    }
    return jsonify(status), 200

@app.route('/saludo', methods=['GET'])
def get_saludo():
    pass

@app.route('/saludo', methods=['POST'])
def post_saludo():
    pass

@app.route('/saludo', methods=['PUT'])
def put_saludo():
    pass

@app.route('/saludo', methods=['DELETE'])
def delete_saludo():
    pass


@app.route('/saludo-todos', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saludo_todos():
    
    if request.method == 'GET':
        return jsonify({"method": request.method}), 200
    
    if request.method == 'POST':
        return jsonify({"method": request.method}), 200
    
    if request.method == 'PUT':
        return jsonify({"method": request.method}), 200
    
    if request.method == 'DELETE':
        return jsonify({"method": request.method}), 200


@app.route('/saludar/<name>/<lastname>', methods=['GET'])
def saludar(name, lastname):
    return jsonify({ "saludo": f"Hola, {name} {lastname}"}), 200


@app.route('/login', methods=['POST', 'PUT'])
def login():

    #data = json.loads(request.data)
    data = request.get_json()
    print(data["username"])


    username = request.json.get('username')
    password = request.json.get('password')
    print(username)
    print(password)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)