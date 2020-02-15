.DEFAULT_GOAL := test


.PHONY: unit
unit:
	mkdir tests/Images
	touch tests/Images/file1.bin
	touch tests/Images/file2.tar
	touch tests/Images/file3.gz
	touch tests/Images/file4.pdf
	python3 -m pytest tests/ --verbose
	rm -r -f tests/Images/

#python -m pytest tests/ --verbose
#rm -r -f /tests/Images