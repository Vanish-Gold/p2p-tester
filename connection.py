import paramiko

class Connect():
	def __init__(self, host, name, password, port=22):
		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.client.connect(hostname=host, username=name, password=password, port=port)
	def get_raw(self,command):
		stdout, stderr = self.client.exec_command(command)[1:]
		if stderr.read().decode('utf')=='':
			return stdout.read().decode('utf')
		else:
			raise ConnectionError('Invalid connection data or internet connetion')