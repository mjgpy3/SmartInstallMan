#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Thu Jun 21 06:41:48 EDT 2012
# 
# 

import sys, unittest, os
sys.path.append('..')
import SmartInstConfigHandler

class testSmartInstConfigHandler(unittest.TestCase):
	def setUp(self):
		self.beingTested = SmartInstConfigHandler.InstConfigHandler('./smartinst.conf', {'distro':'', 'lastline':''})

	def test_ConfigFileExistsReturnsTrueIfTheConfigFileIsFound(self):
		os.system('touch ./smartinst.conf')
		self.assertTrue(self.beingTested.ConfigFileExists())
		os.system('rm ./smartinst.conf')		

	def test_ConfigFileExistsReturnsFalseIfNoFileIsFound(self):
		self.assertFalse(self.beingTested.ConfigFileExists())

	def test_GetDistroFromEtcIssueWorks(self):
		dist = self.beingTested.GetDistroFromEtcIssue()
		self.assertTrue(dist in self.beingTested.supportedDistros )

	def test_ParseConfigSetsValuesCorrectly(self):
		self.beingTested.UpdateConfig()
		self.beingTested.ParseConfig()
		self.assertTrue(self.beingTested.config['distro'] in self.beingTested.supportedDistros)
		self.assertEqual(self.beingTested.config['lastline'], '0')
                os.system('rm ./smartinst.conf')

	
def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(testSmartInstConfigHandler))
	return suite

if __name__ == '__main__':
	unittest.TextTestRunner(verbosity=2).run(suite())
