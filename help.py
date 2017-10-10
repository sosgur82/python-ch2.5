# help 함수
# help(print)
# help 함수 doc를 불러옴
# """ 이걸로 help함수를 쓰면 나오는 내용을 설정할수있다. plus.__doc__ 도 같이 바뀜
def plus(a, b):
    """
    return the sum of parameta a,b
    :param a:
    :param b:
    :return:
    """
    return a+b


help(plus)

#plus.__doc__ = 'return the sum of parameta a,b'

print(plus.__doc__)