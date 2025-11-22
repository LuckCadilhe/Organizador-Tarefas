
organizador_tarefas = {
    1: 'Adicionar nova tarefa',
    2: 'Listar tarefas existentes',
    3: 'Marcar tarefa como concluída',
    4: 'Editar tarefa',
    5: 'Remover tarefa',
    6: 'Sair do sistema'
}

def exibir_menu():
        print('\n --- Menu Organizador Tarefas ---')
        for chave, valor in organizador_tarefas.items():
            print(f'{chave} - {valor}')
        print('----------------------------')

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        
    def adicionar_tarefas(self):
        
        while True:
            saida = input('\nDeseja adicionar uma nova tarefa? (s/n): ').lower().strip()
            
            if saida == 'n':
                print('\nVocê saiu das tarefas.')
                break
            
            if saida != 's':
                print('\nErro, opção invalida. Tente novamente.')
                continue
                
            nova_tarefa = input('Digite a sua tarefa: ')
        
            if nova_tarefa.strip() == '':
                print('\nErro na tarefa (entrada vazia)')
            else:
                self.tarefas.append(nova_tarefa.strip())
                print(f'\nTarefa {nova_tarefa.strip()} adicionada.')
                  
    def checar_tarefas(self):
        
        if not self.tarefas:
            print('Não há tarefas listadas.')
        else:
            print('\n--- Lista de Tarefas ---')
            for index, tarefa in enumerate(self.tarefas, start=1):
                print(f'Tarefa {index}: {tarefa}')
            print('-------------------------')

        
gerenciador = GerenciadorTarefas() 

def menu_principal():
    while True:
        exibir_menu()
        
        try:
            opcao = int(input('Digite a opção desejada de 1 a 6 : '))
        except ValueError:
            print('Número errado, escolha novamente.')
            continue
        
        if opcao == 1:
            gerenciador.adicionar_tarefas()
        elif opcao == 2:
            gerenciador.checar_tarefas()
            input('\nPressione uma ENTER para voltar ao Menu.')
            continue
        elif opcao == 6:
            break
        elif opcao in organizador_tarefas:
            print(f"A opção '{organizador_tarefas[opcao]}' ainda não foi implementada.")
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    menu_principal()
