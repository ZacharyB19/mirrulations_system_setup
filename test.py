from flask import Flask, request, Response
import redis

r = redis.Redis()
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

@app.route('/addToRedis')
def addToRedis():
    r.set('key', 'value')
    return 'Added'

@app.route('/testGetRedis')
def testGetRedis():
    return_value = r.get('key')
    return return_value

@app.route('deleteRedisData')
def deleteRedisData():
    r.delete('key')
    return 'Deleted'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
