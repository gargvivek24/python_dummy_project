import time
start = time.time()
start= round(start, 2)
print("Start time is ", start)
import dicegame
time.sleep(5)
end = time.time()
end=round(end, 2)
print("End time is ", end )
execution_time = round(end-start, 2)
print("Time taken by program to execute ", execution_time, " Seconds")
