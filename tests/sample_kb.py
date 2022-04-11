import sys 
sys.path.append('../')

from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion,ABoxAxiom,RoleAssertion,TBoxAxiom,Subsumption
from reasoner.common.constructors import Concept,All,Some,Instance, Role


little_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))]

small_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(Concept("Machine"),Instance("Icarus"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological")))]

simple_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(Concept("Machine"),Instance("Icarus"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological"))),
TBoxAxiom(Subsumption(Concept("Machine"),Not(Concept("Man")))),
TBoxAxiom(Subsumption(Concept("Biological"),Concept("Man")))]

inconsistent_test_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(And(Concept("Machine"),Concept("Man")),Instance("Adam"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological"))),
TBoxAxiom(Subsumption(Concept("Machine"),Not(Concept("Man")))),
TBoxAxiom(Subsumption(Concept("Biological"),Concept("Man")))]

yet_another_kb=[
ABoxAxiom(ClassAssertion(Concept("Man"),Instance("Aditya"))),
ABoxAxiom(ClassAssertion(And(Concept("Machine"),Concept("Man")),Instance("Adam"))),
TBoxAxiom(Subsumption(Concept("Man"),Concept("Biological"))),
TBoxAxiom(Subsumption(Concept("Biological"),Concept("Man"))),
TBoxAxiom(Subsumption(And(Concept("Machine"),Concept("Man")),Concept("Augmented")))]

test3=[
TBoxAxiom(Subsumption(Concept("Bird"), Concept("Flies"))),
TBoxAxiom(Subsumption(Concept("Penguin"), Concept("Bird"))),
TBoxAxiom(Subsumption(Concept("Penguin"), Not(Concept("Flies")))),
TBoxAxiom(Subsumption(Concept("Flies"), Not(Concept("Penguin")))),
ABoxAxiom(ClassAssertion(Concept("Penguin"),Instance("tweety")))
]


test2=[ABoxAxiom(ClassAssertion(Concept("Bird"),Instance("tweety"))),
TBoxAxiom(Subsumption(Concept("Human"), Some("hasParent", Concept("Human")))),
ABoxAxiom(ClassAssertion(Concept("Human"),Instance("tweety")) )
]

test1= [
ABoxAxiom(ClassAssertion(Concept("Orphan"),Instance("harrypotter"))),
TBoxAxiom(Subsumption(Concept("Human"), Some("hasParent", Concept("Human")))),
ABoxAxiom(RoleAssertion(Role("hasParent"), Instance("harryPotter"), Instance("jamesPotter")))]

sample= [ABoxAxiom(RoleAssertion("hasParent", Instance("harryPotter"), Instance("jamesPotter")))]