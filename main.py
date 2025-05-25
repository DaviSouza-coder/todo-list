import argparse
from gerenciador import GerenciadorTarefas

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas CLI em Python!")

    subparser = parser.add_subparsers(dest="comando", help="Comando disponiveis")

    # Adicionar uma nova tarefa
    parser_adicionar = subparser.add_parser("adicionar", help="Adicionar uma nova tarefa")
    parser_adicionar.add_argument("titulo", type=str, help="Titulo da tarefa")
    parser_adicionar.add_argument("descricao", type=str, help="Descrição da tarefa")
    parser_adicionar.add_argument("data_vencimento", type=str, help="Data de vencimento da tarefa")

    # Listar tarefas
    parser_listar = subparser.add_parser("listar", help="Listar todas as tarefas")
    parser_listar.add_argument("--status", choices=["Pendente", "Concluida"], help="Filtrar por status da tarefa")

    # Editar tarefas
    parse_editar = subparser.add_parser("editar", help="Editar uma tarefa")
    parse_editar.add_argument("indice", type=int, help="Indice da tarefa a ser editada")
    parse_editar.add_argument("--titulo", type=str, help="Novo titulo da tarefa")
    parse_editar.add_argument("--descricao", type=str, help="Nova descrição da tarefa")
    parse_editar.add_argument("--data_vencimento", type=str, help="Nova data de vencimento da tarefa")

    # Remover tarefas
    parser_remover = subparser.add_parser("remover", help="Remover uma tarefa")
    parser_remover.add_argument("indice", type=int, help="Indice da tarefa ser removida")

    # Marcar tarefa como concluida
    parser_marcar_concluida = subparser.add_parser("concluir", help="Marcar uma tarefa como concluida")
    parser_marcar_concluida.add_argument("indice", type=int, help="Indice da tarefa a ser marcada como concluida")

    # Processar argumentos
    args = parser.parse_args()
    gerenciador = GerenciadorTarefas()

    if args.comando == "adicionar":
        gerenciador.adicionar_tarefa(args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "listar":
        gerenciador.lista_tarefas(args.status)
    elif args.comando == "editar":
        gerenciador.editar_tarefa(args.indice - 1, args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "remover":
        gerenciador.remover_tarefa(args.indice - 1)
    elif args.comando == "concluir":
        gerenciador.marcar_concluida(args.indice - 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
