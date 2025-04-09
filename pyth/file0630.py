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

def support():
	return 65489

def level():
	return 82433

def argue():
	return 7980

def minute():
	return 32645

def usually():
	return 92390
