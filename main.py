class tarefas():
    def __init__(self):
        self.tarefas = []
        
    def adicionar_tarefas(self, tarefa):
        self.tarefas.append(tarefa)
        print(f'Tarefa {tarefa} adicionada.')
    
    def checar_tarefas(self):
        if not self.tarefas:
            print('Não há tarefas listadas.')
        else:
            print('\n--- Lista de Tarefas ---')
            for index, tarefas in enumerate(self.tarefas, start=1):
                print(f'Tarefa  {index}: {tarefas}')
            print('-------------------------')
        
lista = tarefas()

while True:
    entrada = input('Adicione uma nova tarefa ou\ndigite "sair" para terminar a operação: ')

    if entrada.lower() == 'sair':
        print('Encerrar processo de adição de tarefas.')
        break
    
    if entrada:
        lista.adicionar_tarefas(entrada)

lista.checar_tarefas()           

