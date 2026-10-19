
V = 4
INF = 99999

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

dist = [row[:] for row in graph]

for k in range(V):
    for i in range(V):
        for j in range(V):
            if (dist[i][k] != INF and
                dist[k][j] != INF and
                dist[i][k] + dist[k][j] < dist[i][j]):

                dist[i][j] = dist[i][k] + dist[k][j]

print("Shortest Distance Matrix:")

for i in range(V):
    for j in range(V):
        if dist[i][j] == INF:
            print("INF", end="\t")
        else:
            print(dist[i][j], end="\t")
    print()

print("EN.No: 92460118673")