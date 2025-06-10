import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))

            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        # Check for the termination sequence '1111111111111110'
        # The character code for '11111110' (decimal 254) is used as the end marker
        # This assumes the message itself does not contain this character.
        # It's better to check for the full 16-bit sequence if possible.
        # For simplicity, based on the previous encode_image function, we'll check for 254.
        if char == '\0':
            break # Kết thúc thông điệp khi gặp dấu kết thúc
        message += char
    
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()