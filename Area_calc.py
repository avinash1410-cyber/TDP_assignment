def calculate_area(length, width):
    area=length * width
    if length == width:
        return f"This is a square!,with Area equal to {area} "
    else:
        return f"This is a rectangle!,with Area equal to {area} "

# Main program
if __name__ == "__main__":
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        
        result = calculate_area(length, width)
        print(result)
    except ValueError:
        print("Please enter valid numbers for length and width.")
