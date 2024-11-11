  # PySide2
# インポート
from PySide2 import QtWidgets, QtCore  # 使うのはこれぐらい
  # やるべきこと
    self.setWindowTitle(title)  # タイトル決め
    self.setAttribute(QtCore.Qt.WA_DeleteOnClose)  # deleteLater()の自動実行
    self.setObjectName(objName(title))  # ウィジェットとしての名前付け
    # Mayaの場合widget作成は不要？
    widget = QtWidgets.QWidget()
    self.setCentralWidget(widget)
    # setParentも不要？
    self.setParent(親？, QtCore.Qt.Window)

    deleteLater()  # 処理が終わった後にオブジェクトを削除 → メモリ解消＆古いデータを呼び出さない
    


  # 機能
    アイテム.setAlignment(QtCore.Qt.AlignLeft)  # 左揃えにする
    アイテム.setMargin(5)  # 行間を設定
    # スペーサー作成
    QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    # セパレータ作成
    frame = QtWidgets.QFrame()
    frame.setFrameShape(QtWidgets.QFrame.HLine)
    frame.setFrameShadow(QtWidgets.QFrame.Sunken)
