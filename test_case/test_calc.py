import sys

import pytest
import yaml

from calc.calc import Calc

sys.path.append('..')


def get_data(calc_method):
    with open("./calc.yml") as file:
        datas = yaml.safe_load(file)
    return datas[f'{calc_method}']['datas'], datas[f'{calc_method}']['ids']


class TestCalc:
    _data1 = get_data('add')
    _data2 = get_data('subtract')
    _data3 = get_data('multiply')
    _data4 = get_data('divide')

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

    @pytest.mark.parametrize('x, y, except_result', _data1)
    def test_add(self, x, y, except_result):
        result = self._calc.add(x, y)
        round(result, 2)
        assert except_result == result

    @pytest.mark.parametrize('x, y, except_result', _data2)
    def test_subtract(self, x, y, except_result):
        result = self._calc.subtract(x, y)
        round(result, 2)
        assert except_result == result

    @pytest.mark.parametrize('x, y, except_result', _data3)
    def test_multiply(self, x, y, except_result):
        result = self._calc.multiply(x, y)
        round(result, 2)
        assert except_result == result

    @pytest.mark.parametrize('x, y, except_result', _data4)
    def test_divide(self, x, y, except_result):
        result = self._calc.divide(x, y)
        round(result, 2)
        assert except_result == result
