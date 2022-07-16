# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewSudoku.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ViewSudoku(object):
    def setupUi(self, ViewSudoku):
        if not ViewSudoku.objectName():
            ViewSudoku.setObjectName(u"ViewSudoku")
        ViewSudoku.setEnabled(True)
        ViewSudoku.resize(762, 620)
        font = QFont()
        font.setPointSize(8)
        ViewSudoku.setFont(font)
        ViewSudoku.setAcceptDrops(False)
        self.tablero = QTableWidget(ViewSudoku)
        if (self.tablero.columnCount() < 9):
            self.tablero.setColumnCount(9)
        if (self.tablero.rowCount() < 9):
            self.tablero.setRowCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(0, 1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(0, 2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(0, 3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(0, 4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(0, 5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(0, 6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(0, 7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(0, 8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(1, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(1, 4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(1, 5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(1, 6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(1, 7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(1, 8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(2, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(2, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(2, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(2, 3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(2, 4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(2, 5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(2, 6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(2, 7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(2, 8, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(3, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem28.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(3, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(3, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(3, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(3, 4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(3, 5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(3, 6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(3, 7, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem35.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(3, 8, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(4, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem37.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(4, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem38.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(4, 2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem39.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(4, 3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem40.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(4, 4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem41.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(4, 5, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem42.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(4, 6, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem43.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(4, 7, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem44.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(4, 8, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem45.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(5, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem46.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(5, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem47.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(5, 2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem48.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(5, 3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem49.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(5, 4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem50.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(5, 5, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem51.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(5, 6, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem52.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(5, 7, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem53.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(5, 8, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem54.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(6, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem55.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(6, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem56.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(6, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem57.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(6, 3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem58.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(6, 4, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem59.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(6, 5, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem60.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(6, 6, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem61.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(6, 7, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem62.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(6, 8, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem63.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(7, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem64.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(7, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem65.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(7, 2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem66.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(7, 3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem67.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(7, 4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem68.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(7, 5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem69.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(7, 6, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem70.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(7, 7, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem71.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(7, 8, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem72.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(8, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem73.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(8, 1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem74.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(8, 2, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem75.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(8, 3, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem76.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(8, 4, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem77.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(8, 5, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem78.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(8, 6, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem79.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(8, 7, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem80.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tablero.setItem(8, 8, __qtablewidgetitem80)
        self.tablero.setObjectName(u"tablero")
        self.tablero.setGeometry(QRect(30, 110, 451, 451))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(15)
        self.tablero.setFont(font1)
        self.tablero.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tablero.setMouseTracking(False)
        self.tablero.setFrameShadow(QFrame.Plain)
        self.tablero.setLineWidth(1)
        self.tablero.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablero.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablero.setRowCount(9)
        self.tablero.setColumnCount(9)
        self.tablero.horizontalHeader().setVisible(False)
        self.tablero.horizontalHeader().setMinimumSectionSize(10)
        self.tablero.horizontalHeader().setDefaultSectionSize(50)
        self.tablero.horizontalHeader().setHighlightSections(False)
        self.tablero.verticalHeader().setVisible(False)
        self.tablero.verticalHeader().setMinimumSectionSize(10)
        self.tablero.verticalHeader().setDefaultSectionSize(50)
        self.tablero.verticalHeader().setHighlightSections(False)
        self.titulo = QLabel(ViewSudoku)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(40, 20, 701, 51))
        font2 = QFont()
        font2.setFamily(u"Arial Rounded MT Bold")
        font2.setPointSize(25)
        font2.setKerning(True)
        self.titulo.setFont(font2)
        self.btnNuevo = QPushButton(ViewSudoku)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setGeometry(QRect(560, 140, 121, 61))
        font3 = QFont()
        font3.setFamily(u"Arial Rounded MT Bold")
        font3.setPointSize(15)
        self.btnNuevo.setFont(font3)
        self.btnResolver = QPushButton(ViewSudoku)
        self.btnResolver.setObjectName(u"btnResolver")
        self.btnResolver.setGeometry(QRect(560, 240, 121, 61))
        self.btnResolver.setFont(font3)
        self.lblResuelto = QLabel(ViewSudoku)
        self.lblResuelto.setObjectName(u"lblResuelto")
        self.lblResuelto.setEnabled(False)
        self.lblResuelto.setGeometry(QRect(510, 390, 231, 51))
        font4 = QFont()
        font4.setFamily(u"Arial Rounded MT Bold")
        font4.setPointSize(20)
        font4.setKerning(True)
        self.lblResuelto.setFont(font4)
        self.line = QFrame(ViewSudoku)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 250, 451, 21))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.HLine)
        self.line_2 = QFrame(ViewSudoku)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 400, 451, 21))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_3 = QFrame(ViewSudoku)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(160, 110, 41, 451))
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_4 = QFrame(ViewSudoku)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(310, 110, 41, 451))
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QFrame.VLine)

        self.retranslateUi(ViewSudoku)

        QMetaObject.connectSlotsByName(ViewSudoku)
    # setupUi

    def retranslateUi(self, ViewSudoku):
        ViewSudoku.setWindowTitle(QCoreApplication.translate("ViewSudoku", u"Sudoku", None))

        __sortingEnabled = self.tablero.isSortingEnabled()
        self.tablero.setSortingEnabled(False)
        self.tablero.setSortingEnabled(__sortingEnabled)

        self.titulo.setText(QCoreApplication.translate("ViewSudoku", u"Algoritmo Gen\u00e9tico: Resoluci\u00f3n de Sudoku ", None))
        self.btnNuevo.setText(QCoreApplication.translate("ViewSudoku", u"Nuevo", None))
        self.btnResolver.setText(QCoreApplication.translate("ViewSudoku", u"Resolver", None))
        self.lblResuelto.setText("")
    # retranslateUi

