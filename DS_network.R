library(networkD3)
library(jsonlite)

## Convert to list format
DS = fromJSON("Diagonal.json", simplifyDataFrame = FALSE)

radialNetwork(List = DS, fontSize = 16, opacity = 0.9)
Diagonal = diagonalNetwork(List = DS, fontSize = 16, opacity = 0.9)
Diagonal
saveNetwork(Diagonal, "Diagonal.html", selfcontained = TRUE)


## Company acquisitions
library(networkD3)
nodes <- read.csv("acq-nodes.csv", header=T, as.is=T)
links <- read.csv("acq-edges.csv", header=T, as.is=T)

D3 = forceNetwork(Links = links,
                  Nodes = nodes,
                  Source = "acquiring_id",
                  Target = "acquired_id",
                  NodeID = "text",
                  Group = "group",
                  colourScale = JS("d3.scaleOrdinal(d3.schemeCategory10);"),
                  fontSize = 18,
                  linkDistance = 200,
                  Value = "price_million",
                  linkWidth = 2,
                  #linkColour = "tomato",
                  Nodesize = "value_million",
                  opacity = 0.8, zoom = F,
                  opacityNoHover = 0.5)

D3             
saveNetwork(D3, "acq.html", selfcontained = TRUE)
