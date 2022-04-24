# Description Logic Reasoner

A description logic reasoner made by extending the naive tableau implementation that can be found [here](https://github.com/dityas/Athene). Made as a part of Semantic Web course offered at IIITD (CSE632).
It takes in the ALC axioms and outputs whether the axiom is consistent or not.

## Running Instructions
1. Clone this repository using the command: `git clone https://github.com/nandikajain/DescriptionLogicReasoner.git`
2. cd into the directory by ```cd DescriptionLogicReasoner```.
3. cd to tests directory by ```cd tests``` and add the ALC axioms of your choice in sample_kb.py and include the tests in test_ontology.py.
4. Run the tests by ```python test_ontology.py``` to get if the ALC axioms are consistent or not.

## Functionalities added
- We have extended the codebase’s implementation to role assertion. Whenever there is a role between a and b, an edge is created between them which is given the role label [reasoning/tableau.py, reasoning/nnf.py, knowledgebase/axioms.py, knowledgebase/model.py, common/constructors.py].
- We updated the Role constructor and and Role Assertion axioms in order to fulfill their functionalities. Then we made adjustments to the axiom several functions that handle the axiom resolution. In tableau.py we made necessary changes so that the edge between
the nodes are properly added.
- Corrected incorrectly written tests in test_axioms.py.
- We also added subproposition (subproperty) rules and relevant test cases for them.

### Implementing Blocking technique
We extended our implementation to the blocking technique in the tableau. Only a no_name node would be the one which would block the tableau, since we are adding
new nodes with no_name Node, and in order to block the tableau to go till infinity, we block the Nodes with the name no_name. We checked that the node should be a node
with name as no_name{x} and that this node should be a subset of the previous nodes in the model present.
A node with a label x is blocked by a node with label y if:<br>
> <i>x is a variable but not an individual</i> <br>
> <i>y is an ancestor of x, and L(x) ⊆ L(y)</i><br>
> <i>or an ancestor of x is blocked</i>



