import collections


def read_input():
    return [list(map(lambda x: x.replace("\n", ""), i.split(','))) for i in open("day3_input.txt")]


def distance(p1, p2):
    _v1 = abs(abs(p1[0]) - abs(p2[0]))
    _v2 = abs(abs(p1[1]) - abs(p2[1]))
    return _v1 + _v2


def get_comparator(point):
    def func(p):
        return distance(point, p)
    return func


def find_intersections(point_list):
    mp = collections.Counter(point_list)
    return list(set(list(filter(lambda x: mp[x] > 1, point_list))))


def grab_points(point, direction, limit):
    lst = []
    for i in range(1, limit+1):
        new_x = point[0] + (direction[0]*i)
        new_y = point[1] + (direction[1]*i)
        lst.append((new_x, new_y))
    return lst


def trace(point, line, intersection, direction_map):
    rt = 0
    for i in line:
        points = grab_points(point, direction_map[i[0]], int(i[1:]))
        for p in range(len(points)):
            if points[p] == intersection:
                rt += (p+1)
                return rt
        point = points[-1]
        rt += len(points)
    return -1


direction_map = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

inputs = read_input()
line1, line2 = inputs[0], inputs[1]
line1_points = []
line2_points = []
current_point = (0, 0)

for i1 in line1:
    res = grab_points(current_point, direction_map[i1[0]], int(i1[1:]))
    current_point = res[-1]
    line1_points += res

current_point = (0, 0)
for i2 in line2:
    res = grab_points(current_point, direction_map[i2[0]], int(i2[1:]))
    current_point = res[-1]
    line2_points += res


intersections = list(set(line1_points).intersection(set(line2_points)))

line1_dist = [trace((0, 0), line1, i, direction_map) for i in intersections]
line2_dist = [trace((0, 0), line2, i, direction_map) for i in intersections]

zipped_dist = list(zip(line1_dist, line2_dist))
zipped_dist.sort(key=lambda x: sum(x))
print(zipped_dist[:5])
print([sum(i) for i in zipped_dist[:5]])
exit()


intersections.sort(key=get_comparator((0, 0)))
print(intersections[:5])
print(distance((0,0), intersections[0]))



