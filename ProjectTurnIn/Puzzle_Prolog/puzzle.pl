example(A).
puzzle(A,B,C,D,E):-append(TEMP2,E,A),append(TEMP1,D,TEMP2),append(B,C,TEMP1),addSame(B,C,D,E).
addSame(A,B,C,D):- val(A,X),val(B,X),val(C,X),val(D,X).
val([H|T],X):- val(T,Y), X is H + Y.
val([],Y):- Y is 0.
