heros=['spider man','thor','hulk','iron man','captain america']

print("1.",len(heros))
heros.append('black panther')
print("2.",heros)

heros.remove("black panther")
heros.insert(3,"black panther")

print("3.",heros)

heros[1:2]=['doctor strange']

print("4.",heros)

heros.sort()

print("5.",heros)