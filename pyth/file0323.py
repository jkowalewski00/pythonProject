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

def read():
	return 57732

def year():
	return 96329

def past():
	return 7729

def resource():
	return 45735

def better():
	return 5811

def perform():
	return 48914
