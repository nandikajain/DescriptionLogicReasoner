import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append('../')

from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion,RoleAssertion,TBoxAxiom,Subsumption
from reasoner.common.constructors import Concept,All,Some,Instance
from reasoner.reasoning.tableau import *

class TestTableau(unittest.TestCase):

    def setUp(self):
        _axiom=Some("hasParent",And(Concept("Man"),Concept("Human")))
        self.pre_graph=get_models({},_axiom,"Aditya")[0]

    def test_simple_and(self):
        axiom=And(And(Concept("Man"),Concept("Living")),And(Concept("Machine"),Concept("Terminator")))
        models=get_models({},axiom,"Aditya")
        self.assertTrue(is_model_consistent(models))

    def test_unsat_and(self):
        axiom=And(And(Concept("Man"),Concept("Living")),And(Not(Concept("Man")),Concept("Terminator")))
        models=get_models({},axiom,"Aditya")
        self.assertFalse(is_model_consistent(models))

    def test_simple_or(self):
        axiom=Or(Concept("Man"),Concept("Terminator"))
        models=get_models({},axiom,"Aditya")
        self.assertTrue(is_model_consistent(models))

    def test_complex_and_or(self):
        axiom=Or(And(Concept("Man"),Not(Concept("Man"))),And(Concept("Machine"),Or(Not(Concept("Machine")),Concept("Machine"))))
        models=get_models({},axiom,"Aditya")
        self.assertTrue(is_model_consistent(models))

    def test_simple_some(self):
        axiom=Some("hasParent",And(Concept("Man"),Concept("Human")))
        models=get_models({},axiom,"Aditya")
        self.assertTrue(is_model_consistent(models))

    def test_simple_all(self):
        axiom=All("hasParent",And(Concept("Engineer"),Concept("Graduate")))
        models=get_models(self.pre_graph,axiom,"Aditya")
        #print(models)


if __name__=="__main__":
    unittest.main()
