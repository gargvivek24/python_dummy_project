game=int(input("Enter which game you wish to play 1 for diceguess 2 for rock paper scissors"))
if game==1:
    import time
    start = time.time()
    start= round(start, 2)
    print("Start time is ", start)
    exec(open("dicegame.py").read())
    time.sleep(5)
    end = time.time()
    end=round(end, 2)
    print("End time is ", end )
    execution_time = round(end-start, 2)
    print("Time taken by program to execute ", execution_time, " Seconds")
elif game==2:
    exec(open("rock_paper_scissors.py").read())