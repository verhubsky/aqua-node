from random import random

from core.pool import Pool


class AquaFarm(object):
    PRICE_COEF = 20

    def __init__(self, budget: float, pools: dict[int, Pool], day: int = 1) -> None:
        self.__budget = budget
        self.__pools = pools
        self.__day = day

    def next_day(self) -> dict[int, dict]:
        self.__day += 1
        daily_report = {}

        for pool_id, pool_object in self.__pools.items():
            pool_stats = pool_object.simulate_day()
            daily_report[pool_id] = pool_stats

        return daily_report

    def buy_feed(self, pool_id: int) -> bool:
        pool_to_refill = self.__pools[pool_id]
        current_budget = self.__budget

        if current_budget <= 0:
            return False

        price = (random() * self.PRICE_COEF) + 1

        if current_budget >= price:
            self.__budget -= price
            pool_to_refill.feeder.refill()
            return True
        return False

    def sell_fish(self, pool_id: int) -> float:
        if pool_id not in self.__pools:
            return 0

        pool = self.__pools[pool_id]
        fishes = pool.fishes

        if fishes.count <= 0:
            return 0

        profit = fishes.count * (fishes.avg_weight / 1000) * 350
        self.__budget += profit
        fishes.count = 0

        return profit

    def get_pools_sorted_by_weight(self) -> list[Pool]:
        return sorted(
            self.__pools.values(), key=lambda pool: pool.fishes.avg_weight, reverse=True
        )

    @property
    def budget(self) -> float:
        return self.__budget

    @property
    def pools(self) -> dict[int, Pool]:
        return self.__pools

    @property
    def day(self) -> int:
        return self.__day
