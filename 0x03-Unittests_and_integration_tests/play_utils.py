#!/usr/bin/env python3

access_nested_map = __import__("utils").access_nested_map

#Play 1;
nested_map = {"a": {"b": {"c": 1}}}
play1 = access_nested_map(nested_map, ["a", "b", "c"])
print(play1)
print("\n")

#Play 2;
play2 = access_nested_map(nested_map, ["a", "b"])
print(play2)
print("\n")

#Play 3;
play3 = access_nested_map(nested_map, ["a", "c"])
print(play3)
print("\n")
