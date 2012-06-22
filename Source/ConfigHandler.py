#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Wed Jun 20 21:51:55 EDT 2012
# 
# 

""" This module contains the ConfigHandler class which is dedicated to handling the configuration for SmartInstallMan """

class ConfigHandler:
	def __init__(self, configName, configDefaults = {}):
		self.fileName = configName
		if type({}) != type(configDefaults): raise TypeError('Default config information must be key value pairs')
		self.config = configDefaults

	def ConfigFileExists(self):
		try:
			with open(self.fileName, 'r') as f: 
				pass
		except IOError:
			return False
		return True

	def ParseConfig(self):
		with open(self.fileName, 'r') as f:
			for line in f.read().split('\n'):
				if line != '': self.config[line.split('=')[0]] = line.split('=')[1]

	def UpdateConfig(self):
		with open(self.fileName, 'w') as f:
			for key in self.config:
				f.write(key + '=' + str(self.config[key]) + '\n')
