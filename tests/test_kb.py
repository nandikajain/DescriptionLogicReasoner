import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append('../')

from reasoner.knowledgebase.knowledgebase import NodeSet,KnowledgeBase
from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion
from reasoner.common.constructors import Concept,Some,All,Instance

class TestKB(unittest.TestCase):

    def setUp(self):
        self.KB=KnowledgeBase()
        self.axioms=[
            ClassAssertion(And(Concept("Man"),Concept("Human")),Instance("Aditya")),
            ClassAssertion(Some("owns",Concept("Conputer")),Instance("Aditya"))
        ]

    def test_axiom_insertion(self):
        self.KB.add_axioms(self.axioms)
        #print(f"{self.KB.abox.axiom_set},{self.KB.tbox.axiom_set}")
        self.assertTrue(self.KB.contains(self.axioms[0]))
        self.assertTrue(self.KB.contains(self.axioms[1]))

if __name__=="__main__":
    unittest.main()
