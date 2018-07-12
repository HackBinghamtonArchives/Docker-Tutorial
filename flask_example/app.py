import os
import socket

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Container ID:</b> {hostname}<br/>" \
           "<img src={image} alt={image}>"

    return html.format(name="Docker", hostname=socket.gethostname(), image='/static/head.jpg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
