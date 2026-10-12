"""DiEditor - lightweight CapCut-style video editor. Run:  python main.py"""
import sys

from PyQt6.QtWidgets import QApplication

from ui import theme
from ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("DiVideoEditor")
    theme.apply_theme(app, dark=True)
    win = MainWindow()
    win.resize(1500, 900)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
