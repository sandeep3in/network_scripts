from ciscoconfparse import CiscoConfParse

# return a dict with interface as key and value is ipaddr/mask

def int_dict_ip_mask(config_file):
    config_file.seek(0)
    
    cisco_parser = CiscoConfParse(config_file, syntax='ios')
    int_details={}
    for interface in cisco_parser.find_objects('^[iI]nterface.*'):
    #print (str(interface.text))
    
        for  sub_conf in interface.children:
            #print(sub_conf)
            intf=interface.re_match_typed('^[iI]nterface\s+(.*)',default='no_match')
            ip=sub_conf.re_match_typed('ip address (.*)',default='no_match')
            if ip != 'no_match':
                int_details[intf]=ip
                #print('the int is {} and ip is {}'.format(intf,ip))

    return int_details


# return a dict with interface as key and value is ipaddr

def int_dict_ip(config_file):
    config_file.seek(0)
    
    cisco_parser = CiscoConfParse(config_file, syntax='ios')
    int_details={}
    for interface in cisco_parser.find_objects('^[iI]nterface.*'):
        
    
        for  sub_conf in interface.children:
            #print(sub_conf)
            intf=interface.re_match_typed('^[iI]nterface\s+(.*)',default='no_match')
            ip=sub_conf.re_match_typed('ip address\s+(\d+.\d+.\d+.\d+).*',default='no_match')
            
           
            if ip != 'no_match':
                int_details[intf]=ip
    return int_details



# return a dict with vlan as key and value is ipaddr

def int_vlan(config_file):
    config_file.seek(0)
    cisco_parser = CiscoConfParse(config_file, syntax='ios')
    vlan_details={}
    for vlan in cisco_parser.find_objects('^[iI]nterface\s+[vV]lan.*'):
        for  sub_conf in vlan.children:
            
            vlan_1=vlan.re_match_typed('^[iI]nterface\s+([vV]lan.*)',default='no_match')
            ip=sub_conf.re_match_typed('ip address\s+(\d+.\d+.\d+.\d+).*',default='no_match')

            if ip != 'no_match':
                vlan_details[vlan_1]=ip
    return vlan_details

    


#/* Driver code

config_file= open('C:\\Users\\Administrator\\Downloads\\sand-br-1-config-1','r') <==== Add the config file offline
int_details_1=int_dict_ip_mask(config_file)

int_details_2=int_dict_ip(config_file)
vlan_details_3=int_vlan(config_file)
print(int_details_1)
print(int_details_2)
print(vlan_details_3)


******************************************

{'Loopback0': '9.254.254.65 255.255.255.255', 'Loopback1021': '9.40.50.1 255.255.255.255', 'Loopback1025': '9.40.62.1 255.255.255.255', 'GigabitEthernet1/0/2': '9.254.254.110 255.255.255.252', 'GigabitEthernet1/0/14': '9.254.254.161 255.255.255.252', 'GigabitEthernet1/0/23': '9.254.254.101 255.255.255.252', 'GigabitEthernet1/0/24': '9.254.254.105 255.255.255.252', 'Vlan50': '9.1.50.10 255.255.255.252', 'Vlan1022': '9.40.60.1 255.255.255.0'}

{'Loopback0': '9.254.254.65', 'Loopback1021': '9.40.50.1', 'Loopback1025': '9.40.62.1', 'GigabitEthernet1/0/2': '9.254.254.110', 'GigabitEthernet1/0/14': '9.254.254.161', 'GigabitEthernet1/0/23': '9.254.254.101', 'GigabitEthernet1/0/24': '9.254.254.105', 'Vlan50': '9.1.50.10', 'Vlan1022': '9.40.60.1'}

{'Vlan50': '9.1.50.10', 'Vlan1022': '9.40.60.1'}
