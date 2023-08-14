import random

# the array to be sorted
C = []
# generate random value into it (from 1~7)
valueOptions = [1,2,3,4,5,6,7]
for i in range(0, 14):
    C.append(random.choice(valueOptions))

def sortArrayC(myC):
    # keep track of the count
    count = [0] * 8
    for v in myC:
        if v >= 1 and v <= 7:
            # increment the count of this value
            count[v] += 1
    sorted = []
    for i in range(1, 8):
        for j in range(0, count[i]):
            # append value for times based on its count
            sorted.append(i)
    return sorted

if __name__ == '__main__':
    print("Original array is : ", C)
    print("Sorted array is : ", sortArrayC(C))