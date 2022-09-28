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
    """
    This function returns the possibilites to make the change with the available coins.
    For each coin in available coins it checks if the total value minus the coin value is greater than or equal to zero.
    If so, the function will be called again, but the total amount will be subtracted from the value of the available coin.
    This will be done with all available currencies to actually calculate what the possible change cases are.
    :param possibilities: array of all possibilites
    :param available_coins: coins available for use passed by the question
    :param combinations: array of possibilites for each case
    :param amount: dynamic amout to calculate the availability of each currency
    :param index: index of available_coins array
    :return: break the recursion to go back
    """
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