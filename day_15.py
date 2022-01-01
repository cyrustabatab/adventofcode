import numpy as np

class Vertex:

    def __init__(self,_id,key):
        self.id = _id
        self.key = key
        self.predecessor = None



    def __lt__(self,other):
        if isinstance(other,Vertex):

            return  self.key <= other.key

    
    def __repr__(self):
        return f"Vertex({self.id},{self.key})"

class MinHeap:
    

    def __init__(self):

        self.a = [None]
        self.mapping = {}
    
    def __len__(self):
        return len(self.a) - 1

    def add(self,vertex):
        self.a.append(vertex)
        self.mapping[vertex.id] = len(self)
        self._swim(len(self))

    

    def _sink(self,i):


        while i * 2 <= len(self):
            j = i * 2

            if j + 1 <= len(self) and self.a[j +1] < self.a[j] :
                j += 1


            if self.a[i] > self.a[j]:
                self._swap(i,j)
                i = j
            else:
                break








    
    def _swim(self,i):



        while i // 2 >= 1 and self.a[i] < self.a[i//2]:
            self._swap(i,i//2)
            i //= 2

    
    def _update(self,_id,new_key,new_predecessor):
        index = self.mapping[_id]
        vertex = self.a[index]
        previous_key = vertex.key

        if new_key < previous_key: 
            vertex.key = new_key
            vertex.predecessor = new_predecessor

            self._swim(index)




    
    def pop(self):



        self._swap(1,len(self))

        v = self.a.pop()
        del self.mapping[v.id]

        self._sink(1)



        return v


    def _swap(self,i,j):

        self.a[i],self.a[j]  = self.a[j],self.a[i]
        self.mapping[self.a[i].id] = i
        self.mapping[self.a[j].id] = j



def dijkstra(graph,start,goal):


    min_heap = MinHeap()

    min_heap.add(Vertex(start,0))


    for vertex in graph:
        if vertex != start:
            min_heap.add(Vertex(vertex,float("inf")))








    

    distances,predecessors = {},{}

    while min_heap:
        minimum_vertex = min_heap.pop()
        distance = minimum_vertex.key
        distances[minimum_vertex.id] = distance
        predecessors[minimum_vertex.id] = minimum_vertex.predecessor


        for neighbor in graph[minimum_vertex.id]:
            if neighbor not in distances:
                total_distance = distance + graph[minimum_vertex.id][neighbor]

                min_heap._update(neighbor,total_distance,minimum_vertex.id)


    goal_distance = distances[goal]

    return goal_distance
    














INPUT_FILE = "input_15_1.txt"

def day_15(input_file=INPUT_FILE):


    graph = {}


        

    
    grid = []


    
    grid = None
    with open(input_file,'r') as f:
        
        matrix = f.read().splitlines()

        for i,line in enumerate(matrix):
            v = list(map(int,line))
            array = np.array(v)
            if grid is None:
                grid = array
            else:
                grid = np.vstack((grid,array))

            '''
            for j,value in enumerate(line):
                coordinate = (i,j)

                graph[coordinate] = {}
                if j + 1 < len(matrix[0]):
                    graph[coordinate][(i,j +1)] = int(matrix[i][j +1])
                if i + 1 < len(matrix):
                    graph[coordinate][(i + 1,j)] = int(matrix[i + 1][j])
            '''
    
    grids= [grid + i for i in range(5)]
    grid = np.hstack(grids)

    grid = np.where(grid >= 10,grid %10 + 1,grid)



    grids = [grid + i for i in range(5)]

    grid = np.vstack(grids)


    
    grid = np.where(grid >= 10,grid % 10 + 1,grid)
    
    rows,cols = grid.shape[0],grid.shape[1]

    for row in range(rows):
        for col in range(cols):
            coordinate = (row,col)
            graph[coordinate] = {}
            if col + 1 < cols:
                graph[coordinate][(row,col +1)] = int(grid[row,col +1])
            if row + 1 < rows:
                graph[coordinate][(row + 1,col)] = int(grid[row + 1,col])

    
    start = (0,0)
    goal = (rows - 1,cols -1)

    graph[goal] = {}



    return dijkstra(graph,start,goal)



if __name__ == "__main__":

    print(day_15())

