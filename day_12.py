from collections import defaultdict

INPUT_FILE = "input_12.txt"


def day_12(input_file=INPUT_FILE):

    

    def dfs_search(current):
        
        if current == goal:
            return 1


        paths = 0
        for neighbor in graph[current]:
            if neighbor not in visited:
                not_in_upper = neighbor not in upper
                if not_in_upper:
                    visited.add(neighbor)
                paths += dfs_search(neighbor)
                if not_in_upper:
                    visited.remove(neighbor)





        return paths



    graph = defaultdict(set)
    upper = set()

    with open(input_file,'r') as f:
        for line in f:
            line = line.strip()
            v1,v2 = line.split('-')
            if v1.isupper():
                upper.add(v1)

            graph[v1].add(v2)
            graph[v2].add(v1)
    

    
    
    start = 'start'
    goal = 'end'
    visited = {start}

    paths = dfs_search(start)


    return paths


def day_12_part_2(input_file=INPUT_FILE):

    

    def dfs_search(current,two_small_visits=False):
        
        if current == goal:
            return 1


        paths = 0
        for neighbor in graph[current]:
            if neighbor not in upper:
                if neighbor in visited:
                    if neighbor not in start_end and not two_small_visits:
                        two_small_visits = True
                        paths += dfs_search(neighbor,two_small_visits)
                        two_small_visits = False
                else:
                    visited.add(neighbor)
                    paths += dfs_search(neighbor,two_small_visits)
                    visited.remove(neighbor)
            else:
                paths += dfs_search(neighbor,two_small_visits)





        return paths



    graph = defaultdict(set)
    upper = set()

    with open(input_file,'r') as f:
        for line in f:
            line = line.strip()
            v1,v2 = line.split('-')
            if v1.isupper():
                upper.add(v1)

            graph[v1].add(v2)
            graph[v2].add(v1)
    

    
    
    start = 'start'
    goal = 'end'
    start_end = {start,goal}
    visited = {start}

    paths = dfs_search(start)


    return paths





if __name__ == "__main__":


    print(day_12_part_2())



















