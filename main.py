import threading
import time
from Window import *
from Path import *

def main():
    window = Window(1000, 1000, "Drawing Curves")
    path = Path(Point(0, 0), Point(500, 500), [Point(12, 125)])
    t1 = threading.Thread(target=window.run)
    t2 = threading.Thread(target=window.draw_path, args=(path,))
    t1.start()
    time.sleep(0.02)
    t2.start()

if __name__ == '__main__':
    main()
