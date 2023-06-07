import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QComboBox, QGridLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Popup Example")

        self.button = QPushButton("Open Popup", self)
        self.button.clicked.connect(self.open_popup)

        self.grid_layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(self.grid_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.next_row = 0

    def open_popup(self):
        dialog = PopupDialog(self)
        if dialog.exec_():
            style, function = dialog.selected_style
            self.add_button(style, function)

    def add_button(self, style, function):
        new_button = QPushButton("New Button", self)
        new_button.setStyleSheet(style)  # Set the style for the new button
        new_button.clicked.connect(function)  # Connect the button click signal to the selected function
        self.grid_layout.addWidget(new_button, self.next_row, 0)  # Add the new button to the grid layout at the next row
        self.next_row += 1

class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Popup Dialog")

        self.selected_style = None

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.option_menu = QComboBox(self)
        self.option_menu.addItem("Style 1")
        self.option_menu.addItem("Style 2")
        self.option_menu.addItem("Style 3")

        self.option_menu.setItemData(0, ("Style 1", self.open_popup_1))
        self.option_menu.setItemData(1, ("Style 2", self.open_popup_2))
        self.option_menu.setItemData(2, ("Style 3", self.open_popup_3))

        layout.addWidget(self.option_menu)

        button = QPushButton("Add Button", self)
        button.clicked.connect(self.add_button)
        layout.addWidget(button)

    def add_button(self):
        index = self.option_menu.currentIndex()
        self.selected_style = self.option_menu.itemData(index)  # Get the selected style and associated function
        self.accept()

    def open_popup_1(self):
        popup = QDialog(self)
        popup.setWindowTitle("Popup 1")
        new_button = QPushButton("New Button", popup)
        new_button.clicked.connect(self.print_sleepy)
        layout = QVBoxLayout()
        layout.addWidget(new_button)
        popup.setLayout(layout)
        popup.exec_()

    def open_popup_2(self):
        popup = QDialog(self)
        popup.setWindowTitle("Popup 2")

        button = QPushButton("Popup Button 2", popup)
        button.clicked.connect(self.print_sleepy)

        layout = QVBoxLayout()
        layout.addWidget(button)
        popup.setLayout(layout)

        popup.exec_()

    def open_popup_3(self):
        popup = QDialog(self)
        popup.setWindowTitle("Popup 3")

        button = QPushButton("Popup Button 3", popup)
        button.clicked.connect(self.print_sleepy)

        layout = QVBoxLayout()
        layout.addWidget(button)
        popup.setLayout(layout)

        popup.exec_()

    def print_sleepy(self):
        print("I'm sleepy")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())