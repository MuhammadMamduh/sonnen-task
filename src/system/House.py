from src.system.utils.Utils import *
import json


class House:
    def __init__(self) -> None:
        self._power_metrics = {
                                # I = W/V
                                'power_used': '3680' + Unit.POWER.value, # +ve means power going into the house = consumption
                                'house_voltage': '230' + Unit.VOLT.value,
                                'frequency': '50' + Unit.FREQUENCY.value,
                                'current': '16' + Unit.CURRENT.value
                                }
        print("House created!")
        # print(self.get_power_metrics())
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
    
