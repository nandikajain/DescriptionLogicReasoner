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

test1= [ ABoxAxiom(ClassAssertion(Concept("Orphan"), Instance("harryPotter"))),
ABoxAxiom(RoleAssertion(Role("hasParent"), Instance("harryPotter"), Instance("jamesPotter"))),
TBoxAxiom(Subsumption(Concept("Orphan"), Some("hasParent", Concept("Human")))),
TBoxAxiom(Subsumption(Concept("Orphan"), And(Concept("Human"),All("hasParent", Not(Concept("Alive")))))),
ABoxAxiom(ClassAssertion(Not(Concept("Alive")),Instance("jamesPotter")))
]

test2=[ABoxAxiom(ClassAssertion(Concept("Bird"),Instance("tweety"))),
TBoxAxiom(Subsumption(Concept("Human"), Some("hasParent", Concept("Human")))),
ABoxAxiom(ClassAssertion(Not(Concept("Human")),Instance("tweety")) ),
TBoxAxiom(Subsumption(Concept("Bird"), Some("hasParent", Concept("Bird")))),
TBoxAxiom(Subsumption(Concept("Bird"), Not(Concept("Human")))),
TBoxAxiom(Subsumption(Concept("Human"), Not(Concept("Bird")))) 
]

test3=[
TBoxAxiom(Subsumption(Concept("Bird"), Concept("Flies"))),
TBoxAxiom(Subsumption(Concept("Penguin"), Concept("Bird"))),
TBoxAxiom(Subsumption(Concept("Penguin"), Not(Concept("Flies")))),
TBoxAxiom(Subsumption(Concept("Flies"), Not(Concept("Penguin")))),
ABoxAxiom(ClassAssertion(Concept("Penguin"),Instance("tweety")))]

test4 = [
ABoxAxiom(ClassAssertion(Concept("Student"), Instance("Gitansh-Jishnu-Nandika"))),
ABoxAxiom(ClassAssertion(Not(Concept("Eager")), Instance("Gitansh-Jishnu-Nandika"))),
TBoxAxiom(Subsumption(Concept("Student"), Some("Attends", Concept("Lecture")))),
TBoxAxiom(Subsumption(Concept("Lecture"), Some("AttendedBy", And(Concept("Lecture"), Concept("Lecture")))))]

testBlocking=[ABoxAxiom(ClassAssertion(Concept("Bird"),Instance("tweety"))),
TBoxAxiom(Subsumption(Concept("Human"), Some("hasParent", Concept("Human")))),
ABoxAxiom(ClassAssertion(Not(Concept("Human")),Instance("tweety")) )
]
