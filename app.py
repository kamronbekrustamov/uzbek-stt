from flask import Flask, request
import nemo_uz as transcriber

application = Flask(__name__)

@application.route("/api/v1/convert")
def convert():
    if request.files:
        audio = request.files.get('audio')
        if audio == None:
            return "<p>You must send the audio file with the key audio", 400
        if audio.filename == "":
            return "<p>The file must have a name</p>"
        return transcriber.transcribe(audio)
    else:
        return "<p>You are supposed to provide audio file in the body</p>", 400

if __name__ == "main":
    application.run()
