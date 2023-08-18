def addAtms(n, k, distances):

    for _ in range(k):
        max_distance_idx = distances.index(max(distances))
        new_distance = max(distances) // 2
        distances.insert(max_distance_idx, new_distance)
        distances[max_distance_idx + 1] -= new_distance

    return distances


if __name__ == '__main__':

    n = 5
    k = 3
    distances = [100, 180, 50, 60, 150]

    new_distances = addAtms(n, k, distances)

    for distance in new_distances:
        print(distance)