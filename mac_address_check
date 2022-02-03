'''
Sample code to extract mac address

Author: Sandeep Joseph
'''

import re
def is_mac(m):
    try:
        m1=re.match('.*?(([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}).*',m)
        return(m1.group(1),':')
    except :
        try:
            m1=re.match('.*?(([a-fA-F0-9]{2}-){5}[a-fA-F0-9]{2}).*',m)
            return(m1.group(1),'-')
        except  :
            try:
                m1=re.match('.*?(([a-fA-F0-9]{4}\.){2}[a-fA-F0-9]{4})',m)
                return(m1.group(1),'.')
            except:
                try:
                    m1=re.match('.*?([a-fA-F0-9]{12})',m)
                    return(m1.group(1),'none')
                except:
                    return ('mac not valid',False)


#/* Driver code*/

m1='mac add is a1:b1:c1:d1:ee:ff '
m2='mac add is a1-b1-c1-d1-ee-ff '
m3='mac add is a1b1.c1d1.eeff'
m4= 'mac add is a1b1c1d1eeff'
m5='mac add is a1:b1:c1:d1:ee:fg '
print(is_mac(m4)[0])
print(is_mac(m3)[0])
print(is_mac(m2)[0])
print(is_mac(m1)[0])
print(is_mac(m5)[0])
