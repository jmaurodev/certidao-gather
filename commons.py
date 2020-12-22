import requests
from tqdm import tqdm
from dotenv import load_dotenv
from threading import Thread
from datetime import date
import os


def _load_env_vars(path=None):
    load_dotenv(path)
    env_vars = {
        'URL_TCU': os.getenv('URL_TCU'),
        'URL_SIAFI': os.getenv('URL_SIAFI'),
        'URL_SICAF': os.getenv('URL_SICAF'),
        'USERNAME': os.getenv('USERNAME'),
        'PASSWORD': os.getenv('PASSWORD')
    }
    return env_vars


def tcu(cnpj, app_type='pdf'):
    response = requests.get(
        env_vars['URL_TCU'] + cnpj,
        verify=False,
        stream=True,
        headers={
            'Accept': 'application/' + app_type
        }
    )
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    filename = 'TCU_' + cnpj + '_' + str(date.today()) + '.' + app_type
    with open(filename, 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
        progress_bar.close()


def siafi():
    response = requests.get(
        env_vars['URL_SIAFI'] + cnpj,
        verify=False,
        stream=True,
        headers={
            'Accept': 'application/' + app_type
        }
    )


def _promt_user(cnpj):
    while True:
        buffer = input('Digite o CNPJ da empresa (apenas números): ')
        buffer = buffer.replace('.', '')
        buffer = buffer.replace('/', '')
        buffer = buffer.replace('-', '')
        if buffer.isnumeric() and len(buffer) == 14:
            cnpj.append(buffer)
        if buffer == '':
            break
    return cnpj


if __name__ == '__main__':
    env_vars = _load_env_vars()
    cnpj = list()
    _promt_user(cnpj)
    for c in cnpj:
        t = Thread(
            target=tcu,
            args=(c,),
        )
        t.start()
