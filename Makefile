
deploy:
	rm -Rf dist/*
	python3 setup.py sdist bdist_wheel
	/home/app/.pyenv/shims/python -m twine upload dist/*

