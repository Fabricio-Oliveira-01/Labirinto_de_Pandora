PYTHON = python3

JUNK = __pycache__ *.pyc labirinto.txt

all: run

map:
	@echo "Gerando um novo labirinto..."
	$(PYTHON) mazeGenerator.py

run:
	@echo "Iniciando o jogo..."
	$(PYTHON) main.py


clean:
	@echo "Limpando arquivos temporários..."
	rm -rf $(JUNK)
	rm -rf */__pycache__


.PHONY: all map run clean