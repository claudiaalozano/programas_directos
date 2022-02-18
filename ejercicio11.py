horas= int(input("Introduzca las horas extra que ha trabajado en este mes:"))
euro= 17
horas_totales= horas + 35
if horas > 36 and horas < 43:
    horas_extra = (horas * 17 ) * 1,25
    sueldo = (35 * 17) + horas_extra
    print("Usted ha trabajado un total de horas extra de " , horas , "por lo que a su sueldo ha ascendido a un total de " , sueldo , ", y ha trabajado un total de " , horas_totales , "horas.")
if horas >= 44:
    horas_extra2 = (horas * 17) * 1,50
    sueldo2 = (35 * 17) + horas_extra2
    print("Usted ha trabajado un total de horas extra de " , horas , "por lo que a su sueldo ha ascendido a un total de " , sueldo2 , ", y ha trabajado un total de " , horas_totales , "horas.")