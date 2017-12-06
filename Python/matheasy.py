#!/usr/bin/env python
from string import lower
from operator import add, sub, mul
from random import randint, choice

ops = { '+': add, '-': sub, '*': mul }
MAXTRIES = 2

def doprob():
    op = choice('+-*')
    nums = [randint(1,10), randint(1,10)]
    nums.sort() ; nums.reverse()
    ans = apply(ops[op], nums)
    pr = '%d %s %s = ' % (nums[0], op, nums[1])
    oops = 0
    while 1:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if oops == MAXTRIES:
                print 'sorry... the answer is\n%s%d' % (pr, ans)
            else:
                print 'incorrect... try again'
                oops = oops + 1
        except (KeyboardInterrupt, EOFError,
                        ValueError), diag:
            print 'invalid input... try again'

def main():
    while 1:
        doprob()
        try:
            opt = lower(raw_input('Try another? ([y]/n) '))
        except (KeyboardInterrupt, EOFError):
            print ; break
        if opt and opt[0] == 'n':
            break

if __name__ == '__main__':
    main()
