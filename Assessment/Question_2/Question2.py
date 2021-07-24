# input values here

old_account_names = ["Arbitrage", "Quant", "Discretionary"]  # input old account names here
capital = [1000, 500, 600]  # input total capital of each account in USD ($)
new_account_names = ["Arbitrage", "Quant", "Discretionary", "SEC Fines"]  # input new account names here
new_allocations = [0.3, 0.5, 0.1, 0.1]  # enter new allocations here for new accounts
old_allocations = [0.476190, 0.238095, 0.285714]
leftover = []
total_capital = sum(new_allocations)

for i in range(len(old_allocations)):
    leftover.append(old_allocations[i] - new_allocations[i])


def is_leftover_available():
    return leftover


def get_leftover_available():
    return leftover * -1  # Returns leftover available


def is_leftover_required():
    return leftover < 0  # Returns True if leftover is required (negative value)


def get_leftover_required():
    return leftover  # Returns leftover required


def leftover_allocation(leftover_available, leftover_required):  # takes in available fraction & required fraction
    if leftover_available < leftover_required:
        return leftover_available
    elif leftover_available >= leftover_required:
        return leftover_required


def allocation_distribution(capital_allocators):
    allocation_distribution = []  # empty list to store solution
    for account in capital_allocators:
        if is_leftover_available() and account.get_leftover_required():
            excess_allocatable = leftover_allocation(get_leftover_available(),
                                                     account.get_leftover_required())
            subtract_allocation(excess_allocatable)
            account.add_allocation(excess_allocatable)
            allocation_distribution.append(excess_allocatable)

    return allocation_distribution


def calculate_allocation_shifts(capital_allocations, total_capital):
    output_allocations = []
    for capital_allocator in capital_allocations:
        output_allocations.append(
            capital_allocator.shift_allocations(capital_allocations))
    final_output = [
        "Send {} to {} from {}".format(
            round(allocation_shift["excess_shiftable"] * total_capital, 2),
            allocation_shift["from"], allocation_shift["to"])
        for allocation_shift in output_allocations
    ]
    return final_output


print(calculate_allocation_shifts(new_allocations, total_capital))
