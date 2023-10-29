

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
	python3 main.py tests/teste.mp4 source
