from src.system.battery.SonnenBatterie import SonnenBatterie
from src.system.PVPanel import PVPanel
from src.system.utils.Utils import Unit
from src.system.Grid import Grid
from src.system.House import House



def main():
    panel = PVPanel()
    grid = Grid()
    house = House()

    panel.set("power_produced", '5000', Unit.POWER.value)
    house.set("power_used", '4500', Unit.POWER.value)
    battery = SonnenBatterie("basic", 2)
    battery.set_amount_of_charge_by_percentage(50)
    print("=====================================")

    battery.controller.power_handler(panel, house, grid, battery)


if __name__ == "__main__":
    main()