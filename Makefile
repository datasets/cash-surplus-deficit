version = "0.1.0"

DATADIR=data
SCRIPTDIR=scripts

data:
	pip install -r $(SCRIPTDIR)/requirements.txt
	python $(SCRIPTDIR)/process.py

clean:
	rm -rf $(SCRIPTDIR)/cache

.PHONY: all data clean
