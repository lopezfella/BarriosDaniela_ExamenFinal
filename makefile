solar.png: monthrg.dat valores.txt fourier.py metro.py
	python fourier.py metro.py

%.dat : a.out
	./a.out 
