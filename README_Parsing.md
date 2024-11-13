# Parsing-logical-expressions
JL, a third representation of syntaxes for propositional logic, other than standard and BMRS.  Its features or merits are followed. First, it does not use parentheses. Second, operators come after their arguments, not between them. Third, the operators have different symbols. 

In JL, variables are written with lowercase letters p, q, etc. The syntax of expressions is defined recursively as usual:

a. Any variable is an expression

b. Any expression followed by N is an expression

c. Any two expressions can be made into another expression by writing A, O, C, or B after them

The semantics of expressions is defined recursively. All expressions mean either + or -; E and F refer to expressions.

a. The meaning of a variable is its meaning

b. The meaning of an expression EN is +  when the meaning of E is - and - when the meaning of E is +

c. The meaning of an expression EFO is + if the meaning of E is + and the meaning of F is +, and - otherwise

d. The meaning of an expression EFC is - if the meaning of E is + or the meaning of F is -, and + otherwise

e. The meaning of an expression EFA is + when the meaning of E is + and the meaning of F is +, and - otherwise

f. The meaning of an expression EFB is + when E and F have the same meaning and - otherwise JL does not use parentheses because it is completely unambiguous. The standard notation ((p → q) → r) translates into JL as pqCrC and (p → (q → r)) translates as pqrCC.

Note：adapted from UCL PLIN0034 coursework.
