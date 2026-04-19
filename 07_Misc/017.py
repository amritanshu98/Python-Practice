# Sort (name, age, height) tuples with priority: name > age > score. E.g. given Tom,19,80 / John,20,90 / Jony,17,91 → sorted by name first, then age, then score.



inp = [("Tom",19,80), ("John",20,90), ("Jony",17,91), ("Amit", 21, 87)]

def sort_fn(x):
    return (x[0], x[1], x[2])

result = sorted(inp, key=sort_fn)

print(result)