import time

def mudar_estado(tarefa_nome, tarefa_estado, novo_estado):

    tarefa_estado = novo_estado
    print(f"Tarefa '{tarefa_nome}' está no estado: {tarefa_estado}")
    time.sleep(1)  # Simula o tempo entre as transições de estado
    return tarefa_estado

def criar(tarefa_nome, tarefa_estado):

    tarefa_estado = mudar_estado(tarefa_nome, tarefa_estado, "Novo")
    tarefa_estado = mudar_estado(tarefa_nome, tarefa_estado, "Pronto")
    tarefa_estado = executar(tarefa_nome, tarefa_estado)
    return tarefa_estado

def executar(tarefa_nome, tarefa_estado):

    tarefa_estado = mudar_estado(tarefa_nome, tarefa_estado, "Em Execução")
    if verificar_bloqueio():

        tarefa_estado = bloquear(tarefa_nome, tarefa_estado)
    else:

        tarefa_estado = concluir(tarefa_nome, tarefa_estado)
    return tarefa_estado

def bloquear(tarefa_nome, tarefa_estado):

    tarefa_estado = mudar_estado(tarefa_nome, tarefa_estado, "Bloqueado")
    time.sleep(2)  # Simula o tempo de bloqueio
    tarefa_estado = mudar_estado(tarefa_nome, tarefa_estado, "Pronto")
    tarefa_estado = executar(tarefa_nome, tarefa_estado)
    return tarefa_estado

def concluir(tarefa_nome, tarefa_estado):

    tarefa_estado = mudar_estado(tarefa_nome, tarefa_estado, "Concluído")
    return tarefa_estado

def verificar_bloqueio():
    return False  # Simula uma condição de bloqueio

def main():
    
    tarefa_nome = "Processamento de Dados"
    tarefa_estado = "Novo"
    tarefa_estado = criar(tarefa_nome, tarefa_estado)

if __name__ == "__main__":
    main()
