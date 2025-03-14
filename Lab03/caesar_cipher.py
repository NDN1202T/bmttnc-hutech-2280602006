import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_Caesar
import requests

print("Starting imports...")  # Kiểm tra import

class MyApp(QMainWindow):
    def __init__(self):
        print("Initializing MyApp...")
        super().__init__()
        self.ui = Ui_Caesar()
        print("Setting up UI...")
        self.ui.setupUi(self)
        print("Connecting buttons...")
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        print("Initialization complete.")

    def call_api_encrypt(self):
        print("Encrypt button clicked.")
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_message"])
                self.show_message("Success", "Encrypted Successfully", QMessageBox.Information)
            else:
                error_msg = response.json().get("error", "Unknown error")
                self.show_message("Error", f"Encryption failed: {error_msg}", QMessageBox.Warning)
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"API request failed: {str(e)}", QMessageBox.Critical)

    def call_api_decrypt(self):
        print("Decrypt button clicked.")
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_message"])
                self.show_message("Success", "Decrypted Successfully", QMessageBox.Information)
            else:
                error_msg = response.json().get("error", "Unknown error")
                self.show_message("Error", f"Decryption failed: {error_msg}", QMessageBox.Warning)
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"API request failed: {str(e)}", QMessageBox.Critical)

    def show_message(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.exec_()

if __name__ == "__main__":
    print("Starting application...")
    app = QApplication(sys.argv)
    print("Creating window...")
    window = MyApp()
    print("Showing window...")
    window.show()
    print("Running app.exec_...")
    sys.exit(app.exec_())