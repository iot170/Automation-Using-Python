import os

os.system("tput setaf 3")

print()
print("\t\t\t Welcome to the My automation tool")
print("\t\t\t ---------------------------------\n")


os.system("tput setaf 7")

#------------------------Function for install docker in local system-------------------
def localdocker():
	print("""
Press 1 to Install Docker Container
Press 2 to Pull the OS image on Doker Contaioner
Press 3 to Install Docker Container
Press 4 to Check Running Container
Press 5 to Install and Configure httpd server in docker container
Press 6 to Install Python Interpretor in docker
Press 7 to Run python code on docker container 
Press 8 to Stop Docker Contianer
""")
	os.system("tput setaf 3")
	tx = input('Enter what you want to do in Docker Container: ')
	os.system("tput setaf 7")
	if int(tx) == 1:
		os.system("tput setaf 3")		
		cfrm = input("Type y/n: ")
		os.system("tput setaf 7")
		if cfrm == 'y':
			os.system("sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
			os.system("dnf repolist -v")
			os.system("dnf install docker-ce --nobest --allowerasing")
			os.system("dnf install https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm")
			os.system("systemctl disable firewalld")
			os.system("systemctl start docker")
			os.system("systemctl enable docker")
		else:
			print("Enter correct")
		
	elif int(tx)==2:
		os.system("tput setaf 3")
		imagename = input("Enter Image name: ")
		imageversion = input("Enter Version: ")
		os.system("tput setaf 7")
		os.system('docker pull {}:{}'.format(imagename, imageversion))

	elif int (tx)==3:
		os.system("tput setaf 3")
		Containername = input("Enter Container name: ")
		imagename = input("Enter OS image name: ")
		imageversion = input("Enter OS image Version: ")
		os.system("tput setaf 7")
		os.system("docker run -it --name {} {}:{}".format(Containername, imagename, imageversion))

	elif int(tx)==4:
		os.system("docker ps")
	elif int(tx)==5:
		os.system("sudo yum install httpd -y")
		os.system("sudo systemctl start httpd")
		os.system("sudo systemctl enable httpd")
	elif int(tx)==6:
		os.system("docker ps")
		osid = input("Enter COntainer ID or Name for attaching Container in which you want to Install Python Interpretor: ")
		os.system("docker attach {}".format(osid))
		os.system("yum install python3")
	else:
		print("Dont support local choice")

#------------------------------------------------------------------------------------

#------------------------Function for install docker in remote system----------------- 
def remotedocker():
	print("""
Press 1 to Install Docker Container
Press 2 to Pull the OS image on Doker Contaioner
Press 3 to Install Docker Container
Press 4 to Check Running Container
Press 5 to Install and Configure httpd server in docker container
Press 6 to Install Python Interpretor in docker
Press 7 to Run python code on docker container 
Press 8 to Stop Docker Contianer
""")
	os.system("tput setaf 3")
	ip = input("Enter your ip: ")
	os.system("tput setaf 7")
	print(ip)
	os.system("tput setaf 3")
	tx = input('Enter what you want to do in Docker Container: ')
	os.system("tput setaf 7")
	if int(tx) == 1:		
		cfrm = input("Type y/n: ")
		if cfrm == 'y':
			os.system('scp docker.repo {}:/etc/yum.repos.d/docker.repo'.format(ip))
    
			os.system("ssh {} sudo dnf repolist -v" .format(ip))
			os.system("ssh {} sudo dnf install --nobest docker-ce" .format(ip))
			os.system("ssh {} sudo dnf install https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm" .format(ip))
			os.system("ssh {} sudo systemctl disable firewalld" .format(ip))
			os.system("ssh {} sudo systemctl start docker" .format(ip))
			os.system("ssh {} sudo systemctl enable docker" .format(ip))
		else:
			print("Enter correct")
	elif int(tx)== 5:
		os.system("ssh {} sudo yum install httpd" .format(ip))
		os.system("ssh {} sudo systemctl start httpd" .format(ip))
		os.system("ssh {} sudo systemctl enable httpd" .format(ip))
		os.system("ssh {} sudo yum install httpd" .format(ip))
	else:
		print("Dont support remote choice")

#-------------------------------------------------------------------------------------

def core_site():
    print('Enter NameNode IP Address :   ', end='')
    NN_ip=input()
   
    os.system('echo \<configuration\> >> core-site.xml')
    os.system('echo \<property\> >> core-site.xml')
    os.system('echo \<name\>fs.default.name\<\/name\> >> core-site.xml')
   
    if cmd=='1':
        os.system('echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))
    else:
        os.system('echo \<value\>hdfs://{}:9001\<\/value\> >> core-site.xml'.format(NN_ip))
   
    os.system('echo \</property\> >> core-site.xml')
    os.system('echo \<\/configuration\> >> core-site.xml')
   
    if cmd=='2':
        os.system('scp core-site.xml {}:/etc/hadoop/core-site.xml'.format(remote_ip))
    else:
        os.system('cp core-site.xml /etc/hadoop/core-site.xml')
    os.system('rm -rf core-site.xml')
    os.system('cp temp.xml core-site.xml')



def hdfs_site():
    
    if cmd2=='4':
        print('Enter DataNode Directory name you want to create :   ' ,end='')
    
    elif cmd2=='3':
        print('Enter NameNode Directory name you want to create :   ' ,end='')
    
    dir_name=input()
    
    if cmd=='2':
        os.system('ssh {} mkdir {}'.format(remote_ip , dir_name))
    else:
        os.system('mkdir {}'.format(dir_name))
    os.system('echo \<configuration\> >> hdfs-site.xml')
    os.system('echo \<property\> >> hdfs-site.xml')
    
    if cmd2=='4':
        os.system('echo \<name\>dfs.data.dir\<\/name\> >> hdfs-site.xml')
    elif cmd2=='3':
        os.system('echo \<name\>dfs.name.dir\<\/name\> >> hdfs-site.xml')
    os.system('echo \<value\>{}\<\/value\> >> hdfs-site.xml'.format(dir_name))
    os.system('echo \</property\> >> hdfs-site.xml')
    os.system('echo \<\/configuration\> >> hdfs-site.xml')
    if cmd=='2':
        os.system('scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml'.format(remote_ip))
    else:
        os.system('cp hdfs-site.xml /etc/hadoop/hdfs-site.xml')
    os.system('rm -rf hdfs-site.xml')
    os.system('cp temp2.xml hdfs-site.xml')


#-----------------------------------------Main Code-----------------------------------

while True:
	print("Press 1 to Configure Local Server\nPress 2 to Configuring Remote Server")
	print('Type Exit to Close\n')
	os.system("tput setaf 3")
	print('Enter Your choice Either Local or Remote: ', end='')
	
	cmd=input()
	os.system("tput setaf 7")
	
	if cmd=='1':
		print()
		print('Press 1 to Run Any Linux Command.')
		print('Press 2 to Configure WebServer.')
		print('Press 3 to Configure and Start NameNode.')
		print('Press 4 to Configure and Start DataNode.')
		print('Press 5 to Docker Container.\n')
		os.system("tput setaf 3")
		print('Enter Your choice: ', end='')
		cmd2=input()
		os.system("tput setaf 7")
    
		if cmd2=='1':
			print('Enter Linux Command:  ' , end='')
			linux_cmd=input()
			os.system('sudo {}'.format(linux_cmd))
    
		elif cmd2=='2':
			os.system('yum install httpd -y')
			os.system('systemctl start httpd')
			os.system('systemctl enable httpd')
			os.system('cp /root/index.html /var/www/html')
    
		elif cmd2=='3':
			os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
			os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
			hdfs_site()
			core_site()
			os.system('hadoop namenode -format')
			os.system('hadoop-daemon.sh start namenode')
			os.system('jps')
    
		elif cmd2=='4':
			os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
			os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
			hdfs_site()
			core_site()
			os.system('sudo hadoop-daemon.sh start datanode')
			os.system('sudo jps')
		elif cmd2=='5':
			localdocker()
    
		else:
			print('Please , Select above given Options . Thank You :)')

	elif cmd=='2':
		print()
		os.system("tput setaf 3")
		print("Enter remote OS IP:  ", end='')
		remote_ip=input()
		os.system("tput setaf 7")
    
		print('Press 1 to Run Any Linux Command')
		print('Press 2 to Configure WebServer')
		print('Press 3 to Configure and Start NameNode')
		print('Press 4 to Configure and Start DataNode')
		print('Press 5 to do Parition')
		print('Press 6 to Docker Container.\n')
		os.system("tput setaf 3")
		print('Enter Your choice: ', end='')
		cmd2=input()
		os.system("tput setaf 7")

		if cmd2=='1':
			print('Enter Linux Command:  ' , end='')
			linux_cmd=input()
			os.system('ssh {} {}'.format(remote_ip ,linux_cmd))
    
		elif cmd2=='2':
			os.system('ssh {} yum install httpd -y'.format(remote_ip))
			os.system('ssh {} systemctl start httpd'.format(remote_ip))
			os.system('ssh {} systemctl enable httpd'.format(remote_ip))
			os.system('scp /root/index.html {}:/var/www/html'.format(remote_ip))
    
		elif cmd2=='3':
			os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(remote_ip))
			os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(remote_ip))
			hdfs_site()
			core_site()
			os.system('ssh {} hadoop-daemon.sh start namenode'.format(remote_ip))
			os.system('ssh {} jps'.format(remote_ip))
    
		elif cmd2=='4':
			os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(remote_ip))
			os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(remote_ip))
			hdfs_site()
			core_site()
			os.system('ssh {} hadoop-daemon.sh start datanode'.format(remote_ip))
			os.system('ssh {} jps'.format(remote_ip))
			os.system('ssh {} hadoop dfsadmin -report'.format(remote_ip))

		elif cmd2=='5':
			os.system('ssh {} fdisk -l'.format(remote_ip))
			os.system('ssh {} fdisk /dev/xvdf'.format(remote_ip))
			os.system('ssh {} mkfs.ext4 /dev/xvdf3'.format(remote_ip))
			print('\t\tEnter name of Directory to mount the HDs')
			dirname=input()
			os.system('ssh {} mkdir {}'.format(remote_ip , dirname))
			os.system('ssh {} mount /dev/xvdf3 {}'.format(remote_ip , dirname))
			os.system('ssh {} df -h'.format(remote_ip))
		elif cmd2=='6':
			remotedocker()
		else:
			print('Select options as mention')
	elif cmd=='Exit':
		break
	else:
		print('\n\t\t\t\tPlease Choose Valid Options mention above')
