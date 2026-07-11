# Frozen Sets - Immutable sets
fs1 = frozenset({1,2,3,4,5,6,7})
fs2 = frozenset({10,9,8,7,6,5})
print(fs1,type(fs1),fs2,type(fs2))
print(fs1 - fs2)