cadastros = [
    {"nome": "Kevin","idade": 17,"curso": "Informática"},
    {"nome": "Bruno Souza", "idade": 16, "curso": "Robótica"}
]
print("=== CADASTROS INICIAIS ===")
for aluno in cadastros:
    print(f"Aluno: {aluno['nome']} | Curso: {aluno['curso']}")
print("-" * 40)
novo_aluno = {
    "nome": "Daniel Santos",
    "idade": 17,
    "curso": "Informática"
}
cadastros.append(novo_aluno)
cadastros.append({
    "nome": "Sofia Goncalves",
    "idade": 17,
    "curso": "Pedagogia"
})
print("=== TABELA ATUALIZADA APÓS O .APPEND() ===")
print(f"Total de registros na memória: {len(cadastros)}")
print("-" * 40)
for i in range(len(cadastros)):
    registro = cadastros[i]
    print(f"Registro [{i}] -> Nome: {registro['nome']} | Idade: {registro['idade']} | Curso: {registro['curso']}")