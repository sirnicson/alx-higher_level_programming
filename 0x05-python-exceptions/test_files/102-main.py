from magic_calculation import magic_calculation

def test_magic_calculation():
    # Test cases with expected output
    
    # Test case 1: when 'a' is greater than 1
    a, b = 2, 3
    result = magic_calculation(a, b)
    print(f"Test case 1: magic_calculation({a}, {b}) = {result}")
    
    # Test case 2: when 'a' is less than 1
    a, b = 1, 5
    result = magic_calculation(a, b)
    print(f"Test case 2: magic_calculation({a}, {b}) = {result}")
    
if __name__ == "__main__":
    test_magic_calculation()

