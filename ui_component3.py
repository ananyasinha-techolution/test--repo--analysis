class Form:
    def __init__(self):
        self.fields = []
    
    def add_field(self, name, field_type):
        self.fields.append({'name': name, 'type': field_type})
    
    def render(self):
        return '<form>' + ''.join([f'<input type="{f["type"]}" name="{f["name"]}">' for f in self.fields]) + '</form>'
