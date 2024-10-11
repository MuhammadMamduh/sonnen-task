from src.system.PVPanel import PVPanel
from src.system.House import House
from src.system.Grid import Grid


class Controller:
    def __init__(self) -> None:
        print("Controller ... Processing ...")

    @staticmethod
    def power_handler(panel:PVPanel, house:House, grid:Grid, battery):
        pv_panel_production = panel.get_value("power_produced")
        house_consumption = house.get_value("power_used")
        power_remaining = pv_panel_production - house_consumption

        print(f"Power Remaining after house consumption = {power_remaining}")
        PVPanel.is_used = True
        # CASE_1: production >= consumption
        if power_remaining >= 0:
            grid.is_used = False
            battery.is_used = False
            # special case
            if power_remaining == 0:
                print(f"There's no extra power to charge the battery or sell it to the government!")
            # charge the batter with the extra power
            while battery.get_battery_percentage() < 100 and power_remaining > 0:
                battery.charge(10)
                power_remaining -= 10
            # if still there's an extra power, sell this extra to the government
            while power_remaining > 0:
                grid.sell_power(10)
                power_remaining -= 10
        # CASE_2: production < consumption
        elif power_remaining < 0:
            battery.is_used = False
            grid.is_used = False

            power_needed = power_remaining * -1
            print(f"Therefore, power Needed after house consumption = {power_needed}")
            # use the battery to fill the power deficiency
            while battery.get_battery_percentage() > 0 and power_needed > 0:
                battery.is_used = True
                battery.discharge(10)
                power_remaining -= 10
            # if the battery is not enough, buy from the government
            while power_needed > 0:
                grid.is_used = True
                grid.buy_power(10)
                power_needed -= 10
    
