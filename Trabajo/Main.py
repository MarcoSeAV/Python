from Productoo import *

prod1 = producto("Maruchan", 16, 100)
prod2 = producto("Coca-Cola 600ml", 18, 150)
prod3 = producto("Leche Entera 1L", 26, 80)
prod4 = producto("Pan de Caja", 45, 40)
prod5 = producto("Huevo 12 pzas", 38, 60)
prod6 = producto("Arroz Blanco 1kg", 22, 120)
prod7 = producto("Frijol Negro 1kg", 35, 90)
prod8 = producto("Aceite Vegetal", 42, 50)
prod9 = producto("Atún en Agua", 19, 200)
prod10 = producto("Pasta Spaghetti", 12, 110)
prod11 = producto("Café Soluble", 85, 30)
prod12 = producto("Azúcar Blanca 1kg", 28, 75)
prod13 = producto("Detergente Polvo", 55, 45)
prod14 = producto("Jabón de Tocador", 15, 180)
prod15 = producto("Papel Higiénico 4 rollos", 32, 100)
prod16 = producto("Cereal de Maíz", 62, 35)
prod17 = producto("Yogurt Natural", 24, 55)
prod18 = producto("Mermelada de Fresa", 48, 25)
prod19 = producto("Galletas María", 17, 140)
prod20 = producto("Salsa de Tomate", 10, 250)

cat1=Categoria("Alimentos")
lst1=[prod1, prod4, prod5, prod6]
for a in lst1:
    
cat1.agregar_producto(prod1)
print(cat1.lista)