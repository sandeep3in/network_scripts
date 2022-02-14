# function to validate the IP address
# Split the IP  and validate if each octect is below 255

def ip_valid(ip):
    ip_valid1=False
    ip1=ip.split('.')
    for i in ip1:
        if int(i) > 255:
            ip_valid1=False
            print('{} octet is invalid'.format(i))
        else:
            ip_valid1=True
    return ip_valid1


def ip_valid_1(ip):
    ip_valid1=False
    ip1=ip.split('.')
    for i in range(len(ip1)):
        
        if int(ip1[i]) > 255:
            
            ip_valid1=False
            print('{} octet is invalid'.format(i+1))
        else:
            ip_valid1=True
    return ip_valid1

# function to findout the class of IP  

def ip_class(ip):
  
    ip1=ip.split('.')
    if int(ip1[0]) in range(0,126):
        print('class A')
    elif int(ip1[0]) in range(128,191):
        print('class B')
    elif int(ip1[0]) in range(192,223):
        print('class C')
    elif int(ip1[0]) in range(224,239):
        print('MUlticast')
    else:
        print('not a valid IP')
        
 
 #/* Driver Code */
 
ip1='192.156.344.133'

if (ip_valid_1(ip1)):
    print('the IP is valid')
else:
    print('the ip is not valid ')
ip10=ip_valid_1(ip1)
ip_class(ip1)
