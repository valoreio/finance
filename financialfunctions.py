#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Code styled according to pycodestyle

__author__ = "Marcos Aurelio Barranco"
__copyright__ = "Copyright 2016, The MIT License (MIT)"
__credits__ = ["Marcos Aurelio Barranco", ]
__license__ = "MIT"
__version__ = "1.3"
__maintainer__ = "Marcos Aurelio Barranco"
__email__ = ""
__status__ = "Production"


'''
input: n, i, pv, pmt, fv
calc: Financial functions
return: dict and json
'''


import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
import json


def ln(x):
    return 1000 * ((x ** (1 / 1000)) - 1)


def main(n=0, i=0, pv=0, pmt=0, fv=0):
    '''
    1. to calculate "n" the followings are required: i, pv and fv
       to calculate "i" the followings are required: n, pv, and fv
       to calculate "PV" the followings are required: n, i, and fv
       to calculate "PMT" the followings are required: n, i and fv
                                                   OR  n, i and pv
       to calculate "FV" the followings are required: n, i and pv

    2. The PV value should only be negative on the HP 12C because
       this calculator works with concept of cash flow and initial
       disbursement of cash flow is considered negative

    3. The HP 12C rounds off the periods in months.
       HP 12 C      --> FV=1.126.825,03, PV=1000000, i=1%
                        n equal to 12 months

    3.1. This function doesn't round it
       --> main(i=1, pv=1000000, fv=1126825.03)
       n equal to 12.000654059154352 months/days

       according to 3.1 you'll receive this one:
       0 n 12.000654059154352
       where:
       0 is just the index inside the python dictionary
       n is Periods
       12.000654059154352 is months/days

    4. The calculations were double checked with the HP 12C
       Coded by Marcos Aurelio Barranco
    '''

    d = {}

    if i > 0 and pv > 0 and fv > 0:
        # n = Periods
        nCalc = ln(fv / pv) / ln(1 + (i / 100))
        d['n'] = nCalc

    if n > 0 and pv > 0 and fv > 0:
        # i = Interest rate
        iCalc = ((fv / pv)**(1 / n)) - 1
        locale.setlocale(locale.LC_ALL, '')
        d['i'] = iCalc * 100

    if n > 0 and i > 0 and fv > 0:
        # PV = Present value
        pvCalc = fv / ((1 + (i / 100))**n)
        locale.setlocale(locale.LC_ALL, '')
        d['PV'] = locale.currency(
            pvCalc, grouping=True, symbol=True)

    if n > 0 and i > 0 and fv > 0:
        # PMTFV_GT0 = Periodic Payment Amount when FV > 0
        CalcUpFV = fv
        CalcDownFV = (i / 100) / (((1 + (i / 100))**n) - 1)
        pmtCalcFV = CalcUpFV * CalcDownFV
        d['PMTFV_GT0'] = locale.currency(
            pmtCalcFV, grouping=True, symbol=True)

    if n > 0 and i > 0 and pv > 0:
        # PMTPV_GT0 = Periodic Payment Amount when PV > 0
        CalcUpPV = pv
        CalcDownPV = ((
            (i / 100) * ((1 + (i / 100))**n)) / (((1 + (i / 100))**n) - 1))
        pmtCalcPV = CalcUpPV * CalcDownPV
        d['PMTPV_GT0'] = locale.currency(
            pmtCalcPV, grouping=True, symbol=True)

    if n > 0 and i > 0 and pv > 0:
        # Future value(FV)
        fvCalc = pv * ((1 + (i / 100))**n)
        locale.setlocale(locale.LC_ALL, '')
        d['FV'] = locale.currency(
            fvCalc, grouping=True, symbol=True)

    js = json.dumps(d, ensure_ascii=False)

    # dictionary and json
    return d, js


if __name__ == '__main__':
    try:

        d, js = main(i=1, pv=1000000, fv=1126825)

        print(d) # Dict
        print(js) # json
        
        #for i, j in enumerate(d):
        #    # index, key, value
        #    print(i, j, d[j])

    except Exception as e:
        raise Exception("ErrValFinFunc-1 : {0}".format(e))
