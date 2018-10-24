def methodception(another):
    return another()


def add_two_numnbers():
    return 37 + 33


print(methodception(lambda: 35 + 35))

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(filter(lambda x: x != 3, my_list)))
