# Copyright (c) 2018 Open Steno Project
# See LICENSE.txt for details.
# Eclipse (.dix) handler tests
# written by Marnanel Thurman <marnanel@thurman.org.uk>

from pathlib import Path

from plover_build_utils.testing import dictionary_test

from plover_eclipse_dictionary import EclipseDictionary


@dictionary_test
class TestEclipseDictionary:

    DICT_CLASS = EclipseDictionary
    DICT_EXTENSION = 'dix'
    DICT_REGISTERED = True
    DICT_LOAD_TESTS = (
        lambda: (
            'eclipse-test.dix',
            r'''
            'U/SURP': 'usurp',
            'U/SKWRA*EU/AES': "you Jay's",
            'U/SPHAOEPB': 'you mean so',
            'U/SRA*E': 'you have a',
            'U/SRA*U': 'you have a',
            'U/STAEUGS': 'eustachian',
            'U/STRAOEUF/TO': 'you strive to',
            'U/SURP': 'usurp',
            'U/TKPWAOEUGS': 'you guys',
            'U/TKROUS/KWREU': 'you drowsy',
            'UD': "you'd",
            'UD/*ER': 'udder',
            'UD/EL': 'Udell',
            'UD/ER': 'udder',
            'UD/ERS': 'udders',
            'UZ/PWEBG/STAPB': 'Uzbekistan',
            '''
        ),
    )
    DICT_SAMPLE = 'eclipse-test.dix'

    @staticmethod
    def make_dict(contents):
        path = Path(__file__).parent / contents
        return path.read_bytes()
