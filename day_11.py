

INPUT_FILE = "input_11.txt"


def day_11(input_file=INPUT_FILE):


    
    grid =[]
    with open(input_file,'r') as f:
        for line in f:
            grid.append(list(map(int,line.strip())))

    

    in_bounds = lambda row,col: 0 <= row <len(grid) and 0 <= col < len(grid[0])

    
    def flash_neighbors(flashed_row,flashed_col):

        
        flashed.add((flashed_row,flashed_col))
        grid[flashed_row][flashed_col] = 0

        for row_diff in range(-1,2):
            for col_diff in range(-1,2):
                adj_row = flashed_row + row_diff
                adj_col = flashed_col + col_diff

                if in_bounds(adj_row,adj_col) and (adj_row,adj_col) not in flashed:
                    grid[adj_row][adj_col] += 1
                    if grid[adj_row][adj_col] > 9:
                        flash_neighbors(adj_row,adj_col)




    times= 100


    num_flashes = 0 
    num_octupuses = len(grid) * len(grid[0])
    i = 0
    while True:
        i += 1 
        flashed = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                value = grid[row][col]
                grid[row][col] += 1
                if grid[row][col] > 9:
                    flashed.add((row,col))


        for flashed_row,flashed_col in flashed.copy():
            flash_neighbors(flashed_row,flashed_col)
            if len(flashed) == num_octupuses:
                return  i










if __name__ == "__main__":


    print(day_11())






