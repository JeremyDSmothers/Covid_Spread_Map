import folium
from folium.map import Popup
from numpy import nan
import pandas as pd

#SETUP DATA
covid_data_set = pd.read_csv('resources/time_series_covid_19_confirmed.csv')
covid_locations = covid_data_set['Province/State']
covid_countries = covid_data_set['Country/Region']
covid_location_names = []
# print(len(covid_data_set))
# breakpoint()
may_26_2021_raw = covid_data_set["5/29/21"]
may_26_2021 = []

covid_lats = covid_data_set['Lat']
covid_longs = covid_data_set['Long']

max = 0
for i in range(len(covid_countries)):
    if str(covid_lats[i]) != 'nan' and str(covid_longs[i]) != 'nan': 
        location_str = ""
        # print(type(covid_locations[i]))
        if str(covid_locations[i]) != 'nan':
            location_str = str(covid_locations[i]) + ', '

        may_26_2021.append(may_26_2021_raw[i])
        if may_26_2021_raw[i] > max:
            max = may_26_2021_raw[i]

        location_str += covid_countries[i]

        covid_location_names.append(location_str)

lat_longs = [(covid_lats[i], covid_longs[i]) for i in range(len(covid_lats)) if str(covid_lats[i]) != 'nan' and str(covid_longs[i]) != 'nan']

name_and_latlong = [(covid_location_names[i], lat_longs[i]) for i in range(len(lat_longs))]

#now i have a value that looks like ('name of country', ([lat value], [long value]))

# fg = folium.FeatureGroup(name="Markers")
# for i in range(len(name_and_latlong)):
#     # print(name_and_latlong[i])
#     geo_tuple = name_and_latlong[i][1]

#     # print('geoTuple', geo_tuple)
#     fg.add_child(folium.Marker(location=[geo_tuple[0], geo_tuple[1]], popup=name_and_latlong[i], icon=folium.Icon(color='black')))

circlesGroup = folium.FeatureGroup(name="Circle Markers")
may_26_2021 = covid_data_set['5/29/21']
for i in range(len(name_and_latlong)):
    circle_meta_data = name_and_latlong[i]
    print(may_26_2021[i], max, may_26_2021/max*100000)

    circlesGroup.add_child(
        folium.CircleMarker(
            radius = (may_26_2021[i] / max) * 100,
            location = [circle_meta_data[1][0], circle_meta_data[1][1]],
            popup = may_26_2021[i],
        )
    )
    
    # may_26_2021[i]
    # print('meh')

    




#init map
map = folium.Map(location=[0, 0], tiles="Stamen Terrain", zoom_start=1)
map.add_child(circlesGroup)

map.save("location_and_names.html")

#

