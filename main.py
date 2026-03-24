def contribution(value):
    if value > 0:
        return 0
    return value ** 4


def sum_valid_powers(numbers, index=0):
    if index == len(numbers):
        return 0
    return contribution(numbers[index]) + sum_valid_powers(numbers, index + 1)


def solve_case(x, numbers):
    if len(numbers) != x:
        return -1
    return sum_valid_powers(numbers)


def parse_numbers(line):
    if not line:
        return []
    return list(map(int, line.split()))


def read_case():
    x = int(input().strip())
    numbers_line = input().strip()
    numbers = parse_numbers(numbers_line)
    return x, numbers


def read_and_solve_cases(remaining_cases):
    if remaining_cases == 0:
        return []

    x, numbers = read_case()
    current_result = solve_case(x, numbers)
    remaining_results = read_and_solve_cases(remaining_cases - 1)

    return [current_result] + remaining_results


def print_results(results, index=0):
    if index == len(results):
        return

    print(results[index])
    print_results(results, index + 1)


def main():
    n = int(input().strip())
    results = read_and_solve_cases(n)
    print_results(results)


if __name__ == "__main__":
    main()