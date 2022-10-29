all: run

run:
	python -m main

ui: 
	python -m main --ui
ai:
	python -m src.GameEngine.GameAI --color=black --diff=1 src/input/in.json src/output/out.json
