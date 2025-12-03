# UI Theme configuration
THEME = {
    'primary_color': '#3498db',
    'secondary_color': '#2ecc71',
    'font_family': 'Arial, sans-serif',
    'border_radius': '8px'
}

def apply_theme(component):
    component.theme = THEME
