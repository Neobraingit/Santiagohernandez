''' En este ejercicio práctico se propone la creación de una sencilla aplicación que nos ayude a verificar la integridad
de un mensaje calculando la función hash de una cadena de texto que el usuario proporcione'''

''' Crear una cabecera para el programa con ASCII Art'''

'''Calculando el hash de una cadena de texto'''

'''Solicitar al usuario una cadena de texto'''

'''Construir la aplicación final'''

'''Ejecutar la aplicación'''

# Resolución del ejercicio
def cabecera():
 print ('''                                               
        ,--,                                   
      ,--.'|                         ,---,     
   ,--,  | :                       ,--.' |     
,---.'|  : '                       |  |  :     
|   | : _' |              .--.--.  :  :  :     
:   : |.'  |  ,--.--.    /  /    ' :  |  |,--. 
|   ' '  ; : /       \  |  :  /`./ |  :  '   | 
'   |  .'. |.--.  .-. | |  :  ;_   |  |   /' : 
|   | :  | ' \__\/: . .  \  \    `.'  :  | | | 
'   : |  : ; ," .--.; |   `----.   \  |  ' | : 
|   | '  ,/ /  /  ,.  |  /  /`--'  /  :  :_:,' 
;   : ;--' ;  :   .'   \'--'.     /|  | ,'     
|   ,/     |  ,     .-./  `--'---' `--''       
'---'       `--`---'                           
                                              
                  by Marcos ''')
cabecera()
print ('A continuación, introduce un texto para calcular el hash: ')
cadena = input()
print ('El hash es:',hash(cadena))



