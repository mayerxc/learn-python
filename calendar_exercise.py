import time
import datetime


now = time.asctime(time.localtime(time.time()))
print(now)

now = time.time()
print("Tomorrow will be", time.asctime(time.localtime(now + 60 * 60 * 24 )) )
print("A year ago it was", time.asctime(time.localtime(now - 365 * 60 * 60 * 24 )) )
print("In 100 hours it will be", time.asctime(time.localtime(now + 60 * 60 * 100 )) )

birthday =  datetime.datetime(1978, 10, 5, 7, 10)
print("I was born on", birthday.isoformat(" "))