# app.py

from flask import Flask, render_template
import folium
import os

app = Flask(__name__)

@app.route('/')
def home():
    m = folium.Map(
        location=[0, 0],
        zoom_start=2,
        tiles=None
    )

    folium.raster_layers.ImageOverlay(
        name='Dangeo Mystic',
        image='static/background.jpg',
        bounds=[[-90, -180], [90, 180]],
        opacity=1,
        interactive=True,
        cross_origin=False
    ).add_to(m)

    def add_race_marker(lat, lon, icon_path, race_name, description):
        icon = folium.CustomIcon(
            icon_image=icon_path,
            icon_size=(40, 40),
            icon_anchor=(20, 20)
        )
        folium.Marker(
            location=[lat, lon],
            icon=icon,
            popup=folium.Popup(f"<strong>{race_name}</strong><br>{description}", max_width=300)
        ).add_to(m)

    # Exemplo de marcador (adicione os outros conforme sua lógica):
    add_race_marker(10, 0, "static/icons/humans.png", "Humans", "Raça com grande adaptabilidade.")

    return render_template("index.html", map_html=m._repr_html_())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
# Conteúdo simulado para app.py
