with open('input.txt') as infile:
    freqs = [int(freq) for freq in infile.readlines()]
print(f"Final frequency: {sum(freqs)}")
current_freq = 0
memo = {current_freq: True}
first_duplicate = None
while first_duplicate is None:
    for freq in freqs:
        current_freq += freq
        if current_freq in memo:
            first_duplicate = current_freq
            break
        memo[current_freq] = True
print(f"First duplicate frequency: {first_duplicate}")
