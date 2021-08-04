import time
from datetime import datetime

s = "03-aug-21:16:55:00"
timestruct = time.strptime(s, "%d-%b-%y:%H:%M:%S")
myTimeS = time.mktime(timestruct)

current = time.time()
print(current)
print(myTimeS)

if myTimeS < current:
    print("we have passed myTimeS")
else:
    print("We have not passed myTimeS")
