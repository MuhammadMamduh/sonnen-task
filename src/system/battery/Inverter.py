from src.system.utils.Utils import *
import json


class Inverter:
    def __init__(self) -> None:
        self._power_metrics = {
                                'max_charge_power': '10' + Unit.POWER.value,
                                'actual_power_inuse': '10' + Unit.POWER.value,
                                'battery_voltage': '102' + Unit.VOLT.value,
                                'sensed_grid_voltage': '220' + Unit.VOLT.value,
                                'current_in': '20' + Unit.CURRENT.value,
                                'grid_freq': '50' + Unit.FREQUENCY.value,
                                }

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
    
