#name: victoria inahuazo
#date: 04/12/24
#email: victoria.inahuazo11@myhunter.cuny.edu

import folium
import pandas as pd

mapBigApple = folium.Map(location= [40.75,-74.125], zoom_start=10)

folium.Marker(location= [40.768014, -73.964515], popup = "Hunter College").add_to(mapBigApple)

mapBigApple.save(outfile='nycMap.html')