import heapq as hp
import math

def Find_Median(arr):
    # this should be linear O(n) using QuickSelect Algorithm
    # but for testing simplicity we use a O(nlogn) simple way here
    # The problem assumes this is given as completed by O(n)
    new_arr = arr.copy()
    new_arr.sort()
    k = math.floor((len(new_arr) - 1) // 2)
    return new_arr[k]

class HeapForMedian:

    # initialize
    def __init__(self):
        # max_heap stores the left half of the array
        # in its negated value so we can take use of the
        # heapq library built-in of Python
        self.max_heap = []
        # min_heap stores the right half of the array
        self.min_heap = []

    def Insert(self, val):
        if not self.max_heap or val < self.max_heap[0]:
            # left half is empty of the value is less than the max of left
            # becuase the build-in heapq only builds min_heap, so we here
            # negate the value and store it into the heap
            hp.heappush(self.max_heap, -val)
        else:
            hp.heappush(self.min_heap, val)

        # adjust the depth so size difference <= 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            # pop the max of left half
            left_max = hp.heappop(self.max_heap)
            # transfer to right half
            hp.heappush(self.min_heap, -left_max)
        elif len(self.min_heap) >  len(self.max_heap) + 1:
            right_min = hp.heappop(self.min_heap)
            hp.heappush(self.max_heap, -right_min)

    def Peek(self):
        if len(self.min_heap) <= len(self.max_heap):
            # we pick the lower median
            return -self.max_heap[0]
        else:
            return self.min_heap[0]

    def Extract(self):
        value = -self.max_heap[0]
        if len(self.min_heap) <= len(self.max_heap):
            # we pick the lower median
            # then heappop the value
            hp.heappop(self.max_heap)
        else:
            value = self.min_heap[0]
            hp.heappop(self.min_heap)
        return value
    
    def Build(self, S):
        # Find median value within O(n)
        md_value = Find_Median(S)
        self.max_heap = []
        self.min_heap = []
        for v in S:
            if v <= md_value:
                self.max_heap.append(-v)
            else:
                self.min_heap.append(v)
        # heapify is O(n)
        hp.heapify(self.max_heap)
        hp.heapify(self.min_heap)

if __name__ == '__main__':
    arr = [5, 9, 1, 6, 2, 11, 4, 7]
    median_hp = HeapForMedian()
    median_hp.Build(arr)
    md_v = median_hp.Extract()
    print("The median value now should be 5, while the poped out value is: ", md_v)
    md_v = median_hp.Extract()
    print("The median value now should be 6, while the poped out value is: ", md_v)
    md_v = median_hp.Peek()
    print("The median value now should be 4, while the peek value is: ", md_v)
    median_hp.Insert(8)
    print("We just inserted 8")
    md_v = median_hp.Peek()
    print("The median value now should be 7, while the peek value is: ", md_v)
    md_v = median_hp.Extract()
    md_v = median_hp.Extract()
    print("The median value now should be 4, while the poped out value is: ", md_v)
    md_v = median_hp.Peek()
    print("The median value now should be 8, while the peek value is: ", md_v)