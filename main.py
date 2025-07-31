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
        """Class to analyze colors"""
    
        self.color_data = [color.upper().strip() for color in color_data]
        self.color_counts = self._count_colors()
    
    def _count_colors(self):
        """Counts the frequency of each color using a dictionary"""
        counts = {}
        for color in self.color_data:
            if color in counts:
                counts[color] += 1
            else:
                counts[color] = 1
        return counts

    def _get_most_common_color(self):
        """Get the most frequent color"""
        max_count = 0
        most_common = ""
        for color, count in self.color_counts.items():
            if count > max_count:
                max_count = count
                most_common = color
        return most_common