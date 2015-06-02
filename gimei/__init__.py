# coding:utf-8
""" gimei """

from .gimei import Name


def make(trgt_num=9):
    """ main

    Keyword arguments:
    trgt_num -- target number of sudoku
    """
    if trgt_num not in [4, 9, 16, 25, 36, 49, 64, 81, 100]:
        trgt_num = 9
    sudoku_maker = SudokuMaker(trgt_num)
    return sudoku_maker.make()
