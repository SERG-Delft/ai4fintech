AFR_SRC = ../
TARGET_FOLDER = out
TARGET_DOC=out/afr-2020-2024
TARGET_PDF=$(TARGET_DOC).pdf
TARGET_QMD=$(TARGET_DOC).qmd

top:
	$(MAKE) install root $(TARGET_PDF)

%.pdf: %.qmd
	quarto render $< --to pdf	

root:
	python report.py > $(TARGET_QMD)
	cat $(TARGET_QMD)

install:
	mkdir -p $(TARGET_FOLDER)
	cp preamble.tex $(TARGET_FOLDER)
	cp -r $(AFR_SRC)img .
	cp -r $(AFR_SRC)/img $(TARGET_FOLDER)

# copy paste into shell
setup:
	virtualenv venv
	source venv/bin/activate
	pip install pyyaml