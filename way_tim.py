#!/usr/bin/env python3
import os 


def getCMD():
    cmd1 = " last -R $username |grep  'down'"


    out =  str(os.popen(cmd1).read()).split("\n")[0].split()

    if int(out[4]) < 10:
        s = f"{out[3]}  {out[4]}"
    else:
        s = f"{out[3]} {out[4]}"
    fin_cmd =  " last -R $username |grep '"+s+"'|grep 'down'|awk ' {print $NF }'"
    
    return fin_cmd 



tm =  str(os.popen(getCMD()).read()).split()

hoursL = []
minutesL = []

for hs in tm:
    hoursL.append(int(f"{hs[1]}{hs[2]}"))
    minutesL.append(int(f"{hs[4]}{hs[5]}"))

H = sum(hoursL) + int(sum(minutesL)/60)

M = sum(minutesL)%60


ut =  str(os.popen("uptime").read()).split()
ut = ut[2]
ut = ut.split(":")
H = H + int(ut[0]) 

if(M + int(ut[1].replace(',','')) ) <= 60:
    M = M + int(ut[1].replace(',','')) 
else:
    H = H + 1





s = f"| {H}h  {M}m |"
if __name__ == "__main__":
    output = {
        "text": s,
        "class":"custom-screen_time"
            }

    print(s)
