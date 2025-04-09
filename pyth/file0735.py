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

def TV():
	return 45432

def bit():
	return 82918

def yes():
	return 62105

def always():
	return 93260

def soon():
	return 79299

def development():
	return 98381
