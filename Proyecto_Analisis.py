import cv2
from PIL import Image
from numpy import asarray
# LECTURA DE IMAGENES
img = cv2.imread('prueba.jpg')
imgGris = cv2.imread('prueba.jpg',0)

#MOSTRAR EN PANTALLA LA IMGEN
cv2.imshow('prueba',img)
cv2.imshow('prueba Gris',imgGris)

#GUARDA LA IMAGEN NUEVA QUE PASEMOS
cv2.imwrite('pruebaGris.jpg',imgGris)

cv2.waitKey(0)
cv2.destroyAllWindows()

#CREAR MATRICES

#LEER LAS IMAGENES DEL PROYECTO
img = Image.open('prueba.jpg')
imgGris = Image.open('pruebaGris.jpg')

print("MATRIZ IMAGEN RGB")
print(img.format)
print(img.size)
print(img.mode)
numpydata = asarray(img)
print(numpydata)

print("MATRIZ IMAGEN GRISES")
print(imgGris.format)
print(imgGris.size)
print(imgGris.mode)
numpydataGris = asarray(imgGris)

print(numpydataGris)
