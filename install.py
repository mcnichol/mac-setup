#!/usr/bin/env python
""" Script for Executing Bash Shell Script without chmod +x """

import subprocess

def main():
    print "Python:\tHandoff to Bash"
    execScript()
    print "Python:\tLooks like I'm done here...Python Out"
    return 

def execScript():
    try: 
        subprocess.call('./scripts/bada-bing.sh',shell=True)
    except OSError as e:
	print "What we've got here is a failure to communicate. ~ This Script"
	print "Sadly there was an error.  Hopefully you are smart enough to fix it"
	print "Probably something with the shell script, 'bada-bing.sh', here's a hint: "
	print e.errno
	print e.filename
	print e.strerror
	return
     

if __name__ == '__main__':
    main()
