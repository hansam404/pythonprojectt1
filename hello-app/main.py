# Python code

from flask import Flask

app = Flask(__name__)

@app.route("/") #python decorator

def index():
        return "Congratulations, it's a web app!  -by Sam"

if __name__=="__main__":
        app.run(host="127.0.0.1", port=8080, debug=True)