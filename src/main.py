from src.system.battery.SonnenBatterie import SonnenBatterie
from src.system.PVPanel import PVPanel
from src.system.utils.Utils import Unit
from src.system.Grid import Grid
from src.system.House import House



def main():
    # panel = PVPanel()

    # panel.set("power_produced", '5000', Unit.POWER.value)
    # panel.set("voltage_produced", '210', Unit.VOLT.value)
    # panel.set("current_produced", '10', Unit.CURRENT.value)
    # print(panel.get_power_metrics())
    # print(panel.get("current_produced"))
    # print(panel.get_value("current_produced"))
     # =================================
    # grid = Grid()
    #
    # grid.set("power_bought", '1000', Unit.POWER.value)
    # grid.set("power_sold", '1000', Unit.POWER.value)
    # grid.set("voltage", '210', Unit.VOLT.value)
    # grid.set("frequency", '10', Unit.FREQUENCY.value)
    #
    # print(grid.get_power_metrics())
    # print(grid.get("frequency"))
    # print(grid.get_value("frequency"))
    # #  # =================================
    # house = House()
    #
    # house.set("power_used", '7000', Unit.POWER.value)
    # house.set("house_voltage", '210', Unit.VOLT.value)
    # house.set("frequency", '10', Unit.FREQUENCY.value)
    # house.set("current", '15', Unit.CURRENT.value)

    # print(house.get_power_metrics())
    # print(house.get("power_used"))
    # print(house.get_value("power_used"))
    # =================================

    panel = PVPanel()
    grid = Grid()
    house = House()

    panel.set("power_produced", '5000', Unit.POWER.value)
    house.set("power_used", '7000', Unit.POWER.value)
    battery = SonnenBatterie("pro", 1)

    battery.controller.power_handler(panel, house, grid, battery)


if __name__ == "__main__":
    main()