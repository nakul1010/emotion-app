from flask import Flask, render_template, Response
from camera import VideoCamera
from camera import emotion_list
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/result')
def result():
    #print(emotion_list)
    sad = emotion_list.count('Sad')
    angry = emotion_list.count('Angry')
    disgust = emotion_list.count('Disgust')
    fear = emotion_list.count('Fear')
    happy = emotion_list.count('Happy')
    surprise = emotion_list.count('Surprise')
    print("\nSad : ",sad)
    print("\nangry : ",angry)
    print("\ndisgust : ",disgust)
    print("\nfear : ",fear)
    print("\nhappy : ",happy)
    print("\nsurprise : ",surprise)
    emotion_list.clear()#very-very imp
    return render_template('final_result.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
