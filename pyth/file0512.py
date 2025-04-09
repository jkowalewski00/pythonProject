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

def just():
	return 98575

def see():
	return 89325

def method():
	return 77234

def production():
	return 47106

def bank():
	return 20581
