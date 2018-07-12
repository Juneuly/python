import os
ip = []
cmd = []

with open('ip1.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            ip.append(line)

with open('cmd.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            cmd.append(line)

for i in range(len(ip)):
    s = 'ssh -x %s %s'%(ip[i],cmd[i])
    x = int(os.popen(s).read())
    if x != 1:
        print "ip: %s cmd: %s result:%d"%(ip[i], cmd[i], x) 
    else:
	print "num:%d ip:%s check successfully!"%(i+1, ip[i])

print "Done!"
