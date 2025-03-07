import square # need
import circle # need
import sys

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    if any(s < 0 for s in size):
        raise ValueError("Size must be non-negative")

    result = eval(f'{fig}.{func}(*{size})')
    sys.stdout.write(f'{func} of {fig} is ' f'{result}\n')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Enter the figure sizes separated by spaces, "
		"size must be non-negative, 1 for circle and square\n").split(' ')))
        if any(s < 0 for s in size):
            print("Size must be non-negative. Please try again.")
            size = []

    calc(fig, func, size)