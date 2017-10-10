# lamda 함수


def blahblah(x):
    return x**2


for i in range(10):
    print("{0}:{1}".format(i, blahblah(i)), end=' ')
else:
    print()

for i in range(10):
    print("{0}:{1}".format(i, (lambda x: x**2)(i)), end=' ')
else:
    print()

strings = ['foo', 'card', 'bar', 'abab', 'aaaa', 'abab', 'foo']
strings.sort(key=lambda x: len(x), reverse=False)
print(strings)

strings = sorted(strings, key=lambda x: strings.count(x))
#strings.sort(key=lambda x: k(x, strings), reverse=False)
print(strings)