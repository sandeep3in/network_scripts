# Function to clean up the device residual files, commonly used before upgrading a device
# The function will invoke the CLI "Install remove active" to clean up the residual files. 
# Works with Cisco IOS_XE


from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
    file_transfer
)


def remove_inactive(device):
    try:
        ssh=ConnectHandler(**device)
        cli_op=ssh.send_command('show version')
        print(cli_op)
        cli_op=ssh.send_command('install remove inactive', expect_string=r".*\[y\/n\]",delay_factor=3)
        print(cli_op)
        cli_op=ssh.send_command('y', expect_string='.*#',delay_factor=2)
        print(cli_op)
            
    except:
        
        print('install remove failed or nothing to clean ')

      
#/* Driver code 
        
device = {
        "device_type": "cisco_ios_telnet",
        "host": host_ip,
        "username": host_username,
        "password": host_password,
        "secret": host_enable,
    }
remove_inactive(device,)
