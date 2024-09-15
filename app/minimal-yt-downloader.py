import os
import time
import urllib.error

from typing import List
from pytubefix import YouTube
from pytubefix.cli import on_progress

MAX_RETRIES = 3
DOWNLOAD_FOLDER = "Videos Downloaded"


def is_valid_youtube_url(url: str) -> bool:
    """
    Verifica se uma URL é válida para o YouTube.

    Parâmetros:
    url (str): URL a ser verificada.

    Retorno:
    bool: Retorna True se a URL for válida, caso contrário False.
    """
    try:
        YouTube(url)
        return True
    except Exception:
        return False


def download_video(url: str) -> None:
    """
    Faz o download de um vídeo do YouTube com tentativas automáticas.

    Parâmetros:
    url (str): URL do vídeo do YouTube a ser baixado.

    Retorno:
    None: Não retorna nenhum valor.
    """
    retry_count = 0

    while retry_count < MAX_RETRIES:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            print(f"🚀 Baixando: {yt.title}")
            
            stream = yt.streams.get_highest_resolution()

            output_path = os.path.join(DOWNLOAD_FOLDER, stream.default_filename)

            stream.download(output_path=DOWNLOAD_FOLDER)

            print(f"✅ Download concluído: {yt.title}, salvo em {output_path}")
            break

        except urllib.error.HTTPError as http_err:
            print(f"❌ Erro HTTP ao tentar baixar o vídeo: {http_err}")
            retry_count += 1
            retry_or_fail(retry_count)
        except Exception as e:
            print(f"❌ Erro ao baixar o vídeo: {e}")
            retry_count += 1
            retry_or_fail(retry_count)


def retry_or_fail(retry_count: int) -> None:
    """
    Gerencia a lógica de tentativas de download.

    Parâmetros:
    retry_count (int): O número de tentativas já feitas.

    Retorno:
    None: Não retorna nenhum valor.
    """
    if retry_count < MAX_RETRIES:
        print(f"🔄 Tentando novamente... ({retry_count}/{MAX_RETRIES})")
        time.sleep(2)
    else:
        print("❌ Falha no download após várias tentativas.")


def get_valid_urls(urls: List[str]) -> List[str]:
    """
    Retorna uma lista de URLs válidas do YouTube.

    Parâmetros:
    urls (List[str]): Lista de URLs a serem verificadas.

    Retorno:
    List[str]: Lista de URLs válidas.
    """
    return [url for url in urls if is_valid_youtube_url(url)]


def get_invalid_urls(urls: List[str]) -> List[str]:
    """
    Retorna uma lista de URLs inválidas do YouTube.

    Parâmetros:
    urls (List[str]): Lista de URLs a serem verificadas.

    Retorno:
    List[str]: Lista de URLs inválidas.
    """
    return [url for url in urls if not is_valid_youtube_url(url)]


def get_user_input(prompt: str, valid_options: List[str]) -> str:
    """
    Obtém uma entrada do usuário até que uma opção válida seja fornecida.

    Parâmetros:
    prompt (str): A mensagem que será mostrada ao usuário.
    valid_options (List[str]): Lista de opções válidas.

    Retorno:
    str: A entrada válida fornecida pelo usuário.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"🙂‍↔️ Entrada inválida. Opções válidas: {', '.join(valid_options)}")


def ask_for_confirmation() -> bool:
    """
    Pergunta ao usuário se deseja proceder com o download.

    Retorno:
    bool: Retorna True se o usuário deseja continuar, caso contrário False.
    """
    return get_user_input("👀 Deseja proceder com o download? (Y/n): ", ['y', 'n', '']) in ('y', '')


def ask_to_repeat() -> bool:
    """
    Pergunta ao usuário se deseja baixar mais vídeos. 🔄➡️

    Retorno:
    bool: Retorna True se o usuário deseja continuar, caso contrário False.
    """
    return get_user_input("🔂 Deseja baixar mais vídeos? (y/N): ", ['y', 'n', '']) == 'y'


def main() -> None:
    """
    Função principal que lida com o processo de download de vídeos do YouTube. 🎬

    Retorno:
    None: Não retorna nenhum valor.
    """
    print("\n")
    print("=========================================================================\n")
    print("==========             MINIMAL YOUTUBE DOWNLOADER              ==========\n")
    print("=========================================================================\n")
    print("\n")

    while True:
        urls_input = input("🔗 Cole uma ou mais URLs do YouTube separadas por espaço: ")
        print("\n")

        urls = urls_input.split()

        invalid_urls = get_invalid_urls(urls)
        valid_urls = get_valid_urls(urls)

        if invalid_urls:
            print("🚨 As seguintes URLs estão com problemas:\n")
            for url in invalid_urls:
                print(f"⛓️‍💥 {url}\n")

        if valid_urls and ask_for_confirmation():
            for url in valid_urls:
                download_video(url)

        if not ask_to_repeat():
            print("👋 Programa encerrado.")
            break


if __name__ == "__main__":
    main()