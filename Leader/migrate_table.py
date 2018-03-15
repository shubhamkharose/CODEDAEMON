import subprocess
import sys
cmd = subprocess.Popen('python manage.py migrate',stderr=subprocess.STDOUT,stdout=subprocess.PIPE,shell=True)
print (cmd.communicate())