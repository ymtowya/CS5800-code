import random

# the array to be sorted
# init with random values
D = []
base = []
length = 9
for i in range(1, 2 * length + 1):
    base.append(i)
random.shuffle(base)
D = base[0 : length]


def sortArrayD(myD):
    # get count array
    n = len(myD)
    count = [0] * (2 * n + 1)
    # set the counts
    for v in myD:
        if 2 * n >= v:
            count[v] = 1
    # set the sorted array
    sorted = []
    for i in range(1, 2 * n + 1):
        if count[i] == 1:
            # if it's set to 1 then it exists
            sorted.append(i)
    return sorted

if __name__ == '__main__':
    print("Original array is : ", D)
    print("Sorted array is : ", sortArrayD(D))