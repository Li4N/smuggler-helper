def convert_hex_to_decimal():
    hex_input = input("Enter the hexadecimal number: ")
    try:
        decimal_output = int(hex_input, 16)
        print(f"Hexadecimal '{hex_input}' in decimal is: {decimal_output}")
    except ValueError:
        print("Invalid input. Make sure to enter a valid hexadecimal number.")

def convert_decimal_to_hex():
    decimal_input = input("Enter the decimal number: ")
    try:
        hex_output = hex(int(decimal_input))
        print(f"Decimal '{decimal_input}' in hexadecimal is: {hex_output}")
    except ValueError:
        print("Invalid input. Make sure to enter a valid decimal number.")

def count_bytes_with_correct_newline(modo):
    user_text = ""
    if mode == "multiline":
        print("Enter multiline text (end with 'EOF' on a new line):")
        input_lines = []
        while True:
            line = input()
            if line == "EOF":
                break
            input_lines.append(line)
        user_text = "\r\n".join(input_lines)
    else:
        user_text = input("Enter the text as oneliner: ")
        user_text = user_text.replace("\\n", "\n")

    text_oneliner = user_text.replace("\r\n", "\\r\\n")
    total_bytes = len(user_text.encode('utf-8'))
    print(f"Text in oneliner format (showing '\\r\\n' for new lines): {text_oneliner}")
    print(f"Total bytes of the entered text: {total_bytes}")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Enter multiline text and count bytes")
        print("2. Enter text as oneliner and count bytes")
        print("3. Convert from hexadecimal to decimal")
        print("4. Convert from decimal to hexadecimal")
        print("0. Exit")
        option = input("Select an option: ")

        if option == "1":
            count_bytes_with_correct_newline("multiline")
        elif option == "2":
            count_bytes_with_correct_newline("oneliner")
        elif option == "3":
            convert_hex_to_decimal()
        elif option == "4":
            convert_decimal_to_hex()
        elif option == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose an option from the menu.")

# To use this script, make sure to run it in your local Python environment.
main_menu()
