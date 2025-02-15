# Random-Password-Generator-Python
Welcome to PyPassword Generator – a fun, simple Python project that helps you create a secure, randomized password based on your preferences!

## What Is It?

This project is a lightweight password generator that asks you how many letters, symbols, and numbers you’d like in your password. It then randomly picks characters from predefined lists, shuffles them, and delivers a unique password every time you run it.

## How It Works

1. **User Input:**  
   You start by specifying the number of letters, symbols, and numbers you want in your password.

2. **Random Selection:**  
   The script uses Python’s `random` module to choose:
   - Letters from a list of both lowercase and uppercase letters.
   - Symbols from a set of common special characters.
   - Numbers from 0 to 9.

3. **Password Assembly:**  
   Each randomly chosen character is added to a list. Once all characters have been selected, the list is shuffled to mix up the order, ensuring that your password is unpredictable.

4. **Display:**  
   Finally, the list is converted into a string and printed out as your new password.
