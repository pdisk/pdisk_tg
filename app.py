import os
UPLOAD_DIRECTORY = "templates/download"
from flask import Flask, request, abort, jsonify, send_from_directory
import subprocess

app = Flask(__name__)
subprocess.Popen('python3 bot.py', shell=True)

@app.route("/files")
def list_files():
    """Endpoint to list files on the server."""

    files = []

    for filename in os.listdir(UPLOAD_DIRECTORY):

        path = os.path.join(UPLOAD_DIRECTORY, filename)

        if os.path.isfile(path):
            files.append(filename)

    return jsonify(files)


@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""

    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@app.route("/files/<filename>", methods=["POST"])
def post_file(filename):
    """Upload a file."""

    if "/" in filename:
        # Return 400 BAD REQUEST

        abort(400, "no subdirectories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)

    # Return 201 CREATED

    return "", 201


@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter

    name = request.args.get("name", None)

    # For debugging

    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all

    if not name:

        response["ERROR"] = "no name found, please send a name."

    # Check if the user entered a number not a name

    elif str(name).isdigit():

        response["ERROR"] = "name can't be numeric."

    # Now the user entered a valid name

    else:

        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format

    return jsonify(response)


@app.route('/u', methods=['GET'])
def indeegx():
    w = request.args.get('url')
    subprocess.Popen('node index.js', shell=True)
    # @app.route('/ni',methods=['GET'])
    return send_from_directory(f"templates/download/{w}", filename=w)

@app.route('/')
def index():
    # c = subprocess.getoutput(f"python3 bot.py")
    return "<h1>Telegram link Generator !!</h1> <!-- Bidvertiser2051838 -->"


@app.route('/index.page')
def indeeeex():
    return "<h1>Telegram link Generator !!</h1> <!-- Bidvertiser2051838 -->"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support

    app.run(threaded=True, port=5000)
