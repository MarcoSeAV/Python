class producto():
    def __init__(self, nombre, precio_base, stock):
        self.nombre=nombre
        self.precio_base=precio_base
        self.stock=stock

    def aplicar_descuento(self, porcentaje):
        self.precio_base*=(1-porcentaje)
        print(f"El nuevo precio es {self.precio_base}")
    
    def actualizar_stock(self, cantidad):
        if (self.stock+cantidad)<0:
            print("No puedes tener stock negativo")
        else:
            self.stock+=cantidad
            print(f"La nueva cantidad es {self.stock}")

class categoria():
    def __init__(self, nombre_categoria):
        self.nombre_categoria=nombre_categoria
        self.lista=[]

    def agregar_producto(self, producto):
        self.lista.append(producto)
        print(f"El producto {producto.nombre} se agrego a la lista")

    def valor_total_categoria(self):
        suma = 0
        for b in self.lista:
            suma += (b.precio_base*b.stock)
        print(f"El valor total de la categoría es {suma}")

class pedido():
    def __init__(self, cliente, estado):
        self.cliente = cliente
        self.productos_comprados=[]

    def calcular_total(self, iva):
        suma_productos = 0   
