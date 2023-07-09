
import math

def cal_x(x):
    return 2 * x + 4 * math.sqrt(50*50+(50-x)*(50-x))

min_v = 1000
min_x = 1000
for i in range(0,51):
    tmp = cal_x(i)
    if min_v > tmp:
        min_v = tmp
        min_x = i

print(min_x, min_v)