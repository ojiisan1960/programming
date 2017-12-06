#!/usr/bin/python

import sys

print "Time to calculate some interest... ok."

print "What is the APR (as a percentage)? ",
apr = float(sys.stdin.readline()) / 100.0
mpr = apr / 12

print "\nWhat is your monthly payment? ",
payment = float(sys.stdin.readline())

print "\nWhat is your beginning balance? ",
balance = float(sys.stdin.readline())

print "-" * 50
print "SCHEDULE..."
print "-" * 50

i = 1
begin_balance = balance
end_balance = balance
total_interest = 0.0
total_paid = 0.0

while end_balance > 0.0:
    print "MONTH", `i`

    interest = mpr * begin_balance
    # Don't overpay.
    if payment <= begin_balance + interest:
        real_payment = payment
    else: real_payment = begin_balance + interest
    
    end_balance = begin_balance + interest - real_payment

    print "\tending balance:"
    print "\t %f + %f - %f = %f" % \
          (begin_balance, interest, real_payment, end_balance)
    ## set up next month.
    i = i + 1
    begin_balance = end_balance
    
    ## count totals.
    total_paid = total_paid + real_payment
    total_interest = total_interest + interest

print "TOTAL PAID: %f\tTOTAL INTEREST PAID: %f" % (total_paid, total_interest)


