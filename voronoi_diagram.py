import numpy as np
import cv2
import random
import math


size = int(input("Size of diagram: "))
gen_point_num = int(input("Number of generating points: "))

grid = np.empty((size, size, 3), int)

gen_points = []

for i in range(gen_point_num):
    # create a generator point, y val, x val, colour
    gen_points.append((random.randrange(size), random.randrange(size),
                       [random.randrange(256), random.randrange(256), random.randrange(256)]))

for y in range(size):
    for x in range(size):
        # calculate maximum euclidean distance
        distance_minimum = math.hypot(size - 1, size - 1)
        j = -1
        for i in range(gen_point_num):
            # calculate euclidean distance to generating point
            distance_to_point = math.hypot(gen_points[i][0] - y, gen_points[i][1] - x)
            if distance_to_point < distance_minimum:
                distance_minimum = distance_to_point
                j = i
        # set the colour value to the closest generator point
        grid[y, x] = gen_points[j][2]

for point in gen_points:
    y, x = point[0], point[1]
    grid[y, x] = [0, 0, 0]

cv2.imwrite("voronoi.png", grid)
