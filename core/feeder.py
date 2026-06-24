class AutoFeeder(object):
    def __init__(self, capacity: float, current_load: float, daily_rate: float) -> None:
        self.__capacity = max(0, capacity)
        self.__current_load = min(current_load, self.__capacity)
        self.__daily_rate = max(0, daily_rate)

    def feed_fishes(self) -> None:
        current_load = self.__current_load

        if current_load <= 0:
            return

        self.__current_load = max(0, current_load - self.__daily_rate)

    def refill(self) -> None:
        self.__current_load = self.__capacity

    @property
    def capacity(self) -> float:
        return self.__capacity

    @property
    def current_load(self) -> float:
        return self.__current_load

    @property
    def daily_rate(self) -> float:
        return self.__daily_rate
