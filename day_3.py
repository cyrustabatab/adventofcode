from collections import defaultdict
from collections.abc import Iterable


INPUT_FILE = "input_3.txt"



def day_3(input_file=INPUT_FILE):

    counts = defaultdict(int)
    num_lines = 0
    gamma = epsilon = 0
    with open(input_file,'r') as f:
        for line in f:
            num_lines += 1
            for i,value in enumerate(line):
                if value == '1':
                    counts[i] += 1

    print(counts)
    num_bits = len(counts)
    for i in range(num_bits):
        one_count = counts[i]
        zero_count = num_lines - one_count
        
        

        value = 1 << (num_bits -1 -  i)
        if one_count > zero_count:
            gamma ^= value
        else:
            epsilon ^= value
           

    

    return gamma * epsilon

def day_3_part_2(input_file=INPUT_FILE):

    

    def get_most_common(l: Iterable[str],i=0):
        
        mapping = defaultdict(list)
        one_count = num_lines = 0
        for line in l:
            num_lines += 1
            one_count += (line[i] == '1')
            mapping[line[i]].append(line)

        zero_count = num_lines - one_count

        if one_count >= zero_count:
            first,second = '1','0'
        else:
            first,second = '0','1'

        return mapping[first],mapping[second]

    mapping = defaultdict(list)
    one_count = 0
    numbers = []
    num_lines = 0
    bit_criteria = {} 

    with open(input_file,'r') as f:


        first,second = get_most_common(f)


    

    bit_criteria['co2'] = first
    bit_criteria['oxygen'] = second

    bit_position = 1 


    while any(len(l) > 1 for l in bit_criteria.values()):

        for criteria,value in bit_criteria.items():
            if len(value) > 1:
                first,second = get_most_common(value,bit_position)
                
                if criteria == 'co2':
                    bit_criteria[criteria] = first
                else:
                    bit_criteria[criteria] = second

        bit_position += 1
        
        print(bit_criteria)

    print(bit_criteria)
    value_1,value_2 = map(lambda x: int(x[0],2),bit_criteria.values())



    return value_1 * value_2


















    
    








if __name__ == "__main__":


    print(day_3_part_2())


