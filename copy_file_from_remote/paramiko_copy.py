import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.1.0",username="<user1>", password="<password>", port=22)
sftp_client=ssh.open_sftp()
sftp_client.chdir("/home/user1")
#copy file from remote server
sftp_client.get("/path/to/host/destination/file.mp3","path/to/remote/source/file.mp3")
#sent files to remote dir
sftp_client.put("path/to/host/source/file.mp3","/path/to/remote/destination/file.mp3")
print(sftp_client.listdir())
sftp_client.close()
ssh.close()
