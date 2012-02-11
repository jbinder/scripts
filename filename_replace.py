# filename_replace
# Replaces a specified string with another in file and directory names, including subdirectories.
# requirements: Python 3.2.2
# usage: python filename_replace.py find replace directory

# Initially developed to fix filename encoding issues (Ãœ = Ü, Ã¶ = ö, Ã¼ = ü, Ã¤ = ä, Ã„ = Ä, ÃŸ = ß, Ã– = Ö).
# example: python filename_replace.py Ã¤ ae testdir

import os
import sys

def getArgs():
	argMap = ['script', 'find', 'replace', 'directory'];
	args = {argMap[i]:sys.argv[i] for i in range(1,4)}
	return args

def safePrint(str):
	"""Needed because of unicode conversion issues."""
	try:
		print(str)
	except:
		print('WARNING: unable to print')

def rename(root, item, find, replace):
	try:
		newItem = item.replace(find, replace)
		safePrint('{0}: {1} => {2}'.format(root, item, newItem))
		os.rename(os.path.join(root,item), os.path.join(root,newItem))
	except Exception as e:
		print('ERROR {0}: {1} '.format(item, str(e)))

try:
	args = getArgs()
except:
	print('usage: filename_replace.py find replace directory')
	sys.exit()

for root, dirs, filenames in os.walk(args['directory'], topdown=False):
	try:
		filenames.extend(dirs)
		for item in filenames:
			if not args['find'] in item:
				continue
			rename(root, item, args['find'], args['replace'])
	except Exception as e:
		print('ERROR: {0}'.format(str(e)))
		tmp = input('press enter to continue')
