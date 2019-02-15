from flask import Flask, request, Response

import json
app = Flask(__name__)

@app.route('/')
def default():
    """
    Default endpoint
    :return: returns empty json
    """
    return json.dumps({})

@app.route('/testEndpoint')
def testEndpoint():
    return "You did it"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
