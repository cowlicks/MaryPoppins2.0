import pyttsx

from flask import request, Response

from app import app

engine = pyttsx.init('espeak')

@app.route('/say', methods=['POST'])
def say():
    phrase = request.json['phrase']
    engine.say(phrase)
    engine.runAndWait()
    return Response(None, 200)
