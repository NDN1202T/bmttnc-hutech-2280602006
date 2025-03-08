class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # Tính số hàng và cột
        num_cols = key
        num_rows = (len(text) + num_cols - 1) // num_cols  # Số hàng
        decrypted_text = [''] * len(text)  # Mảng để lưu kết quả
        
        # Tính số ký tự trong từng cột
        pos = 0
        for col in range(num_cols):
            pointer = col
            while pointer < len(text):
                decrypted_text[pointer] = text[pos]
                pos += 1
                pointer += num_cols
        
        return ''.join(decrypted_text)
