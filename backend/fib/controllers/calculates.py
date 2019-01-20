#from settings import INPUT_CONFINES


def fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n-1) + fib(n-2)


class FibController:
    def calculate(self, data):
        start = data['from']
        to = data['to']
        result = self.run_algo(start, to)
        result = self.format_result(result)
        return result

    def run_algo(self, start, to):
        n = 0
        cur = fib(n)
        result = []
        while cur <= to:
            if cur >= start:
                result.append(cur)
            n += 1
            cur = fib(n)
        return result

    def format_result(self, result):
        compl_result = ''
        for num in result:
            compl_result += str(num) + ', '
        compl_result = compl_result[:len(compl_result) - 2]
        return compl_result
            


if __name__ == '__main__':
    data = {'from': 0, 'to': 1}
    fibber = FibController()
    result = fibber.calculate(data)
    print(result)