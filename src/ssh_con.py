def ssh_con(ip, port, usr, pwd, command):
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    cli.connect(ip, port=port, username=usr, password=pwd)
    
    stdin, stdout, stderr = cli.exec_command(command)
    if stdout !=[]:
        lines = stdout.readlines()
        for line in lines:
            print (line.split("\n")[0])
    if stderr !=[]:
        lines = stderr.readlines()
        for line in lines:
            print (line.split("\n")[0])
    cli.close()



ssh_con(svr_ip, svr_port, svr_usr, svr_pwd, "export LD_LIBRARY_PATH=/usr/local/magiccrypto/lib:/usr/local/magiccrypto/lib/mariadb; cd /dbsafer/ ; ./pnp_server_manager start")