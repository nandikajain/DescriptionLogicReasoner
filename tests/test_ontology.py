import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append('../')

from reasoner.knowledgebase.knowledgebase import KnowledgeBase
from sample_kb import *

class TestWithOntology(unittest.TestCase):

    def setUp(self):
        self.kb=KnowledgeBase()

    def test1_kb(self):
        self.kb.load_from_list(test1)
        self.kb.run_sat()
        print("KB is:\n")
        self.kb.print_kb()
        print("Computed models are:\n")
        self.kb.model.debug_print()
        print()
        
    def test2_kb(self):
        self.kb.load_from_list(test2)
        self.kb.run_sat()
        print("KB is:\n")
        self.kb.print_kb()
        print("Computed models are:\n")
        self.kb.model.debug_print()
        print()
        
    def test3_kb(self):
        self.kb.load_from_list(test3)
        self.kb.run_sat()
        print("KB is:\n")
        self.kb.print_kb()
        print("Computed models are:\n")
        self.kb.model.debug_print()
        print()
        
    def test4_kb(self):
        print("=================================================================================================")
        self.kb.load_from_list(test4)
        self.kb.run_sat()
        print("KB is:\n")
        self.kb.print_kb()
        print("-------------------------------------")
        print("Computed models are:\n")
        self.kb.model.debug_print()
        print("=================================================================================================")

    def testBlocking_kb(self):
        print("=================================================================================================")
        self.kb.load_from_list(testBlocking)
        self.kb.run_sat()
        print("KB is:\n")
        self.kb.print_kb()
        print("-------------------------------------")
        print("Computed models are:\n")
        self.kb.model.debug_print()
        print("=================================================================================================")

if __name__=="__main__":
    unittest.main()