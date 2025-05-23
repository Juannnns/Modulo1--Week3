# Funciones reutilizables
def preparar_pollo_a_la_plancha(presentacion):
    if presentacion == "tiras":
        descripcion = "Pollo a la planchaa cortado en tiras"
    else:
        descripcion = "Pechuga de pollo a la plancha entera"
    print(f"Preparando {descripcion}")
    return descripcion 

def preparar_salsa_cesar(pimienta_negra_molida):
    salsa = {
        "pimienta negra" : pimienta_negra_molida,
        "sal" : "al gusto",
        "zumo de limon" : "10 ml"
    }
    print("Preparando salsa César con los siguientes ingredientes: ")
    print(salsa)
    return salsa

def preparar_salsa_cesar():
    print("\nPreparando salsa César con pollo...")
    pollo = preparar_pollo_a_la_plancha("tiras")
    salsa = preparar_salsa_cesar(True)
    ingredientes = ["lechuga romana",
                    "crutones", 
                    "queso parmesano", 
                    pollo, 
                    "salsa cesar,"]
    pasos = ["Lavar y cortar las lechugas",
             "Agregar crutones y queso",
             "Agregar el pollo", 
             "Añadir la salsa y mezclar"]
    return emplatado("ensalada cesar", salsa, "tiras", ingredientes, pasos)

def preparar_wrap_cesar():
    print("\nPreparando wrap de pollo con la salsa césar...")
    pollo = preparar_pollo_a_la_plancha("tiras")
    salsa = preparar_salsa_cesar(False)
    ingredientes = [
        "torilla de trigo", pollo, "lechuga", "salsa César", "queso rallado"
    ]
    pasos = [
        "Calentar la tortilla",
        "Agregar el pollo",
        "Agregar lechuga y queso",
        "Añadir salsa y enrollar"
    ]
    return emplatado("wrap_cesar", salsa, "tiras", ingredientes, pasos)

def preparar_sandwich_de_pollo():
    print("\nPreparando sandwich clásico de pollo...")
    pollo = preparar_pollo_a_la_plancha("normal")
    salsa = {
        "pimienta_negra" : False,
        "sal" : "al gusto",
        "zumo de limon" : "10 ml"
    }
    ingredientes = [
        "pan de sandwich", "queso", "lechuga", "tomate", pollo
    ]
    pasos= [
        "Tostar ligeramente el pan",
        "Colocar el pollo",
        "Colocar el queso", 
        "Agregar vegetales y cerrar el sandwich"
    ]
    return emplatado("sandwich", salsa, "normal", ingredientes, pasos)

def emplatado(nombre_receta, salsa, presentacion_pollo, ingredientes, pasos):
    return {
        "receta" : nombre_receta,
        "salsa" : salsa,
        "presentacion_pollo" : presentacion_pollo,
        "ingredientes" : ingredientes,
        "pasos" : pasos
    }
    
# Interfaz por consola
def menu_consola():
    while True:
        print("==== Asistente virtual de cocina ====")
        print("1. Preparar ensalada César con pollo")
        print("2. Preparar wrap de pollo con salsa")
        print("3. Preparar Sándwich clásico de pollo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            receta = preparar_salsa_cesar()
            mostrar_receta(receta)
        elif opcion == "2":
            receta = preparar_wrap_cesar()
            mostrar_receta(receta)
        elif opcion == "3":
            preparar_sandwich_de_pollo()
            mostrar_receta(receta)
        elif opcion == "4":
            print("¡Gracias por cocinar con nosotros!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            
# Mostrar receta emplatada
def mostrar_receta(receta):
    print("\n=== EMPLATADO FINAL ===")
    print(f"Receta: {receta['receta']}")
    print(f"Presentación del pollo: {receta['presentacion_pollo']}")
    print(f"Ingredientes:")
    for ingrediente in receta["ingredientes"]:
        print(f" - {ingrediente}")
    print("Pasos: ")
    for i, paso in enumerate(receta["pasos"], start=1):
        print(f"{i}. {paso}")
    print("Salsa: ")
    for k, v in receta["salsa"].items():
        print(f" - {k}:  {v}")
        
# Ejecutar consola
if __name__ == "__main__":
    menu_consola()