def func1(a, b):
    print a
    print b

def func2(x, y):
    print x, y

def func3(c, d):
    print c+d

def main():
    func1(2, 3)
    func2(5, 6)
    func3(d=4, c=2)

if __name__ == "__main__":
    main()
