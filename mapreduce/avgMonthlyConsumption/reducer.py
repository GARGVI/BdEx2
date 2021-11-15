__author__ = 'Gemma'
import sys

(countMonths, total) =(0,0)

for line in sys.stdin:
    (month, totalKwh) = line.split('\t')
    (countMonths, total)  = (countMonths + 1, total + float(totalKwh))

avgMonthlyConsumption = total/countMonths
print ('%s\t%f' % ('avgMonthlyConsumption', avgMonthlyConsumption))