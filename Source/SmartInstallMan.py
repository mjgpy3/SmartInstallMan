#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jun 22 16:10:29 EDT 2012
# 
# 

import SmartInstConfigHandler, FileIOHandler, sys, os

if __name__ == '__main__':
	configHandler = SmartInstConfigHandler.InstConfigHandler()
	configHandler.InitConfig()
	fileIO = FileIOHandler.FileIOHandler()	

	fileIO.PackagesFileToList()

	if len(sys.argv) > 1:
		if sys.argv[1] == '-i' or sys.argv[1] == '--install':
			errorMessage = ""
			for package in fileIO.installedPackages:
				if os.system(configHandler.config['packman'] + ' ' + configHandler.config['afterkey'] + ' ' + package) != 0:
					errorMessage += '"' + package + '" failed to install\n'
			if errorMessage != "":
				print errorMessage + "\n(If nothing installed, perhaps use sudo)"
		if sys.argv[1] == '-u' or sys.argv[1] == '--update':
			fileIO.AppendBashHistoryToList(configHandler.config['packman'], configHandler.config['afterkey'])
	                fileIO.ListToPackagesFile()
	else:
		fileIO.AppendBashHistoryToList(configHandler.config['packman'], configHandler.config['afterkey'])
		fileIO.ListToPackagesFile()
	
	
