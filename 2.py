def calculator(func):
    def obertka(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"Result: {result}")
        except (NameError, SyntaxError, TypeError):
            print("Invalid expression")
    return obertka

@calculator
def calculate(expression):
    return eval(expression, {}, {})
