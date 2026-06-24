from random import random

from core.feeder import AutoFeeder
from core.fish import FishBatch


class Pool(object):
    OXYGEN_COEF = 15
    POLLUTION_COEF = 13

    def __init__(
        self,
        pool_id: int,
        oxygen_level: float,
        pollution_level: float,
        fishes: FishBatch,
        feeder: AutoFeeder,
    ) -> None:
        self.__pool_id = pool_id
        self.__oxygen_level = min(100, oxygen_level)
        self.__pollution_level = max(0, pollution_level)
        self.__fishes = fishes
        self.__feeder = feeder

    def aerate_water(self) -> None:
        current_oxygen_level = self.__oxygen_level
        self.__oxygen_level = min(
            100, current_oxygen_level + (random() * self.OXYGEN_COEF * 1.5)
        )

    def clean_filter(self) -> None:
        current_pollution_level = self.__pollution_level
        self.__pollution_level = max(
            0, current_pollution_level - (random() * self.POLLUTION_COEF * 1.5)
        )

    def simulate_day(self):
        self.aerate_water()
        self.clean_filter()

        # If there are fish on farm
        if self.fishes.count > 0:
            if self.feeder.current_load > 0:
                self.feeder.feed_fishes()
                self.fishes.grow()
            else:
                self.fishes.die()

            # More fish weigth -> more polluion and more they consume xygen
            biomass_factor = (self.fishes.count * self.fishes.avg_weight) / 20000.0

            self.__pollution_level += (random() * self.POLLUTION_COEF) * (
                1 + biomass_factor
            )
            self.__oxygen_level -= (random() * self.OXYGEN_COEF) * (1 + biomass_factor)

        # Critical problems on farm
        if self.__oxygen_level < 15 or self.__pollution_level > 65:
            self.fishes.die()

            self.__pollution_level -= 10
            self.__oxygen_level += 10

        self.__pollution_level = max(0, min(100, self.__pollution_level))
        self.__oxygen_level = max(0, min(100, self.__oxygen_level))

        return {
            "oxygen_level": self.__oxygen_level,
            "pollution_level": self.__pollution_level,
            "fish_count": self.fishes.count,
            "current_load": self.feeder.current_load,
        }

    @property
    def pool_id(self) -> int:
        return self.__pool_id

    @property
    def oxygen_level(self) -> float:
        return self.__oxygen_level

    @property
    def pollution_level(self) -> float:
        return self.__pollution_level

    @property
    def fishes(self) -> FishBatch:
        return self.__fishes

    @property
    def feeder(self) -> AutoFeeder:
        return self.__feeder
