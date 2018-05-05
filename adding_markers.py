import folium
map = folium.Map(location=[17.454372,78.423417],zoom_start=35)
fg = folium.FeatureGroup(name="MyMap")
fg.add_child(folium.Marker(location=[17.454372,78.423417],popup="I am home",icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[17.454290,78.423404],popup="Rayudu Tiffins",icon=folium.Icon(color='blue')))
map.add_child(fg)

map.save("map_markers.html")
print("map saved")
            
