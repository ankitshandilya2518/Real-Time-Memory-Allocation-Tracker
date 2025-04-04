'''import sys
from PyQt5.QtWidgets import QApplication
from gui import MemoryTrackerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    window = MemoryTrackerApp()  # Create the main window (GUI)
    window.show()  # Show the GUI
    sys.exit(app.exec_())  # Start the event loop
'''

from PyQt5.QtWidgets import QApplication
import sys
from gui import MemoryTrackerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoryTrackerApp()
    window.show()
    sys.exit(app.exec_())
