class Button:
    def __init__(self, text, color='blue'):
        self.text = text
        self.color = color
    
    def render(self):
        return f'<button style="color: {self.color}">{self.text}</button>'
