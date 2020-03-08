# python-mmap-ipc

This repository is an example on how to do fast inter-process
communication using memory mapped file in python. It is designed to be
a minimal learning material that will help you understand memory mapped file
quicker.

It shows you how to send an image from one python process to another python
process with total delay of around 3-4 milliseconds.
The image shape is 1280x720 and is RGB.

This code can be used for streaming video content from one process to another.

## Getting started

There are 2 main files: `server.py` and `client.py`

- `server.py` will read the image from a webcam (at index 0) and continuously
  writes images as bytes to a memory mapped file.
- `client.py` will continuously read the memory mapped file as bytes, convert
  them back to an image, and show the image.

1. Run `python server.py` on a command prompt.
2. Run `python client.py` on another command prompt.
3. You will see the image webcam content being shown in an OpenCV window.
4. Go and inspect how the code is working. It's a short code so you will
  understand pretty quick. Then you can apply the idea to your work.

Note that you can can run multiple clients to see multiple windows.

## Exercise

Because this repository is designed to be _minimal_, it does not show you
the best practice or a well designed protocol. There are many features that you
can add and it will improve the performance of the code.

Thus, the following improvements are left as exercise for reader:

- Write the shape and dtype of the image into the file, so that any kind of
  image shape is supported.
- Make the client read the image only if it's new. This can be done by
  putting a counter/timestamp number into the file and check it against
  your previous image's counter/timestamp.
- Write timestamp into the file, and when you read the image, subtract the new
  timestamp by the file's timestamp, that will tell your true latency.
- Write client in other language that supports memory mapped file. You should
  be able to read the image from the python server.
- Lock the file or make sure the file is completely written before reading to
  ensure that the reader does not read the file while it's being written.
  Or you can add timestamp at the front and back of the file and compare their
  equality. If they are equal when reading, it means the file is written
  completely.

## Requirements

- numpy
- opencv-python

## Pros of memory-mapped file

- Memory-mapped file feature exists in other programming
languages. It means that you can communicate between any language that supports
this feature.
- It's faster than writing/reading from a file on a disk.
- It's faster than using internet protocol like TCP/IP, HTTP, etc.

The downside is that you need to come up with your own protocol of managing
the file. And it's still slower than shared-memory in the same programming
language.
