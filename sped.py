import os
import requests
from dotenv import load_dotenv


def _load_env_vars(path=None):
    load_dotenv(path)
    env_vars = {
        'HOST': os.getenv('HOST'),
        'USERNAME': os.getenv('USERNAME'),
        'PASSWORD': os.getenv('PASSWORD'),
        'POSTO': os.getenv('POSTO'),
        'NOME': os.getenv('NOME'),
        'FUNCAO': os.getenv('FUNCAO')
    }
    return env_vars


def load_text(filename='template.html'):
    texto = open(filename).read()
    texto = texto.replace('$GDH_NC', '011200JAN21')
    texto = texto.replace('$ATENDER', 'Teste de SPED')
    texto = texto.replace('$UG', '160296')
    texto = texto.replace('$PI', 'I3DAFUNADOM')
    texto = texto.replace('$NC', '123456')
    texto = texto.replace('$VALOR', '100.000,00')
    texto = texto.replace('$OM', '20 CIA COM PQDT')
    return texto


def login(host, username, password):
    session = requests.Session()
    session.get(
        'http://%s/sped/administracao/sessao/eb/logon.jsp' % (host)
    )
    r = session.post(
        'http://%s/sped/administracao/sessao/eb/j_security_check' % (host),
        data={
            'j_username': username,
            'j_password': password
        }
    )
    r = session.get(
        'http://%s/sped/protocolo/redacao/RedigirAction.do?method=novo' % (
            host),
        data={
            'method': 'novo'
        }
    )
    r = session.post(
        'http://%s/sped/protocolo/redacao/eb/RoteadorRedigirAction.do?method=roteadorEdicao' % (
            host),
        data={
            'tipoVinculo': '',
            'numero': 'auto',
            'campo-nup': 'nup-auto',
            'local': env_vars['LOCAL'],
            'data': 'auto',
            'campoDo': '1',
            'doExibicao': 'Chefe do Centro de Controle Orcamentario',
            'idUsuarioDO': '262',
            'campoAo': '1',
            'idAos': '',
            'idUsuarioExterno': '',
            'ao': '',
            'diex': 'diex',
            'filtro': '',
            'filtro': '',
            'usuariosDisponiveisDO': '262',
            'filtro': '',
            'codomExt': '',
            'assunto': 'ASSUNTO',
            'anexo': '',
            'texto': load_text(),
            'usuarioDisponiveis': '-1',
            'postoImpedimento': '',
            'nomeImpedimento': '',
            'funcaoImpedimento': '',
            'posto': env_vars['POSTO'],
            'nome': env_vars['NOME'],
            'funcao': env_vars['FUNCAO'],
            'usuariosDisponiveis': 'null',
            'porOrdemDo': '',
            'idDocVinculador': 'null',
            'descricaoVinculosReferencia': '',
            'descricaoVinculosAnexo': '',
            'descricaoAnexoExterno': 'fileName##||flAnexo##||btAdicionar##Anexar documento local'
        }
    )
    pass


if __name__ == '__main__':
    env_vars = _load_env_vars()
    login(
        env_vars['HOST'],
        env_vars['USERNAME'],
        env_vars['PASSWORD']
    )
