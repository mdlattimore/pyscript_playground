import random
from pprint import pprint
from matplotlib import pyplot as plt


def point_on_triangle(a, b, c):
    """
    Random point in the triangle with vertices a, b and c.
    """
    x, y = sorted([random.random(), random.random()])
    s, t, u = x, y - x, 1 - y
    return (s * a[0] + t * b[0] + u * c[0],
            s * a[1] + t * b[1] + u * c[1])
def draw():
    a = (0, 10.4)
    b = (-6, 0)
    c = (6, 0)
    num_dots = int(Element('number').value)
    corners = [a, b, c]
    random_start = point_on_triangle(a, b, c)
    points = [a, b, c, random_start]
    for n in range(num_dots):
        corner = random.choice(corners)
        new_point = (round(((points[-1][0] + corner[0]) / 2), 4), round(((points[-1][1] + corner[1]) / 2), 4))
        points.append(new_point)

    xmin, xmax, ymin, ymax = -6, 6, 0, 10

    fig, ax = plt.subplots(figsize=(7, 7))
    plt.subplots_adjust(bottom=.3)
    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect="equal")
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    x, y = zip(*points)
    plt.title(f"{num_dots} Dots")
    plt.scatter(x, y, s=1)
    
    display(plt, target="display", append=False) # set append to False to clear div before displaying new plot