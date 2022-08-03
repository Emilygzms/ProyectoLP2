# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:52:43 2022

@author: Emily
"""

import os

# MENU PRODUCTO

def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido


def agregar_productos():
    print("\nAGREGAR PRODUCTO")
    print("---------------------------")
    archivo = 'codigo.txt'
    contenido = input("Código de producto: ")
    agregar_contenido_archivo(archivo, contenido)
    
    archivo1 = 'nombre.txt'
    contenido1 = input("Nombre de producto: ")
    agregar_contenido_archivo(archivo1, contenido1)
    
    archivo2 = 'precio.txt'
    contenido2 = input("Precio de producto: S/.")
    agregar_contenido_archivo(archivo2, contenido2)

def listar_productos():
    print("\nLISTAR PRODUCTO")
    print("------------------------------------")
    
    listar_codigo = leer_archivo('codigo.txt')
    listar_nombre = leer_archivo('nombre.txt')
    listar_precio = leer_archivo('precio.txt')
   
    cod = listar_codigo.split(",")
    nom = listar_nombre.split(",")
    pre = listar_precio.split(",")
 
    print("CÓDIGO\t\tPRODUCTO\t\tPRECIO")
    print("------------------------------------")
    for i  in range(len(cod)):
        print(f" {cod[i]}\t{nom[i]}\t\t{pre[i]}")

def salir():
    print("\nGracias... Vuelva pronto")  

def error():
    print("Opción incorrecta")

def menu():
    print("\n*********MENU PRINCIPAL***********")
    print("1. Listar producto")
    print("2. Agregar producto")
    print("3. Salir")
    
# OPERACIONES ARCHIVO



def agregar_contenido_archivo(nombre_archivo, contenido):
    archivo = open(nombre_archivo,"at")
    archivo.write("," + contenido)
    archivo.close()
   
def agregar_usuario():
    archivo = 'usuario.txt'
    contenido = input("Nuevo usuario:")
    agregar_contenido_archivo(archivo, contenido)
    
def agregar_clave():
    archivo = 'clave.txt'
    contenido = input("Nueva clave:")
    agregar_contenido_archivo(archivo, contenido)
    
def eliminar_archivo(nombre):
    os.remove(nombre)
    
def crea_archivo(nombre, contenido):
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()

def crear_archivo_usuario():
    archivo = 'usuario.txt'
    contenido= input('Nuevo usuario: ')
    crea_archivo(archivo, contenido)

def crear_archivo_clave():
    archivo = 'clave.txt'
    contenido= input('Nueva clave: ')
    crea_archivo(archivo, contenido)
    


# Declarar variable usuario y contraseña que lee el usuario y la clave


'''
def validar(a):
      usuario = 'kevin'
      contraseña = 123
      numero = a
      print("\n\n***LOGIN*")
      dato1 = input('\nIngrese usuario: ')
      dato2 = input('Ingrese la clave: ')
      if numero <= 3:  
         if usuario == dato1 and contraseña == dato2:
            print("\n¡BIENVENIDO AL PROGRAMA!\n")
         
         else:            
            print("\n*Usuario y/o clave incorrectos...*\n")               
            contador = numero+1                
            validar(contador)
        
      else:
            print("programa fallando")
            
        
validar(1)'''

contador = 1
def validar(a):
    
    usuario = leer_archivo('usuario.txt')
    contraseña = leer_archivo('clave.txt')
    numero = a
    
    print("\n\n*********LOGIN***********")
        
    dato1 = input('\nIngrese usuario: ')
    dato2 = input('Ingrese la clave: ')
    
    if numero <= 2:
        if usuario == dato1 and contraseña == dato2:
             print("\n¡BIENVENIDO AL PROGRAMA!\n")
             
             opcion = 1
             while opcion <= 3:
                 menu()
                 opcion = int(input("Seleccione una opción [1-3]: "))
                 if opcion ==1:
                     listar_productos()
                 elif opcion == 2:
                     agregar_productos()
                 elif opcion == 3:
                     salir()
                 else:
                     error()
        else:            
            print("\n*Usuario y/o clave incorrectos...*\n")               
            contador = numero+1                
            validar(contador)
         
    else:
          print("\n***Ha sobrepasado el número de intentos. BYE :D...***\n")
          salir()
        
validar(1)


'''
eliminar_archivo('usuario.txt')
eliminar_archivo('clave.txt')

crear_archivo_usuario()
crear_archivo_clave()'''
