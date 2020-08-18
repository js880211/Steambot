'''
Created on 2020年8月18日

@author: User
'''
import flask

app =flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


app.run(port=5000)