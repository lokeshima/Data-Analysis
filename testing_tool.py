import time
import paramiko

source_server='****'
destination_server='****'
source_run_id='1483364735'
destination_run_id='15614431'
source_QL2_DAY='5895'
destination_QL2_DAY='5890'
source_file_path='/caesius/storage/results'
destination_file_path='/caesius/storage/results'

lsresult=''

commands = ['sudo su - caesius', 'javadev','ssh '+source_server+'',
            'scp -r '+source_file_path+'/'+source_QL2_DAY+'/'+source_run_id+' '+destination_server+':/tmp/'+source_run_id+'',
            'ssh '+destination_server+'','cd /tmp','mkdir '+source_run_id+'_prod',
            'mv '+source_run_id+' '+source_run_id+'_prod','cd '+source_run_id+'_prod','unzip -j "'+source_run_id+'" "raw.csv"',
            'mkdir '+destination_run_id+'_alpha','cd '+destination_run_id+'_alpha',
            'cp '+destination_file_path+'/'+destination_QL2_DAY+'/'+destination_run_id+' .','unzip '+destination_run_id+'','ls',
            'cp /tmp/'+source_run_id+'_prod/raw.csv .',
            'zip -r '+destination_run_id+' 15614485 15614486 15614487 raw.csv  rawetl.csv',
            'rm -rf '+destination_run_id+'','mv '+destination_run_id+'.zip '+destination_run_id+'',
            'cp '+destination_run_id+' '+destination_file_path+'/'+destination_QL2_DAY+'/']



#'scp -r /caesius/storage/results/5741/1465563354 carrot:/tmp/1465563354']





client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('host_name', username='****', password='****',port=22)
channel = client.invoke_shell()

# clear welcome message and send newline
time.sleep(1)
channel.recv(9999)
channel.send("\n")
time.sleep(1)

# for command in commands:
#     channel.send(command + "\n")
#     while not channel.recv_ready(): #Wait for the server to read and respond
#      time.sleep(0.1)
#      time.sleep(0.1) #wait enough for writing to (hopefully) be finished
#      output = channel.recv(9999) #read in
#      print(output.decode('utf-8'))
#      time.sleep(0.1)
# channel.close()
# client.close()

for command in commands:
    channel.send(command + "\n")
    while not channel.recv_ready(): #Wait for the server to read and respond
        time.sleep(0.1)
    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
    output = channel.recv(9999) #read in
    print(output.decode('utf-8'))
    time.sleep(0.1)
channel.close()
