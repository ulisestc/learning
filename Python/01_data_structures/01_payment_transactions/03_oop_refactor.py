class Transaccion:
    def __init__(self, user_id, monto, estado = "pendiente"):
            self.user_id = user_id
            self.monto = monto
            self.estado = estado

def procesar_transacciones(lista_datos):
    resultado = {}

    for  transaccion in lista_datos:
        if transaccion.estado== "completado":
            if transaccion.user_id not in resultado:
                resultado[transaccion.user_id] = transaccion.monto
            else: 
                resultado[transaccion.user_id] += transaccion.monto
    
    return resultado


transaccion_1 = Transaccion(user_id="A", monto=100, estado="completado")
transaccion_2 = Transaccion(user_id="B", monto=50)

print(transaccion_2.estado)

datos_banco_oop = [
    Transaccion(user_id="A", monto=10, estado="completado"),
    Transaccion(user_id="B", monto=50), # Entra como pendiente por defecto
    Transaccion(user_id="D", monto=500, estado="completado"),
    Transaccion(user_id="A", monto=20, estado="completado")
]

print(procesar_transacciones(datos_banco_oop))