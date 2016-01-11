'''

This is Nathan Hughes' entry for Daily programmer
Challenge #248 [Easy] Draw me like one of your bitmaps 

This script will convert inputs into the Netpbm RGB formats 

'''


# Get some input that should look like this:

# X Y Size of the input image 
# Point followed by 5 params ( R, G, B, X, Y) 
# Line followed by 7 params ( R, G, B, X1, Y1, X2, Y2) 
# Rect followed by 7 params (R, G, B, X1, Y1, X2, Y2) 
# Any part of the program not painted can be assumed to be black 


# Small class to create an object for the information given about the image 
class NetpbmImage:
    def __init__(self, width, height):
        # Init to be size of zero
        self.size = [width, height]
        # List of points in the shape, should be 2D list
        self.points = [[Point() for y in range(height + 1)] for x in range(width + 1)]

    def add_point(self, x, y, point):
        if x < self.size[0] and y < self.size[1]:
            self.points[x][y] = point

    def output_data(self):
        # Time to sav to file
        file = open("image.ppm", "w")

        file.write('P3 \n')
        file.write(str(self.size[0]) + ' ' + str(self.size[1]) + '\n')
        file.write('255 \n')

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                for color in self.points[x][y].getColor():
                    file.write(str(color) + ' ')
            file.write('\n')

        file.close()


# Class to represent a single point
class Point:
    def __init__(self):
        self.color = [0, 0, 0]

    def setColor(self, R, G, B):
        self.color = [R, G, B]

    def getColor(self):
        return self.color


# functions to eval best move to make for line
def move_down(x1, y1, x2, y2):
    return abs((x1 + y1+1) - (x2 + y2))


def move_up(x1, y1, x2, y2):
    return abs((x1 + y1-1) - (x2 + y2))


def move_right(x1, y1, x2, y2):
    return abs((x1+1 + y1) - (x2 + y2))


def move_left(x1, y1, x2, y2):
    return abs((x1-1 + y1) - (x2 + y2))


def find_shortest_path(x1, y1, x2, y2):
    # Take the 4 points and return a list of points in between them
    # poss do a while loop doing while != y2 y++ then while != x2 x++ alternate to get zigzag of a line?
    points_to_draw = [[x1, y1]]  # add the initial point

    # gonna try some breadth first searching methods here
    total_distance = abs((x1 + y1) - (x2 + y2))

    while total_distance != 0:

        if move_down(x1, y1, x2, y2) < total_distance:  # if moving down is closer to goal
            if move_right(x1, y1, x2, y2) < total_distance:  # if moving down and right
                x1 += 1
                y1 += 1
            elif move_left(x1, y1, x2, y2) < total_distance:  # if moving down and left
                x1 -= 1
                y1 += 1
            else:  # just move down
                y1 += 1
        elif move_up(x1, y1, x2, y2) < total_distance:  # then moving up is the way to go
            if move_right(x1, y1, x2, y2) < total_distance:  # if moving up and right
                x1 += 1
                y1 -= 1
            elif move_left(x1, y1, x2, y2) < total_distance:  # if moving up and left
                x1 -= 1
                y1 -= 1
            else:  # just move up
                y1 -= 1
        elif move_left(x1, y1, x2, y2 < total_distance):
                x1 -= 1
        else:  # must be right just
            x1 += 1

        points_to_draw.append([x1, y1])
        total_distance = abs((x1 + y1) - (x2 + y2))

    return points_to_draw


def perform_instruction(instruction, image):
    info = instruction.split()  # This will be a list of elements in the inputted instruction

    if 'point' in info[0]:  # if it's a draw point instruction
        tmp_point = Point()  # Create a new point
        tmp_point.setColor(int(info[1]), int(info[2]), int(info[3]))  # Set the color of the point as per instruction
        image.add_point(int(info[4]), int(info[5]), tmp_point)

    elif 'line' in info[0]:  # if it's a draw line instruction
        path = find_shortest_path(int(info[4]), int(info[5]), int(info[6]), int(info[7]))
        for point in path:
            tmp_point = Point()
            tmp_point.setColor(int(info[1]), int(info[2]), int(info[3]))
            image.add_point(point[0], point[1], tmp_point)

    elif 'rect' in info[0]:
        # This is very messy and could be done way way better and I can only aplogise
        if int(info[4]) <= int(info[6]):
            if int(info[5]) <= int(info[7]):
                # This assumes that x1 < x2 and y1 < y2
                for x in range(int(info[4]), int(info[6])+1):
                    for y in range(int(info[5]), int(info[7])+1):
                        tmp_point = Point()
                        tmp_point.setColor(int(info[1]), int(info[2]), int(info[3]))
                        image.add_point(x, y, tmp_point)
            else:
                for x in range(int(info[4]), int(info[6])+1):
                    for y in range(int(info[7]), int(info[5])+1):
                        tmp_point = Point()
                        tmp_point.setColor(int(info[1]), int(info[2]), int(info[3]))
                        image.add_point(x, y, tmp_point)
        else:
            if int(info[5]) <= int(info[7]):
                for x in range(int(info[6]), int(info[4])+1):
                    for y in range(int(info[5]), int(info[7])+1):
                        tmp_point = Point()
                        tmp_point.setColor(int(info[1]), int(info[2]), int(info[3]))
                        image.add_point(x, y, tmp_point)
            else:
                for x in range(int(info[6]), int(info[4])+1):
                    for y in range(int(info[7]), int(info[5])+1):
                        tmp_point = Point()
                        tmp_point.setColor(int(info[1]), int(info[2]), int(info[3]))
                        image.add_point(x, y, tmp_point)

# Call the user to enter in heights and widths

width, height = input('Width and height please').split()

image = NetpbmImage(int(width), int(height))  # Create a new image to be handled

print('Please input the data of the image, end input with "quit" ')

while True:  # Start loop to get input
    command = input()

    # Allow the user to quit
    if 'quit' in command:
        break

    perform_instruction(command, image)


image.output_data()
