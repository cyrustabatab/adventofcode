from collections import Counter


INPUT_FILE = "input_14.txt"


def day_14(input_file=INPUT_FILE):

    

    rule_to_addition = {}
    with open(input_file,'r') as f:
        
        polymer = next(f).strip()
        next(f)

        for line in f:
            line = line.strip()

            characters,addition = line.split(' -> ')
            rule_to_addition[characters] = addition


    
    counts = Counter(polymer)

    num_steps = 40


    
    for _ in range(num_steps):
        new_polymer = []
        for i in range(len(polymer) - 1):
            new_polymer.append(polymer[i])
            pair = polymer[i:i +2]
            if pair in rule_to_addition:
                character = rule_to_addition[pair]
                new_polymer.append(character)
                counts[character] += 1
        new_polymer.append(polymer[-1])

        polymer = ''.join(new_polymer)
    

    minimum = float("inf") 
    maximum = float("-inf")
    for character,count in counts.items():
        if  count < minimum:
            minimum = count
        if count > maximum:
            maximum = count

    
    print(counts)
    return maximum - minimum


def day_14_2(input_file=INPUT_FILE):

    
    pair_counts = Counter()
    counts= Counter()
    rule_to_addition = {}
    with open(input_file,'r') as f:
        polymer = next(f).strip()


        for i in range(len(polymer)-1):
            pair = polymer[i:i +2]
            pair_counts[pair] += 1
            counts[polymer[i]] += 1


        counts[polymer[-1]] += 1

        next(f) # skip blank line

        for line in f:

            line = line.strip()

            rule,addition = line.split(" -> ")
            rule_to_addition[rule] = addition




    
    num_steps = 40


    for _ in range(num_steps):
        for pair,count in pair_counts.copy().items():
            if pair in rule_to_addition:
                character_to_add =rule_to_addition[pair]
                new_pairs = (pair[0] + character_to_add,character_to_add + pair[1])
                for new_pair in new_pairs:
                    pair_counts[new_pair] += count

                pair_counts[pair] -= count

                counts[character_to_add] += count




    max_count = max(counts.values())
    min_count = min(counts.values())


    return max_count - min_count


















if __name__ == "__main__":

    print(day_14_2())
