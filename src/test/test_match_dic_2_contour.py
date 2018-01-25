# import add_path fist to add path to sys.path
from .add_path import *
import unittest
from libs.match_dic_2_contour import match_dic_2_contour
'''
summary: create a class and add a method for each test.

to_do: for more tests, the test_list will go to another file

'''


class MatchDic2Contour(unittest.TestCase):
    pass

def make_method(input_):
    test_name = 'test_{}'.format(input_[0]+input_[1]+input_[3])
    def test_input(self):
        self.assertTrue(match_dic_2_contour(*input_),u'{}  failed'.format(input_))
    return test_name, test_input

def add_methods(klass, *inputs):
    for input in inputs:
        test_name, test_input = make_method(input_ = input)
        setattr(klass, test_name, test_input)

test1  = ('../final_data/dicoms/SCD0000201', '../final_data/contourfiles/SC-HF-I-2/i-contours/IM-0001-0100-icontour-manual.txt',True,'13.dcm')

test2  = ('../final_data/dicoms/SCD0000201', '../final_data/contourfiles/SC-HF-I-2/i-contours/IM-0001-0100-icontour-manual.txt',True,'60.dcm')

test_list = [test1,test2]
add_methods(MatchDic2Contour,*test_list)
