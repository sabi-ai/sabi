
deploy:
	rm -Rf dist/*
	python3 setup.py sdist bdist_wheel
	python -m twine upload dist/*

