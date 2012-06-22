#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Wed Jun 20 21:51:55 EDT 2012
# 
# 

""" This module contains the ConfigHandler class which is dedicated to handling the configuration for SmartInstallMan"""

import os
from ConfigHandler import *

class InstConfigHandler(ConfigHandler):
	def __init__(self):
		ConfigHandler.__init__(self, 'smartinst.conf', {'distro':'', 'packman':'', 'afterkey':'' })
		self.supportedDistros = {'ubuntu':'apt-get'}
		self.packmanToAfterKey = {'apt-get':'install'}

	def GetDistroFromEtcIssue(self):
		wordsInIssue = map(lambda x: x.lower(), os.popen('cat /etc/issue').read().split(' '))
		for word in wordsInIssue:
			if word in self.supportedDistros: return word
		raise Exception('This is not a supported distro')

	def InitConfig(self):
		if not self.ConfigFileExists():
	                self.config['distro'] = self.GetDistroFromEtcIssue()
	                self.config['packman'] = self.supportedDistros[self.config['distro']]
	                self.config['afterkey'] = self.packmanToAfterKey[self.config['packman']]
			self.UpdateConfig()
		self.ParseConfig()

a = InstConfigHandler()
a.InitConfig()
