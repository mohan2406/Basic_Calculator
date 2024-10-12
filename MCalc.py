
from PostfixEvaluator import PostfixEvaluator



from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QKeyEvent

    

class MCalc(PostfixEvaluator, QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        PostfixEvaluator.__init__(self, [])

        self.setWindowTitle("MCalc")
        self.setWindowIcon(QIcon('./Assets/icon.png'))

        self.input_box = QLineEdit()

        font = self.input_box.font()
        font.setPointSize(font.pointSize() + 5)
        self.input_box.setFont(font)
        self.input_box.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.input_box.setFixedHeight(50)

        buttons = self.create_button()

        layout = QGridLayout()

        layout.addWidget(self.input_box, 0, 0, 1, 0)
        layout.setSpacing(2)
        layout.setRowMinimumHeight(0, 75)
        row, col = 0, 0
        for i in buttons.keys():
            if (col%5)==0:
                col = 0
                row += 1
            layout.addWidget(buttons[i], row, col)
            if i == '=':
                buttons[i].setStyleSheet("background: rgba(0, 128, 0, 0.3); color: white")
                buttons[i].pressed.connect(self.calculate)
            elif i == 'C':
                buttons[i].setStyleSheet("background: rgba(187, 0, 0, 0.3);  color: white; font-size: 15pt; font-weight: bold")
                buttons[i].pressed.connect(self.clear)
            else:
                if i.isdecimal():
                    buttons[i].setStyleSheet("font-size: 15pt; font-weight: bold; color: #404040")
                buttons[i].pressed.connect(
                        lambda val=i: self.display(val)
                        )
            buttons[i].setFixedSize(60, 60)
            col += 1

        widget = QWidget()
        widget.setLayout(layout)
        self.setFixedSize(QSize(350,380))
        self.setCentralWidget(widget)

    def display(self, v):
        self.input_box.insert(v)
        self.input_box.setFocus()

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Enter) or (event.key() == Qt.Key_Return):
            self.calculate()

    def ERROR(self, statement: str) -> None:
        self.input_box.setText(str(statement))
        self.input_box.setFocus()
        self.input_box.selectAll()
        self.error = True

    def calculate(self):
        self.set_expr(self.input_box.text())
        self.convert()
        self.set_postfix_expr(self.get_postfix_expr())
        result = self.evaluate()
        if self.error:
            self.error = False
        else:
            self.input_box.setText(str(result))
        self.input_box.setFocus()


    def clear(self):
        self.input_box.clear()
        self.input_box.setFocus()

    @staticmethod
    def create_button():
        b = dict()
        j = 1
        for i in range(1, 21):
            if i==4:
                b['('] = QPushButton('(')
            elif i==5:
                b['+'] = QPushButton('+')
            elif i==9:
                b[')'] = QPushButton(')')
            elif i==10:
                b['-'] = QPushButton('-')
            elif i==14:
                b['^'] = QPushButton('^')
            elif i==15:
                b['*'] = QPushButton('*')
            elif i==16:
                b['.'] = QPushButton('.')
            elif i==17:
                b['0'] = QPushButton('0')
            elif i==18:
                b['C'] = QPushButton('C')
            elif i==19:
                b['='] = QPushButton('=')
            elif i==20:
                b['/'] = QPushButton('/')
            else:
                b['{}'.format(j)] = QPushButton('{}'.format(j))
                j+=1
        return b

app = QApplication([])
window = MCalc()

window.show()
app.exec()
