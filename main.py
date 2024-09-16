from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from operations import save_to_database
from operations import fetch_all_user_details_from_database

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/submitUserData', methods=['POST'])
def submit_user_data():
    user_data = request.get_json()
    username = user_data['username']
    password = user_data['password']
    db_response = save_to_database(username, password)
    return jsonify({'message': db_response})

@app.route('/getAllUserDetails')
def get_all_user_details():
    user_data = fetch_all_user_details_from_database()
    return jsonify({'payload':user_data, 'message': 'Enter Username and Password!'})

if __name__ == '__main__':
    app.run(debug=True)
