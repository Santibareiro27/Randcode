import os
import msvcrt

my_list = []

def pause():
    print('\nPresione una tecla para continuar...')
    msvcrt.getch()
    os.system('cls')

def menu():
    auxname = 'name'
    print('--MENU--')
    print('1 - Show names')
    print('2 - Search name')
    print('3 - Insert name')
    print('4 - Delete name')
    print('5 - Quit')
    opt = msvcrt.getch().decode('utf-8')
    os.system('cls')
    match opt:
        case '1':
            if my_list:
                for i in my_list:
                    print(i)
            else:
                print('La lista esta vacia')
        case '2':
            if my_list:
                auxname = input('Ingrese un nombre a buscar: ').capitalize()
                try:
                    print(f'Se encontro {auxname} en la posicion',my_list.index(auxname)+1)
                except:
                    print('No se encontro el nombre buscado')
            else:
                print('La lista esta vacia')
        case '3':
            auxname = input('Ingrese un nombre a añadir: ')
            my_list.append(auxname.capitalize())
            my_list.sort()
        case '4':
            if my_list:
                auxname = input('Ingrese un nombre a eliminar: ').capitalize()
                try:
                    my_list.remove(auxname)
                    print(f'Se elimino {auxname} con exito')
                except:
                    print('No se encontro el nombre buscado')
            else:
                print('La lista esta vacia')
        case '5':
            return False
        case _:
            print('Error de ingreso')
    pause()
    return True

while menu():
    pass
print('Programa finalizado')