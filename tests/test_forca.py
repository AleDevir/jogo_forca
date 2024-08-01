# pylint: disable=line-too-long
'''
Testes forca.py
pytest tests/test_forca.py -vv
'''

from unittest.mock import patch
from unittest import TestCase
from src.forca import forca


class Test(TestCase):
    '''
    Classe de teste para inputs.
    '''
    ################################################
                # TESTES FLUXO PRINCIPAL #
    ################################################

    @patch('src.forca.escolher_uma_palavra_aleatoriamente')
    @patch('src.forca.obter_letra')
    def test_main_ganhou(self, get_input, escolher_uma_palavra_aleatoriamente_mok):
        '''
        Teste do fluxo principal onde o jogador ganha.  
        python -m unittest -v tests.test_forca.Test.test_main_ganhou -v
        '''
        escolher_uma_palavra_aleatoriamente_mok.return_value = 'abc'
        get_input.side_effect = ['D', 'a', 'S', 'F', 'b', 'c']
        forca()

    @patch('src.forca.escolher_uma_palavra_aleatoriamente')
    @patch('src.forca.obter_letra')
    def test_main_perdeu(self, get_input, escolher_uma_palavra_aleatoriamente_mok):
        '''
        Teste do fluxo principal onde o jogador perde. 
        python -m unittest -v tests.test_forca.Test.test_main_perdeu -v
        '''
        escolher_uma_palavra_aleatoriamente_mok.return_value = 'abc'
        get_input.side_effect = ['D', 'Q', 'S', 'F', 'U', 'T']
        forca()
