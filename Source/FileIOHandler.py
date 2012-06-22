#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jun 22 14:44:30 EDT 2012
# 
# 

import os

class FileIOHandler:
	def __init__(self, packagesFile = 'smartpack.lst'):
		self.installedPackages = []
		self.packagesFile = packagesFile
		os.system('touch ' + self.packagesFile)

	def PackagesFileToList(self):
		with open(self.packagesFile, 'r') as f:
			self.installedPackages = filter(lambda x: x not in [''], f.read().split('\n'))

	def ListToPackagesFile(self):
		with open(self.packagesFile, 'w') as f:
			for package in set(self.installedPackages): f.write(package + '\n')

	def AppendBashHistoryToList(self, commandToLookFor, packsComeAfter):
		for line in os.popen('cat ~/.bash_history | grep "' + commandToLookFor + '"').readlines():
			if packsComeAfter in line.split(' '):
				for foundPackage in filter(lambda x: x not in ['\n', ''], line.split(' ')[line.split(' ').index(packsComeAfter) + 1:]):
					self.installedPackages.append(foundPackage.replace('\n', ''))
