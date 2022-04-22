class graph:
    def __init__(self, weighted, directed):
            self.dict = {}
            self.weighted = weighted
            self.directed = directed

    def addVertex(self, label):
        if label not in self.dict:
            self.dict[label] = []
            return True
        return False

    def addEdge(self, source, destination, weight):
        if self.weighted == False:
            weight = -1
        if source not in self.dict or destination not in self.dict:
            print("Source or Destination Vertex not in graph...")
            return False
        self.dict[source].append((destination, weight))
        print(source + " - " + destination + " Edge has added weight: " + str(weight))
        if self.directed == False:
            self.dict[destination].append((source, weight))
            print(destination + " - " + source + " Edge has added because it is not directed graph weight: " + str(weight))
        return True

    def printGraph(self):
        for key, value in self.dict.items():
            print(key + " => ",end = " ")
            for x in value:
                print(x[0] + " (" + str(x[1]) + ")", end = " ")
            print("")

gp = graph(True, False)
gp.addVertex('A')
gp.addVertex('B')
gp.addVertex('C')

gp.addEdge('A', 'B', 10)
gp.addEdge('A', 'C', 7)
gp.addEdge('B', 'C', 2)

gp.printGraph()


print(gp.dict)