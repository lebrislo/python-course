# Collection: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple

# Counter
a = "aaaaabbbbbccccccdddddd"
my_counter = Counter(a)

print(my_counter)  # Counter({'a': 5, 'b': 5, 'c': 6, 'd': 6})

print(my_counter.items())  # dict_items([('a', 5), ('b', 5), ('c', 6), ('d', 6)])

print(my_counter.keys())  # dict_keys(['a', 'b', 'c', 'd'])

print(my_counter.values())  # dict_values([5, 5, 6, 6])

print(my_counter.most_common(1))  # [('c', 6)]


# namedtuple
Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)  # Point(x=1, y=-4)


# OrderedDict
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
print(ordered_dict)  # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# defaultdict
d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d["a"])  # 1
print(d["c"])  # 0


# deque
d = deque()
d.append(1)
d.append(2)
print(d)  # deque([1, 2])

d.appendleft(3)
print(d)  # deque([3, 1, 2])

d.pop()
print(d)  # deque([3, 1])

d.extend([4, 5, 6])
print(d)  # deque([3, 1, 4, 5, 6])

d.rotate(1)
print(d)  # deque([6, 3, 1, 4, 5])
