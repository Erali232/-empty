#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGroupBox, RadioGroupBox, QPushButton

dsaaawdwadsaapp = QApplication([])
window = QWidget()
window.resize(400,400)
window.setWindowTitle('Memory Card')

ok = QPushButton('Ответить')
tt_Question = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox('Варианты ответов')
qwerty_1 = QRadioButton('???????')
qwerty_2 = QRadioButton('???????')
qwerty_3 = QRadioButton('???????')
qwerty_4 = QRadioButton('???????')

layout_an1 = QHBoxLayout()
layout_an2 = QVBoxLayout()
layout_an3 = QVBoxLayout()
layout_an2.addWidget(qwerty_1)
layout_an2.addWidget(qwerty_2)
layout_an3.addWidget(qwerty_3)
layout_an3.addWidget(qwerty_4)

layout_an1.addLayout(layout_an2)
layout_an1.addLayout(layout_an3)

RadioGroupBox.setLayout(layout_an1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

linux.show()
app.exec()