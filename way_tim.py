#!/usr/bin/env python3

import os 
tm =  str(os.popen("scrntime -d 1 -s 1").read()).split()


date = [tm[0][-3:], tm[1][:2 ]]
time = [tm[3], tm[4][:2]]
bar = int(time[0][0])



if int(time[0][0]) != 9:
    str = f"[ {time[0]}:{time[1]} ]"
else:
    str = "[ GO TOUCH GRASS ]"








if __name__ == "__main__":
    output = {
        "text": str,
        "class":"screen_time"
            }
    print(str)







