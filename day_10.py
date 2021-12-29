INPUT_FILE = "input_10.txt"

def day_10(input_file=INPUT_FILE):

        
    score_mapping = {')': 1,']': 2,'}': 3,'>': 4}


    closing_to_opening = {')': '(',']': '[','}': '{','>': '<'}


    score = 0


    
    stack = []
    with open(input_file,'r') as f:

        for line in f:


            for i in range(len(line) - 1):
                character = line[i]
                if character not in closing_to_opening:
                    stack.append(character)
                else:
                    opening = stack.pop()

                    if opening != closing_to_opening[character]:
                        score += score_mapping[character]
                        break



    return score


def day_10_2(input_file=INPUT_FILE):

        
    score_mapping = {')': 1,']': 2,'}': 3,'>': 4}

    closing_to_opening = {')': '(',']': '[','}': '{','>': '<'}
    opening_to_closing = {value: key for key,value in closing_to_opening.items()}




    scores = [] 
    with open(input_file,'r') as f:

       
       for line in f:
            stack = []
            score = 0

            for i in range(len(line) - 1):
                character = line[i]
                if character not in closing_to_opening:
                    stack.append(character)
                else:
                    opening = stack.pop()
                    if opening != closing_to_opening[character]:
                        break
            else:
                if stack:
                    for character in reversed(stack):
                        closing = opening_to_closing[character]
                        score *= 5
                        score += score_mapping[closing]

                    scores.append(score)


    scores.sort()


    middle = scores[len(scores)//2]


    return middle




        





if __name__ == "__main__":


    print(day_10_2())
    
