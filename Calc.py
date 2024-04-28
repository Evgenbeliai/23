#test  гита 28.04/2024
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLineEdit,QHBoxLayout,QVBoxLayout)

app = QApplication([])

'''Интерфейс приложения'''
#параметры окна приложения
calc_win = QWidget()
calc_win.setWindowTitle('Калькулятор')
calc_win.resize(200, 50)
        
#Подключение виджетов
formyla = QLineEdit('')

button_0 = QPushButton("0")
button_1 = QPushButton("1")
button_2 = QPushButton("2")
button_3 = QPushButton("3")
button_4 = QPushButton("4")
button_5 = QPushButton("5")
button_6 = QPushButton("6")
button_7 = QPushButton("7")
button_8 = QPushButton("8")
button_9 = QPushButton("9")

button_plus = QPushButton("+")
button_minus = QPushButton("-")
button_mul = QPushButton("*")
button_div = QPushButton("/")
button_tochka= QPushButton(".")
button_ravno = QPushButton("=")

verh_1 = QHBoxLayout()
verh_1.addWidget(button_7)
verh_1.addWidget(button_8)
verh_1.addWidget(button_9)
verh_1.addWidget(button_plus)

verh_2 = QHBoxLayout()
verh_2.addWidget(button_6)
verh_2.addWidget(button_5)
verh_2.addWidget(button_4)
verh_2.addWidget(button_minus)

verh_3 = QHBoxLayout()
verh_3.addWidget(button_3)
verh_3.addWidget(button_2)
verh_3.addWidget(button_1)
verh_3.addWidget(button_mul)

verh_4 = QHBoxLayout()
verh_4.addWidget(button_0)
verh_4.addWidget(button_tochka)
verh_4.addWidget(button_ravno )
verh_4.addWidget(button_div)



main = QVBoxLayout()
main.addWidget(formyla)

main.addLayout(verh_1)
main.addLayout(verh_2)
main.addLayout(verh_3)
main.addLayout(verh_4)
main.addStretch(4)

calc_win.setLayout(main)

'''Функции приложения'''
formyls = []
def add_button():
    formyls.append("+")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)
    
    
def ravno_button():
    formyls_str = "".join(formyls)    
    try:
        result = eval(formyls_str) 
  

        formyla.setText (str(result))
    except:
        formyla.setText(" ")
        formyla.setText("Ошибка")    
    
    
    
    
    
    
    
    
def minus_button():
    formyls.append("3.14")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)
    
def div_button():
    formyls.append("/")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)

def mul_button():
    formyls.append("*")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)
    
def tochka_button():
    formyls.append(".")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)
    

        

def button_9_():
    formyls.append("9")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)

def button_8_():
    formyls.append("8")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)

def button_7_():
    formyls.append("7")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)
    
def button_6_():
    formyls.append("6")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)
    
def button_5_():
    formyls.append("5")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)

def button_4_():
    formyls.append("4")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)

def button_3_():
    formyls.append("3")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)

def button_2_():
    formyls.append("2")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)

def button_1_():
    formyls.append("1")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)

def button_0_():
    formyls.append("0")
    formyls_str = "".join(formyls)  
    formyla.setText (formyls_str)



button_plus.clicked.connect(add_button)
button_minus.clicked.connect(minus_button)
button_mul.clicked.connect(mul_button)
button_div.clicked.connect(div_button)
button_tochka.clicked.connect(tochka_button)
button_ravno.clicked.connect(ravno_button)

button_0.clicked.connect(button_0_)
button_1.clicked.connect(button_1_)
button_2.clicked.connect(button_2_) 
button_3.clicked.connect(button_3_) 
button_4.clicked.connect(button_4_) 
button_5.clicked.connect(button_5_) 
button_6.clicked.connect(button_6_)
button_7.clicked.connect(button_7_)
button_8.clicked.connect(button_8_) 
button_9.clicked.connect(button_9_) 



calc_win.show()
app.exec()




