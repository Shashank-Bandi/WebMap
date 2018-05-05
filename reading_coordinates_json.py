import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

map=folium.Map(location=[38.59,-99.09],zoom_start=6)

fg=folium.FeatureGroup(name="MyMap")
def color_select(el):
    if el<1000:
        return "green"
    elif 1000<el<2000:
        return 'orange'
    else:
        return 'red'



for lt,lg,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,lg],popup=str(el)+"mts",icon=folium.Icon(color=color_select(el))))
    map.add_child(fg)


map.save("USA_VOlcano.html")
print("Map Generated")
