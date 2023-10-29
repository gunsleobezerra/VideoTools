

install_dependencies:
	@echo "Installing dependencies..."
	sudo apt-get install ffmpeg
	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
	rm -rf poetry.lock
	poetry install
	poetry shell

run_teste: poetry.lock 
	@echo "Running..."
	poetry shell
	python3 main.py -v tests/teste.mp4 -d source -as 10 

run_teste_url: poetry.lock 
	@echo "Running..."
	poetry shell
	python3 main.py -url https://www.youtube.com/watch?v=Gnh3dwps_jE -d source -as 10 -tc 10000

generate_help: poetry.lock 
	@echo "Generating help..."
	poetry shell
	python3 main.py --help > help.txt

clean_source: 
	@echo "Cleaning source..."
	rm -rf source/*
