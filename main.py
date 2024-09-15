from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from operations import save_to_database

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/submitUserData', methods=['POST'])
def submit_user_data():
    user_data = request.get_json()
    username = user_data['username']
    password = user_data['password']
    save_to_database(username, password)
    return jsonify({'message': 'Data received successfully'})

if __name__ == '__main__':
    app.run(debug=True)
