catalogo = [
    {"produto": "Avião de pelucia", "preco": 10.00, "em_estoque": True},
    {"produto": "Cartaz de avião", "preco": 3.65, "em_estoque": False }
]

for item in catalogo:
    print(f"Item: {item['produto']} - R$ {item['preco']}")