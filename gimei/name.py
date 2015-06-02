# coding: utf-8
""" SudokuMaker Class """

import math
import random


class Name(object):
    """ name """
    def __init__(self, trgt_num):
        self.__trgt_num = trgt_num
        self.__decision_num = int(math.sqrt(trgt_num))

    def make(self):
        """ make sudoku function
        """
        return sudoku_list
