import pyttsx

from flask import request, Response

from app import app

engine = pyttsx.init('espeak')
engine.setProperty('rate', 140)

@app.route('/say', methods=['POST'])
def say():
    phrase = request.json['phrase']
    engine.say(phrase)
    engine.startLoop()
    return Response(None, 200)

@app.route('/mute')
def mute():
    engine.stop()
    return Response(None, 200)
