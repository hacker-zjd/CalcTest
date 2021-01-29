import sys

import pytest

from calc.calc import Calc, GetData

sys.path.append("..")


class TestCalc:
    get = GetData()
    _data1 = get.get_data('add')
    _data2 = get.get_data('subtract')
    _data3 = get.get_data('multiply')
    _data4 = get.get_data('divide')

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

    @pytest.mark.parametrize('x, y, except_result', _data1[0], ids=_data1[1])
    def test_add(self, x, y, except_result):
        print(f"a={x} , b ={y} ,result={except_result}")
        result = self._calc.add(x, y)
        round(result, 2)
        assert except_result == result

    @pytest.mark.parametrize('x, y, except_result', _data2[0], ids=_data2[1])
    def test_subtract(self, x, y, except_result):
        result = self._calc.subtract(x, y)
        round(result, 2)
        assert except_result == result

    @pytest.mark.parametrize('x, y, except_result', _data3[0], ids=_data3[1])
    def test_multiply(self, x, y, except_result):
        result = self._calc.multiply(x, y)
        round(result, 2)
        assert except_result == result

    @pytest.mark.parametrize('x, y, except_result', _data4[0], ids=_data4[1])
    def test_divide(self, x, y, except_result):
        result = self._calc.divide(x, y)
        round(result, 2)
        assert except_result == result

    if __name__ == '__main__':
        pytest.main(['-v', '-s'])
