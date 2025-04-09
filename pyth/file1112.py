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

def amount():
	return 13612

def size():
	return 38138

def discussion():
	return 36814

def difference():
	return 74927
