all:note answers
note:
	xelatex note.tex
	xelatex note.tex
answers:
	xelatex answers.tex
	xelatex answers.tex
clean:
	rm *.out *.log *.pdf *.bbl *.aux *.blg