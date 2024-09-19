# Step 1: Create Morse dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', 
    ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', 
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', 
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Step 1.1: Create Reverse Morse Code dictionary
reverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}

# Step 2: Function to convert text to Morse code
def text_to_morse(text):
    morse_output = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_output.append(morse_code_dict[char])
        else:
            morse_output.append('?')  # Handle unknown characters
    return ' '.join(morse_output)

# Step 3: Function to convert Morse code to text
def morse_to_text(morse):
    text_output = []
    morse_letters = morse.split(' ')
    
    for code in morse_letters:
        if code in reverse_morse_code_dict:
            text_output.append(reverse_morse_code_dict[code])
        else:
            text_output.append('?')  # Handle unknown Morse code symbols
    return ''.join(text_output)

# Step 4: Ask the user for input
mode = input("Type '1' for text to Morse, or '2' for Morse to text: ")

if mode == '1':
    user_input = input("Enter the text you want to convert to Morse Code: ")
    print("Morse Code:", text_to_morse(user_input))
elif mode == '2':
    morse_input = input("Enter the Morse code you want to convert to text (separate letters with spaces and words with '/'): ")
    print("Text:", morse_to_text(morse_input))
else:
    print("Invalid option.")
