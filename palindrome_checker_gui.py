from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout
from PySide6.QtGui import QFont, QPalette, QColor
from PySide6.QtCore import Qt

class PalindromeChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.light_theme = True
        self.init_ui()
    
    def init_ui(self):
        # Create widgets
        self.input_label = QLabel("Enter a string:")
        self.input_field = QLineEdit()
        self.check_button = QPushButton("Check")
        self.result_label = QLabel("")
        self.theme_button = QPushButton("Switch to Dark Theme")
        self.exit_button = QPushButton("Exit")
        
        # Set widget styles
        self.update_styles()
        
        # Set fonts
        font = QFont('Arial', 14)
        self.setFont(font)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.check_button)
        layout.addWidget(self.result_label)
        
        # Top button layout
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.exit_button)
        top_layout.addStretch()
        top_layout.addWidget(self.theme_button)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addLayout(layout)
        self.setLayout(main_layout)
        
        # Connect button click events
        self.check_button.clicked.connect(self.check_palindrome)
        self.theme_button.clicked.connect(self.toggle_theme)
        self.exit_button.clicked.connect(self.close)
        
        # Set window properties
        self.setWindowTitle("Palindrome Checker")
        self.setGeometry(300, 300, 350, 200)
    
    def update_styles(self):
        if self.light_theme:
            self.setStyleSheet("""
                QWidget {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                }
                QLabel {
                    font-size: 16px;
                    margin-bottom: 10px;
                    color: #333;
                }
                QLineEdit {
                    padding: 10px;
                    font-size: 14px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    background-color: #fff;
                }
                QPushButton {
                    padding: 10px;
                    font-size: 14px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                QLabel#result_label {
                    font-size: 14px;
                    margin-top: 15px;
                }
            """)
            self.theme_button.setText("Switch to Dark Theme")
        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: #333;
                    font-family: Arial, sans-serif;
                }
                QLabel {
                    font-size: 16px;
                    margin-bottom: 10px;
                    color: #f0f0f0;
                }
                QLineEdit {
                    padding: 10px;
                    font-size: 14px;
                    border: 1px solid #555;
                    border-radius: 5px;
                    background-color: #555;
                    color: #f0f0f0;
                }
                QPushButton {
                    padding: 10px;
                    font-size: 14px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                QLabel#result_label {
                    font-size: 14px;
                    margin-top: 15px;
                    color: #f0f0f0;
                }
            """)
            self.theme_button.setText("Switch to Light Theme")

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.update_styles()

    def check_palindrome(self):
        text = self.input_field.text()
        if self.is_palindrome(text):
            self.result_label.setText("✅ The input string is a palindrome.")
        else:
            self.result_label.setText("❌ The input string is not a palindrome.")
    
    def is_palindrome(self, s):
        cleaned_str = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned_str == cleaned_str[::-1]

if __name__ == "__main__":
    app = QApplication([])
    window = PalindromeChecker()
    window.show()
    app.exec()
