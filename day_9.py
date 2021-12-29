import bisect
from functools import reduce


INPUT_FILE = "input_9.txt"



def day_9(input_file=INPUT_FILE):


    grid = []
    with open(input_file,'r') as f:
        grid = f.readlines()

    
    
    rows = len(grid)
    cols = len(grid[0]) - 1 # ignore new line at end
    
    in_bounds = lambda row,col: 0 <= row < rows and 0 <= col < cols
    
    risk_score_sum = 0
    for row in range(rows):
        for col in range(cols):
            value = grid[row][col]
            adjacent = ((row-1,col),(row +1,col),(row,col -1),(row,col + 1))
            if all(value < grid[adj_row][adj_col] for adj_row,adj_col in adjacent if in_bounds(adj_row,adj_col)):
                risk_score = int(value) + 1
                risk_score_sum += risk_score





    return risk_score_sum







def day_9_2(input_file=INPUT_FILE):


    grid = []
    with open(input_file,'r') as f:
        grid = f.readlines()

    
    def dfs_search(row,col):

        visited.add((row,col))

        
        neighbors = ((row +1,col),(row -1,col),(row,col -1),(row,col +1))
        
        size = 1
        for n_row,n_col in neighbors:
            if in_bounds(n_row,n_col) and grid[n_row][n_col] != '9' and (n_row,n_col) not in visited:
                size += dfs_search(n_row,n_col)



        return size

    
    rows = len(grid)
    cols = len(grid[0]) - 1 # ignore new line at end
    
    in_bounds = lambda row,col: 0 <= row < rows and 0 <= col < cols
    
    visited = set()
    basin_lengths = [float("-inf")] * 3
    for row in range(rows):
        for col in range(cols):
            value = grid[row][col]
            if value != '9' and (row,col) not in visited:
                size = dfs_search(row,col)

                if size > basin_lengths[0]:
                    basin_lengths.pop(0)
                    bisect.insort_left(basin_lengths,size)


    mult = reduce(lambda x,y: x*y,basin_lengths)
    return mult










    


if __name__ == "__main__":


    print(day_9_2())



