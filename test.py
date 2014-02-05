from GetVersion import get_version

print 'Usage: %s' %  __file__
print '   ver: %s' % get_version(__file__) 

from os import system
system('git log')