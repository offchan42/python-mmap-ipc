"""
Continuously read images from a memory-mapped file and show them on a window.
"""
import mmap
import time

import cv2 as cv
import numpy as np

shape = (720, 1280, 3)
n = np.prod(shape)
mm = mmap.mmap(-1, n, "ARandomTagName")
while True:
    # read image
    start = time.perf_counter()
    mm.seek(0)
    imgb = mm.read(n)
    img = np.frombuffer(imgb, dtype=np.uint8).reshape(shape)
    stop = time.perf_counter()

    print("Reading Latency:", (stop - start) * 1000, "ms")
    cv.imshow("img", img)
    key = cv.waitKey(1) & 0xFF
    key = chr(key)
    if key == "q":
        break
cv.destroyAllWindows()
mm.close()
