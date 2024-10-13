from src.system.utils.Utils import Unit
from src.system.PVPanel import PVPanel
from src.system.House import House
from src.system.Grid import Grid



class Controller:

    @staticmethod
    def calculate_charging_rate(battery):
        amount_of_charge_before_charging = battery.get_amount_of_charge()
        charging_rate = int((battery.get_max_storage_capacity() - amount_of_charge_before_charging) / 5)
        print(f"Charging Rate: {charging_rate}{Unit.POWER.value}")
        return charging_rate

    @staticmethod
    def power_handler(panel:PVPanel, house:House, grid:Grid, battery):
        pv_panel_production = panel.get_value("power_produced")
        house_consumption = house.get_value("power_used")
        power_remaining = pv_panel_production - house_consumption
        PVPanel.is_used = True

        # CASE_1: production >= consumption
        if power_remaining >= 0:
            grid.is_used = False
            battery.is_used = False
            if power_remaining == 0:
                print(f"There's no extra power to charge the battery or sell it to the government!")
            else:
                print(f"PV Power Remaining after house consumption = {power_remaining}")
                print(f"Battery is {battery.get_battery_percentage()} % - {battery.get_power_needed_till_full()}{Unit.POWER.value} needed to be full")
                # charge the battery with the extra power
                charging_rate = Controller.calculate_charging_rate(battery)
                while battery.get_battery_percentage() < 100 and power_remaining > 0:
                    battery.charge(charging_rate)
                    power_remaining = power_remaining - charging_rate

                # if still there's an extra power, sell this extra to the government
                if power_remaining > 0:
                    print(f"PV Power Remaining after house consumption & fully charging the battery = {power_remaining}")
                    selling_rate = int(power_remaining / 5)
                    while power_remaining > 0:
                        grid.sell_power(selling_rate)
                        power_remaining -= selling_rate
                else:
                    print(f"All the extra power has been taken to charge the battery, nothing to sell to the government!")
        # CASE_2: production < consumption
        elif power_remaining < 0:
            battery.is_used = False
            grid.is_used = False
            power_needed = power_remaining * -1

            print(f"Power Consumption Deficit = {power_needed}{Unit.POWER.value}")
            print(f"Battery Contains {battery.get_amount_of_charge()}{Unit.POWER.value} ({battery.get_battery_percentage()}%)")
            if battery.get_battery_percentage() > 0:
                # use the battery to fill the power deficiency
                print(f"Therefore, start consuming the battery power")
                discharge_rate = int(battery.get_amount_of_charge() / 5)
                while battery.get_battery_percentage() > 0 and power_needed > 0:
                    battery.is_used = True
                    battery.discharge(discharge_rate)
                    power_needed -= discharge_rate
            # if the battery is not enough, buy from the government
            if power_needed > 0:
                print(f"Power Needed to fill house consumption after emptying the battery = {power_needed}")
                grid_consumption_rate = int(power_needed / 5)
                while power_needed > 0:
                    grid.is_used = True
                    grid.buy_power(grid_consumption_rate)
                    power_needed -= grid_consumption_rate
            else:
                print(f"The Battery has covered the power deficit, no need to buy from the government!")

