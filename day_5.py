

INPUT_FILE = "input_5.txt"





def day_5(input_file=INPUT_FILE):
    
    def traverse_line(point_1,point_2):




        x1,y1 = point_1
        x2,y2 = point_2

        case_1 = False
        if x1 == x2:
            case_1 = True
            values = (y1,y2)
        else:
            values = (x1,x2)
        
        start,end = sorted(values)
        current = start
        intersections = 0
        while current != end + 1:
            coordinate = (x1,current) if case_1 else (current,y1)
            if coordinate in coordinates:
                if not coordinates[coordinate]:
                    intersections += 1
                    coordinates[coordinate] = True
            else:
                coordinates[coordinate] = False



            current += 1
        return intersections



    num_intersections = 0
    coordinates = {}
    with open(input_file,'r') as f:

        for line in f:

            values = line.split("->")
            
            points = []
            for value in values:
                point = tuple(map(int,value.split(',')))

                points.append(point)

            point_1,point_2 = points
            print(point_1,point_2)


            if (point_1[0] == point_2[0]) or (point_1[1] == point_2[1]):
                num_intersections += traverse_line(point_1,point_2)


    return num_intersections




        


def day_5_part_2(input_file=INPUT_FILE):
    
    def traverse_line(point_1,point_2):




        x1,y1 = point_1
        x2,y2 = point_2



        
        pairs = [[x1,x2],[y1,y2]]

        start_end_diffs = []
        for start,end in pairs:

            if start != end:
                if start < end:
                    diff = 1
                    end += 1
                else:
                    diff = -1
                    end -= 1
            else:
                diff = 0


            start_end_diffs.append((start,end,diff))



    
        
        current_x,end_x,x_diff = start_end_diffs[0]
        current_y,end_y,y_diff = start_end_diffs[1]

        intersections = 0
        while current_x != end_x or  current_y != end_y:
            coordinate = (current_x,current_y)
            if coordinate in coordinates:
                if not coordinates[coordinate]:
                    intersections += 1
                    coordinates[coordinate] = True
            else:
                coordinates[coordinate] = False




            current_x += x_diff
            current_y += y_diff
        return intersections



    num_intersections = 0
    coordinates = {}
    with open(input_file,'r') as f:

        for line in f:

            values = line.split("->")
            
            points = []
            for value in values:
                point = tuple(map(int,value.split(',')))

                points.append(point)

            point_1,point_2 = points


            num_intersections += traverse_line(point_1,point_2)


    return num_intersections


if __name__ == "__main__":

    print(day_5_part_2())
            










        









