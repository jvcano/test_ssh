import paramiko

def start_connection():
    host = input("what is the ip: ")
    port = 22
    username = input("username: ")
    password = input("password: ")
    command = "pwd"10
    print("connecting")

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host, port, username, password)
    print("connected")

    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()

    print("{}".format(stdout.read()))
    print("{}".format(type(ssh)))
    

if __name__ == '__main__':
    start_connection()