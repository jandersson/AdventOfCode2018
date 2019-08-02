test_input = "dabAcCaCBAcCcaDA"

def catalyze(polymer: str) -> str:
    for i, char in enumerate(polymer):
        if i == len(polymer) - 1:
            return polymer
        next_char = polymer[i+1]
        if char.lower() == next_char.lower():
            if char != next_char:
                return polymer[:i] + polymer[i+2:]


def run_catalyzer(polymer):
    num_iterations = 0
    while True:
        num_iterations += 1
        original_polymer = polymer
        polymer = catalyze(original_polymer)
        if polymer == original_polymer:
            print(f"catalyzer took {num_iterations} iterations")
            return polymer


print(len(run_catalyzer(test_input)))

with open('input.txt') as infile:
    data = infile.readlines()[0]

print(len(run_catalyzer(data)))
