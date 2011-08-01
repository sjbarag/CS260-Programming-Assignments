# for python binary!
PI=python

# set the following to TRUE if the .py files need to be u+x - they
# don't on my system (ArchLinux), so I'm trying to avoid elevating priveleges
# as much as possible.
#SETEXEC=TRUE
#SETEXEC=FALSE

default: q1 q2 q3 q4 q5 q6 q7 q8 q9 q10 q11 q12

permissions:
		chmod u+x p1-1.py p1-2.py
		chmod u+x p2-1.py p2-2.py
		chmod u+x p3.py
		chmod u+x p4-1.py p4-2.py
		chmod u+x p5-1.py p5-2.py p5-3.py
		chmod u+x p6-1.py p6-2.py
		chmod u+x p7.py
		chmod u+x p8.py
		chmod u+x p9-1.py p9-2.py
		chmod u+x p10.py
		chmod u+x p11.py
		chmod u+x p12.py

q1: p1-1.py p1-2.py
	@echo "======== Executing Q1 ========"
	@echo "    List as an array:"
	$(PI) p1-1.py
	@echo
	@echo "    List as a linked-list:"
	$(PI) p1-2.py
	@echo "======== End of Q1 ========"
	@echo

q2: p2-1.py p2-2.py
	@echo "======== Executing Q2 ========"
	@echo "    Stack as an array:"
	$(PI) p2-1.py
	@echo
	@echo "    Stack as a linked-list:"
	$(PI) p2-2.py
	@echo "======== End of Q2 ========"
	@echo

q3:	p3.py
	@echo "======== Executing Q3 ========"
	@echo "    Queue:"
	$(PI) p3.py
	@echo "========= End of Q3 ========="
	@echo

q4: p4-1.py p4-2.py
	@echo "======== Executing Q4 ========"
	@echo "    Tree as a list of children:"
	$(PI) p4-1.py
	@echo
	@echo "    Tree as leftmost child/right sibling:"
	$(PI) p4-2.py
	@echo "======== End of Q4 ========"
	@echo

q5: p5-1.py p5-2.py p5-3.py
	@echo "======== Executing Q5 ========"
	@echo "    Timing of Python's list class:"
	$(PI) p5-1.py
	@echo
	@echo "    Timing of my list-as-array class:"
	$(PI) p5-2.py
	@echo
	@echo "    Timing of my list-as-pointers class:"
	$(PI) p5-3.py
	@echo "======== End of Q5 ========"
	@echo

q6: p6-1.py p6-2.py
	@echo "======== Executing Q6 ========"
	@echo "    Timing of trees as list of children:"
	$(PI) p6-1.py
	@echo
	@echo "    Timing of trees as leftmost child/right sibling:"
	$(PI) p6-2.py
	@echo "======== End of Q6 ========"
	@echo

q7: p7.py
	@echo "======== Executing Q7 ========"
	@echo "    Merging of n lists. (in this case: 3):"
	$(PI) p7.py
	@echo "======== End of Q7 ========"
	@echo

q8: p8.py
	@echo "======== Executing Q8 ========"
	@echo "    Concatenation of a list of lists:"
	$(PI) p8.py
	@echo "======== End of Q8 ========"
	@echo

q9: p9-1.py p9-2.py
	@echo "======== Executing Q9 ========"
	@echo "    Tree height for list of children:"
	$(PI) p9-1.py
	@echo
	@echo "    Tree height for leftmost child/right sibling:"
	$(PI) p9-2.py
	@echo "======== End of Q9 ========"
	@echo

q10: p10.py
	@echo "======== Executing Q10 ========"
	@echo "    Level printing of a tree:"
	$(PI) p10.py
	@echo "======== End of Q10 ========"
	@echo

q11: p11.py
	@echo "======== Executing Q11 ========"
	@echo "    Order conversions:"
	$(PI) p11.py
	@echo "======== End of Q11 ========"
	@echo

q12: p12.py
	@echo "======== Executing Q12 ========"
	@echo "    Pre/post-fix expressions evaluation:"
	$(PI) p12.py
	@echo "======== End of Q12 ========"	
