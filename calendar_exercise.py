import time

now = time.asctime(time.localtime(time.time()))
print(now)

now = time.time()
print("Tomorrow will be", time.asctime(time.localtime(now + 60 * 60 * 24 )) )