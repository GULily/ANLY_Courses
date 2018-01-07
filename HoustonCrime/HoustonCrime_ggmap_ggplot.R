library(maps)
library(ggplot2)
library(ggmap)

head(crime)
dim(crime)
str(crime)
table(crime$offense)

# subset: violent crimes
violent_crimes = subset(crime, offense %in% 
                          c("aggravated assault", "murder", "rape", "robbery"))
dim(violent_crimes)
# reorder levels of crimes
violent_crimes$offense = factor(violent_crimes$offense, 
                                levels = c("robbery", "aggravated assault",
                                           "rape", "murder"))

houston = get_map(location = "Houston, Texas", zoom = 14, source = "osm")
ggmap(houston)
ggmap(houston) + geom_point(data = violent_crimes,
                      aes(x=lon, y=lat, color=offense)) +#size=offense
  ggtitle("Houston crime from January 2010 to August 2010")

ggmap(houston) + stat_bin2d(data = violent_crimes,
                            aes(x=lon, y=lat, color=offense, fill=offense),
                            size=.5, bins=50, alpha=.5) +
  ggtitle("Houston crime from January 2010 to August 2010")

