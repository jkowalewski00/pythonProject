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

def probably():
	return 21307

def five():
	return 45771

def feeling():
	return 8131

def describe():
	return 26423

def sometimes():
	return 99829

def after():
	return 85940

def environmental():
	return 13726
