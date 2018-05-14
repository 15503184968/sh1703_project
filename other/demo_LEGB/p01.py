#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 演示LEGB
'''


DEBUG = True


def func_01():
    ''' 演示LEGB的L '''
    print('func_01(): ...')
    x = 3
    print('x: {}'.format(x))


def func_02():
    ''' 演示LEGB的E '''
    print('func_02(): ...')
    x = 3

    def func_02_2():
        print('func_02_2(): ...')
        print('x: {}'.format(x))

    func_02_2()


def func_03():
    ''' 演示LEGB的G '''
    print('func_03(): ...')
    print('DEBUG: {}'.format(DEBUG))


def func_04():
    ''' 演示LEGB的B '''
    print('func_04(): ...')
    x = hex(5)
    print('x: {}'.format(x))


def main():
    func_01()


if __name__ == '__main__':
    main()
