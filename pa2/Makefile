# for python binary!
PI=python

default: q1 q2 q3 q4 q5 q6 q8 q9

report:
		pdflatex --output-directory=report/ report/report.tex

permissions:
		chmod u+x p1.py
		chmod u+x p2.py
		chmod u+x p3.py
		chmod u+x p4.py
		chmod u+x p5.py
		chmod u+x p6.py
		chmod u+x p8.py
		chmod u+x p9.py

q1: p1.py
	@echo "======== Executing Q1 ========"
	@echo "    Huffman Algorithm:"
	$(PI) p1.py
	@echo "======== End of Q1 ========"
	@echo

q2: p2.py alice30.txt
	@echo "======== Executing Q2 ========"
	@echo "    Open Hashing:"
	$(PI) p2.py < alice30.txt
	@echo "======== End of Q2 ========"
	@echo

q3:	p3.py alice30.txt
	@echo "======== Executing Q3 ========"
	@echo "    Closed Hashing:"
	$(PI) p3.py < alice30.txt
	@echo "========= End of Q3 ========="
	@echo

q4: p4.py
	@echo "======== Executing Q4 ========"
	@echo "    Binary Search Trees:"
	$(PI) p4.py
	@echo "======== End of Q4 ========"
	@echo

q5: p5.py alice30.txt
	@echo "======== Executing Q5 ========"
	@echo "    Tries:"
	$(PI) p5.py < alice30.txt
	@echo "======== End of Q5 ========"
	@echo

q6: p6.py
	@echo "======== Executing Q6 ========"
	@echo "    Dijkstra's Shortest Path Algorithm"
	$(PI) p6.py
	@echo "======== End of Q6 ========"
	@echo

q8: p8.py
	@echo "======== Executing Q8 ========"
	@echo "    Floyd's Algorithm"
	$(PI) p8.py
	@echo "======== End of Q8 ========"
	@echo

q9: p9.py
	@echo "======== Executing Q9 ========"
	@echo "    Depth-first Search"
	$(PI) p9.py
	@echo "======== End of Q9 ========"
	@echo
