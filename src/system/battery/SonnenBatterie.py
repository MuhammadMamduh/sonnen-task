from src.system.battery.BatteryModule import BatteryModule
from src.system.battery.Controller import Controller
from src.system.battery.Inverter import Inverter
from src.system.utils.Utils import Unit


class SonnenBatterie:
    is_used = False
    def __init__(self, model: str, no_of_batteries: int) -> None:
        self.__input_validation(self, model, no_of_batteries)

        self.controller = Controller()
        self.inverter = Inverter()
        self.battery_module = []
        for x in range(no_of_batteries):
            self.battery_module.append(BatteryModule())

        # Added Value
        self.no_of_batteries = no_of_batteries
        self.max_storage_capacity = self.no_of_batteries * self.battery_module[0].get_value("max_charge_power")
        self.amount_of_charge = self.max_storage_capacity
        print(f'This sonnenBatterie is of "{model}" model & it contains {no_of_batteries} battery module(s), each of {self.battery_module[0].get("max_charge_power")}, the total storage capacity = {self.max_storage_capacity}{Unit.POWER.value}')
        # print(f"The details of each battery module is: {self.battery_module[0].get_power_metrics()}")
        # print(f"This sonnenBatterie contains an Inverter with following details: {self.inverter.get_power_metrics()}")
        # print(f"This sonnenBatterie contains a Controller that controllers the Logic behind the power management")

    @staticmethod
    def __input_validation(self, model: str, no_of_batteries: int):
        models = ["basic", "standard", "pro"]
        # generic validation
        if model not in models:
            raise ValueError(f"The model value entered is not valid! The valid values are {models}, Value entered = {no_of_batteries}")
        elif no_of_batteries < 1:
            raise ValueError(f"Number of batteries cannot be less than 0! Value entered = {no_of_batteries}")
        elif no_of_batteries > 5:
            raise ValueError(f"Number of batteries cannot be more than 5! Value entered = {no_of_batteries}")

        # plan-specific validation
        if model.lower() == "basic" and no_of_batteries > 2:
            raise ValueError(f"For the basic battery model, the number of batteries cannot be more than 2! Value entered = {no_of_batteries}")
        elif model.lower() == "standard" and no_of_batteries > 3:
            raise ValueError(f"For the basic battery model, the number of batteries cannot be more than 3! Value entered = {no_of_batteries}")

    def get_max_storage_capacity(self):
        return self.max_storage_capacity

    def get_amount_of_charge(self):
        return self.amount_of_charge

    def get_power_needed_till_full(self):
        return self.max_storage_capacity - self.amount_of_charge

    def set_amount_of_charge_by_watt(self, amount: int):
        if (amount > 0) and (amount < self.max_storage_capacity):
            self.amount_of_charge = amount
            print(f"Current amount of charge = {self.amount_of_charge}")
        else:
            print(f"Invalid value, amount of charge should be > 0 and < Max Capacity (= {self.no_of_batteries * self.battery_module[0].get_value("max_charge_power")})")

    def set_amount_of_charge_by_percentage(self, percent: int):
        if (percent > 0) and (percent <= 100):
            self.amount_of_charge = int((self.max_storage_capacity * percent)/100)
            print(f"The Battery is now {self.get_battery_percentage()}% charged ({self.amount_of_charge}{Unit.POWER.value})")
        else:
            print(f"Invalid value, percentage of charge should be between 1 and 100")

    def get_battery_percentage(self):
        each_battery_max_charge_power = self.battery_module[0].get_value("max_charge_power")
        return int((self.amount_of_charge / (self.no_of_batteries * each_battery_max_charge_power))*100)

    def discharge(self, amount):
        battery_percentage = self.get_battery_percentage()
        print(f"Current Battery {battery_percentage} %")
        if battery_percentage == 0:
            print(f"Battery is Empty!")
        else:
            if self.amount_of_charge - amount <= 0:
                self.amount_of_charge = 0
            else:
                self.amount_of_charge -= amount
            battery_percentage = self.get_battery_percentage()
            print(f"Battery is discharging ... {battery_percentage}%")

    def charge(self, amount):
        if self.amount_of_charge + amount >= self.max_storage_capacity:
            self.amount_of_charge = self.max_storage_capacity
            battery_percentage = self.get_battery_percentage()
            print(f"Battery is full!")
        else:
            self.amount_of_charge = self.amount_of_charge + amount
            battery_percentage = self.get_battery_percentage()
            print(f"Battery is charging ...")
        print(f"Battery is {battery_percentage} % charged ( = {self.get_amount_of_charge()}{Unit.POWER.value})")




    # def discharge_till_empty(self):
    #     battery_percentage = self.get_battery_percentage()
    #     print(f"Current Battery Charge is {battery_percentage} %")
    #     while self.amount_of_charge >0 and battery_percentage > 0:
    #         battery_percentage = self.get_battery_percentage()
    #         self.amount_of_charge = self.amount_of_charge - 10
    #         if self.amount_of_charge % 10 ==0:
    #             print(f"Battery is in use ... discharging ... {battery_percentage}%")
    #     print(f"Battery is Empty {battery_percentage}%")


    # def charge_till_full(self):
    #     battery_percentage = self.get_battery_percentage()
    #     print(f"Current Battery {battery_percentage} %")
    #     each_battery_max_charge_power = self.battery_module[0].get_value("max_charge_power")
    #     while self.amount_of_charge < self.no_of_batteries*each_battery_max_charge_power and battery_percentage <100:
    #         battery_percentage = self.get_battery_percentage()
    #         self.amount_of_charge = self.amount_of_charge
    #         if self.amount_of_charge % 10 == 0:
    #             print(f"Battery is charging ... {battery_percentage}%")
    #     print(f"Battery is full {str(self.get_battery_percentage())}%")
