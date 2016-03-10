import random
import time

ARRAY_LEN = 30000

def bubble_sort(data):
    changed = True
    while changed:
        changed = 0
        for i in range(len(data)-1):
            if data[i] > data[i + 1]:
                data[i], data[i+1] = data[i+1], data[i]
                changed = True

def sort_array():
    print("Bubble sorting array of {0} elements".format(ARRAY_LEN))
    data = []
    for i in range(ARRAY_LEN):
        data.append(random.randint(0, 2**24))
    # bubble_sort(data)
    data.sort()

start = time.time()
sort_array()
end = time.time()
print("{0} ms".format(int((end-start)*1000)))
