
from flask import Flask, render_template
from auth import auth_bp
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Registrar o blueprint de autenticação
app.register_blueprint(auth_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
