replace = {
    'a': '@', 'b': '!@', 'c': '(', 'd': '@!', 'e': '!^', 'f': '!=',
    'g': '&', 'h': '#', 'i': '!', 'j': '?', 'k': '!~', 'l': '!_',
    'm': '/`|',
    'n': '|\\|',
    'o': '*', 'p': '|*', 'q': '*|', 'r': '|^',
    's': '$', 't': '-|', 'u': '|_|',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '><', 'y': '>|', 'z': '-/_',
}


class Encryption:
    def __init__(self):
        while True:
            print("\n1. Encrypt text")
            print("2. Decrypt text")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.encrypt_text()
            elif choice == "2":
                self.decrypt_text()
            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Try again.")

    def encrypt_text(self):
        user_input = input("Enter your text: ").lower()

        encoded = "".join(replace.get(char, char) for char in user_input)
        print("Encoded :", encoded)

    def decrypt_text(self):
        user_input = input("Enter your text: ")

        sorted_by_length = sorted(replace.items(), key=lambda item: len(item[1]), reverse=True)

        decoded = user_input
        for key, value in sorted_by_length:
            decoded = decoded.replace(value, key)

        print("Original:", decoded)

if __name__ == "__main__":
    enctext = Encryption()
