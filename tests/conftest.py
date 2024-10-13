from src.system.battery.SonnenBatterie import SonnenBatterie
from src.system.utils.Utils import Unit
from src.system.PVPanel import PVPanel
from src.system.House import House
from src.system.Grid import Grid
import pytest


@pytest.fixture(params=[("basic", 1), ("standard", 3), ("pro", 5)])
def init_fixture(request):
    panel = PVPanel()
    grid = Grid()
    house = House()
    model = request.param[0]
    no_of_batteries = request.param[1]
    return panel, grid, house, SonnenBatterie(model, no_of_batteries)