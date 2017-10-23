from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui_map


import os
import htmltest as html


import sys
##import psutil



class MapDlg(QDialog, ui_map.Ui_Dialog):
    def __init__(self, parent=None):
        super(MapDlg, self).__init__(parent)
        msize = '15 digit beacon UIN'
        self.setupUi(self)

        self._lat = 45.483
        self._long = -73.576
        self.currentframe = self.mapWebView.page().currentFrame()
        self.mapWebView.loadFinished.connect(self.handleLoadFinished)
        self.set_code(html.google_map)

    def set_code(self, h):
        self.mapWebView.setHtml(h)

    def handleLoadFinished(self, ok):
        if ok:
            self.get_marker_coordinates()


    def get_marker_coordinates(self):
        print self._lat,self._long
        self.currentframe.evaluateJavaScript('Marker({},{})'.format(self._lat, self._long))
        self.setWindowTitle("Latitude:  {}   Longitude:  {}".format(self._lat, self._long))




if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MapDlg()
    form.show()
    app.exec_()
