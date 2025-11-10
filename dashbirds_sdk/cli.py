import sys
from colorama import Fore, Style

from .f_document_loaders import extract_document, save_md_file
from .cli_methods import check_params


def main():
    """Função principal da CLI do Dashbirds SDK"""
    
    # Verifica se há argumentos suficientes
    if len(sys.argv) < 2:
        print(Fore.RED + "Erro: Argumentos insuficientes" + Style.RESET_ALL)
        print("Uso: dsb -de <URL>")
        sys.exit(1)
    
    # Verifica o comando
    if sys.argv[1] == '-de':
        if len(sys.argv) < 3:
            print(Fore.RED + "Erro: URL não fornecida" + Style.RESET_ALL)
            print("Uso: dsb -de <URL>")
            sys.exit(1)
        
        source = sys.argv[2]
        
        # Extrai o documento
        result = extract_document(source)
        
        if not result:
            print(Fore.RED + "Erro: URL inválida ou falha na extração" + Style.RESET_ALL)
            sys.exit(1)
        
        # Exibe o conteúdo
        print(Fore.BLUE + result['content'] + Style.RESET_ALL)
        
        # Pergunta se deseja salvar
        if input('Save File? (s/n): ').lower() == 's':
            save_md_file(result['content'], result['file_name'])
            print(Fore.GREEN + 'Arquivo salvo com sucesso!' + Style.RESET_ALL)
        
        print('Done!')
    
    else:
        print(Fore.RED + f"Comando desconhecido: {sys.argv[1]}" + Style.RESET_ALL)
        print("Uso: dsb -de <URL>")
        sys.exit(1)

    # check_params()


if __name__ == '__main__':
    main()
