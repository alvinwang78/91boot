import sys 
import os

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
 
from ui.main import Ui_mainWindow

from docx import Document



class MainWindow (QMainWindow):
  
  def __init__(self):

    super(MainWindow, self).__init__()
 
    self.ui = Ui_mainWindow()
    self.ui.setupUi(self)
    self._banding()
 
  def _banding(self):
    self.ui.chooseFolder.clicked.connect(self.chooseFolder)
    self.ui.start.clicked.connect(self.start)

  def chooseFolder(self):
    folder_name = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹","../")
    self.ui.folderName.setText(folder_name)
    
  def start(self):

    self.ui.start.setText('执行中....')
    self.ui.start.setEnabled(False)

    oldName = self.ui.oldName.text()
    newName = self.ui.newName.text()

    old_word = self.ui.oldWord.text()
    new_word = self.ui.newWord.text()

    if folder_name is None:

      log_html = '请选择文件夹'
      self.ui.showLog.setHtml(log_html)

    else:

      log_html = '开始执行 <br>'
      self.ui.showLog.setHtml(log_html)

      for root, dirs, files in os.walk(folder_name):
        for file in files:

          file_name = os.path.join(root, file)
          ext = os.path.splitext(file_name)[-1]
          
          if (ext == '.docx'):

            log_html = log_html + '文件夹 ' + folder_name + '<br>'
            self.ui.showLog.setHtml(log_html)

            doc = Document(file_name)

            # 执行替换函数
            for paragraph in doc.paragraphs:  # 遍历文档段落
              for run in paragraph.runs:  # 遍历段落的字块
                print(run.text)
                run.text = run.text.replace(old_word, new_word)  # 替换字块的文字，然后赋值给字块

            # 遍历文档的表格， 替换表格里的要替换的文字
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        cell.text = cell.text.replace(old_word, new_word)

            doc.save(file_name)

      log_html = log_html + '执行完成'
      self.ui.showLog.setHtml(log_html)

    self.ui.start.setText('开始')
    self.ui.start.setEnabled(True)

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
 
  window = MainWindow()
  window.show()

  sys.exit(app.exec())