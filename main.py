
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
                
            nova_tarefa = input('Digite a sua tarefa: ').strip()
        
            if nova_tarefa == '':
                print('\nErro na tarefa (entrada vazia)')
            else:
                self.tarefas.append(nova_tarefa)
                print(f'\nTarefa {nova_tarefa} adicionada.')
                  
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
            print('Opção inválida, digite um numero.')
            continue
        match opcao:
            case 1:
                gerenciador.adicionar_tarefas()
            case 2:
                gerenciador.checar_tarefas()
                input('\nPressione uma ENTER para voltar ao Menu.')
                continue
            case 6:
                break
            
            case _:
                print("\nOpção inválida. Tente novamente.")
            
if __name__ == "__main__":
    menu_principal()
