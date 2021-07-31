from cipher_art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceaser_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = (position + shift_amount) % 26
            else:
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += char
    print(f"The {cipher_direction} text is {end_text}")


keep_running = True
while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser_cipher(start_text=text, shift_amount=shift % 26, cipher_direction=direction)
    result = input("Type 'yes' if want to continue. Otherwise type 'no'.\n")
    keep_running = True if result == "yes" else False

print("Have a good day !!")