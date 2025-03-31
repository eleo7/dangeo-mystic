
from flask import Flask, render_template
from auth import auth_bp
import folium
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(auth_bp)

@app.route("/")
def index():
    m = folium.Map(location=[0, 0], zoom_start=2, tiles=None)
    folium.Marker(location=[10, 10], popup="Raça Teste").add_to(m)
    return render_template("index.html", map_html=m._repr_html_())

if __name__ == "__main__":
    app.run(debug=True)
