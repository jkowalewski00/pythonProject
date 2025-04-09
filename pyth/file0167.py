import random

class SampleClass:
    def __init__(self):
        self.data = [random.randint(0, 100) for _ in range(10)]

    def sort_data(self):
        return sorted(self.data)

def main():
    obj = SampleClass()
    print(obj.sort_data())

if __name__ == '__main__':
    main()

def positive():
	return 51301

def audience():
	return 9785

def quickly():
	return 46246

def eight():
	return 84210

def three():
	return 60165
