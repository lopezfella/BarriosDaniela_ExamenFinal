solar.png: monthrg.dat fourier.py
	python fourier.py

%.dat : a.out
	./a.out 
