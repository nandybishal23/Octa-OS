import subprocess

out = subprocess.check_output('wmic logicaldisk get  DriveType, caption', shell=True)

for drive in str(out).strip().split('\\r\\r\\n'):
	if '2' in drive:
		
		print(drive.split(':'))
		