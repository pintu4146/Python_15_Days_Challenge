


#dict is simple data strucutre which raised keyerror when specific keys are missing
# defaultdict pupulate

# frequency count

text = "apple banana apple orange banana apple"

# using dict

freq_count = {}
for word in text.split(' '):
    if word in freq_count.keys():
        freq_count[word] +=1
    else:
        freq_count[word] = 1
print(freq_count)

# using default dict

from collections import defaultdict

freq_count_using_defaultdict = defaultdict(int)
for word in text.split(' '):
    freq_count_using_defaultdict[word] +=1
print(f"using defaultdict:{dict(freq_count_using_defaultdict)}")
