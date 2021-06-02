import math


class Polygon:
    def __init__(self):
        self.edge_number = 3
        self.edges_length = []

    def getEdgeNumber(self):
        return self.edge_number

    def setEdgeNumber(self, number):
        self.edge_number = number

    def input_edges(self):
        length = self.edge_number
        for i in range(length):
            value = input(f"Enter length of the edge{i}: ")
            self.edges_length.append(int(value))

    def output_edges(self):
        length = self.edge_number
        edge_list = self.edges_length
        for i in range(length):
            print(f"length of edge{i}: {edge_list[i]}")


class Triangle(Polygon):
    def perimeter(self):
        return sum(self.edges_length)

    def acreage(self):
        p = self.perimeter() / 2
        acr = p
        for item in self.edges_length:
            acr *= (p - item)
        acr = round(math.sqrt(acr), 2)
        return acr


tria = Triangle();
tria.input_edges()
tria.output_edges()
print("perimeter:", tria.perimeter())
print("acreage:", tria.acreage())
