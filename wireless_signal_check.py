import subprocess
import re
from tabulate import tabulate
import time
import csv
import sys

# https://www.youtube.com/watch?v=TXM9Di6BF-I&t=2s

counter=input('enter the counter value \n ')
signal=''
signal_total=0
ssid="null"
path =raw_input('enter the file path  for log files \n')
path1=raw_input('enter the file path  for csv files \n')
fo=open(path,'w+')
sandcsv=open(path1,'wb')
writer=csv.writer(sandcsv)
writer.writerow(('Iteration','signal','BSSID','SSID'))
print('='*100)


#try:
#    os.remove(path)
#except:
#    print ('file not there')

for i in range(1,counter+1):
    # Get the output of netsh show wlan  for signal and SSID
    for j in range(0,11):
        try:
            signal =subprocess.check_output('netsh wlan show interface | FIND "Signal"',shell=True)
            SSID_all =subprocess.check_output('netsh wlan show interface | FIND "SSID"',shell=True)
            break
        except:
            print("lost connectivity with the wireless")
            fo.write('Lost connecvity with wireless \n')
            if j==10:
                print ('{} value of j inside if '.format(j))
                fo.close()
                sandcsv.close()
                sys.exit()
        j=j+1
       # print ('{} value of j '.format(j))
            
         
    
    #Regex to match the signal value 
    signal1=re.match('.*(Signal).*(:).?([0-9]*).*',signal)
    #converting string to integer
    signal2=int(signal1.group(3))
    # summing up the dignal value 
    signal_total=signal2+signal_total
    # taking average 
    signal_average=signal_total/i
    #regex to match SSID  & BSSID 
    SSID=re.match('.*(SSID).*:(.*)(\r).*',SSID_all)
    # split by new line and taking the 2nd element
    BSSID1=SSID_all.split('\n')[1]
    BSSID2=re.match('.*(BSSID)(\s+)(:)(.*)',BSSID1)
    BSSID=BSSID2.group(4).strip('\r')
   # print (' signal strength is {} at {}  iternations for SSID {} BSSID is {} '.format(signal2,i,SSID.group(2),BSSID))
    print tabulate([["Iteration","signal","BSSID","SSID"],[i ,signal2,BSSID,SSID.group(2)]],tablefmt="fancy_grid")
    text_write=tabulate([["Iteration","signal","BSSID","SSID"],[i ,signal2,BSSID,SSID.group(2)]])
    writer.writerow((i,signal2,BSSID,SSID.group(2)))
    time.sleep(2)
    fo.write(text_write)
    i =i +1
    
print ("=" *70)    
#print ('Average signal strength is {} at {} iternations  for SSID {} '.format(signal_average,i-1,SSID.group(2)))
print tabulate([['Average signal strength is {} at {} iternations  for SSID {} '.format(signal_average,i-1,SSID.group(2))]],tablefmt="fancy_grid")
text_write=tabulate([['Average signal strength is {} at {} iternations  for SSID {} '.format(signal_average,i-1,SSID.group(2))]])
fo.write(text_write)
fo.close()
sandcsv.close()
print ("=" *70)  




    
