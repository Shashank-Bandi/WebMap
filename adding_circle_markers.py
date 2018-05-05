import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

map=folium.Map(location=[38.59,-99.09],zoom_start=6)

fg=folium.FeatureGroup(name="MyMap")

for lt,lg,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,lg],popup=str(el)+"mts",radius=10,color='red',fill=True,fill_opacity=0.2))
    map.add_child(fg)
map.save("USA_VOlcano_circle.html")
print("Map Generated")
