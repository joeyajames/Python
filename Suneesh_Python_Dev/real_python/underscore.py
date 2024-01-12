class ABC:
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3

    def get_a(self):
        return self.a

    def _get_b(self):
        return self._b

    def __get_c(self):
        return self.__c


obj = ABC()
for ele in list(dir(obj)):
    print(ele)

print("-" * 10)
print(obj.get_a())
print(obj._get_b())
print(obj._ABC__get_c())

print(obj.a)
print(obj._b)
# print(obj.__c)
print(obj._ABC__c)
