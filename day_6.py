from collections import deque
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-d","--days",help="num of days",required=True,type=int)
args = vars(ap.parse_args())



INPUT_FILE = "input_6.txt"


def day_6(days,input_file=INPUT_FILE):
    

    class Fish:


        def __init__(self,initial_timer,start_timer=6):
            self.timer = initial_timer
            self.start_timer = start_timer


        def reset(self):
            self.timer = self.start_timer
        

        def update(self):
            
            if self.timer == 0:

                self.timer = self.start_timer

                return Fish(self.start_timer + 2)
            else:
                self.timer -= 1
    

        def __repr__(self):
            return f"Fish({self.timer})"

    with open(input_file,'r') as f:

        values = list(map(lambda x: Fish(int(x)),f.read().split(',')))




    for _ in range(days):
        for fish in values.copy():
            new_fish = fish.update()
            if new_fish:
                values.append(new_fish)


    

    return len(values)








if __name__ == "__main__":

    days = args["days"]
    print(day_6(days))
