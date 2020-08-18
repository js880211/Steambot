'''
Created on 2020年8月18日

@author: User
'''
import flask

bot=flask.Flask(__name__)
bot.config["DEBUG"] = True


@bot.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


bot.run()