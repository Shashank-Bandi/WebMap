import folium
map = folium.Map(location=[17.454372,78.423417],zoom_start=35)
map.save("test_map.html")
print("Map file created")
map1 = folium.Map(location=[17.454372,78.423417],zoom_start=35,tiles="Mapbox Bright")

map1.save("test_map_1.html")
print("Map file created")
