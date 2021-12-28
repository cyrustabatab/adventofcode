

INPUT_FILE = "input_7.txt"

def day_7(input_file=INPUT_FILE):
    

    with open(input_file,'r') as f:
        crabs = list(map(int,f.read().split(',')))




    crabs.sort() 
    if len(crabs) % 2 == 0:
        median = (crabs[len(crabs)//2 -1] + crabs[len(crabs)//2])//2
    else:
        median = crabs[len(crabs)//2]


    fuel_spent = 0 


    for value in crabs:
        fuel_spent += abs(value -median)
    


    return fuel_spent



def day_7_part_2(input_file=INPUT_FILE):


    with open(input_file,'r') as f:
        crabs = list(map(int,f.read().split(',')))

    minimum = min(crabs)
    maximum = max(crabs)

    min_cost = float("inf")
    for position in range(minimum,maximum + 1):
        cost = 0
        for crab in crabs:
            distance = abs(crab - position)
            cost += (distance * (distance + 1))/2
        if cost < min_cost:
            min_cost = cost
    


    return min_cost










if __name__ == "__main__":


    print(day_7_part_2())


