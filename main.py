#DICIONARIO PARA SER BUSCADO A OPÇÃO DE 1 A 6 NO MENU
organizador_tarefas = {
    1: 'Adicionar nova tarefa',
    2: 'Listar tarefas existentes',
    3: 'Marcar tarefa como concluída',
    4: 'Editar tarefa',
    5: 'Remover tarefa',
    6: 'Sair do sistema'
}
#FUNÇÃO PARA EXIBIÇÃO DO MENU
def exibir_menu():
        print('\n --- Menu Organizador Tarefas ---')
        for chave, valor in organizador_tarefas.items():
            print(f'{chave} - {valor}')
        print('----------------------------')

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        #PRIMEIRA ETAPA ADICIONAR TAREFAS
    def adicionar_tarefas(self):
        
        while True:
            saida = input('\nDeseja adicionar uma nova tarefa? (s/n): ').lower().strip()
            #ESTRUTURA PARA SEMPRE ADICIONAR UMA TAREFA, ATÉ ONDE O CLIENTE DESEJAR
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
        #CHECAGEM DAS TAREFAS JÁ LISTADAS
        if not self.tarefas:
            print('Não há tarefas listadas.')
        else:
            print('\n--- Lista de Tarefas ---')
            for index, tarefa in enumerate(self.tarefas, start=1):
                print(f'Tarefa {index}: {tarefa}')
            print('-------------------------')

        
gerenciador = GerenciadorTarefas() 
#FUNÇÃO INICIAL PARA CHECAGEM DO MENU DE 1 A 6
def menu_principal():
    while True:
        exibir_menu()
        
        try:
            opcao = int(input('Digite a opção desejada de 1 a 6 : '))
        except ValueError:
            print('Opção inválida, digite um numero.')
            continue
        #AQUI FOI UTILIZADO MATCH-CASE PARA SER MELHOR A LEITURA AO INVÊS DE IF-ELIF-ELSE.
        match opcao:
            case 1:
                gerenciador.adicionar_tarefas()
            case 2:
                gerenciador.checar_tarefas()
                input('\nPressione ENTER para voltar ao Menu.')
                continue
            case 6:
                break
            
            case _:
                print("\nOpção inválida. Tente novamente.")
#ESSE IF IRÁ SEMPRE CHAMAR O MENU QUANDO           
menu_principal()
