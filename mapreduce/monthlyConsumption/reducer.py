__author__ = 'Gemma'
import sys

(lastMonth, total) = (None, 0)

for line in sys.stdin:
    (month, Kwh) = line.split('\t')

    if lastMonth and month != lastMonth:
        print ('%s\t%f' % (lastMonth, total))
        (lastMonth, total) = (month, float(Kwh))

    else:
        (lastMonth, total) = (month, total + float(Kwh))

if lastMonth:
    print ('%s\t%f' % (lastMonth, total))