import numpy as np
import matplotlib.pyplot as plt
import json

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

class Sort(object):
    counts = 0

    def insertionSort(self, x):
        arr = np.array(x)
        for i in range(1, x.size):
            j = i
            while j >= 1 and arr[j] < arr[j-1]:
                Sort.counts += 1
                swap(arr, j, j-1)
                j = j - 1
        return arr
    
    def mergeSort(self, arr):
        result = np.array([])
        if arr.size < 5:
            result = self.insertionSort(np.array(arr))
        else:
            result = np.zeros(arr.size)
            halfway = int(arr.size / 2)
            list1 = np.array(arr[0:halfway])
            list2 = np.array(arr[halfway::])
            list1 = self.mergeSort(list1)
            list2 = self.mergeSort(list2)
            i1 = 0
            i2 = 0
            i = 0
            while i1 < list1.size and i2 < list2.size:
                if list1[i1] < list2[i2]:
                    result[i] = list1[i1]
                    i1 += 1
                else:
                    result[i] = list2[i2]
                    i2 += 1
                i += 1
                Sort.counts += 1
            while i1 < list1.size:
                result[i] = list1[i1]
                i1 += 1
                i += 1
                Sort.counts += 1
            while i2 < list2.size:
                result[i] = list2[i2]
                i2 += 1
                i += 1
                Sort.counts += 1
        return result
"""
s = Sort()
np.random.seed(0)

num_per_size = 50
sizes = []
steps1 = []
steps2 = []
for n in range(10, 400):
    print(n)
    for i in range(num_per_size):
        sizes.append(n)
        x = np.random.randint(0, n*2, n)
        x1 = s.insertionSort(x)
        steps1.append(Sort.counts)
        Sort.counts = 0
        x2 = s.mergeSort(x)
        steps2.append(Sort.counts)
        x = np.sort(x)
        if not np.allclose(x, x1):
            print("insertion sort failed")
        if not np.allclose(x, x2):
            print("Merge sort failed")

json.dump({'sizes':sizes, 'steps1':steps1, 'steps2':steps2}, open("steps.txt", "w"))
"""
res = json.load(open("steps.txt"))
sizes, steps1, steps2 = res['sizes'], res['steps1'], res['steps2']

sizes = np.array(sizes)
steps1 = np.array(steps1)
steps2 = np.array(steps2)

plt.figure(figsize=(12, 8))
plt.scatter(steps1, steps2, c=sizes, cmap='afmhot')
plt.xlabel("Insertion Sort Steps")
plt.ylabel("Merge Sort Steps")
plt.title("Merge Sort / Insertion Sort Comparison")
plt.colorbar()
ax = plt.gca()
ax.set_facecolor((0.6, 0.6, 0.6))
plt.savefig("Timings.svg", bbox_inches='tight')