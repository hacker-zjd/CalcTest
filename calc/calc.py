import os
import sys

import yaml


class Calc:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            x / y
        except ZeroDivisionError:
            print("You can't divide by zero.")
        return x / y


sys.path.append("..")


class GetData:
    def get_data(self, name):
        path = os.path.join(os.getcwd(), "../calc.yml")
        print(path)
        with open(path) as file:
            datas = yaml.safe_load(file)
        return (datas[f'{name}']['datas'], datas[f'{name}']['ids'])
