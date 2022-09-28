def sortingWorks(points,hours):
    import math
    import random
    distances = []
    byDistance = []
    x1 = random.choice(points)
    byDistance.append(points.index(x1))
    for i in points:
        if i != x1:
            distances.append(math.sqrt(((i[0]-x1[0])**2)+((i[1]-x1[1])**2)))
        else:
            distances.append(8000)

    byDistance.append(distances.index(min(distances)))

    distances = []
    x2 = points[byDistance[1]]
    for i in points:
        if i != x2 and i != x1:
            distances.append(math.sqrt(((i[0]-x2[0])**2)+((i[1]-x2[1])**2)))
        else:
            distances.append(8000)

    byDistance.append(distances.index(min(distances)))

    for i in range(len(points)):
        if i not in byDistance:
            byDistance.append(i)

    byHours = sorted(hours, reverse=True)
    return byDistance, byHours


def main():
    points = [[-1,1], [4,5], [2,7], [-4,4]]
    hours = [2.3, 1, 2.5, 0.45]
    byDistance, byHours = sortingWorks(points,hours)
    dictDistance = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    dictHours = {hours[0]: 'A', hours[1]: 'B', hours[2]: 'C', hours[3]: 'D'}
    print('By Distance:')
    print(dictDistance[byDistance[0]], dictDistance[byDistance[1]], dictDistance[byDistance[2]], dictDistance[byDistance[3]])
    print('By Hours:')
    print(dictHours[byHours[0]], dictHours[byHours[1]], dictHours[byHours[2]], dictHours[byHours[3]])

main()