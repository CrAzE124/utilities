import sys
import subprocess

args = sys.argv
branch_name = args[1] # 0 = branch.py
print "\nBranch Name: " + branch_name + "\n"

# Now we need to pass this to the CLI to clone, branch, etc...
subprocess.call('cd /var/www/', shell=True)
subprocess.call('cp -R 43668 ' + branch_name, shell=True)
subprocess.call('cd ' + branch_name, shell=True)
subprocess.call('git fetch', shell=True)
subprocess.call('git checkout ' + branch_name, shell=True)
subprocess.call('rm -Rf app/cache/*', shell=True)
subprocess.call('rm -Rf app/logs/*', shell=True)
subprocess.call('chown -R apache:apache ./*', shell=True)
subprocess.call('cp /etc/httpd/branch-conf.d/43668.conf /etc/httpd/branch-conf.d/' + branch_name + '.conf', shell=True)
subprocess.call('sed -i \'s/43668/' + branch_name + '/g\' /etc/httpd/branch-conf.d/' + branch_name + '.conf', shell=True)
subprocess.call('service httpd reload', shell=True)

