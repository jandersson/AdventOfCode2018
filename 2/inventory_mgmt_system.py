def count_letters(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

with open('input.txt') as infile:
    ids = [id.strip() for id in infile.readlines()]

double_counts = 0
triple_counts = 0
for id in ids:
    counts = count_letters(id)
    if 2 in counts.values():
        double_counts += 1
    if 3 in counts.values():
        triple_counts += 1
print(f"Checksum: {triple_counts * double_counts}")

similar_ids = []
diff_index = []
for id in ids:
    for second_id in ids:
        diff_count = 0
        for index, letter in enumerate(id):
            if letter != second_id[index]:
                diff_count += 1
            if diff_count > 1:
                continue
        if diff_count == 1:
            similar_ids.append(second_id)
            if id not in similar_ids:
                similar_ids.append(id)
