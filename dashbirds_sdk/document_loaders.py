import os
import sys
from urllib.parse import urlparse

from docling.document_converter import DocumentConverter
from docling_core.types.doc.document import DoclingDocument
from colorama import Fore, Style, init as init_colorama


# Inits
init_colorama()


def is_url_valid(text: str) -> bool:  # True or False
    '''Recebe um valor do tipo texto e retorna True se o texto for uma URL.'''
    if not isinstance(text, str):
        return False

    try:
        result = urlparse(text)
        return all([result.scheme, result.netloc])
    except:
        return False


def convert_document(source: str) -> DoclingDocument:
    '''Recebe uma URL e converte em um objeto da classe DoclingDocument que pode ser processado.'''
    converter = DocumentConverter()
    doc = converter.convert(source).document
    return doc


def extract_file_name(document: DoclingDocument) -> str:
    file_name = f'{document.name}_{document.origin.binary_hash}'
    return file_name


def remove_unnecessary_tags(content: str) -> str:
    return content.replace('<!-- image -->', '')


def extract_document(source: str) -> dict:

    if not is_url_valid(source):
        return {}

    doc = convert_document(source)
    
    # Extract File Name
    file_name = extract_file_name(doc)
    
    # Extract Content
    content = doc.export_to_markdown()

    # Remove Tags
    content = remove_unnecessary_tags(content)

    result = {'file_name': file_name, 'content': content}

    return result


def save_md_file(content: str, file_name: str , docs_path: str = 'C:\\Dashbirds_SDK_outputs\\md') -> bool:
    """Quando o usuário permite, é criada uma pasta com os outputs para uma pasta na raiz. (C://)"""
    
    # Cria o diretório se não existe.
    if not os.path.isdir(docs_path):
        os.makedirs(docs_path)

    with open(f"{docs_path}/{file_name}.md", "w", encoding="utf-8") as file:
        file.write(content)

    return True


if __name__ == '__main__':
    source = sys.argv[1]
    result = extract_document(source)

    print(Fore.BLUE + result['content'] + Style.RESET_ALL)

    if input('Save File? ').lower() == 's':
        save_md_file(result['content'], result['file_name'])
    
    print('Done!')