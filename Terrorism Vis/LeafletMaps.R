
library(leaflet)
library(htmlwidgets)
data = read.csv("TerrorismDATA_clean.csv")
data2010 = data[data$iyear>=2010,]
data2000 = data[data$iyear>=2000 & data$iyear<=2009,]



ass2000 <- leaflet(data = data2000) %>%
  addTiles() %>%
  # Overlay groups
  addMarkers(data=data2000[data2000$attacktype1==1,],lat=~latitude, lng=~longitude, popup=~summary, 
             clusterOptions = markerClusterOptions(), group = "Assassination (2000-2009)") %>% 
  # Layers control
  addLayersControl(
    overlayGroups = c("Assassination (2000-2009)"),
    options = layersControlOptions(collapsed = FALSE)
  )
ass2000
saveWidget(ass2000, 'ass2000.html')


ass2010 <- leaflet(data = data2010) %>%
  addTiles() %>%
  # Overlay groups
  addMarkers(data=data2010[data2010$attacktype1==1,],lat=~latitude, lng=~longitude, popup=~summary, 
             clusterOptions = markerClusterOptions(), group = "Assassination (2010-2016)") %>% 
  # Layers control
  addLayersControl(
    overlayGroups = c("Assassination (2010-2016)"),
    options = layersControlOptions(collapsed = FALSE)
  )
ass2010
saveWidget(ass2010, 'ass2010.html')






arm2000 <- leaflet(data = data2000) %>%
  addTiles() %>%
  # Overlay groups
  addMarkers(data=data2000[data2000$attacktype1==2,],lat=~latitude, lng=~longitude, popup=~summary, 
             clusterOptions = markerClusterOptions(), group = "Armed Assault (2000-2009)") %>% 
  # Layers control
  addLayersControl(
    overlayGroups = c("Armed Assault (2000-2009)"),
    options = layersControlOptions(collapsed = FALSE)
  )
arm2000
saveWidget(arm2000, 'arm2000.html')


arm2010 <- leaflet(data = data2010) %>%
  addTiles() %>%
  # Overlay groups
  addMarkers(data=data2010[data2010$attacktype1==2,],lat=~latitude, lng=~longitude, popup=~summary, 
             clusterOptions = markerClusterOptions(), group = "Armed Assault (2010-2016)") %>% 
  # Layers control
  addLayersControl(
    overlayGroups = c("Armed Assault (2010-2016)"),
    options = layersControlOptions(collapsed = FALSE)
  )
arm2010
saveWidget(arm2010, 'arm2010.html')








boob2000 <- leaflet(data = data2000) %>%
  addTiles() %>%
  # Overlay groups
  addMarkers(data=data2000[data2000$attacktype1==3,],lat=~latitude, lng=~longitude, popup=~summary, 
             clusterOptions = markerClusterOptions(), group = "Bombing/Explosion (2000-2009)") %>% 
  # Layers control
  addLayersControl(
    overlayGroups = c("Bombing/Explosion (2000-2009)"),
    options = layersControlOptions(collapsed = FALSE)
  )
boob2000
saveWidget(boob2000, 'boob2000.html')


boob2010 <- leaflet(data = data2010) %>%
  addTiles() %>%
  # Overlay groups
  addMarkers(data=data2010[data2010$attacktype1==3,],lat=~latitude, lng=~longitude, popup=~summary, 
             clusterOptions = markerClusterOptions(), group = "Bombing/Explosion (2010-2016)") %>% 
  # Layers control
  addLayersControl(
    overlayGroups = c("Bombing/Explosion (2010-2016)"),
    options = layersControlOptions(collapsed = FALSE)
  )
boob2010
saveWidget(boob2010, 'boob2010.html')








haj2000 <- leaflet(data = data2000) %>%
  addTiles() %>%
  # Overlay groups
  addMarkers(data=data2000[data2000$attacktype1==4,],lat=~latitude, lng=~longitude, popup=~summary, 
             clusterOptions = markerClusterOptions(), group = "Hijacking (2000-2009)") %>% 
  # Layers control
  addLayersControl(
    overlayGroups = c("Hijacking (2000-2009)"),
    options = layersControlOptions(collapsed = FALSE)
  )
haj2000
saveWidget(haj2000, 'haj2000.html')


haj2010 <- leaflet(data = data2010) %>%
  addTiles() %>%
  # Overlay groups
  addMarkers(data=data2010[data2010$attacktype1==4,],lat=~latitude, lng=~longitude, popup=~summary, 
             clusterOptions = markerClusterOptions(), group = "Hijacking (2010-2016)") %>% 
  # Layers control
  addLayersControl(
    overlayGroups = c("Hijacking (2010-2016)"),
    options = layersControlOptions(collapsed = FALSE)
  )
haj2010
saveWidget(haj2010, 'haj2010.html')





