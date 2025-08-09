"""
Q:
You are given a list of strings representing tags collected from multiple articles:

tags = ["python", "ai", "ml", "python", "fastapi", "ml"]
Tasks:

Use reduce() to concatenate all tags into a single string separated by commas.
Expected output:
"python,ai,ml,python,fastapi,ml"

Use reduce() to get a set of unique tags across the list.
Expected output:
{"python", "ai", "ml", "fastapi"}

Constraints:

Use reduce() from functools

Provide the appropriate initializer (default value)

Avoid using set(tags) or "separator".join() directly



"""
from functools import reduce

tags = ["python", "ai", "ml", "python", "fastapi", "ml"]

# concatenate all tags into a single string separated by commas.
# using join

conc_tags = ','.join(tags)
print(f'Using joins: {conc_tags}')

# reduce

conc_tags_reducer = reduce(lambda acc, next: acc + ',' + next, tags, tags[0])
print(f'Using reducer: {conc_tags_reducer}')

# Use reduce() to get a set of unique tags across the list.

unique_tags = reduce(lambda acc, next:  acc.union({next}), tags, set())
print(unique_tags)
