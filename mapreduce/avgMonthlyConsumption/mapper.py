__author__ = 'Gemma'
import sys

for line in sys.stdin:
    (month, totalKwh) = line.split('\t')
    print ('%s\t%f' % ('1', float(totalKwh)))