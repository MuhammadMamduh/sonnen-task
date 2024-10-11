import pytest

from src.system.PVPanel import PVPanel
from src.system.Grid import Grid
from src.system.House import House
from src.system.battery.SonnenBatterie import SonnenBatterie
from src.system.utils.Utils import Unit

@pytest.fixture(params=[("basic", 1), ("standard", 3), ("pro", 5)])
def scenario_1():
    panel = PVPanel()
    house = House()
    battery = SonnenBatterie("basic", 1)
    grid = Grid()

    #IF
    panel.set("power_produced", "5000", Unit.POWER.value)
    house.set("power_used", "1000", Unit.POWER.value)
    # Then
    # IF battery % < 100 charge it
    # IF battery % = 100, sell to the grid


@pytest.fixture
def my_pv_panel():
    panel = PVPanel()
    panel.set("power_produced", "5000", Unit.POWER.value)
    return PVPanel()

@pytest.fixture
def my_house():
    house = House()
    house.set("power_used", "1000", Unit.POWER.value)
    return House()

@pytest.fixture(params=[("basic", 1), ("standard", 3), ("pro", 5)])
def my_battery(request):
    model = request.param[0]
    no_of_batteries = request.param[1]
    return SonnenBatterie(model, no_of_batteries)

@pytest.fixture
def the_grid():
    return Grid()

# @pytest.mark.parametrize("a,b,expected", testdata)
def test_sb_consumption_less_than_pv_and_remaining_more_than_zero(my_battery):
    panel = PVPanel()
    house = House()
    battery = SonnenBatterie("basic", 1)
    grid = Grid()

    #IF power_produced >= power_used
    panel.set("power_produced", "5000", Unit.POWER.value)
    house.set("power_used", "1000", Unit.POWER.value)
    # Use panel
    # Then IF power_remaining > 0
    # battery % < 100 charge it
    # battery % = 100, sell to the grid
    # ELSE ... do nothing
def test_sb_consumption_less_than_pv_and_remaining_equals_than_zero():
    print("test_sb_consumption_less_than_pv_and_remaining_equals_than_zero")
def test_sb_consumption_more_than_pv_and_storage_is_enough():
    print("test_sb_consumption_less_than_pv_and_remaining_equals_than_zero")
def test_sb_consumption_more_than_pv_and_storage_is_not_enough():
    print("test_sb_consumption_more_than_pv_and_storage_is_not_enough")