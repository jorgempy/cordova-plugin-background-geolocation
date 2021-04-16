#!/usr/bin/python3

import subprocess

def install_sub():
        if latest_url is not None:
                cmd = ['git', 'clone', '--depth',  '1', latest_url] 
                if latest_path is not None:
                        cmd += [latest_path]
                print(subprocess.run(cmd, capture_output=True))


latest_path = None
latest_url = None
with open('.gitmodules' ,'r') as ri:
	for line in ri.readlines():
		if line.startswith('[submodule'):
			install_sub()

			latest_path = None
			latest_url = None
		if line.strip().startswith('path'):
			latest_path = line.split('=')[1].strip()
		if line.strip().startswith('url'):
			latest_url = line.split('=')[1].strip()
install_sub()
