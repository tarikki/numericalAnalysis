__author__ = 'extradikke'

data_points = [(0, 0, 1), (1, 1, 3), (3, 3, 2)]
data_points = [(1, 1, -6), (2, 2, 2), (4, 4, 12)]
data_points = [(16, 16, .25), (64, 64, .125), (100, 100, .1)]
data_points = [(0, 0, 2), (1, 1, 2), (4, 4, 160), (9, 9, 2024)]


def approx_poly(x_coordinate, data_points):
    result_set = data_points
    while len(result_set) != 1:
        temp_set = []
        print(result_set)
        for i in range(0, len(result_set) - 1):
            y_coord = ((result_set[i + 1][1] - x_coordinate) * result_set[i][2] + (x_coordinate - result_set[i][0]) *
                       result_set[i + 1][2]) / (result_set[i + 1][1] - result_set[i][0])
            temp_set.append((result_set[i][0], result_set[i + 1][1], y_coord))
            print((result_set[i][0], result_set[i + 1][1], y_coord))
        result_set = temp_set
    print(result_set)
    return result_set[0][2]





if __name__ == '__main__':
        data_points = [(0, 0, 1), (1, 1, 3), (3, 3, 2)]
        x_coordinates = [x for x in range(0,11)]
        coordinates = zip(x_coordinates, [approx_poly(x, data_points) for x in x_coordinates ])
        for thing in coordinates:
            print("%f \t %f" % thing)