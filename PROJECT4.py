import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QLineEdit, QComboBox, QStackedWidget, QScrollArea 
)
from PyQt6.QtGui import QFont, QPixmap, QKeyEvent, QStyleHints
from PyQt6.QtCore import Qt

# --- Slide 1 ---
class Slide1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        title = QLabel("Geometry Space Analyser")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont('Arial', 38, QFont.Weight.Bold))
        layout.addWidget(title)
        title.setStyleSheet("color:#003366;")

        self.next_button = QPushButton("Next")
        layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.next_button.setStyleSheet("background-color: #1E90FF; color: white; font-weight: bold;")

        self.setLayout(layout)

# --- Slide 2 with scroll area ---
class Slide2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        content = QWidget()
        content_layout = QVBoxLayout()

        explanation = QLabel(
            "Imagine you have a large square. At each of its four corners, there's a smaller circle placed snugly in the corner — each one touching two edges of the square.\n\n"
            "Now, look at the space left in the center. Here's the challenge:\n\n"
            "🔹 Can we fit another circle perfectly in that space?\n"
            "🔹 Or can we fit a square instead?\n\n"
            "Based on what shape you choose to inscribe, the program will calculate how much space it takes up — i.e., the area of that shape.\n\n"
            "You will provide:\n\n"
            "- The side length of the large square\n"
            "- The radius of each of the four corner circles\n"
            "- The type of shape you want to fit in the center — either a circle or a square\n\n"
            "The system will then compute the area of the largest inscribed shape (circle or square) that fits completely in the remaining space — touching all four corner circles."
        )
        explanation.setWordWrap(True)
        explanation.setFont(QFont('Arial', 14))
        explanation.setStyleSheet("color:black;")

        content_layout.addWidget(explanation)

        btn_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.prev_button.setStyleSheet("background-color: #1E90FF; color: white; font-weight: bold;")
        self.next_button = QPushButton("Next")
        self.next_button.setStyleSheet("background-color: #1E90FF; color: white; font-weight: bold;")
        btn_layout.addWidget(self.prev_button)
        btn_layout.addWidget(self.next_button)
        content_layout.addLayout(btn_layout)

        content.setLayout(content_layout)
        scroll_area.setWidget(content)

        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

# --- Geometry Calculation Functions ---
def calculate_circle_area(side, radius):
    R = (side * math.sqrt(2) / 2) - radius * (math.sqrt(2) + 1)
    if R <= 0:
        return None
    return round(math.pi * (R ** 2), 2)

def calculate_square_area(side, radius):
    S = side - radius * (2 + math.sqrt(2))
    if S <= 0:
        return None
    return round(S ** 2, 2)

# --- Slide 3 with 2 images side-by-side added ---
class Slide3(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Image display layout
        images_layout = QHBoxLayout()
        # Replace 'image1.png' and 'image2.png' with your actual image paths
        pixmap1 = QPixmap(r"C:\Users\Deepshika Reddy\OneDrive\Dokumen\circle dia.jpg")
        pixmap2 = QPixmap(r"C:\Users\Deepshika Reddy\OneDrive\Dokumen\square dia.jpg")
        pixmap1 = pixmap1.scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)
        pixmap2 = pixmap2.scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)

        label_img1 = QLabel()
        label_img1.setPixmap(pixmap1)
        label_img1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label_img2 = QLabel()
        label_img2.setPixmap(pixmap2)
        label_img2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        images_layout.addStretch(1)
        images_layout.addWidget(label_img1)
        images_layout.addStretch(1)
        images_layout.addWidget(label_img2)
        images_layout.addStretch(1)

        main_layout.addLayout(images_layout)

        # Input form
        self.side_label = QLabel("Square side length:")
        self.side_label.setStyleSheet("color:black;")
        self.radius_label = QLabel("Corner circle radius:")
        self.radius_label.setStyleSheet("color:black;")
        self.shape_label = QLabel("Center shape:")
        self.shape_label.setStyleSheet("color:black;")

        self.side_input = QLineEdit()
        self.side_input.setStyleSheet("background-color:#D3d3d3;color:black;")
        self.radius_input = QLineEdit()
        self.radius_input.setStyleSheet("background-color:#D3d3d3;color:black;")
        self.shape_choice = QComboBox()
        self.shape_choice.addItems(["Circle", "Square"])
        self.shape_choice.setStyleSheet("background-color:#D3d3d3;color:black;")

        form_layout = QVBoxLayout()
        form_layout.addLayout(self.row(self.side_label, self.side_input))
        form_layout.addLayout(self.row(self.radius_label, self.radius_input))
        form_layout.addLayout(self.row(self.shape_label, self.shape_choice))


        main_layout.addLayout(form_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.prev_button.setStyleSheet("background-color: #1E90FF; color: white; font-weight: bold;")
        self.calc_button = QPushButton("Calculate Area")
        self.calc_button.setStyleSheet("background-color: #1E90FF; color: white; font-weight: bold;")
        btn_layout.addWidget(self.prev_button)
        btn_layout.addWidget(self.calc_button)
        main_layout.addLayout(btn_layout)

        # Result label
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 24))
        self.result_label.setWordWrap(True)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

        self.calc_button.clicked.connect(self.calculate_area)

        # For Enter-key navigation on inputs
        self.inputs = [self.side_input, self.radius_input]
        for inp in self.inputs:
            inp.returnPressed.connect(self.focus_next_input)

    def row(self, label, widget):
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(widget)
        return hbox

    def focus_next_input(self):
        sender = self.sender()
        if sender in self.inputs:
            idx = self.inputs.index(sender)
            if idx + 1 < len(self.inputs):
                self.inputs[idx + 1].setFocus()
            else:
                self.calc_button.click()

    def calculate_area(self):
        try:
            side = float(self.side_input.text())
            radius = float(self.radius_input.text())
            shape = self.shape_choice.currentText()

            if shape == "Circle":
                area = calculate_circle_area(side, radius)
            else:
                area = calculate_square_area(side, radius)

            if area is None:
                self.result_label.setText("⚠ Invalid Geometry: Circles are too large!")
                self.result_label.setStyleSheet("color: red;")


            else:
                
                self.result_label.setText(f"✅ Area of inscribed {shape.lower()}: {area} units²")
                self.result_label.setStyleSheet("color: #2ECC71;")  # Green for success

        except ValueError:
            self.result_label.setText("⚠ Please enter valid numbers for side and radius.")
            self.result_label.setStyleSheet("color: red;") 


# --- Main Window managing slides ---
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Geometry Space Analyser")
        self.setGeometry(200, 200, 600, 450)
        self.setStyleSheet("background-color: #F5FAFF;") 

        self.stack = QStackedWidget()
        self.slide1 = Slide1()
        self.slide2 = Slide2()
        self.slide3 = Slide3()

        self.stack.addWidget(self.slide1)
        self.stack.addWidget(self.slide2)
        self.stack.addWidget(self.slide3)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

        # Connect buttons for navigation
        self.slide1.next_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.slide2))

        self.slide2.prev_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.slide1))
        self.slide2.next_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.slide3))

        self.slide3.prev_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.slide2))

    def keyPressEvent(self, event: QKeyEvent):
        # Enter to navigate slides except Slide3 inputs handle enter themselves
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            current_widget = self.stack.currentWidget()
            if current_widget == self.slide3:
                event.ignore()
            else:
                current_index = self.stack.currentIndex()
                if current_index + 1 < self.stack.count():
                    self.stack.setCurrentIndex(current_index + 1)
        else:
            super().keyPressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
