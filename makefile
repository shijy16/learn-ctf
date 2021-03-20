all:note answers writeup
note:
	xelatex note.tex
	xelatex note.tex
answers:
	xelatex answers.tex
	xelatex answers.tex
writeup:
	xelatex writeup.tex
	xelatex writeup.tex
clean:
	rm *.out *.log *.pdf *.bbl *.aux *.blg