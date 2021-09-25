# regression function:
def xy_regression(points):
    xy_data = []
    x = []
    y = []
    xy = []
    x2 = []
    y2 = []

    x_sum = 0
    y_sum = 0
    xy_sum = 0
    x2_sum = 0
    y2_sum = 0

    for point in points:
        xy_data.append(point)

    for point in xy_data:
        xy.append(point[0] * point[1])
        x2.append(point[0] * point[0])
        y2.append(point[1] * point[1])
        x.append(point[0])
        y.append(point[1])

    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = sum(xy)
    x2_sum = sum(x2)
    y2_sum = sum(y2)

    a = (y_sum * x2_sum) - (x_sum * xy_sum)
    a /= (len(xy_data) * x2_sum) - (x_sum * x_sum)

    b = (len(xy_data) * xy_sum) - (x_sum * y_sum)
    b /= (len(xy_data) * x2_sum) - (x_sum * x_sum)

    # print("y = " + str(a) + " + (" + str(b) + ")x")
    return [a, b]


# get line value
def get_line_value(x, line):
    return (line[1] * x) + line[0]







# ---------------------------------------------
data = []
data.append([65, 132, 7.6])
data.append([68, 140, 7.4])
data.append([70, 145, 7.1])
data.append([72, 145, 6.5])
data.append([74, 145, 6.3])


# print data
# print("x1,  x2,  y")
# for point in data:
#     print(point)


# define x,y lists and model
xy_lists = []         # where we store individual (x,y) coordinate lists
model = []            # where we store the lines of best fit, each model index corresponds to a point in the prediction


# print x1 and x2 lists
# for i in range(0, len(data[0]) - 1):
#     for j in range(0, len(data)):
#         print(data[j][i])
#     print("----")


# populate xy_lists with x1 and x2 lists with corresponding outputs
for i in range(0, len(data[0]) - 1):
    xy_data = []
    for j in range(0, len(data)):
        x = data[j][i]
        y = data[j][len(data[0]) - 1]
        xy_data.append([x, y])
    xy_lists.append(xy_data)


# print individual lists
# for xy_list in xy_lists:
#     print(xy_list)


# find the line of best fit for each individual list within the 2d array, then append it to the model
for xy_list in xy_lists:
    line = xy_regression(xy_list)
    model.append(line)


# look at the lines in the model (a + bx)
# for line in model:
#     a = line[0]    # intercept
#     b = line[1]    # slope
#     print("y = " + str(a) + " + (" + str(b) + ")x")


# predict a new data point
point = [72, 140]
result = 0
for i in range(0, len(point)):
    result += get_line_value(point[i], model[i])
result /= len(point)
print("prediction: " + str(result))