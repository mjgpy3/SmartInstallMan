#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Thu Jun 21 06:41:48 EDT 2012
# 
# 

import sys, unittest, os
sys.path.append('..')
import FileIOHandler

def CreatePackageFile(fileName):
	os.system('touch ' + fileName)
	for i in range(5):
		os.system('echo package' + str(i) + ' >> ' + fileName)

def DeletePackageFile(fileName):
	os.system('rm ' + fileName)


class testFileIOHandler(unittest.TestCase):
	def setUp(self):
		self.beingTested = FileIOHandler.FileIOHandler()

	def test_PackagesFileToListSuccessfullyTakesInAGeneratedPackageFileInTheCorrectFormat(self):
		CreatePackageFile('smartpack.lst')
		self.beingTested.PackagesFileToList()
		self.assertEqual(map(lambda x: 'package' + str(x), range(5)), self.beingTested.installedPackages)
		DeletePackageFile('smartpack.lst')

	def test_ListToPackagesFileSuccessfullyWritesAShortListToAFileAndIsVerifiableWithPackagesFileToList(self):
		self.beingTested.installedPackages = ['virtualbox', 'diff', 'nmap', 'wireshark']
		self.beingTested.ListToPackagesFile()
		self.beingTested.installedPackages = []
		self.beingTested.PackagesFileToList()
		for package in self.beingTested.installedPackages:
			self.assertTrue(package in ['virtualbox', 'diff', 'nmap', 'wireshark'])
		DeletePackageFile('smartpack.lst')

	def test_ListToPackageFileDoesNotWriteDuplicateEntriesEvenIfTheyAreInTheList(self):
		packagesWRepeat = ['virtualbox', 'diff', 'nmap', 'wireshark', 'virtualbox']
		self.beingTested.installedPackages = packagesWRepeat
                self.beingTested.ListToPackagesFile()
                self.beingTested.installedPackages = []
                self.beingTested.PackagesFileToList()
		self.assertTrue(len(packagesWRepeat) > len(self.beingTested.installedPackages))
                DeletePackageFile('smartpack.lst')	

def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(testFileIOHandler))
	return suite

if __name__ == '__main__':
	unittest.TextTestRunner(verbosity=2).run(suite())
