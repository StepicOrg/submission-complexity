SHELL := /bin/bash
COMPLEXITY_PATH = '$(shell pwd)'
GRAMMARS_PATH = '$(COMPLEXITY_PATH)/complexity/grammars'
PARSERS_PATH = '$(COMPLEXITY_PATH)/complexity/parsers'

generate-cpp:
	antlr4 -o $(PARSERS_PATH)/cpp -package . -listener -Dlanguage=Python3 -no-visitor -lib $(GRAMMARS_PATH) \
	       $(GRAMMARS_PATH)/CPP14.g4

optimize:
	python3 scripts/optimize.py -p $(PARSERS_PATH)

generate: generate-cpp optimize

install-antlr:
	cd /usr/local/lib
	curl -O http://www.antlr.org/download/antlr-4.7-complete.jar
	export CLASSPATH=".:/usr/local/lib/antlr-4.7-complete.jar:$$CLASSPATH"
	alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7-complete.jar:$$CLASSPATH" org.antlr.v4.Tool'
	alias grun='java org.antlr.v4.gui.TestRig'
