__author__ = 'Gemma'

import csv
import sys
from datetime import datetime


for line in sys.stdin:
    (fechaHora, Kwh) = line.split(';')

    mes = datetime.strptime(fechaHora, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m')
    try:
        Kwh = float(Kwh)
    except ValueError:
        Kwh = 0

    print ('%s\t%f' % (mes, Kwh))