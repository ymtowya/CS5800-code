


def scaling_maximum_flow(G, s, t, c):
    # flow
    f = {}
    # Residual graph
    Gf = {}
    for e in E:
        f[e] = 0
    # k in the smallest power of 2 greater or equal to c
    k = min_2_power_floor(c)

    while k >= 1:
        # get the residual graph after
        # taking the flow with w capacity
        # Gf[k] = k - residual graph
        Gf[k] = Get_residual_graph(G, f, k)
        # while we can find an augment path P in Gf[k]
        while not find_augmenting_path(Gf[k]).isEmpty():
            p = find_augmenting_path(Gf[k])
            # update the flow
            f = augment(f, c, p)
            Gf[k] = Update_residual_graph(G, f, k)
        k = k / 2
    return f
    