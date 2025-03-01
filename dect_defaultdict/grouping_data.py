names = ["Alice", "Bob", "Amanda", "Brian"]



from collections import defaultdict

grouped_data_by_first_letter = defaultdict(list)

for name in names:
    grouped_data_by_first_letter[name[0]].append(name)
print(dict(grouped_data_by_first_letter))