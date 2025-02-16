def rttd(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1

res = rttd(122345, 500)
print(res)
for _ in res:
    print(_, "\n")