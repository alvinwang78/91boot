import sys 
import os

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
 
from ui.main import Ui_mainWindow

from docx import Document

# 遍历文件夹
def scan_path(path_name,file_list):

  for item in os.scandir(path_name):

      if item.is_dir():

        scan_path(item.path,file_list)

      elif item.is_file():

        ext = os.path.splitext(item.path)[-1]

        if (ext == '.docx' and item.name.startswith('.') == False):
          file_list.append(item.path)

#替换文件里的文字
def replace_word(file, old_word, new_word):

  doc = Document(file)

  # 执行替换函数
  for p in doc.paragraphs:  # 遍历文档段落
    for run in p.runs:  # 遍历段落的字块
      if old_word in run.text:
        run.text = run.text.replace(old_word, new_word)

  # 遍历文档的表格， 替换表格里的要替换的文字
  for table in doc.tables:
      for row in table.rows:
          for cell in row.cells:
            for p in cell.paragraphs:
              for run in p.runs:
                if old_word in run.text:
                 run.text = run.text.replace(old_word, new_word)

  # 替换页眉
  for p in doc.sections[0].header.paragraphs:
    for run in p.runs:
      print(run.text)
      if old_word in run.text:
        run.text = run.text.replace(old_word, new_word)

  # 替换页脚
  for p in doc.sections[0].footer.paragraphs:
    for run in p.runs:
      if old_word in run.text:
        run.text = run.text.replace(old_word, new_word)

  doc.save(file)

class MainWindow (QMainWindow):
  
  def __init__(self):

    super(MainWindow, self).__init__()
 
    self.ui = Ui_mainWindow()
    self.ui.setupUi(self)
    self._banding()
 
  def _banding(self):
    self.ui.choosePath.clicked.connect(self.choosePath)
    self.ui.start.clicked.connect(self.start)

  def choosePath(self):
    path_name = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹","../")
    self.ui.pathName.setText(path_name)
    
  def start(self):

    self.ui.start.setText('执行中....')
    self.ui.start.setEnabled(False)

    path_name = self.ui.pathName.text()

    old_name = self.ui.oldName.text()
    new_name = self.ui.newName.text()

    old_word = self.ui.oldWord.text()
    new_word = self.ui.newWord.text()

    if path_name == '':

      log_html = '请选择文件夹'
      self.ui.showLog.setHtml(log_html)

    else:

      log_html = '开始执行 <br>' + path_name + '<br>'
      self.ui.showLog.setHtml(log_html)

      file_list = []
      scan_path(path_name,file_list)

      for file in file_list:

        log_html = log_html + file + '<br>'
        self.ui.showLog.setHtml(log_html)

        replace_word(file,old_word,new_word)

    log_html = log_html + '执行完成'
    self.ui.showLog.setHtml(log_html)

    self.ui.start.setText('开始')
    self.ui.start.setEnabled(True)

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
 
  window = MainWindow()
  window.show()

  sys.exit(app.exec())