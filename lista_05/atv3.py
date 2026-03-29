# 3) O gerente de projetos precisa consolidar as listas de tarefas
# de duas equipes distintas: equipe A e equipe B.
# Após unir as listas, remover uma tarefa específica informada pelo usuário.
# Validar as entradas e informar caso a tarefa não seja encontrada.

equipe_a = ["Analisar requisitos", "Criar wireframe", "Desenvolver login"]
equipe_b = ["Testar sistema", "Corrigir bugs", "Criar wireframe"]

tarefas = equipe_a + equipe_b

print("Lista consolidada de tarefas:")
for tarefa in tarefas:
    print("-", tarefa)

tarefa_remover = input("\nDigite o nome da tarefa que deseja remover: ").strip()

if tarefa_remover == "":
    print("Entrada inválida.")
else:
    if tarefa_remover in tarefas:
        tarefas.remove(tarefa_remover)
        print("\nTarefa removida com sucesso.")
    else:
        print("\nTarefa não encontrada.")

print("\nLista final de tarefas:")
for tarefa in tarefas:
    print("-", tarefa)