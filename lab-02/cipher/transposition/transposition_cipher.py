class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    def decrypt(self, text, key):
        decrypted_text = [''] * key  # Khởi tạo danh sách rỗng với số phần tử bằng key
        row, col = 0, 0              # Khởi tạo hàng và cột

        for symbol in text:
            decrypted_text[col] += symbol  # Thêm ký tự vào cột hiện tại
            col += 1

            # Khi đạt tới cuối cột, chuyển sang dòng tiếp theo
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1

        return ''.join(decrypted_text)     # Ghép các ký tự lại thành chuỗi kết quả
    # Đây là bản cập nhật hoán vị

