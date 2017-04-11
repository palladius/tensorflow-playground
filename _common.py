"""Common stuff.

Great article on reflection: http://stackoverflow.com/questions/2654113/python-how-to-get-the-callers-method-name-in-the-called-method
"""


import inspect
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # to remove the warnings




if __name__ == '__main__':
	print "I'm just a library - please don't execute me again or I'll go to lib/HR.py"
else:
	print "Thanks for trating me as a library. I'm NOT an object, or from Maine! Called by: '{}'".format(inspect.stack()[1][1])
	#print 'caller name: ', inspect.stack()[1]