import os
from helper import greet_user

def main():
    user = input("Enter your name: ")
    greet_user(user)
    
    # Bug: No error handling for environment variable
    config = os.environ["CONFIG"] 
    print("Config loaded:", config)
    
    # Bug: Unnecessary global variable
    global result
    result = 0

if __name__ == "__main__":
    main()


# Intentional issues in app.py:
# No try/except around os.environ["CONFIG"] (could raise KeyError)
# Global variable used unnecessarily
# No logging, just prints