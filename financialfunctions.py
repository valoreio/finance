#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Code styled according to pycodestyle

__author__ = "Marcos Aurelio Barranco"
__copyright__ = "Copyright 2016, The MIT License (MIT)"
__credits__ = ["Marcos Aurelio Barranco", ]
__license__ = "MIT"
__version__ = "1.2"
__maintainer__ = "Marcos Aurelio Barranco"
__email__ = ""
__status__ = "Production"

'''
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
# ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


import locale


def ln(x):
    n = 1000.0
    return n * ((x ** (1 / n)) - 1)

def financial_functions(n=0, i=0, pv=0, pmt=0, fv=0):
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
       HP 12 C      --> FV=1638.37, PV=1000, i=4.20
                        n equal to 12 months

       This function doesn't round it
       --> FinancialFunctions(i=4.2, pv=1000, fv=1638.37)
       n equal to 12.00267993234954 months/days

    4. The calculations were double checked with the HP 12C
       Coded by Marcos Aurelio Barranco
    '''

    if n == 0 and fv > 0 and pv > 0 and i > 0:
        nCalc = valoreio.ln(fv / pv) / valoreio.ln(1 + (i / 100))
        print("Periods(n) = {}".format(nCalc))

    if i == 0 and fv > 0 and pv > 0 and n > 0:
        iCalc = ((fv / pv)**(1 / n)) - 1
        locale.setlocale(locale.LC_ALL, '')
        print("Interest rate(i) = {}%".format(iCalc * 100))

    if pv == 0 and fv > 0 and i > 0 and n > 0:
        pvCalc = fv / ((1 + (i / 100))**n)
        locale.setlocale(locale.LC_ALL, '')
        print("Present value(PV) = {}".format(
            locale.currency(pvCalc, grouping=True, symbol=True)))

    if pmt == 0 and fv > 0 and i > 0 and n > 0:
        CalcUpFV = fv
        CalcDownFV = (i / 100) / (((1 + (i / 100))**n) - 1)
        pmtCalcFV = CalcUpFV * CalcDownFV
        print("Periodic Payment Amount(PMT) = {}".format(
            locale.currency(pmtCalcFV, grouping=True, symbol=True)))

    if pmt == 0 and pv > 0 and i > 0 and n > 0:
        CalcUpPV = pv
        CalcDownPV = ((
            (i / 100) * ((1 + (i / 100))**n)) / (((1 + (i / 100))**n) - 1))
        pmtCalcPV = CalcUpPV * CalcDownPV
        print("Periodic Payment Amount(PMT) = {}".format(
            locale.currency(pmtCalcPV, grouping=True, symbol=True)))

    if fv == 0 and pv > 0 and i > 0 and n > 0:
        fvCalc = pv * ((1 + (i / 100))**n)
        locale.setlocale(locale.LC_ALL, '')
        print("Future value(FV) = {}".format(
            locale.currency(fvCalc, grouping=True, symbol=True)))


if __name__ == '__main__':
    try:
        print(financial_functions(n=12, pv=1000, fv=1638.37))

    except Exception as e:
        raise Exception("ErrValFinFunc-1 : {0}".format(e))
