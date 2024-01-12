class Prime():
    def __init__(self, number):
        self._number = number

    def check_prime(self, num) -> bool:
        result = False
        if num == 2:
            result = True
        elif num > 2:
            for i in range(2, num):
                # print(f"num : i = {num} : {i}")
                if num % i == 0:
                    result = False
                    break
                result = True
        # print(f"num : result = {num} : {result} ")
        return result

    def print_prime(self):
        return [i for i in range(self._number + 1) if self.check_prime(i)]


prime = Prime(13)
print(prime.print_prime())
