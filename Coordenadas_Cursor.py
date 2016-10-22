import pyautogui
print ("Coordenadas Mouse \n\n\nEnter para determinar las coordenadas del cursor \nControl + C. para salir del programa")
Coordenadas = pyautogui.position()
try:
    while True:
        #TODO Da las coordenadas del mouse, solo imprime una vez cada valor
        if Coordenadas != pyautogui.position():
            print('Coordenadas actuales: ' ,pyautogui.position())
            Coordenadas = pyautogui.position()
except KeyboardInterrupt:
    print ('\nPrograma finalizado.')
