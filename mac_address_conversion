'''
Sample code to convert mac address

Author: Sandeep Joseph
'''

def mac_convert_hypen(mac):
    # remove the delimiter if any 
    mac=mac.replace(':','')
    mac=mac.replace('.','')
    mac=mac.replace('-','')
    #/* Conversion to colon 
    b=mac[0]
    for i in range(1,len(mac),2):
        	b=b+'-'.join(mac[i:i+2])
    return b


def mac_convert_colon(mac):
    # remove the delimiter if any 
    mac=mac.replace(':','')
    mac=mac.replace('.','')
    mac=mac.replace('-','')
    #/* Conversion to colon 
    b=mac[0]
    for i in range(1,len(mac),2):
        	b=b+':'.join(mac[i:i+2])
    return b


def mac_convert_dot(mac):
    # remove the delimiter if any 
    mac=mac.replace(':','')
    mac=mac.replace('.','')
    mac=mac.replace('-','')
    #/* Conversion to colon 
    b1=mac[0:4]
    b2=mac[4:8]
    b3=mac[8:12]
  
    b1=b1+'.'+b2+'.'+b3
    return b1

def mac_convert_raw(mac):
    # remove the delimiter if any 
    mac=mac.replace(':','')
    mac=mac.replace('.','')
    mac=mac.replace('-','')
    return mac


#/* Driver code*/

m1='a1:b1:c1:d1:ee:ff '
m2='a1-b1-c1-d1-ee-ff '
m3='a1b1.c1d1.eeff'
m4= 'a1b1c1d1eeff'

print (mac_convert_dot(m4))
print (mac_convert_hypen(m4))
print (mac_convert_raw(m1))
