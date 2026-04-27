algoritmop determinista.py
# Ejemplo de algoritmo determinista: Cálculo del valor de una inversión aplicando interés compuesto.
def calcular_inversion(inversion_inicial, tasa_interes, tiempo):
    """
    Calcula el valor de una inversión con interés compuesto.
   
    :param inversion_inicial: Monto inicial de la inversión.
    :param tasa_interes: Tasa de interés anual (en porcentaje).
    :param tiempo: Tiempo en años.
    :return: Valor final de la inversión.
    """
    valor_final = inversion_inicial  (1 + tasa_interes / 100) * tiempo
    return valor_final
# Ejemplo de uso
inversion_inicial = 1000  # Monto inicial de la inversión
tasa_interes = 5  # Tasa de interés anual en porcentaje
tiempo = 10  # Tiempo en años
valor_final = calcular_inversion(inversion_inicial, tasa_interes, tiempo)
print(f"Inversión inicial: {inversion_inicial} unidades monetarias")
print(f"Tasa de interés: {tasa_interes}% anual")
print(f"Tiempo: {tiempo} años")
print(f"El valor final de la inversión es: {valor_final:.2f} unidades monetarias")
