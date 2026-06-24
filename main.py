from core.farm import AquaFarm
from resources.objects import p1, p2, p3


def main() -> None:
    pools_dict = {
        p1.pool_id: p1,
        p2.pool_id: p2,
        p3.pool_id: p3,
    }

    farm = AquaFarm(budget=1000.0, pools=pools_dict)

    try:
        while True:
            print(f"\nДень: {farm.day} | Бюджет: {farm.budget:.2f}")
            print("1. Симуляция следующего дня")
            print("2. Пополнить кормушку")
            print("3. Вывести статус рыб в бассейнах")
            print("4. Продать рыбу")
            print("5. Сортировка бассейнов по весу")
            print("0. Выход")

            choice = input("Выберите действие: ")

            match choice:
                case "1":
                    report = farm.next_day()

                    print("\nСтатистика:")

                    for p_id, stats in report.items():
                        print(
                            f"Бассейн {p_id} | "
                            f"Уровень кислорода: {stats['oxygen_level']:.1f}% | "
                            f"Уровень загрязнения: {stats['pollution_level']:.1f}% | "
                            f"Количество рыб: {stats['fish_count']} | "
                            f"Корма в кормушке: {stats['current_load']:.1f}"
                        )

                case "2":
                    try:
                        pool_id = int(
                            input("Введите ID бассейна для пополнения кормушки: ")
                        )

                        if pool_id in farm.pools:
                            success = farm.buy_feed(pool_id)
                            if success:
                                print(f"Кормушка бассейна {pool_id} успешно пополнена.")
                            else:
                                print("Недостаточно средств в бюджете.")
                        else:
                            print("Бассейн с таким ID не существует.")
                    except ValueError:
                        print("Ошибка: необходимо ввести числовой ID бассейна.")

                case "3":
                    print("\nДетальный статус рыб:")

                    for pool_id, pool in farm.pools.items():
                        print(
                            f"Бассейн {pool_id} | "
                            f"Вид: {pool.fishes.species} | "
                            f"Особей: {pool.fishes.count} единиц | "
                            f"Средний вес: {pool.fishes.avg_weight:.2f} | Корма: {pool.feeder.current_load:.1f}"
                        )

                case "4":
                    try:
                        pool_id = int(input("Введите ID бассейна для продажи рыбы: "))
                        revenue = farm.sell_fish(pool_id)

                        if revenue > 0:
                            print(f"Партия успешно продана. Выручка: {revenue:.2f}")
                        else:
                            print(f"В бассейне (ID={pool_id}) нет рыбы для продажи.")

                    except ValueError:
                        print("Ошибка: необходимо ввести числовой ID бассейна.")

                case "5":
                    sorted_pools = farm.get_pools_sorted_by_weight()
                    print("\nБассейны по убыванию веса рыбы:")
                    for pool in sorted_pools:
                        print(
                            f"Бассейн {pool.pool_id} | "
                            f"Вид: {pool.fishes.species} | "
                            f"Средний вес: {pool.fishes.avg_weight:.2f} г."
                        )

                case "0":
                    print("Завершение работы симулятора.")
                    break

                case _:
                    print("Неизвестная команда. Попробуйте еще раз.")

    except KeyboardInterrupt:
        print("\n\nДосрочное завершение работы.")


if __name__ == "__main__":
    main()
