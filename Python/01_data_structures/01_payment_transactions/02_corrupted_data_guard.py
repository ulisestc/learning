datos_banco = [
    {"user_id": "A", "monto": 10, "estado": "completado"},
    {"user_id": "B", "monto": 50, "estado": "pendiente"},
    {"user_id": "D", "monto": 500},  # <--- DATO CORRUPTO
    {"user_id": "A", "monto": 20, "estado": "completado"},
]

# 2. Crear función que itere sobre lista y retorne el dicc

def procesar_transacciones(lista_datos):
    resultado = {}

    for  transaccion in lista_datos:
        if "estado" in transaccion and transaccion["estado"] == "completado":
            if transaccion["user_id"] not in resultado:
                resultado[transaccion["user_id"]] = transaccion["monto"]
            else: 
                resultado[transaccion["user_id"]] += transaccion["monto"]
    
    return resultado

print (procesar_transacciones(datos_banco))