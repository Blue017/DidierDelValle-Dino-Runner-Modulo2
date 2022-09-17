from dino_runner.components.power_ups.power_up import Power_Up
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

class Shield(Power_Up):
    def __init__(self) -> None:
        super().__init__(SHIELD, SHIELD_TYPE)