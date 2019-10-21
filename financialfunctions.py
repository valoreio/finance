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
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def ln(x):
    n = 1000
    return n * ((x ** (1 / n)) - 1)


def main(fct, n=0, i=0, pv=0, pmt=0, fv=0):
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
       HP 12 C      --> FV=1638.37, PV=1000, i=4.199987193598798%
                        n equal to 12 months

       This function doesn't round it
       --> main(fct='n', i=4.199987193598798, pv=1000, fv=1638.37)
       n equal to 12.00267993234954 months/days

    4. The calculations were double checked with the HP 12C
       Coded by Marcos Aurelio Barranco
    '''

    if fct == 'n' and i > 0 and pv > 0 and fv > 0:
        # Periods(n)
        # to i=4.199987193598798%, pv=1000 and fv=1638.37 it returns 12.002715788466276 months
        nCalc = ln(fv / pv) / ln(1 + (i / 100))
        return "Periods(n) :", nCalc

    if fct == 'i' and n > 0 and pv > 0 and fv > 0:
        # Interest rate(i)
        # to n=12, pv=1000 and fv=1638.37 it returns 4.199987193598798%
        iCalc = ((fv / pv)**(1 / n)) - 1
        locale.setlocale(locale.LC_ALL, '')
        return "Interest rate(i) %: ", iCalc * 100

    if fct == 'pv' and n > 0 and i > 0 and fv > 0:
        # Present value(PV)
        # to fv=1638.37, i=4.199987193598798%, n=12 it returns 1000
        pvCalc = fv / ((1 + (i / 100))**n)
        locale.setlocale(locale.LC_ALL, '')
        return "Present value(PV) :", locale.currency(
            pvCalc, grouping=True, symbol=True)

    if fct == 'pmt-fv' and n > 0 and i > 0 and fv > 0:
        # Periodic Payment Amount(PMT) when FV > 0
        # to fv=1638.37, i=4.199987193598798%, n=12 it returns 107.79
        CalcUpFV = fv
        CalcDownFV = (i / 100) / (((1 + (i / 100))**n) - 1)
        pmtCalcFV = CalcUpFV * CalcDownFV
        return "Periodic Payment Amount(PMT-FV>0) :", locale.currency(
            pmtCalcFV, grouping=True, symbol=True)
            
    if fct == 'pmt-pv' and n > 0 and i > 0 and pv > 0:
        # Periodic Payment Amount(PMT) when PV > 0
        # to pv=1000, i=4.199987193598798%, n=12 it returns 107.79
        CalcUpPV = pv
        CalcDownPV = ((
            (i / 100) * ((1 + (i / 100))**n)) / (((1 + (i / 100))**n) - 1))
        pmtCalcPV = CalcUpPV * CalcDownPV
        return "Periodic Payment Amount(PMT-PV>0)", locale.currency(
            pmtCalcPV, grouping=True, symbol=True)

    if fct == 'fv' and n > 0 and i > 0 and pv > 0:
        # Future value(FV)
        # to n=12, i=4.199987193598798%, pv=1000 it returns 1638.37
        fvCalc = pv * ((1 + (i / 100))**n)
        locale.setlocale(locale.LC_ALL, '')
        return "Future value(FV)", locale.currency(
            fvCalc, grouping=True, symbol=True)


if __name__ == '__main__':
    try:
        retorno, value = main(fct='n', i=4.199987193598798, pv=1000, fv=1638.37)
        print(retorno, value)
        retorno, value = main(fct='i', n=12, pv=1000, fv=1638.37)
        print(retorno, value)
        retorno, value = main(fct='pv', n=12, i=4.199987193598798, fv=1638.37)
        print(retorno, value)
        retorno, value = main(fct='pmt-fv', n=12, i=4.199987193598798, fv=1638.37)
        print(retorno, value)
        retorno, value = main(fct='pmt-pv', n=12, i=4.199987193598798, pv=1000)
        print(retorno, value)
        retorno, value = main(fct='fv', n=12, i=4.199987193598798, pv=1000)
        print(retorno, value)

    except Exception as e:
        raise Exception("ErrValFinFunc-1 : {0}".format(e))
