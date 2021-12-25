

INPUT_FILE = "input.txt"


def day_1(input_file=INPUT_FILE):

    previous = float("inf")
    increases = 0
    with open(input_file,'r') as f:

        for line in f:
            score = int(line)

            if score > previous:
                increases += 1


            previous = score



    return increases


def day_1_part_2(input_file=INPUT_FILE):


    previous_three_window = float("inf")
    increases = 0
    

    with open(input_file,'r') as f:
        scores = []
        for _ in range(3):

            score = int(next(f))
            scores.append(score)

        
        previous_sum = sum(scores)
        score_1,score_2,score_3 = scores


        for score in f:
            score = int(score)
            current_sum = previous_sum - score_1 + score
            score_1,score_2,score_3 = score_2,score_3,score

            if current_sum > previous_sum:
                increases += 1

            previous_sum = current_sum




    return increases














if __name__ == "__main__":


    print(day_1_part_2())









