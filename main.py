from Simulation import *
from Node import *

def main():
    project = Simulation(
        1000,
        1000,
        "Drawing curves, but cool",
        Node(Point(0, 0)),
        Node(Point(500, 500)),
        15
    )

    project.start()


if __name__ == '__main__':
    main()
