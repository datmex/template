from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def home():
    text = {"hola"}
    return render_template("home.html",
        title = 'Home',
        text = text)


app.debug = True
if __name__ == "__main__":
    app.run()
