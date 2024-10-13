from src.system.utils.Utils import *
import json


class PVPanel:
    is_used = False
    def __init__(self) -> None:

        self._power_metrics = {
                                # In electrical systems, power is calculated as: P = V * I
                                # W represents electrical power consumption per second
                                'power_produced': '300' + Unit.POWER.value,
                                'voltage_produced': '30' + Unit.VOLT.value,
                                'current_produced': '10' + Unit.CURRENT.value
                                }
        print("PVPanel created!")
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
    
