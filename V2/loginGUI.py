import sys
import LoginSystem.loginCRUD as loginCRUD
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QDesktopWidget, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class LoginWindow(QDialog):
    def __init__(self, parent):
        loginCRUD.check_database_exists()
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Login-System (with GUI)")
        self.setFixedSize(650, 350)
        self.center()
        
        self.user_id = 0
        
        self.lbl_welcome = QLabel(self)
        self.lbl_pls_login = QLabel(self)
        self.lbl_username = QLabel("Username:", self)
        self.lbl_password = QLabel("Password:", self)
        self.lbl_confirm_password = QLabel("Confirm Password:", self)

        self.txtBox_username = QLineEdit(self)
        self.txtBox_password = QLineEdit(self)
        self.txtBox_confirm_password = QLineEdit(self)
        
        self.btn_exit = QPushButton("Exit",self)
        self.btn_login = QPushButton("Login", self)
        self.btn_registration = QPushButton("Registration", self)
        self.btn_register = QPushButton("Register", self)
        self.btn_clear = QPushButton("Clear", self)
        self.btn_back = QPushButton("Back", self)
        
        self.btn_back.hide()
        self.btn_register.hide()
        self.lbl_confirm_password.hide()
        self.txtBox_confirm_password.hide()

        self.initUI()
    
    def initUI(self):
        self.lbl_welcome.setText("Welcome!")
        self.lbl_welcome.setFont(QFont("Arial", 30))
        self.lbl_welcome.setGeometry(0,0, 700, 50)
        self.lbl_welcome.setStyleSheet( "font-weight: bold;"
                                        "color: blue;")
        self.lbl_welcome.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        
        self.lbl_pls_login.setText("Please log in.")
        self.lbl_pls_login.setFont(QFont("Arial", 20))
        self.lbl_pls_login.setGeometry(0, 40, 700, 75)
        self.lbl_pls_login.setStyleSheet(   "font-style: italic;"
                                            "color: blue;")
        self.lbl_pls_login.setAlignment(Qt.AlignCenter)
        
        
        self.lbl_username.setFont(QFont("Arial", 18))
        self.lbl_username.setGeometry(80, 130, 150, 70)
        self.lbl_username.setAlignment(Qt.AlignRight)
        self.lbl_username.setStyleSheet("color: blue")
        
        self.txtBox_username.setGeometry(250, 125, 300, 35)
        self.txtBox_username.setFont(QFont("Arial", 16))
        
        self.lbl_password.setFont(QFont("Arial", 18))
        self.lbl_password.setGeometry(80, 170, 150, 70)
        self.lbl_password.setAlignment(Qt.AlignRight)
        self.lbl_password.setStyleSheet("color: blue")
        
        self.txtBox_password.setGeometry(250, 165, 300, 35)
        self.txtBox_password.setFont(QFont("Arial", 16))
        
        
        self.btn_exit.setGeometry(575, 300, 50, 30)
        self.btn_exit.setFont(QFont("Arial", 12))
        self.btn_exit.setStyleSheet("font-weight: bold;"
                                    "color: red;")
        self.btn_exit.clicked.connect(self.exit_application)
        
        self.btn_login.setGeometry(490, 205, 60, 35)
        self.btn_login.setFont(QFont("Arial", 14))
        self.btn_login.setStyleSheet("color: blue;")
        self.btn_login.clicked.connect(self.check_login)
        
        self.btn_registration.setGeometry(25, 300, 115, 35)
        self.btn_registration.setFont(QFont("Arial", 12))
        self.btn_registration.setStyleSheet("font-weight: bold;"
                                            "color: red;")
        self.btn_registration.clicked.connect(self.registration)
        
        self.btn_clear.setGeometry(250, 205, 60, 35)
        self.btn_clear.setFont(QFont("Arial", 14))
        self.btn_clear.setStyleSheet("color: blue;")
        self.btn_clear.clicked.connect(self.clear_input)
    
    def center(self):
        # Bildschirmgröße ermitteln
        qr = self.frameGeometry()  # Erhalten Sie die Geometrie des Fensters
        cp = QDesktopWidget().availableGeometry().center()  # Erhalten Sie die Bildschirmmitte
        qr.moveCenter(cp)  # Bewege die Fenstergeometrie zur Bildschirmmitte
        self.move(qr.topLeft())  # Setzen Sie die Fensterposition auf die obere linke Ecke der Geometrie
    
    def exit_application(self):
        dlg = ConfirmDialog("Exit?", "Exit the application?")
        if dlg.exec():
            sys.exit()

    def clear_input(self):
        self.txtBox_username.clear()
        self.txtBox_password.clear()
        self.txtBox_confirm_password.clear()
       
    def back_login(self):
        self.btn_back.hide()
        self.btn_register.hide()
        self.lbl_confirm_password.hide()
        self.txtBox_confirm_password.hide()
        self.btn_login.show()
        self.btn_registration.show()
        
        self.initUI()
     
    def registration(self):
        self.btn_login.hide()
        self.btn_registration.hide()
        self.btn_back.show()
        self.btn_register.show()
        self.lbl_confirm_password.show()
        self.txtBox_confirm_password.show()
        
        self.lbl_welcome.setText("Registration")
        self.lbl_pls_login.setText("Please create a new account!")
        
        self.lbl_username.setGeometry(80, 130, 150, 70)
        self.txtBox_username.setGeometry(250, 125, 300, 35)
        self.lbl_password.setGeometry(80, 170, 150, 70)
        self.txtBox_password.setGeometry(250, 165, 300, 35)
        self.btn_clear.setGeometry(250, 245, 60, 35)
        
        self.btn_back.setGeometry(25, 300, 50, 30)
        self.btn_back.setFont(QFont("Arial", 12))
        self.btn_back.setStyleSheet("font-weight: bold;"
                                    "color: red;")
        self.btn_back.clicked.connect(self.back_login)
        
        
        self.btn_register.setGeometry(465, 245, 85, 35)
        self.btn_register.setFont(QFont("Arial", 14))
        self.btn_register.setStyleSheet("color: blue;")
        self.btn_register.clicked.connect(self.register)
        
        self.lbl_confirm_password.setGeometry(20, 210, 210, 70)
        self.lbl_confirm_password.setFont(QFont("Arial", 18))
        self.lbl_confirm_password.setStyleSheet("color: blue;")
        self.lbl_confirm_password.setAlignment(Qt.AlignRight)
        
        self.txtBox_confirm_password.setGeometry(250, 205, 300, 35)
        self.txtBox_confirm_password.setFont(QFont("Arial", 16))
        
    def register(self):
        username: str = self.txtBox_username.text()
        password: str = self.txtBox_password.text()
        password_confirm: str = self.txtBox_confirm_password.text()
        
        if password == password_confirm:
            dlg = ConfirmDialog("Register?", "Confirm the registration?")
            
            if dlg.exec():  # Create new Account
                loginCRUD.create_account(username, password)
                dlg2 = ConfirmDialog("Success", "Account successfully created!")
                
                if dlg2.exec(): # Return to Login-Screen
                    self.clear_input()
                    self.back_login()
                    self.txtBox_username.setFocus()
                    
        else:
            dlg = OkDialog("Error", "Passwords don't match!")
            if dlg.exec():
                self.clear_input
                self.txtBox_username.setFocus()
        
    def check_login(self):
        username: str = self.txtBox_username.text()
        password: str = self.txtBox_password.text()
        login_confirmed, self.user_id = loginCRUD.compare_login(username, password)
        
        if login_confirmed:
            #dlg = OkDialog("Success!", f"Welcome {username}!")
            #if dlg.exec():
                self.parent.user_id = self.user_id
                self.parent.username = username
                #self.parent.show()
                #print(self.parent.user_id)
                self.close()
            
        else:
            dlg = OkDialog("Error", "Wrong credentials!")
            if dlg.exec():
                self.clear_input()
                self.txtBox_username.setFocus()


class ConfirmDialog(QDialog):
    def __init__(self, title: str, message: str):
        super().__init__()
        self.setWindowTitle(title)
        
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        mssg = QLabel(message)
        mssg.setFont(QFont("Arial", 10))
        mssg.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(mssg)
        layout.addWidget(self.buttonBox)
        
        self.setLayout(layout)

class OkDialog(QDialog):
    def __init__(self, title: str, message: str):
        super().__init__()
        self.setWindowTitle(title)
        
        button = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(button)
        self.buttonBox.accepted.connect(self.accept)
        
        mssg = QLabel(message)
        mssg.setFont(QFont("Arial", 10))
        mssg.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(mssg)
        layout.addWidget(self.buttonBox)
        
        self.setLayout(layout)

def login():
    if loginCRUD.check_database_exists():
        app = QApplication(sys.argv)
        window = LoginWindow()
        window.show()
        sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    login()