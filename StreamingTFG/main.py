import sys, gi, threading
from aplicacion import StreamingTFG
from PySide2.QtWidgets import QApplication

gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')

from gi.repository import Gst, GstVideo, GLib

app = QApplication([])
window = StreamingTFG(app)
window.show()
loop = GLib.MainLoop()
threading.Thread(target=loop.run)
res = app.exec_()
loop.quit()
sys.exit(res)
