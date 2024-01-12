def display(set1):
    print(f"Type = {type(set1)}, id = {id(set1)} , value = {set1}")


set1 = {1, 2, 3, 4, 5, 1, 1, 1, 1, ("a",)}

display(set1)

empty_set = set(())
display(empty_set)

# set2 = set([1, 2, 3, 3, 4, 4, 4])
set2 = set((1, 2, 3, 3, 4, 4, 4))
# set2 = set("99")

display(set2)

set3 = list((x ** 2 for x in range(5) if x % 2 == 0))
display(set3)

set4 = {1, 1, 1, 2, 3, 4, frozenset(("a", "b"))}
display(set4)

set4.add(99)
display(set4)
ss = set4.update(["q", "w", "e", "r", "r"])
# set4.add(["q", "w", "e", "r"])
display(set4)
display(ss)

display(set4.pop())
set4.remove(2)
display(set4)
set4.discard(99)
display(set4)
