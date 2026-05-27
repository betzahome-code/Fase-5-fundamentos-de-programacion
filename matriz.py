# Función para calcular la cantidad a pedir con validación
def calcular_pedido(stock_actual, stock_minimo):
    try:
        stock_actual = int(stock_actual)
        stock_minimo = int(stock_minimo)
    except (TypeError, ValueError):
        raise ValueError("Los valores de stock deben ser enteros")

    if stock_actual < 0 or stock_minimo < 0:
        raise ValueError("Los stocks deben ser valores no negativos")

    return max(0, stock_minimo - stock_actual)


# Matriz de artículos de la panadería
# [Código, Nombre, Stock Actual, Stock Mínimo]
articulos = [
    [101, "Pan Frances", 20, 30],
    [102, "Pan Integral", 15, 20],
    [103, "Croissant", 8, 15],
    [104, "Muffin de Chocolate", 12, 10],
    [105, "Torta de Vainilla", 3, 5],
    [106, "Galletas", 25, 25],
    [107, "Pan de Queso", 6, 12],
    [108, "Donas", 18, 20],
    [109, "Brownies", 4, 10],
    [110, "Pastel de Pollo", 7, 10]
]


def generar_reporte(articulos):
    """Genera una lista de pedidos a partir de la matriz de artículos.

    Retorna una lista de tuplas: (codigo, nombre, cantidad_a_pedir)
    """
    pedidos = []
    for fila in articulos:
        if not isinstance(fila, (list, tuple)) or len(fila) != 4:
            print("Fila ignorada (formato inválido):", fila)
            continue

        codigo, nombre, stock_actual, stock_minimo = fila
        try:
            cantidad = calcular_pedido(stock_actual, stock_minimo)
        except ValueError as e:
            print(f"Error en artículo {fila}: {e}")
            continue

        if cantidad > 0:
            pedidos.append((codigo, nombre, cantidad))

    return pedidos


if __name__ == "__main__":
    pedidos = generar_reporte(articulos)
    if not pedidos:
        print("No se requieren pedidos. Inventario en niveles óptimos.")
    else:
        print("===== LISTA DE PEDIDOS PANADERÍA =====")
        for codigo, nombre, cantidad in pedidos:
            print(f"{codigo} - {nombre}: {cantidad} unidades")