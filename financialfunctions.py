#!/usr/bin/env python3
'''
input: n, i, pv, pmt, fv
calc: Financial functions
return: dict and json
'''
# -*- coding: utf-8 -*-
# Code styled according to pycodestyle
# Code parsed, checked possible errors according to pyflakes and pylint

import locale
import json

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


__author__ = "Marcos Aurelio Barranco"
__copyright__ = "Copyright 2016, The MIT License (MIT)"
__credits__ = ["Marcos Aurelio Barranco", ]
__license__ = "MIT"
__version__ = "2"
__maintainer__ = "Marcos Aurelio Barranco"
__email__ = ""
__status__ = "Production"


def logaritmo(periods):
    '''
    Function to calcule ln, logarithm
    '''
    return 1000 * ((periods ** (1 / 1000)) - 1)


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

    dict_retorno = {}

    if i > 0 and pv > 0 and fv > 0:
        # n = Periods
        nCalc = logaritmo(fv / pv) / logaritmo(1 + (i / 100))
        dict_retorno['n'] = nCalc

    if n > 0 and pv > 0 and fv > 0:
        # i = Interest rate
        iCalc = ((fv / pv)**(1 / n)) - 1
        locale.setlocale(locale.LC_ALL, '')
        dict_retorno['i'] = iCalc * 100

    if n > 0 and i > 0 and fv > 0:
        # PV = Present value
        pvCalc = fv / ((1 + (i / 100))**n)
        locale.setlocale(locale.LC_ALL, '')
        dict_retorno['PV'] = locale.currency(
            pvCalc, grouping=True, symbol=True)

    if n > 0 and i > 0 and fv > 0:
        # PMTFV_GT0 = Periodic Payment Amount when FV > 0
        CalcUpFV = fv
        CalcDownFV = (i / 100) / (((1 + (i / 100))**n) - 1)
        pmtCalcFV = CalcUpFV * CalcDownFV
        dict_retorno['PMTFV_GT0'] = locale.currency(
            pmtCalcFV, grouping=True, symbol=True)

    if n > 0 and i > 0 and pv > 0:
        # PMTPV_GT0 = Periodic Payment Amount when PV > 0
        CalcUpPV = pv
        CalcDownPV = ((
            (i / 100) * ((1 + (i / 100))**n)) / (((1 + (i / 100))**n) - 1))
        pmtCalcPV = CalcUpPV * CalcDownPV
        dict_retorno['PMTPV_GT0'] = locale.currency(
            pmtCalcPV, grouping=True, symbol=True)

    if n > 0 and i > 0 and pv > 0:
        # Future value(FV)
        fvCalc = pv * ((1 + (i / 100))**n)
        locale.setlocale(locale.LC_ALL, '')
        dict_retorno['FV'] = locale.currency(
            fvCalc, grouping=True, symbol=True)

    json_retorno = json.dumps(dict_retorno, ensure_ascii=False)

    # dictionary and json
    return dict_retorno, json_retorno


if __name__ == '__main__':
    try:

        dict_ret, json_ret = main(i=1, pv=1000000, fv=1126825)

        print(dict_ret) # Dict
        print(json_ret) # JSON

        for i, j in enumerate(dict_ret):
            # index, key, value
            print(i, j, dict_ret[j])

    except Exception as err:
        raise Exception("ErrValFinFunc-1 : {0}".format(err))
