#!/usr/bin/env python

import unittest
from ids import validar_id


class TestIds(unittest.TestCase):

    @classmethod
    def setUp(self):
        
        #cada tupla en la lista continene el un id para 
        #testear y si dicho id es valido 

        self.ids = [
             ('ASD123457lop1',False),
             ('pepe234PEP',True),
             ('Python123x',False),
             ('PyThonx123',True),
             ('PyThon123xasdadsadasd',False),
             ('asdasd',False),
             ('PyTh.n123x',False),
             ('',False),
             ('#@!!!@#.;-',False),
        ]

        

    def test_ids(self):
        for id,es_valido in self.ids:
            print(f"{es_valido} \t-> {id}")
            self.assertEqual( validar_id(id), es_valido)


def create_suite(classes, unit_tests_to_run):
    
    suite = unittest.TestSuite()
    unit_tests_to_run_count = len( unit_tests_to_run )

    for _class in classes:
        _object = _class()
        for function_name in dir( _object ):
            if function_name.lower().startswith( "test" ):
                if unit_tests_to_run_count > 0 \
                        and function_name not in unit_tests_to_run:
                    continue
                suite.addTest( _class( function_name ) )
    return suite


def run_tests() -> bool:
    print("> run test")
    runner = unittest.TextTestRunner()
    classes =  [
        TestIds,
    ]

    unit_tests_to_run =  [ ]
    result = runner.run( create_suite( classes, unit_tests_to_run ) )
    return result.wasSuccessful()



if __name__ == "__main__":
    run_tests()

