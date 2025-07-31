import statistics
import psycopg2


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

    def get_mean_color(self):
        """
        Since colors are categorical type of data, the mode (most frequent) is returned as the mean.
        """
        return self._get_most_common_color()
    
    def get_most_worn_color(self):
        """
        Returns the color that is mostly worn throughout the week?
        """
        return self._get_most_common_color()
    
    def get_median_color(self):
        """
        Returns the median color after sorting the colors alphabetically
        """
        sorted_colors = sorted(self.color_data)
        n = len(sorted_colors)
        median_index = n // 2
        return sorted_colors[median_index]

    def get_color_variance(self):
        """
        calculate the variance based on frequency distribution.
        """
        frequencies = list(self.color_counts.values())
        return statistics.variance(frequencies)
    
    def get_red_probability(self):
        """
        Probability that a randomly chosen color is red
        """
        red_count = self.color_counts.get('RED', 0)
        total_count = len(self.color_data)
        return red_count / total_count
    
    def save_to_postgresql(self, connection_params):
        """
        Saves the colours and their frequencies(color_counts) in postgresql database
        """
        try:
            # Connect to PostgreSQL
            conn = psycopg2.connect(**connection_params)
            cur = conn.cursor()

            # Create table if it doesn't exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS color_frequencies (
                id SERIAL PRIMARY KEY,
                color VARCHAR(10) NOT NULL,
                frequency INTEGER NOT NULL
            );
            """
            cur.execute(create_table_query)

            # Clear existing data
            cur.execute("DELETE FROM color_frequencies;")