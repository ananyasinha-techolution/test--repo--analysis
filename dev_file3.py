class AdvancedCalculator:
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        result = eval(f'{a} {operation} {b}')
        self.history.append(f'{a} {operation} {b} = {result}')
        return result
