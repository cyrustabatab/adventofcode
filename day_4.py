from collections import defaultdict


INPUT_FILE = "input_4.txt"



def day_4(input_file=INPUT_FILE):

    

    with open(input_file,'r') as f:

        numbers = f.readline().split(',')

        
        board_to_rows = {}
        
        number = -1
        num_rows = None
        for line in f:
        
            if line == '\n':
                number += 1
                row_number = 0

                if number != 0:
                    if not num_rows:
                        num_rows = len(rows)
                    rows.extend(cols.values())
                    
                    board_to_rows[number] = rows
                
                rows = []

                cols = defaultdict(set)
            else:
                
                row =set()
                for i,number_ in enumerate(line.split()):
                    row.add(number_)
                    cols[i].add(number_)



                
                rows.append(row)



    
        # for last board
        rows.extend(cols.values())

        
        board_to_rows[number] = rows
    


        def calculate_score(board,number):
            
            sum_ = 0
            
            for i in range(num_rows):
                row = board[i]
                sum_ += sum(map(int,row))

            return sum_ * number 
        
        for number in numbers:
            keys_to_remove  = []
            keys = list(board_to_rows.keys())
            for key in keys:
                board = board_to_rows[key]
                for values in board:
                    if number in values:
                        values.remove(number)
                        if not values:
                            win =  calculate_score(board,int(number))
                            del board_to_rows[key]
                            break






        return win









if __name__ == "__main__":


    print(day_4())











