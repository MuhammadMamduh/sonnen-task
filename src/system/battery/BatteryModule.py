from src.system.utils.Utils import *
import json


class BatteryModule:
    def __init__(self) -> None:
            self._power_metrics = {
                                    'temp': '40' + Unit.TEMP.value,
                                    'voltage': '100' + Unit.VOLT.value,
                                    'max_charge_power': '1000' + Unit.POWER.value,
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
    
