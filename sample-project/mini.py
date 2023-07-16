from flask import Flask, jsonify, request
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.route("/")
def test_server():
    return "<h1>Server is runnings.!!!</h1>"


@app.route("/test_info")
def test_server_info():
    return "<h1>Test Server is info.!!!</h1>"


@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    # show the user profile for that user

    return f'User {escape(username)}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        reqData = request.get_json()

        return do_the_login(reqData)
    else:
        return show_the_login_form()

def do_the_login(reqData): 
    respData = {}

    if(reqData["password"] == "rock"):
        respData = {
            "username" : reqData["username"],
            "status" : "Success"
        }
        return jsonify(respData) 
    else :
        respData = {
            "username" : reqData["username"],
            "status" : "Fail"
        }
        return jsonify(respData) , 404
    # Convert data to JSON and send the response
     


def show_the_login_form():
    return "login info data."




# Command to run : flask --app mini run
# Debug mode : flask --app mini run --debug