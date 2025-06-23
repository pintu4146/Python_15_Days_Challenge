from collections import defaultdict

names = ["Alice", "Bob", "Amanda", "Brian"]

grouped_data_by_first_letter = defaultdict(list)

for name in names:
    grouped_data_by_first_letter[name[0]].append(name)
print(f'{dict(grouped_data_by_first_letter)}')
