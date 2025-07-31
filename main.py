import statistics
import psycopg2
import random


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

            # Insert color frequencies
            for color, frequency in self.color_counts.items():
                insert_query = """
                INSERT INTO color_frequencies (color, frequency) 
                VALUES (%s, %s);
                """
                cur.execute(insert_query, (color, frequency))
            
            conn.commit()
            cur.close()
            conn.close()
            
            print("Color frequencies saved successfully to postgres database")
            return True

        except Exception as e:
            print("Error occured while saving to postgres: " + str(e))
            return False


def recursive_search(arr, target, start=0, end=None):
    """
    Recursive search algorithm to search for the given number in a list
    Returns the index of the target number, or -1 if not found.
    """
    if end is None:
        end = len(arr) - 1

    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_search(arr, target, start, mid - 1)
    else:
        return recursive_search(arr, target, mid + 1, end)


def generate_random_binary_and_convert():
    """
    Generates random 4 digits number of 0s and 1s and convert to base 10
    """
    # Generate random 4-digit binary in digits and strings
    binary_digits = [random.choice(['0', '1']) for _ in range(4)]
    binary_string = ''.join(binary_digits)

    # Convert to base 10
    decimal_value = int(binary_string, 2)

    return binary_string, decimal_value

def fibonacci_sum(n):
    """
    Returns the sum of the first 50 fibonacci sequence
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    fib_sum = 1 # Sum of first two fibonacci numbers (0 + 1)
    prev1, prev2 = 0, 1

    for i in range(3, n + 1):
        current = prev1 + prev2
        fib_sum += current
        prev1, prev2 = prev2, current

    return fib_sum
    
def main():
    """Main function to run all tests"""
    print("BINCOM ICT SOLUTIONS - PYTHON TECHNICAL INTERVIEW TEST")
    # Initialize color analyzer with actual HTML data
    analyzer = ColorAnalyzer(ACTUAL_COLOR_DATA)
    # Question 1
    print(f"1. Mean color (mode): {analyzer.get_mean_color()}")
    
    # Question 2  
    print(f"2. Most worn color: {analyzer.get_most_worn_color()}")
    
    # Question 3
    print(f"3. Median color: {analyzer.get_median_color()}")
    
    # Question 4 (BONUS)
    print(f"4. Variance of colors: {analyzer.get_color_variance():.2f}")
    
    # Question 5 (BONUS)
    red_prob = analyzer.get_red_probability()
    print(f"5. Probability of red color: {red_prob:.4f}")

    # Question 6 - PostgreSQL 
    print(f"6. PostgreSQL save:")
    
    # Update these with your actual PostgreSQL connection details
    db_params = {
    'host': 'localhost',
    'database': 'bincom_test',  
    'user': 'postgres',
    'password': 'your_new_password'
}
    
    success = analyzer.save_to_postgresql(db_params)
    if success:
        print("Data successfully saved to PostgreSQL!")
    else:
        print("Failed to save to PostgreSQL")

    # Question 7 (BONUS) - Recursive search
    print(f"\n7. RECURSIVE SEARCH DEMONSTRATION:")
    test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"   Searching in sorted list: {test_list}")
    
    while True:
        try:
            search_num = input("   Enter a number to search for (or 'skip' to continue): ")
            if search_num.lower() == 'skip':
                break
            search_num = int(search_num)
            result = recursive_search(test_list, search_num)
            if result != -1:
                print(f"   ✓ Number {search_num} found at index {result}")
            else:
                print(f"   ✗ Number {search_num} not found in the list")
            break
        except ValueError:
            print("   Please enter a valid number or 'skip'")
        except KeyboardInterrupt:
            break

    # Question 8 - Random binary to decimal
    print(f"\n8. RANDOM BINARY TO DECIMAL:")
    for i in range(5):  # Generate 5 examples
        binary, decimal = generate_random_binary_and_convert()
        print(f"   Binary: {binary} → Decimal: {decimal}")
    
    # Question 9 - Fibonacci sum
    print(f"\n9. SUM OF FIRST 50 FIBONACCI NUMBERS:")
    fib_sum = fibonacci_sum(50)
    print(f"   Sum = {fib_sum:,}")

if __name__ == "__main__":
    main()