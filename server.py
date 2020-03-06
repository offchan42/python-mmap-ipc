"""
Continuously read images from webcam and write them to a memory-mapped file.
"""
import mmap
import time

import cv2 as cv

print("Opening camera...")
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

mm = None
print("Writing images to a memory-mapped file...")
try:
    while True:
        ret, img = cap.read()
        if not ret:
            break
        if mm is None:
            mm = mmap.mmap(-1, img.size, "ARandomTagName")

        # write image
        start = time.perf_counter()
        imgb = img.tobytes()
        mm.seek(0)
        mm.write(imgb)
        stop = time.perf_counter()

        print("Writing Latency:", (stop - start) * 1000, "ms")
except KeyboardInterrupt:
    pass
print("Closing resources")
cap.release()
mm.close()
