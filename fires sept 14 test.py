import json

in_file = open('US_fires_9_1.json','r')

out_file = open('readable_fi_data.json', 'w')

fi_data= json.load(in_file)

json.dump(fi_data, out_file, indent=4)

#list_of_fis = fi_data['features']
'''
print(type(list_of_fis))

print(len(list_of_fis))

'''

brights,lons,lats=[],[],[]

for fi in fi_data:
    bright = fi["brightness"]
    lon = fi["longitude"]
    lat = fi["latitude"]
    brights.append(bright)
    lons.append(lon)
    lats.append(lat)
'''
print ("brights")
print(brights[:10])
print ("Lons")
print(lons[:10])
print ("Lats")
print(lons[:10])
'''

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]
data= [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker':{
        'size':[1/40*bright for bright in brights],
        'color': brights,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar': {'title':'brightness'}
    },
}]

my_layout = Layout(title= 'US fires')

fig= {'data' : data, 'layout' :my_layout}

offline.plot(fig, filename='US_fires_sept1.html')