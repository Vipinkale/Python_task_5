
import re
from input_module import get_user_input

def get_numeric_data(user_input):
    
    numeric_data = re.sub(r'\D', '', user_input)
    return numeric_data

def main():

    user_input = get_user_input()
    

    numeric_data = get_numeric_data(user_input)
    
    if numeric_data:
        print(f"Numeric data extracted: {numeric_data}")
    else:
        print("No numeric data found.")

if __name__ == "__main__":
    main()
