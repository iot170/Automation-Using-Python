import os


print('\t\t\t  Linux Assistant For Automation ')
print("\t\t\t----------------------------------- ")
print()



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

while True:
    print("Press 1 to Configure Local Server\nPress 2 to Configuring Remote Server")
    print('Type Exit to Close\n')
    print('Enter Your choice : ', end='')
    cmd=input()

    if cmd=='1':
        print('Press 1 to Run Any Linux Command.')
        print('Press 2 to Configure WebServer.')
        print('Press 3 to Configure and Start NameNode.')
        print('Press 4 to Configure and Start DataNode.\n')
        print('Enter Your choice  ', end='')
        cmd2=input()
    
        if cmd2=='1':
            print('Enter Linux Command :-   ' , end='')
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
    
        else:
            print('Please , Select above given Options . Thank You :)')

    elif cmd=='2':
        print("Enter remote OS IP :-   ", end='')
        remote_ip=input()
    
        print('press 1 to Run Any Linux Command')
        print('press 2 to Configure WebServer')
        print('press 3 to Configure and Start NameNode')
        print('press 4 to Configure and Start DataNode\n')
        print('press 5 to do Parition')
        print('Enter Your choice: ', end='')
        cmd2=input()

        if cmd2=='1':
            print('Enter Linux Command :   ' , end='')
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
            os.system('ssh {} hadoop namenode -format'.format(remote_ip))
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
        else:
            print('Select options as mention')
    elif cmd=='Exit':
        break
    else:
        print('\n\t\t\t\tPlease Choose Valid Options mention above')
