from morse_code_converter import MorseCodeConverter

converter = MorseCodeConverter()

print("Hello! Welcome to the Morse Code Converter!")

ask_again = True
while ask_again:
    ask_again2 = True
    while ask_again2:
        response = input('Would you like to "decode" ("d" for short) or "encode" ("e" for short)? ').lower()

        if response == "encode" or response == "e":
            response = input("Input a text: ")
            ask_again3 = True
            while ask_again3:
                to_real_char = input('Would you like it to return as period (".") and hash ("-")? (Y/N): ').lower()
                if to_real_char == "yes" or to_real_char == "y":
                    print(f"Here is the following code:\n{converter.string_to_code(string=response, to_real_char=True)}\n")
                    ask_again2 = False
                    ask_again3 = False
                elif to_real_char == "no" or to_real_char == "n":
                    print(f"Here is the following code:\n{converter.string_to_code(string=response)}\n")
                    ask_again2 = False
                    ask_again3 = False
                else:
                    print("Please correctly select the following response: ")

        elif response == "decode" or response == "d":
            if converter.previous:
                response = input('Input a code, input "PRE" to use the previous code: ')
            else:
                response = input('Input a code: ')
            print(f"Here is the following text:\n{converter.code_to_string(code=response)}\n")
            ask_again2 = False

        else:
            print("Please correctly select the following response: ")

    ask_again4 = True
    while ask_again4:
        response = input("Would you like to continue? (Y/N): ").lower()
        if response == "yes" or response == "y":
            ask_again4 = False
        elif response == "no" or response == "n":
            ask_again = False
            ask_again4 = False
            print("Bye! ヾ(•ω•`)o")
        else:
            print("Please correctly select the following response: ")
