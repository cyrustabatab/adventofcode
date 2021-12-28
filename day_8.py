from collections import defaultdict
INPUT_FILE = "input_8.txt"


# 2,3,4,7


def check_uniqueness(values,letter_to_segment,segments_to_number):

    seen = set()
    for value in values:
        sequence =[letter_to_segment.get(c) for c in value]
        if None not in sequence:
            sequence = tuple(sorted(sequence))
            if sequence in segments_to_number:
                number = segments_to_number[sequence]
                if number in seen:
                    return False
                seen.add(number)
            else:
                return False

    return True



def solve(letters,letters_index,valid_letters,possible_segments,letter_to_segment,segments_to_number,values):

    if not check_uniqueness(values,letter_to_segment,segments_to_number):
        return False

    if letters_index == len(letters):
        return True
    
    
    letter = letters[letters_index]

    
    
    for segment in possible_segments.copy():
        if letter not in valid_letters or segment in valid_letters.get(letter):
            letter_to_segment[letter] = segment
            possible_segments.remove(segment)
            if solve(letters,letters_index + 1,valid_letters,possible_segments,letter_to_segment,segments_to_number,values):
                return True
            possible_segments.add(segment)
            letter_to_segment[letter] = None


    return False










def day_8(input_file=INPUT_FILE):

    



    length_to_segments = {2: {1,5},4: {1,2,3,5},3: {0,2,5},8: set(range(0,7))}

    

    all_ = tuple(range(0,7))








    segments_to_number = {(2,5): 1,(0,1,2,4,5,6): 0,(0,2,3,4,6): 2,(0,2,3,5,6): 3, (1,2,3,5): 4,(0,1,3,5,6): 5,(0,1,3,4,5,6): 6,(0,2,5): 7,all_: 8,(0,1,2,3,5,6): 9}
    

    

    result = 0

    with open(input_file,'r') as f:

        for line in f:
            valid_letters = defaultdict(set)

            first_part,second_part = line.split("|")
            values = first_part.split()

            for value in values:
                if len(value) in length_to_segments:
                    possible_locations = length_to_segments[len(value)]
                    for character in value:
                        valid_letters[character].update(possible_locations)


    


    letter_to_segment = {}
    solve(letters,0,valid_letters,letter_to_segment,segments_to_number)
    

    return result


def day_8_part_2(input_file=INPUT_FILE):


    length_to_segments = {2: {1,5},4: {1,2,3,5},3: {0,2,5},8: set(range(0,7))}

    
    
    letters = ('a','b','c','d','e','f','g')



    all_ = tuple(range(0,7))








    segments_to_number = {(2,5): 1,(0,1,2,4,5,6): 0,(0,2,3,4,6): 2,(0,2,3,5,6): 3, (1,2,3,5): 4,(0,1,3,5,6): 5,(0,1,3,4,5,6): 6,(0,2,5): 7,all_: 8,(0,1,2,3,5,6): 9}
    

    


    result = 0

    sum_ = 0
    with open(input_file,'r') as f:
        for line in f:
            valid_letters = defaultdict(set)

            first_part,second_part = line.split("|")
            values = first_part.split()
            print(values)
            for value in values:
                if len(value) in length_to_segments:
                    possible_locations = length_to_segments[len(value)]
                    for character in value:
                        valid_letters[character].update(possible_locations)
            
            possible_segments = set(range(0,7))
            letter_to_segment = {}
            solve(letters,0,valid_letters,possible_segments,letter_to_segment,segments_to_number,values)

            print(letter_to_segment)            
            values = second_part.split()
            print(values)
            numbers = []
            for value in values:
                sequence =tuple(sorted([letter_to_segment[c] for c in value]))
                number = segments_to_number[sequence]
                numbers.append(str(number))

            number = int(''.join(numbers))
            sum_ += number


    return sum_





    

if __name__ == "__main__":
    
    print(day_8_part_2())






