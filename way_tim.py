#!/usr/bin/env python3

import os 
tm =  str(os.popen("scrntime -d 1").read()).split()


date = [tm[0][-3:], tm[1][:2 ]]
time = [tm[3], tm[4][:2]]
bar = tm[5][7:-7]




s = f"[ {date[0]} {date[1]}   {time[0]}:{time[1]} {bar} ]" 







if __name__ == "__main__":
    output = {
        "text": s,
        "class":"custom-screen_time"
            }
    print(s)







