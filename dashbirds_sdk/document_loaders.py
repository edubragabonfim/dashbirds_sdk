import sys
from urllib.parse import urlparse

from docling.document_converter import DocumentConverter
from docling_core.types.doc.document import DoclingDocument


def is_url_valid(text: str) -> bool:
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
    if is_url_valid(source):
        converter = DocumentConverter()
        doc = converter.convert(source).document
        return doc
    else:
        return DoclingDocument(name='')


def extract_file_name(document: DoclingDocument) -> str:
    file_name = f'{document.name}_{document.origin.binary_hash}'
    return file_name


def extract_document(source: str) -> dict:
    doc = convert_document(source)
    
    # Extract File Name
    file_name = extract_file_name(doc)
    
    # Extract Content
    content = doc.export_to_markdown()

    result = {'file_name': file_name, 'content': content}

    return result


if __name__ == '__main__':
    _source = sys.argv[1]
    data = extract_document(_source)

    print(data['content'])