# %%
#Code implementation in python with it's plot. 
import matplotlib.pyplot as plt

def count_integer_points(P, Q):
    po = sum(1 for x in P if x % 2 != 0)
    pe = len(P) - po
    qo = sum(1 for x in Q if x % 2 != 0)
    qe = len(Q) - qo
    return po * qo + pe * qe

def compute_integer_points(P, Q):
    points = []
    for p in P:
        for q in Q:
            if (q - p) % 2 == 0:
                x = (q - p) // 2
                y = x + p
                points.append((x, y))
    return points

def plot_lines_and_points(P, Q, points):

    all_vals = P + Q
    mn = min(all_vals) - 10
    mx = max(all_vals) + 10

    X = range(mn, mx + 1)

    for p in P:
        Y = [x + p for x in X]
        plt.plot(X, Y, linewidth=0.8)

    for q in Q:
        Y = [-x + q for x in X]
        plt.plot(X, Y, linewidth=0.8)

    if points:
        px = [x for x, y in points]
        py = [y for x, y in points]
        plt.scatter(px, py, s=20)

    plt.title("Lines and Integer Intersection Points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

n = int(input("Enter number of p_i values: "))
P = list(map(int, input("Enter p_i values: ").split()))

m = int(input("Enter number of q_i values: "))
Q = list(map(int, input("Enter q_i values: ").split()))

ans = count_integer_points(P, Q)
print("\nTotal integer intersection points =", ans)

points = compute_integer_points(P, Q)

plot_lines_and_points(P, Q, points)