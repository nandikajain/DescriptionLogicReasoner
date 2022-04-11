import unittest
import sys 
import logging

#logging.basicConfig(level=logging.DEBUG)
sys.path.append('../')

from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion,RoleAssertion,TBoxAxiom,Subsumption, Subproposition
from reasoner.common.constructors import Concept,All,Some,Instance, Role

class TestAxioms(unittest.TestCase):

    def test_and_constructor(self):
        axiom=And(Concept("Man"),Some("hasChild",Concept("Human")))
        self.assertIsInstance(axiom,And)

    def test_or_constructor(self):
        axiom=Or(Concept("Man"),Concept("Woman"))
        self.assertIsInstance(axiom,Or)

    def test_not_constructor(self):
        axiom=Not(Concept("Human"))
        self.assertIsInstance(axiom,Not)

    def test_and_equality(self):
        axiom1=And(Concept("Man"),Concept("Woman"))
        axiom1_terma = axiom1.term_a
        axiom1_termb = axiom1.term_b 
        axiom2=And(Concept("Man"),Concept("Woman"))
        axiom2_terma = axiom2.term_a
        axiom2_termb = axiom2.term_b
        axiom3=And(Concept("Woman"),Concept("Man"))
        axiom3_terma = axiom3.term_a
        axiom3_termb = axiom3.term_b
        self.assertTrue(((axiom1_terma == axiom2_terma) and (axiom1_termb == axiom2_termb)) or ((axiom1_terma == axiom2_termb) and (axiom1_termb == axiom2_terma)))
        self.assertTrue(((axiom1_terma == axiom3_terma) and (axiom1_termb == axiom3_termb)) or ((axiom1_terma == axiom3_termb) and (axiom1_termb == axiom3_terma)))

    def test_and_inequality(self):
        axiom1=And(Concept("Man"),Concept("Human"))
        axiom2=And(Concept("Woman"),Concept("Human"))
        self.assertNotEqual(axiom1,axiom2)

    def test_or_equality(self):
        axiom1=Or(Concept("Man"),Concept("Woman"))
        axiom1_terma = axiom1.term_a
        axiom1_termb = axiom1.term_b        
        axiom2=Or(Concept("Man"),Concept("Woman"))
        axiom2_terma = axiom2.term_a
        axiom2_termb = axiom2.term_b
        axiom3=Or(Concept("Woman"),Concept("Man"))
        axiom3_terma = axiom3.term_a
        axiom3_termb = axiom3.term_b
        self.assertTrue(((axiom1_terma == axiom2_terma) and (axiom1_termb == axiom2_termb)) or ((axiom1_terma == axiom2_termb) and (axiom1_termb == axiom2_terma)))
        self.assertTrue(((axiom1_terma == axiom3_terma) and (axiom1_termb == axiom3_termb)) or ((axiom1_terma == axiom3_termb) and (axiom1_termb == axiom3_terma)))

    def test_or_inequality(self):
        axiom1=Or(Concept("Man"),Concept("Human"))
        axiom2=Or(Concept("Woman"),Concept("Human"))
        self.assertNotEqual(axiom1,axiom2)

    def test_not_equality(self):
        axiom1=Not(Concept("Man"))
        axiom2=Not(Concept("Man"))
        self.assertEqual(axiom2,axiom1)

    def test_not_inequality(self):
        A = Concept("Man")
        B = Not(A)
        axiom1=Not(Concept("Man"))
        axiom2=Not(Concept("Woman"))
        self.assertNotEqual(axiom1,axiom2)
        self.assertTrue(A, Not(B))

    def test_assertion_constructor(self):
        instance=Instance("Aditya")
        _class=Concept("Man")
        axiom=ClassAssertion(_class,instance)
        self.assertEqual(axiom.definitions,_class)
        self.assertEqual(axiom.instance,instance)

    def test_role_assertion(self):
        instance1=Instance("Aditya")
        instance2=Instance("Icarus")
        axiom=RoleAssertion("hasComputer",instance1,instance2)
        self.assertEqual(axiom.role,"hasComputer")
        self.assertEqual(axiom.instance1,instance1)
        self.assertEqual(axiom.instance2,instance2)

    def test_tbox_wrapper(self):
        axiom=And(Concept("Man"),Concept("Machine"))
        wrapper=TBoxAxiom(axiom)
        self.assertEqual(axiom,wrapper.axiom)

    def test_subsumption_axiom(self):
        axiom1=Concept("Man")
        axiom2=Concept("Human")
        axiom3 = Concept("Man")
        axiom=Subsumption(axiom1,axiom2)
        axiom_ = Subsumption(axiom2,axiom3)
        self.assertTrue(Subsumption(axiom1, axiom3))
        self.assertEqual(axiom1,axiom.axiom1)
        self.assertEqual(axiom2,axiom.axiom2)

    def test_subproposition_axiom(self):
        subprop1 = "hasSon"
        subprop2 = "hasChild"
        subprop3 = "hasHuman"
        axiom = Subproposition(subprop1, subprop2)
        axiom_ = Subproposition(subprop2, subprop3)
        self.assertTrue(Subproposition(subprop1, subprop3))
        
if __name__=="__main__":
    unittest.main()
