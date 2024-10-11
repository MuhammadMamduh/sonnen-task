from src.system.utils.Utils import *
import json


class Grid:
    is_used = False
    def __init__(self) -> None:
        self._power_metrics = {
                                # W represents electrical power consumption per second
                                'power_bought': '0' + Unit.POWER.value,
                                'power_sold': '0' + Unit.POWER.value,
                                'voltage': '230' + Unit.VOLT.value,
                                'frequency': '50' + Unit.FREQUENCY.value,
                                }
        print("Grid created with default values as follows: ")
        print(self.get_power_metrics())
    def set(self, key: str, value: str, measurement: str) -> bool:
        if key in self._power_metrics:
            self._power_metrics[key] = value + measurement
            return True
        else:
            return False
    
    def get(self, key: str) -> str:
        return str(self._power_metrics.get(key))

    def get_value(self, key: str) -> int:
        return Utils.int_value(self._power_metrics.get(key))

    def get_power_metrics(self) -> str:
        return json.dumps(self._power_metrics, indent=4)

    def sell_power(self, amount):
        power_sold = self.get_value("power_sold")
        print(f"Current Power Sold  = {power_sold} {Unit.POWER.value}")

        power_sold+=amount

        self.set("power_sold", str(power_sold), Unit.POWER.value)

    def buy_power(self, amount):
        power_bought = self.get_value("power_bought")
        print(f"Current Power Bought  = {power_bought} {Unit.POWER.value}")

        power_bought+=amount

        self.set("power_bought", str(power_bought), Unit.POWER.value)
    
