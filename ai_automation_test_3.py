# test_python_bug.py

def add_numbers(a, b):
    return a + b

def main():
    # BUG: undefined variable `y`
    x = 10
    result = add_numbers(x, y)
    print("Result:", result)

if __name__ == "__main__":
    main()
