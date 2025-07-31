ACTUAL_COLOR_DATA = [
    # Monday
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM',
    'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN',
    
    # Tuesday  
    'ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE',
    'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE',
    
    # Wednesday
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED',
    'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE',
    
    # Thursday
    'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM',
    'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN',
    
    # Friday
    'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED',
    'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE'
]

class ColorAnalyzer:
    """Class to analyze color data from staff dress colors"""
    
    def __init__(self, color_data):
        self.color_data = [color.upper().strip() for color in color_data]
        self.color_counts = self._count_colors()