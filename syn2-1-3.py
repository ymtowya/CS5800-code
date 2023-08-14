
n = get_num_vertex()
k = get_word_len()
arr = []

# 2-layer loop on each pair of vertices
for v1 in Vertex:
    for v2 in Vertex:
        diff_count = 0
        # inner loop visit each character
        # to determine the transformation to make
        for i in range(k):
            if v1[k] != v2[k]:
                diff_count += 1
        arr.append(diff_count)

dist = [[POS_INF for i in range(n)] for j in range(n)]
# build the edge weight, 
# if connected then set to 1
edges = build_adj_arr(vertices)
for e in edges:
    (u, v) = get_vertex(e)
    dist[u][v] = e.weight
for v in vertices:
    dist[v][v] = 0
for v1 in vertices:
    for v2 in vertices:
        for v3 in vertices:
            # update the shortest path from v1 to v2
            dist[v1][v2] = Math.min(dist[v1][v2], dist[v1][v3] + dist[v2][v3])