
def catalyze(polymer: str) -> str:
    """Naive implementation"""
    for i, char in enumerate(polymer):
        if i == len(polymer) - 1:
            return polymer
        next_char = polymer[i+1]
        if char.lower() == next_char.lower():
            if char != next_char:
                return polymer[:i] + polymer[i+2:]


def run_catalyzer(polymer: str) -> str:
    print(f"running catalyzer on {len(polymer)} unit polymer")
    num_iterations = 0
    while True:
        # TODO: catalyze polymer in one iteration
        num_iterations += 1
        original_polymer = polymer
        polymer = catalyze(original_polymer)
        if polymer == original_polymer:
            print(f"catalyzer took {num_iterations} iterations")
            print(f"catalyzed polymer is {len(polymer)} units")
            return polymer


test_input = "dabAcCaCBAcCcaDA"

with open('input.txt') as infile:
    data = infile.readlines()
    assert len(data) == 1
    data = data[0].strip()

run_catalyzer(test_input)
# Answer to problem 1
run_catalyzer(data)

unit_types = ['a', 'b', 'c', 'd']
for unit in unit_types:
    print(f"removing unit {unit} from polymer")
    run_catalyzer(test_input.replace(unit, '').replace(unit.capitalize(), ''))

# Answer to problem 2
results = {unit: 0 for unit in unit_types}
for unit in unit_types:
    print(f"removing unit {unit} from polymer")
    modified_data = data.replace(unit, '').replace(unit.capitalize(), '')
    results[unit] = len(run_catalyzer(modified_data))
min_key = min(results, key=results.get)
print(f"{min_key} -> {results[min_key]} units")
