import sys 
sys.path.append('../')

from reasoner.knowledgebase.axioms import And,Or,Not,ClassAssertion,ABoxAxiom,RoleAssertion,TBoxAxiom,Subsumption
from reasoner.common.constructors import Concept,All,Some,Instance


test1= [
ABoxAxiom(ClassAssertion(Concept("Orphan"),Instance("harrypotter"))),
TBoxAxiom(Subsumption(Concept("Human"), Some("hasParent", Concept("Human")))),
ABoxAxiom(RoleAssertion(Role("hasParent", Concept("Human")), Instance("harryPotter"), Instance("jamesPotter")))]

test2=[ABoxAxiom(ClassAssertion(Concept("Bird"),Instance("tweety"))),
TBoxAxiom(Subsumption(Concept("Human"), Some("hasParent", Concept("Human")))),
ABoxAxiom(ClassAssertion(Concept("Human"),Instance("tweety")) )
]


test3=[
TBoxAxiom(Subsumption(Concept("Bird"), Concept("Flies"))),
TBoxAxiom(Subsumption(Concept("Penguin"), Concept("Bird"))),
TBoxAxiom(Subsumption(Concept("Penguin"), Not(Concept("Flies")))),
TBoxAxiom(Subsumption(Concept("Flies"), Not(Concept("Penguin")))),
ABoxAxiom(ClassAssertion(Concept("Penguin"),Instance("tweety")))]

test4 = [
ABoxAxiom(ClassAssertion(Concept("Student"),Instance("Gitansh-Jishnu-Nandika"))),
ABoxAxiom(ClassAssertion(Not(Concept("Student")),Instance("Gitansh-Jishnu-Nandika"))),    
  
]


