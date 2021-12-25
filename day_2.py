

INPUT_FILE = "input_2.txt"

def day_2(input_file=INPUT_FILE):

    
    horizontal = depth = 0
    with open(input_file,'r') as f:
        for line in f:
            command,number = line.split()
            number = int(number)

            if command == 'forward':
                horizontal += number
            elif command == 'up':
                depth -= number
            else:
                depth += number


    return horizontal*depth



def day_2_part_2(input_file=INPUT_FILE):

    
    horizontal = depth = aim =  0
    with open(input_file,'r') as f:
        for line in f:
            command,number = line.split()
            number = int(number)

            if command == 'forward':
                horizontal += number
                depth += aim * number
            elif command == 'up':
                aim -= number
            else:
                aim += number


    return horizontal*depth


if __name__ == "__main__":

    print(day_2_part_2())






