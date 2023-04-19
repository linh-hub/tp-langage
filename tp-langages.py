#!/usr/bin/env python3
"""
Developpez votre projet de TP automates finis dans ce fichier.
"""

from contextfree import StackAutomaton, EPSILON, Grammar

def is_deterministic(a):
        
        for(source1,letter1,head1,push1,target1) in a.get_transitions():
            for(source2,letter2,head2,push2,target2) in a.get_transitions():
                if (source1 == source2 and target1 == target2):
                    if (letter1 == letter2 and head1 == head2):
                        return False
        return True

def take_transition(a,s, current_state,current_stack,position):
    for(source,letter,head,push,target) in a.get_transitions():
        source == current_state
        letter == s[position]
        head == current_stack
        push == push 
    
def execute(a,s):
    if ( a == False):
        print("ERROR")
    current_state = a.initialstate
    current_stack = a.initialstack
    position = 0
    while(current_state != a.get_final() and s[position] != "%"):
        take_transition(a,s,current_state,current_stack,position)
    for (source,letter,head,push,target) in self.transitionList:    
        current_state = a.target
        current_stack = 
    position +=1
    return 

if __name__ == "__main__": # If the module is run from command line, test it
    """
    a=StackAutomaton("aut")
    a.add_transition("0","a","Z0",["A","Z0"],"1")
    a.add_transition("1","b","A",[],"0")
    a.set_initialstate("0")
    a.set_initialstack("Z0")
    a.make_final("1")
    a.to_txtfile("./tests/automaton0.pa")
    
    
    
    
    
    a1.make_copy(a)
    print(a1)
    
    g1=Grammar("gr1")
    g1.from_txtfile("./tests/grammar1.gr")
    print(g1)
    
   
    
    g3=Grammar("palidromes")
    g3.add_rule("S",["a"])
    g3.add_rule("S",["%"])
    g3.add_rule("S",["b"])
    g3.add_rule("S",["T"])
    g3.add_rule("T",["Xa","T","Xa"])
    g3.add_rule("T",["Xb","T","Xb"])
    g3.add_rule("T",["S"])
    g3.add_rule("T",["%"])
    g3.add_rule("Xa",["a"])
    g3.add_rule("Xb",["b"])
    g3.set_axiom("S")
    g3.to_txtfile("./tests/grammar_palindromes.ap")
    #print(g3)
    
    
    a1=StackAutomaton("palindromes")
    a1.add_transition("q0","%","S",["T"],"q0")
    a1.add_transition("q0","%","T",["S"],"q0")
    a1.add_transition("q0","a","Xa",[],"q0")
    a1.add_transition("q0","%","T",[],"q0")
    a1.add_transition("q0","a","Xa",[],"q0")
    a1.set_initialstate("q0")
    a1.set_initialstack("S")
    a1.make_final("q0")
    a1.to_txtfile("./tests/automaton_palindromes.ap")
    print(a1)
    
    
    g4=Grammar("anbn")
    g4.add_rule("A",["aZ0b"])
    g4.add_rule("Z0",["%"])
    g4.add_rule("Z0",["A"])
    g4.set_axiom("A")
    g4.to_txtfile("./tests/automaton anbn.gr")
    print(g4)
   
    
    
    a2=StackAutomaton("anbn")
    a2.add_transition("q0","a","Z0",["A","Z0"],"q1")
    a2.add_transition("q1","a","A",["A","A"],"q1")
    a2.add_transition("q1","b","A",["%"],"q2")
    a2.add_transition("q2","b","A",["%"],"q2")
    a2.add_transition("q2","%","Z0",["%"],"q3")
    a2.set_initialstate("q0")
    a2.set_initialstack("Z0")
    a2.make_final("q3")
    a2.to_txtfile("./tests/automaton anbn.ap")
    print(a2)
    print(a2.get_transitions())
    
    
    a1=StackAutomaton("aut1")
    a1.from_txtfile("./tests/automaton1.pa")
    print(a1.get_alphabet())
    print(a1.get_stackalphabet())
    print(a1.get_states())
    print(a1.get_transitions())


   

    a1=StackAutomaton("palindromes")
    a1.add_transition("q0","%","S",["T"],"q0")
    a1.add_transition("q0","%","T",["S"],"q0")
    a1.add_transition("q0","a","Xa",[],"q0")
    a1.add_transition("q0","%","T",[],"q0")
    a1.add_transition("q0","a","Xa",[],"q0")
    a1.set_initialstate("q0")
    a1.set_initialstack("S")
    a1.make_final("q0")
    
                
    
    a2 = is_deterministic(a1)
    print(a2)     
      """   
    a2=StackAutomaton("anbn")
    a2.add_transition("q0","a","Z0",["A","Z0"],"q1")
    a2.add_transition("q1","a","A",["A","A"],"q1")
    a2.add_transition("q1","b","A",["%"],"q2")
    a2.add_transition("q2","b","A",["%"],"q2")
    a2.add_transition("q2","%","Z0",["%"],"q3")
    a2.set_initialstate("q0")
    a2.set_initialstack("Z0")
    a2.make_final("q3")
    a3 = execute(a2,"ab")
    print(a3)
    