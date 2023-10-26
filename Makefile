# Copyright (c) 2023 MDSANIMA

# This is Makefile helper for test, build, install, and more.


.PHONY: test build

all: test build

test:
	@echo "\033[1;30mNo test right now!\033[0m"
	@python -c "from mdsanima_dev.colors import get_complex_color; get_complex_color('TESTING...', 198)"

build:
	python -m build

install:
	pip install .
