#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
I create the class Fib to learn iteration and slice.
The secrets are in the function __next__ and __getitem__.
__next__ makes Fib iterable and __getitem__ makes Fib support slice.
* Author : Jiaqi Li
* Date   : 01/25/2019
'''
class Fib(object):
    def __init__(self, n):
        self.a, self.b = 0, 1
        self.temp_a,self.temp_b = 0,1
        self.sample = []
        if isinstance(n, int) and n>0 and n<51:
            for i in range(n):
                self.temp_a, self.temp_b = self.temp_b, self.temp_a + self.temp_b
                self.sample.append(self.temp_a)
            self.Len = len(self.sample)
        else:
            raise ValueError('input parameter must be integer between 1~50')
    
    def __str__(self):
        return 'Fibonacci sequence\n'
    __repr__ = __str__
    
    def __call__(self):
        print('Fibonacci sequence\n')
    
    def __iter__(self):
        return self
        
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        else:
            return self.a
    
    def is_between(self, begin, end, inter):
        return begin <= inter < end or begin >= inter > end
        
    def __getitem__(self, n):
        if isinstance(n, slice):
            L = []
            start, step, stop = n.start, n.step, n.stop
            if step == None:
                step = 1
            # print('start = %s, step = %s, stop = %s' % (start, step, stop))
            if step == 0:
                return L
            elif step > 0:
                if start == None:
                    start = 0
                if stop == None:
                    stop = self.Len
            else:
                if start == None:
                    start = -1
                if stop == None:
                    stop = -self.Len - 1
            if start < 0:
                start += self.Len
            if stop < 0:
                stop += self.Len
            if (stop - start)*step <= 0:
                return L
            elif start < 0 and stop <= 0 or start >= self.Len and stop > self.Len:
                return L
            else:
                start = min(self.Len - 1, max(0, start))
                stop = max(-1, min(self.Len, stop))
                middle = start
                while self.is_between(start, stop, middle):
                    L.append(self.sample[middle])
                    middle += step
                return L 
        elif isinstance(n, int):
            if n < 0:
                n += self.Len
            if 0 <= n and n < self.Len:
                return self.sample[n]
            else:
                raise IndexError('index out of range')
        else:
            raise TypeError('indices must be integers or slices')