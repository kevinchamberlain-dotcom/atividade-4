produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque": 14
}
print("=== PRODUTO CADASTRADO ===")
print(produto)
print(f"Nome do produto: {produto['nome']}")
print(f"Preco do produto: {produto['preco']}")
print("-"* 40)

produto["preco"] = 220.0
produto["estoque"] = produto["estoque"] + 6
produto["categoria"] = "Periféricos"

print("=== PRODUTO ATUALIZADO ===")
print(produto)
print(f"Novo Estoque Total: {produto['estoque']} unidades")
print("-"* 40)

usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}
print("=== INSPEÇÃO DE REGISTRO ===")
print("Chaves de Registros:", usuario.keys())
print("Valores de Registros:", usuario.values())