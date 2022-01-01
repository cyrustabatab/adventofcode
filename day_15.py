
INPUT_FILE = "input_15.txt"

def day_15(input_file=INPUT_FILE):


    graph = {}



    with open(input_file,'r') as f:
        
        matrix = f.read().splitlines()
        for i,line in enumerate(matrix):
            for j,value in enumerate(line):
                coordinate = (i,j)

                graph[coordinate] = {}
                if j + 1 < len(matrix[0]):
                    graph[coordinate][(i,j +1)] = matrix[i][j +1]
                if i + 1 < len(matrix):
                    graph[coordinate][(i + 1,j)] = matrix[i + 1][j]



    print(graph)









if __name__ == "__main__":

    day_15()

