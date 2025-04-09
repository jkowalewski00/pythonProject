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

def measure():
	return 69570

def direction():
	return 32995

def expert():
	return 8504

def style():
	return 78858

def chance():
	return 81632

def time():
	return 34046
