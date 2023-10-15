from main import Bulb

bulb = Bulb()
def test_bulb_isOff():
    assert bulb.getStatus() == "Bulb is not glowing"

def test_bulb_isOn():
    bulb.isOn()
    assert bulb.getStatus() == "Bulb is glowing"

def test_bulb_status():
    bulb.isOff()
    assert bulb.getStatus() == "Bulb is not glowing"

