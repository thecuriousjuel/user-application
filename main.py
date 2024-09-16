"""
The starting point of the flask application containing the api routes.
"""
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from operations import save_to_database
from operations import fetch_all_user_details_from_database
from operations import initialize

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    """
    Renders the homepage of the application.
    """
    return render_template('index.html')

@app.route('/submitUserData', methods=['POST'])
def submit_user_data():
    """
    Gets the data from the request (frontend) and saves
    in the database. 
    """
    user_data = request.get_json()
    username = user_data['username']
    password = user_data['password']
    db_response = save_to_database(username, password)
    return jsonify({'message': db_response})

@app.route('/getAllUserDetails')
def get_all_user_details():
    """
    Gets all the users that are saved in the database.
    """
    user_data = fetch_all_user_details_from_database()
    return jsonify({'payload':user_data})

if __name__ == '__main__':
    initialize()
    app.run(debug=True)
