# Create a networkD3
library(networkD3)
nodes <- read.csv("network/nodes.csv", header=T, as.is=T)
links <- read.csv("network/edges.csv", header=T, as.is=T)


D3 = forceNetwork(Links = links,
             Nodes = nodes,
             Source = "country",
             Target = "natlty1",
             NodeID = "name",
             Group = "id",
             fontSize = 20)

D3             
saveNetwork(D3, "D3since2000.html", selfcontained = TRUE)
