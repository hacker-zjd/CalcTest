#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

import pytest
import yaml

from calc.calc import Calc

sys.path.append("..")


def get_data():
    file = "./data/calc.yml"
    if not os.path.exists(file):
        raise FileNotFoundError("No such file: calc.yml")
    with open(file) as f:
        datas: list = yaml.safe_load(f)
    return datas


class TestCalc:
    data = get_data()
    print(data)

    @classmethod
    def setup_class(cls):
        print("开始计算")

    @classmethod
    def teardown_class(cls):
        print("计算结束")

    def setup(self):
        self._calc = Calc()
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('x, y, except_result', data['add']['datas'], ids=data['add']['ids'])
    def test_add(self, x, y, except_result):
        print(f"a={x} , b ={y} ,result={except_result}")
        result = self._calc.add(x, y)
        round(result, 2)
        assert except_result == result

    @pytest.mark.parametrize('x, y, except_result', data['subtract']['datas'], ids=data['subtract']['ids'])
    def test_subtract(self, x, y, except_result):
        result = self._calc.subtract(x, y)
        round(result, 2)
        assert except_result == result

    @pytest.mark.parametrize('x, y, except_result', data['multiply']['datas'], ids=data['multiply']['ids'])
    def test_multiply(self, x, y, except_result):
        result = self._calc.multiply(x, y)
        round(result, 2)
        assert except_result == result

    @pytest.mark.parametrize('x, y, except_result', data['divide']['datas'], ids=data['divide']['ids'])
    def test_divide(self, x, y, except_result):

        if y == 0:
            try:
                self._calc.divide(x, y)
            except ZeroDivisionError as e:
                print("You can't divide by zero")
        else:
            result = self._calc.divide(x, y)
            round(result, 2)
            assert except_result == result

    if __name__ == '__main__':
        pytest.main(['-v', '-s'])
