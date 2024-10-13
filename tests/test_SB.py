from src.system.utils.Utils import Unit
import pytest


@pytest.mark.parametrize("power_produced, power_used", [("5000", "3000")])
def test_pv_production_greater_than_house_consumption(init_fixture, power_produced, power_used):
    # basic -> charge the battery, & sell to the government
    # standard -> charge the battery, & sell to the government
    # pro -> charge the battery, but not enough to sell
    panel, grid, house, battery = init_fixture
    panel.set("power_produced", power_produced, Unit.POWER.value)
    house.set("power_used", power_used, Unit.POWER.value)
    battery.set_amount_of_charge_by_percentage(50)

    prev_battery_charge = battery.get_amount_of_charge()
    battery_max_charge = battery.max_storage_capacity
    battery_need_of_charge = battery_max_charge - prev_battery_charge
    prev_power_bought = grid.get_value("power_bought")
    prev_power_sold = grid.get_value("power_sold")
    print("====================================================")
    battery.controller.power_handler(panel, house, grid, battery)
    print("====================================================")
    extra_power = int(power_produced) - int(power_used)
    extra_power_after_charging_the_battery = extra_power - battery_need_of_charge

    if extra_power > 0:
        new_power_bought = grid.get_value("power_bought")
        assert prev_power_bought == new_power_bought

    if extra_power_after_charging_the_battery > 0:
        new_power_sold = grid.get_value("power_sold")
        assert new_power_sold == prev_power_sold + extra_power_after_charging_the_battery

    if extra_power >= battery_need_of_charge:
        assert battery.get_amount_of_charge() == battery_max_charge
    else:
        expected_battery_charge = prev_battery_charge + extra_power
        assert battery.get_amount_of_charge() == expected_battery_charge

@pytest.mark.parametrize("power_produced, power_used", [("5000", "5000")])
def test_pv_production_equals_house_consumption(init_fixture, power_produced, power_used):
    # basic -> consume all the power generated, nothing left to charge the battery or sell to the government
    # standard -> consume all the power generated, nothing left to charge the battery or sell to the government
    # pro -> consume all the power generated, nothing left to charge the battery or sell to the government
    panel, grid, house, battery = init_fixture
    panel.set("power_produced", power_produced, Unit.POWER.value)
    house.set("power_used", power_used, Unit.POWER.value)
    battery.set_amount_of_charge_by_percentage(50)

    prev_battery_charge = battery.get_amount_of_charge()
    prev_power_bought = grid.get_value("power_bought")
    prev_power_sold = grid.get_value("power_sold")
    print("====================================================")
    battery.controller.power_handler(panel, house, grid, battery)
    print("====================================================")
    extra_power = int(power_produced) - int(power_used)

    assert extra_power == 0

    new_power_bought = grid.get_value("power_bought")
    assert prev_power_bought == new_power_bought

    new_power_sold = grid.get_value("power_sold")
    assert new_power_sold == prev_power_sold

    assert prev_battery_charge == battery.get_amount_of_charge()

@pytest.mark.parametrize("power_produced, power_used", [("5000", "7000")])
def test_pv_production_less_than_house_consumption(init_fixture, power_produced, power_used):
    # basic -> discharge the battery & buy
    # standard -> discharge the battery & buy
    # pro -> discharge, no need to buy
    panel, grid, house, battery = init_fixture
    panel.set("power_produced", power_produced, Unit.POWER.value)
    house.set("power_used", power_used, Unit.POWER.value)
    battery.set_amount_of_charge_by_percentage(50)

    prev_battery_charge = battery.get_amount_of_charge()
    prev_power_bought = grid.get_value("power_bought")
    prev_power_sold = grid.get_value("power_sold")
    print("====================================================")
    battery.controller.power_handler(panel, house, grid, battery)
    print("====================================================")
    power_shortage = int(power_used) - int(power_produced)
    power_shortage_after_discharging_the_battery = power_shortage - prev_battery_charge

    if power_shortage > 0:
        new_power_sold = grid.get_value("power_sold")
        assert prev_power_sold == new_power_sold

    if power_shortage_after_discharging_the_battery > 0:
        new_power_bought = grid.get_value("power_bought")
        assert new_power_bought == prev_power_bought + power_shortage_after_discharging_the_battery

    if power_shortage >= prev_battery_charge:
        assert battery.get_amount_of_charge() == 0
    else:
        expected_battery_charge = prev_battery_charge - power_shortage
        assert battery.get_amount_of_charge() == expected_battery_charge