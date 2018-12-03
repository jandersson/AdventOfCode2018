import re
with open('input.txt') as infile:
    claims = [claim.strip() for claim in infile.readlines()]

fabric = [[0 for x in range(1001)] for y in range(1001)]
claim_re = re.compile("#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)")
for claim in claims:
    match = claim_re.match(claim)
    if match:
        claim_id = match.group(1)
        claim_pos = (int(match.group(2)), int(match.group(3)))
        claim_dims = (int(match.group(4)), int(match.group(5)))
        for x in range(claim_pos[0], claim_pos[0] + claim_dims[0]):
            for y in range(claim_pos[1], claim_pos[1] + claim_dims[1]):
                fabric[y][x] += 1

num_contested_inches = 0
for row in fabric:
    for col in row:
        if col > 1:
            num_contested_inches += 1

print(f"Number of square inches with 2 claims or more: {num_contested_inches}")
