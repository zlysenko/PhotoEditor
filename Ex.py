import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Діалог відкриття файлів (і папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
 
from PyQt5.QtCore import Qt # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap # оптимізована для показу на екрані картинка
 
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

app = QApplication([])
win = QWidget() 
win.setStyleSheet('''
        background-color: #2E3440;
        color: #D8DEE9;
        font-family: 'Segoe UI', sans-serif;
        font-size: 14px;''')      

win.resize(1000, 700) 
win.setWindowTitle('Easy Editor')

lb_image = QLabel("Картинка")
lb_image.setStyleSheet('''
        border: 2px dashed #4C566A;
        min-height: 300px;
        border-radius: 10px;
        background-color: #3B4252;
        qproperty-alignment: 'AlignCenter';''')

btn_dir = QPushButton("Папка")
btn_dir.setStyleSheet('''
                      
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
        
    }
    QPushButton:pressed {
        background-color: #212121;
    }''')

lw_files = QListWidget()



btn_left = QPushButton("Вліво")
btn_left.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
        
    }
    QPushButton:pressed {
        background-color: #212121;
    }
''')

btn_right = QPushButton("Вправо")
btn_right.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color: #212121;
    }
''')

btn_flip = QPushButton("Дзеркало")
btn_flip.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')

btn_sharp = QPushButton("Різкість")
btn_sharp.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')

btn_bw = QPushButton("Ч/Б")
btn_bw.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color: #212121;
    }
''')

btn_cl = QPushButton("Насиченість")
btn_cl.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color: #212121;
    }
''')

btn_bl = QPushButton("Розмити")
btn_bl.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')

btn_inv = QPushButton("Інверсія")
btn_inv.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color: #212121;
    }
''')

btn_save = QPushButton("Зберегти")
btn_save.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color: #212121;
    }
''')

btn_back = QPushButton("Назад")
btn_back.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')

btn_reset = QPushButton("Оригінал")
btn_reset.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')

btn_comiks = QPushButton("Комікс")
btn_comiks.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')

btn_export = QPushButton("Експортувати")
btn_export.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')

btn_contour = QPushButton("Контур")
btn_contour.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')

btn_glass = QPushButton("Скло")
btn_glass.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')

btn_pixel = QPushButton("Піксель")
btn_pixel.setStyleSheet('''
    QPushButton {
        background-color: #5E81AC;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #e3008c;
    }
    QPushButton:pressed {
        background-color:  #212121;
    }
''')



row = QHBoxLayout()     # Основний рядок
row2 = QHBoxLayout()
col1 = QVBoxLayout()         # ділиться на два стовпці
col2 = QVBoxLayout()
col3 = QVBoxLayout()
col1.addWidget(btn_dir)      # у першому – кнопка вибору директорії
col1.addWidget(lw_files)     # та список файлів
col2.addWidget(lb_image, 95)  # у другому - картинка
row_tools1 = QHBoxLayout()    # та рядок кнопок
row_tools2 = QHBoxLayout()
row_tools3 = QVBoxLayout()


row_tools1.addWidget(btn_left)
row_tools1.addWidget(btn_right)
row_tools1.addWidget(btn_flip)
row_tools1.addWidget(btn_sharp)
row_tools1.addWidget(btn_bw)
row_tools1.addWidget(btn_cl)
col2.addLayout(row_tools1)


row_tools2.addWidget(btn_bl)
row_tools2.addWidget(btn_inv)
row_tools2.addWidget(btn_comiks)
row_tools2.addWidget(btn_contour)
row_tools2.addWidget(btn_glass)
row_tools2.addWidget(btn_pixel)
col2.addLayout(row_tools2)

row_tools3.addWidget(btn_save)
row_tools3.addWidget(btn_back)
row_tools3.addWidget(btn_reset)
row_tools3.addWidget(btn_export)
col3.addLayout(row_tools3)
 
row.addLayout(col1, 20)
row.addLayout(col2, 80)
row.addLayout(col3, 0)

win.setLayout(row)


win.show()
 
workdir = ''
 
def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result
 
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
   extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
 
   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)
 
btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
   def __init__(self):
      self.image  = None
      self.filename = None
      self.dir = None
      self.save_dir = 'redactor_photo/'
      self.history = []
      self.original = None


   def loadImage(self, dir, filename):
      self.dir = dir
      self.filename = filename
      image_path = os.path.join(dir, filename)
      self.image = Image.open(image_path)
      
      self.original = self.image.copy()
      self.history = []


 
   def showImage(self, path):
      lb_image.hide()
      pixmapimage = QPixmap(path)
      w, h = lb_image.width(), lb_image.height()
      pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
      lb_image.setPixmap(pixmapimage)
      lb_image.show()

   def add_to_history(self):
      if self.image:
         self.history.append(self.image.copy())

   def do_bw(self):
      if self.image:
         self.add_to_history()
         self.image = self.image.convert("L")
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)

   def do_colorful(self, factor=1.5):
        ''' Підвищити насиченість кольорів '''
        if self.image:
         self.add_to_history()
         enhancer = ImageEnhance.Color(self.image)
         self.image = enhancer.enhance(factor)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)

   def do_blur(self):
        ''' Застосувати розмиття '''
        if self.image:
         self.add_to_history()
         self.image = self.image.filter(ImageFilter.BLUR)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)

   def do_posterize(self):
        if self.image:
            self.add_to_history()
            self.image = ImageOps.posterize(self.image.convert("RGB"), bits=4)
            self.saveImage()
            self.showImage(os.path.join(self.dir, self.save_dir, self.filename))

   def do_invert(self):
        ''' Інверсія кольорів '''
        if self.image:
         self.add_to_history()
         if self.image.mode != 'RGB':
            self.image = self.image.convert('RGB')
         self.image = ImageOps.invert(self.image)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)

   def do_left(self):
       if self.image:
         self.add_to_history()
         self.image = self.image.transpose(Image.ROTATE_90)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)

   def do_right(self):
       if self.image:
         self.add_to_history()
         self.image = self.image.transpose(Image.ROTATE_270)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)

   def do_flip(self):
       if self.image:
         self.add_to_history()
         self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)

   def do_sharpen(self):
        if self.image:
         self.add_to_history()
         self.image = self.image.filter(ImageFilter.SHARPEN)
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)      
       
   def back(self):
      if self.history:
         self.image = self.history.pop()
         self.saveImage()
         image_path = os.path.join(self.dir, self.save_dir, self.filename)
         self.showImage(image_path)
 
   def saveImage(self):
        ''' зберігає копію файлу у підпапці '''
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

   def clear_history(self):
    if self.original:
        self.image = self.original.copy()
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
        self.history = []  # очищаємо історію

   def exportImage(self):
        if self.image:
            filepath, _ = QFileDialog.getSaveFileName(None, "Зберегти як", self.filename, "Images (*.png *.jpg *.bmp)")
            if filepath:
                self.image.save(filepath)

   def do_contour(self):
        if self.image:
            self.add_to_history()
            self.image = self.image.filter(ImageFilter.CONTOUR)
            self.saveImage()
            self.showImage(os.path.join(self.dir, self.save_dir, self.filename))

   def do_pixel(self, pixel_size=10):
        if self.image:
            self.add_to_history()
            img_small = self.image.resize(
                (self.image.width // pixel_size, self.image.height // pixel_size),
                resample=Image.NEAREST)
            self.image = img_small.resize(self.image.size, Image.NEAREST)
            self.saveImage()
            self.showImage(os.path.join(self.dir, self.save_dir, self.filename))

   def do_glass(self):
        if self.image:
            import random
            self.add_to_history()
            img = self.image.convert("RGB")
            pixels = img.load()
            w, h = img.size
            for i in range(w):
                for j in range(h):
                    dx = random.randint(-2, 2)
                    dy = random.randint(-2, 2)
                    nx = min(max(i + dx, 0), w - 1)
                    ny = min(max(j + dy, 0), h - 1)
                    pixels[i, j] = pixels[nx, ny]
            self.image = img
            self.saveImage()
            self.showImage(os.path.join(self.dir, self.save_dir, self.filename))


workimage = ImageProcessor()

def showChosenImage():
   if lw_files.currentRow() >=0:
      filename = lw_files.currentItem().text()
      workimage.loadImage(workdir, filename)
      image_path = os.path.join(workimage.dir, workimage.filename)
      workimage.showImage(image_path)


lw_files.currentRowChanged.connect(showChosenImage)

btn_bw.clicked.connect(workimage.do_bw)
btn_bl.clicked.connect(workimage.do_blur)
btn_inv.clicked.connect(workimage.do_invert)
btn_cl.clicked.connect(lambda: workimage.do_colorful())
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_flip.clicked.connect(workimage.do_flip)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_save.clicked.connect(workimage.saveImage)
btn_back.clicked.connect(workimage.back)
btn_reset.clicked.connect(workimage.clear_history)
btn_comiks.clicked.connect(workimage.do_posterize)
btn_contour.clicked.connect(workimage.do_contour)
btn_pixel.clicked.connect(lambda: workimage.do_pixel())
btn_glass.clicked.connect(workimage.do_glass)


app.exec()
