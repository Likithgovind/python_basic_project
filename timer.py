import time
my_time=int(input("enter the time: "))
for i in range(my_time,0,-1):
    seconds=i%60
    minute=int(i/60)%60
    hours=int(i/3600)
    print(f"{hours:02}:{minute:02}:{seconds:02}")
    time.sleep(1)

#
print("TIME's  UP")