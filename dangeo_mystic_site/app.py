
from flask import Flask, render_template
import folium
import os

app = Flask(__name__)

@app.route("/")
def home():
    m = folium.Map(location=[0, 0], zoom_start=2, tiles=None)
    folium.raster_layers.ImageOverlay(
        name="Dangeo Mystic",
        image="static/background.jpg",
        bounds=[[-90, -180], [90, 180]],
        opacity=1
    ).add_to(m)
    icon = folium.CustomIcon("static/icons/humans.png", icon_size=(40, 40))
    folium.Marker([10, 0], icon=icon, popup="Humans").add_to(m)
    return render_template("index.html", map_html=m._repr_html_())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
