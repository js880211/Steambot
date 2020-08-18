'''
Created on 2020年8月18日

@author: User
'''
import flask
import json

bot=flask.Flask(__name__)
bot.config["DEBUG"] = True

@bot.route('/', methods=['GET'])
def home():
    f=open("data.json","r")
    lis1=f.read()
    lis1=json.loads(lis1)
    s=''.join(lis1)
    return s

if __name__ == '__main__':
    bot.run()