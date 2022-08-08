from decoractor import timing


class FibonacciList(object):
    def __init__(self):
        self.res = []

    def create_fibonacci(self, number):
        if number == 1 or number == 2:
            return 1
        else:
            return self.create_fibonacci(number - 1) + self.create_fibonacci(number - 2)

    @timing
    def select_odd_fibonacci(self, total_number):
        if isinstance(total_number, int):
            for i in range(1, total_number):
                res = self.create_fibonacci(i)
                if res % 2 != 0:
                    self.res.append(res)
            return self.res
        else:
            return "input is not valid number"


if __name__ == '__main__':
    Fibonacci_list = FibonacciList()
    # 请输入斐波那契数列第几项
    number = 7
    res_list = Fibonacci_list.select_odd_fibonacci(number)
    print(res_list)
