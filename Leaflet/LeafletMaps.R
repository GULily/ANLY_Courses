######################################################################
##This code works well and creates an interactive layered leaflet/R map
## The map is choropleth and markered
##
## Required datasets are here:
##    CancerCountyFIPS.csv
##    CancerCountyFIPS_Breast.csv
##    LandUseDatasetREALLatlong.csv
## AND ##
############
# Download county shape file.
## !! This is important. Shape files can be found here
#https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html
#us.map <- tigris::counties(cb = TRUE, year = 2015)
#OR
# Download county shape file from Tiger.
# https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html
# I downloaded the zip and placed all files in the zip into my RStudio folder
##us.map <- readOGR(dsn = ".", layer = "cb_2016_us_county_20m", stringsAsFactors = FALSE)
##head(us.map)
###############
##Not all of these libraries are required for this code, but
## they are good for more generalized goals
############################################################################

##https://www.statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=99&cancer=001&race=07&sex=
##0&age=001&type=incd&sortVariableName=rate&sortOrder=default#results

library(leaflet)

CancerRates <- read.csv('CancerCountyFIPS.csv')
CancerRatesB <- read.csv('CancerCountyFIPS_Breast.csv')
LandUse <- read.csv('LandUseDatasetREALLatlong.csv')

# Rename columns to make for a clean df merge later.
##GEOID is the same as FIPS
colnames(CancerRates) <- c("location", "GEOID", "rate")
colnames(CancerRatesB) <- c("location", "GEOID", "rateB")
colnames(LandUse) <- c("offset", "lat", "lng", "url", "name")

##Add leading zeos to any FIPS code that's less than 5 digits long to get a good match.
##formatC is from C code formatting - creates a 5 digit int
CancerRates$GEOID <- formatC(CancerRates$GEOID, width = 5, format = "d", flag = "0")
CancerRatesB$GEOID <- formatC(CancerRatesB$GEOID, width = 5, format = "d", flag = "0")

CancerRates =  merge(CancerRates, CancerRatesB, by = "GEOID", all = T)
CancerRates = CancerRates[,-4]

## Convert column called location to two columns: State and County
library(tidyr)
CancerRates <- separate(CancerRates, location.x, into = c("county", "state"), sep = ", ")

##Remove the (...) from the state values
CancerRates[] <- lapply(CancerRates, function(x) gsub("\\s*\\([^\\)]+\\)", "", x))
##Remove the space# from the end of some of the values in the rate column
CancerRates[] <- lapply(CancerRates, function(x) gsub("\\#", "", x))

# Convert full state names to abbreviations for a clean df merge later.
CancerRates$state <- state.abb[match(CancerRates$state, state.name)]

#Change CancerRates$rate to a number
CancerRates$rate <- as.numeric(as.character(CancerRates$rate))
CancerRates$rateB <- as.numeric(as.character(CancerRates$rateB))



# Download county shape file.
## !! This is important. Shape files can be found here
#https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html
#us.map <- tigris::counties(cb = TRUE, year = 2015)
#OR
# Download county shape file from Tiger.
# https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html
# I downloaded the zip and placed all files in the zip into my RStudio folder
library(rgdal)
us.map <- readOGR(dsn = ".", layer = "cb_2016_us_county_20m", stringsAsFactors = FALSE)
head(us.map)
# Remove Alaska(2), Hawaii(15), Puerto Rico (72), Guam (66), Virgin Islands (78), American Samoa (60)
#  Mariana Islands (69), Micronesia (64), Marshall Islands (68), Palau (70), Minor Islands (74)
us.map <- us.map[!us.map$STATEFP %in% c("02", "15", "72", "66", "78", "60", "69",
                                        "64", "68", "70", "74"),]
# Make sure other outling islands are removed.
us.map <- us.map[!us.map$STATEFP %in% c("81", "84", "86", "87", "89", "71", "76",
                                        "95", "79"),]

# Merge spatial df with downloaded data.
## This is important
## Now we have our data and the needed carto data
cancermap <- merge(us.map, CancerRates, by=c("GEOID"))

# Format popup data for leaflet map.
popup_dat <- paste0("<strong>County: </strong>", 
                    cancermap$county, 
                    "<br><strong>Cancer Rate (Age Adjusted) Out of 100,000: </strong>", 
                    cancermap$rate)
popup_datB <- paste0("<strong>County: </strong>", 
                    cancermap$county, 
                    "<br><strong>Breast Cancer Rate (Age Adjusted) Out of 100,000: </strong>", 
                    cancermap$rateB)



#Grouping for map options and User Choices
#https://rstudio.github.io/leaflet/showhide.html

##Make pop up for the land use sites
# Format popup data for leaflet map.
popup_LU <- paste0("<strong>Use Name: </strong>", 
                   LandUse$name, 
                   "<br><strong>Link: </strong>", 
                   LandUse$url)
popup_GU = "<strong>Georgetown University</strong>"
popup_SV = "<strong>Silicon Valley</strong>"


pal <- colorQuantile("YlOrRd", NULL, n = 9)
gmap <- leaflet(data = cancermap) %>%
  # Base groups
  addTiles() %>%
  setView(lng = -105, lat = 40, zoom = 4) %>% 
  addPolygons(fillColor = ~pal(rate), 
              fillOpacity = 0.8, 
              color = "#BDBDC3", 
              weight = 1,
              popup = popup_dat,
              group="Cancer Rate/100,000 by Counties") %>% 
  
  addPolygons(fillColor = ~pal(rateB), 
              fillOpacity = 0.8, 
              color = "#BDBDC3", 
              weight = 1,
              popup = popup_datB,
              group="Breast Cancer Rate/100,000 by Counties") %>% 
  
  # Overlay groups
  addCircleMarkers(data=LandUse,lat=~lat, lng=~lng, popup=popup_LU, 
                   radius = 2, fillOpacity = 0.8, group = "Land Use Sites") %>% 
  
  addMarkers(lat=38.9076, lng=-77.0723, popup=popup_GU, 
            group = "Georgetown University") %>% 
  
  addMarkers(lat=37.3875, lng=-122.0575, popup=popup_SV, 
            group = "Silicon Valley") %>% 
  
  # Layers control
  addLayersControl(
    baseGroups = c("Cancer Rate/100,000 by Counties", 
                   "Breast Cancer Rate/100,000 by Counties",
                   "NULL"),
    overlayGroups = c("Land Use Sites", "Georgetown University", "Silicon Valley"),
    options = layersControlOptions(collapsed = FALSE)
  )
gmap

library(htmlwidgets)
saveWidget(gmap, 'leaflet.html')#, selfcontained = TRUE)
