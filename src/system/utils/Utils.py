from enum import Enum
import re

class Unit(Enum):
    TEMP = " C"
    VOLT = " V"
    POWER = " W"
    CURRENT = " A"
    FREQUENCY = " Hz"

class Utils:

    @staticmethod
    def int_value(value_and_unit) -> int:
        return list(map(int, re.findall(r'\d+', value_and_unit)))[0]
