import paramiko

def runonshell(client, cmdlines):
	"""Receive ssh connect, send command, close connection
	Args: 
		client(paramiko.SSHClient): ssh client object
		cmdlines(list): command str list
	Return:
		dict_ret(dict):{'cmd':cmdlines, 'recv':[]}

    	"""

	sh = client.invoke_shell()
	dict_ret = {'cmd':cmdlines, 'recv':[]}
	print(dict_ret)
	for cmd in cmdlines:
		ret = sh.send(cmd+"\n")
		buf=''
		while sh.recv_ready():
			buf = sh.recv(4096)
			print(buf)
			dict_ret['recv'].append(re.split('[\r\n]+', buf.decode('utf-8'))[3:-1])
	sh.close()
	return dict_ret

