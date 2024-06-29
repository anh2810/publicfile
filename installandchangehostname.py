import os



# update and upgrade system

os.system('yum update & upgrade -y')
os.system('yum install nano -y')

# set hostname
 
hostname = input('Enter your hostname you desired: ')
os.system('hostnameclt set-hostname' +  hostname)
os.system('exec bash')

# edit hostname
internal_ip = input('Enter internal ip address: ')
hostrecordname = input('Enter desired hostname: ')
os.system('echo "{internal_ip} {hostrecordname}" > /etc/hosts')