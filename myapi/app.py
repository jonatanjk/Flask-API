from flask import Flask, request

app = Flask(__name__)




@app.route('/getdata', methods=['POST'])
def return_request():
    output = request.get_json()
    output["uploader"] = "tester"
    return output