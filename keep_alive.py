from flask import Flask
#from gevent.pywsgi import WSGIServer

from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)
  #from waitress import serve
  #serve(app, host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()