import re

#*** Parse WLAN from  WLC*****#
# return dictionary  with index as the key and a list with profile name and SSID name

def parse_wlan(w1):
    w_op={}
    wl_list=[]
    w2=w1.split('\n')
    
    for i in w2:
        wl_list=[]
        w3=re.search('^(\d+)\s+([a-zA-Z_\-0-9]*)\s+([a-zA-Z_\-0-9]*).*',i,re.MULTILINE|re.DOTALL)
        
                
        try:
            wl_list.append(w3.group(2)),wl_list.append(w3.group(3))
            w_op[w3.group(1)]=wl_list
        except:
            pass
    
    return w_op




#**** Driver code*****#

wlan_op= '''

17   sand-sc-op_Global_NF_c3cdc6ec    sand-sc-open                     UP     [open]                                                                        
18   sand-sc-we_Global_NF_b812c39a    sand-sc-webauth                  UP     [open],MAC Filtering,[Web Auth]
'''
print (parse_wlan(wlan_op))
