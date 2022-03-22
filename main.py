def elegir():
    variable = int(input("\nEjercicios de Agregación y Composición de POO\n\nIntroduzca qué ejercicio desea realizar: \n1. El día siguiente.\n2. ¿Inmortal?\n3. Alternativa a la herencia múltiple.\n"))
    if variable == 1:
        from Clases import edificio
    elif variable == 2:
        from Clases import inmortal
    elif variable == 3:
        from Clases import asociacion 
    else:
        print("Sólo son válidos los valores 1, 2 y 3.\n")
        elegir()
elegir()