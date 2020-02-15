.DEFAULT_GOAL := test


.PHONY: unit
unit:
	mkdir Images
	touch Images/file1.bin
	touch Images/file2.tar
	touch Images/file3.gz
	touch Images/file4.pdf
	python3 -m pytest --verbose
	rm -r -f Images/

#python -m pytest tests/ --verbose
#rm -r -f /tests/Images