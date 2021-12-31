import numpy as np
import re

INPUT_FILE = "input_13.txt"


def fold(grid,direction,line):
    
    rows,cols = len(grid),len(grid[0])

    if direction == 'x':
        if line >= cols -1 :
            return grid
        after_length = cols - line - 1
        
        first_half = grid[:,:line][:,::-1]
        second_half = grid[:,line + 1:]
    else:
        if line >= rows - 1:
            return grid
        after_length = rows - line - 1

        first_half = grid[:line,:]
        second_half = grid[line+1:,:][::-1,:]

    if after_length > line:
        new_grid = second_half
        smaller = first_half
    else:
        new_grid = first_half
        smaller = second_half

    

        
    if direction == 'x':
        difference = new_grid.shape[1] - smaller.shape[1]
        for row in range(0,rows):
            for col in range(0,len(smaller[0])):
                value = smaller[row,col]

                if value  and not new_grid[row,difference + col]:
                    new_grid[row,difference + col] = True
    else:
        difference = new_grid.shape[0] - smaller.shape[0]
        for col in range(0,cols):
            for row in range(0,len(smaller)):
                value = smaller[row,col]

                if value  and not new_grid[difference + row,col]:
                    new_grid[difference + row,col] = True


    return new_grid






def count_dots(grid):

    return (grid.sum())







def day_13(input_file=INPUT_FILE):

    
    coordinates = []
    max_x = max_y = float("-inf")
    folds = []
    with open(input_file,'r') as f:
        for line in f:
            if line != '\n':
                if line.startswith('fold'):
                    match = re.search(r'.=\d+',line).group()
                    type_,number = match.split('=')
                    number = int(number)
                    folds.append((type_,number))
                else:
                    x,y = map(int,line.split(','))
                    coordinates.append((x,y))
                    max_x,max_y = max(max_x,x),max(max_y,y)


    
    grid = np.zeros((max_y + 1,max_x + 1),dtype='bool')

    
    for x,y in coordinates:
        grid[y,x] = True

    
    print(folds)
    for f in folds:
        grid =  fold(grid,*f)
        print(grid.shape)

    for row in grid:
        for col in row[::-1]:
            if col:
                print('#',end=' ')
            else:
                print('.',end=' ')
        print()


if __name__ == "__main__":

    print(day_13())











    


        



