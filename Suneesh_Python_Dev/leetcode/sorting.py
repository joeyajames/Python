list_to_sort = [
    "acbc",
    "abc",
    "eabc",
    "sun",
    "moon"
]

print(f"After using sorted() = {sorted(list_to_sort, key=lambda x: len(x))}.\nInitial List = {list_to_sort}")

list_to_sort.sort()
print(f"\nAfter using sort() = {list_to_sort}")
