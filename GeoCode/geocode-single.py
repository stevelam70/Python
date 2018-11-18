import geocoder
g=geocoder.google('11/9 Anselm Street , Strathfield South ,NSW,2136, Australia')
g.latlng
print(g.latlng)

b=geocoder.google('11/9 Anselm Street , Strathfield South ,NSW,2136, Australia')
b.latlng
print(b.latlng)
