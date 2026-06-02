transacciones = [
    {"user_id": "A", "monto": 10, "estado": "completado"},
    {"user_id": "B", "monto": 50, "estado": "pendiente"},
    {"user_id": "A", "monto": 20, "estado": "completado"},
    {"user_id": "C", "monto": 100, "estado": "fallido"},
    {"user_id": "B", "monto": 30, "estado": "completado"}
]

# 1. Crear diccionario vacio
# 2. Iterar para cada elemento
# 3. Si estado != completado -> seguimos
# 4. Si == completado, checamos user_id...

transacciones_filtradas = {}

for  transaccion in transacciones:
    if transaccion["estado"] == "completado":
        if transaccion["user_id"] not in transacciones_filtradas:
            transacciones_filtradas[transaccion["user_id"]] = transaccion["monto"]
        else: 
            transacciones_filtradas[transaccion["user_id"]] += transaccion["monto"]

print(transacciones_filtradas)