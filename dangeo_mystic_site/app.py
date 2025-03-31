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

    # Fundo do mapa
    folium.raster_layers.ImageOverlay(
        name='Dangeo Mystic',
        image='static/background.jpg',
        bounds=[[-90, -180], [90, 180]],
        opacity=1,
        interactive=True,
        cross_origin=False
    ).add_to(m)

    def add_race_marker(lat, lon, icon_file, name, description):
        icon_path = f"static/icons/{icon_file}"
        icon = folium.CustomIcon(
            icon_image=icon_path,
            icon_size=(40, 40),
            icon_anchor=(20, 20)
        )
        folium.Marker(
            location=[lat, lon],
            icon=icon,
            popup=folium.Popup(f"<b>{name}</b><br>{description}", max_width=300)
        ).add_to(m)

    # Lista de raças com localização, ícone e lore
    races = [
        (40, -30, "aspectos.png", "Aspectos", "Controladores de elementos naturais e forças cósmicas."),
        (35, -10, "warlocks.png", "Warlocks", "Mestres da necromancia e artes arcanas."),
        (25, -20, "celestiais.png", "Celestiais Luminaris", "Anjos que preservam o equilíbrio do mundo."),
        (-30, 10, "darkin.png", "Darkin", "Seres corrompidos pela guerra, poderosos e sombrios."),
        (0, 25, "gods.png", "Gods", "Entidades divinas com poderes absolutos."),
        (-10, 30, "drakthar.png", "Drak’thar", "Híbridos de humanos e dragões, dominadores elementais."),
        (20, 60, "drakanis.png", "Drakanis", "Seres de magma e lava, dominam o fogo."),
        (10, -40, "elves.png", "Elves", "Elfos florestais guardiões da natureza."),
        (5, -10, "guardians.png", "Prime Guardians", "Entidades ancestrais com conhecimento primordial."),
        (10, 0, "humans.png", "Humans", "Inteligentes, adaptáveis e determinados."),
        (-20, -25, "korigans.png", "Korigans", "Guerreiros forjados nas cinzas da guerra."),
        (5, 40, "lyssara.png", "Lyssara", "Seres nascidos da pura energia do mundo."),
        (-10, 45, "morkanites.png", "Morkanites", "Híbridos ágeis de humanos e lagartos."),
        (15, -35, "orcs.png", "Orcs", "Combatentes brutais e sedentos por glória."),
        (-5, 20, "sylphar.png", "Sylphar", "Fadas velozes com domínio sobre magia natural."),
        (20, 80, "therianthros.png", "Therianthros", "Híbridos de humanos e animais, ligados à natureza."),
        (-25, 65, "volkreens.png", "Volkreens", "Seres de pura eletricidade e manipulação energética."),
        (-35, 35, "dwarves.png", "Dwarves", "Pequenos mestres da forja e engenharia.")
    ]

    for lat, lon, icon, name, desc in races:
        add_race_marker(lat, lon, icon, name, desc)

    return render_template("index.html", map_html=m._repr_html_())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
