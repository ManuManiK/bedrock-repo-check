def greet_user(name):
    print(f"Hello {name}")

    # Bug: No validation if name is empty or None


# Intentional issues in helper.py:
# No validation on name
# Should check if name is not empty