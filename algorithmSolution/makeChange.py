FINAL_STATE = 0


def make_change(available_coins: list[int], amount: int) -> list[list[int]]:
    possibilities = []
    combinations = [0, 0, 0, 0]
    find_possibilities(possibilities, available_coins, combinations, amount, 0)
    return possibilities


def find_possibilities(
        possibilities: list[list[int]],
        available_coins: list[int],
        combinations: list[int],
        amount: int,
        index: int
):
    if amount == FINAL_STATE:
        possibilities.append(list(combinations))
        return

    for coin_index in range(len(available_coins) - 1, index - 1, -1):
        if amount - available_coins[coin_index] >= 0:
            combinations[coin_index] += 1
            find_possibilities(
                possibilities,
                available_coins,
                combinations,
                amount - available_coins[coin_index],
                coin_index
            )
            combinations[coin_index] -= 1


if __name__ == '__main__':
    coin_array = [25, 10, 5, 1]
    amout = 12
    final_change = make_change(coin_array, amout)

    print(final_change)