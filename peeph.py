class Op:
    def __init__(self, l, r):
        self.l = l
        self.r = r


def main():
    op = [Op("a", "9"), Op("b", "c+d"), Op("e", "c+d"), Op("f", "b+e"), Op("r", "f")]
    pr = []
    z = 0
    n = len(op)

    print("Intermediate Code")
    for item in op:
        print(f"{item.l}={item.r}")

    for i in range(n - 1):
        temp = op[i].l
        for j in range(n):
            if temp in op[j].r:
                pr.append(Op(op[i].l, op[i].r))
                z += 1
    pr.append(Op(op[n - 1].l, op[n - 1].r))
    z += 1

    print("\nAfter Dead Code Elimination")
    for item in pr:
        print(f"{item.l}\t={item.r}")

    for m in range(z):
        tem = pr[m].r
        for j in range(m + 1, z):
            if pr[j].r in tem:
                t = pr[j].l
                pr[j].l = pr[m].l
                for i in range(z):
                    if t in pr[i].r:
                        a = pr[i].r.index(t)
                        print(f"pos: {a}")
                        pr[i].r = pr[i].r[:a] + pr[m].l + pr[i].r[a + 1 :]

    print("Eliminate Common Expression")
    for item in pr:
        print(f"{item.l}\t={item.r}")

    for i in range(z):
        for j in range(i + 1, z):
            if pr[i].r == pr[j].r and pr[i].l == pr[j].l:
                pr[i].l = ""

    print("Optimized Code")
    for item in pr:
        if item.l:
            print(f"{item.l}={item.r}")


if __name__ == "__main__":
    main()
