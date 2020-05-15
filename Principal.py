import cv2
import numpy as np


class Proyecto:
    @staticmethod
    def read_image(path_img):
            if isinstance(path_img, str):
                img = cv2.imread(path_img)
                return img
            else:
                print("Formato No Valido")
                return None
    @staticmethod
    def save_img(img, nombre_img):
        nombre_img = nombre_img + ".jpg"
        cv2.imwrite(nombre_img, img)
#1
class Reducir_tamano:
    @staticmethod
    def __reducir_tamano(img):
        reducir = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
        return reducir
#2
class Recorte_img:
    @staticmethod
    def recorte(img):
        altura, ancho = img.shape[0:2]
        inifila = int(altura*.15)
        inicolum = int(ancho*.15)
        finfila = int(altura*.85)
        fincolum = int(ancho*.85)
        recorte = img[inifila:finfila, inicolum:fincolum]
        return recorte
#3
class Img_borroso:
    @staticmethod
    def borroso(img):
        borros = cv2.medianBlur(img,5)
        return borros
#4
class Bordes_img:
    @staticmethod
    def bordes(img):
        bordes = cv2.Canny(img,100,200)
        return bordes
#5
class Contraste_img:
    @staticmethod
    def contraste(img):
        contraste= cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
        return contraste
#Main
if __name__ == '__main__':
    img = Proyecto.read_image("data.png")
    #1
    redutamano= Reducir_tamano.__reducir_tamano(img)
    Proyecto.save_img(img=redutamano , nombre_img ='Reducir la Imagen')
    #2
    recort =Recorte_img.recorte(img)
    Proyecto.save_img(img=recort, nombre_img="Recorte de Imagen")
    #3
    borros = Img_borroso.borroso(img)
    Proyecto.save_img(img=borros, nombre_img="Imagen Borrosa")
    #4
    border = Bordes_img.bordes(img)
    Proyecto.save_img(img=border, nombre_img="Detector de Borde")
    #5
    contrast=Contraste_img.contraste(img)
    Proyecto.save_img(img=contrast ,nombre_img='Contraste')
    print("Proyecto Terminado")
    print('Autor: Daniel Alvarez')
