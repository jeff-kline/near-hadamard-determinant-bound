SHELL := /bin/sh
PYTHON ?= $(RESEARCH_PYTHON)
PDFLATEX ?= pdflatex
export SOURCE_DATE_EPOCH := 1794700800
export FORCE_SOURCE_DATE := 1

.PHONY: paper check verify infimum rebuild require-python
require-python:
	@test -n "$(PYTHON)" || { echo 'Set PYTHON to an absolute virtual-environment interpreter path.'; exit 1; }
	@case "$(PYTHON)" in /*) ;; *) echo 'PYTHON must be an absolute path.'; exit 1;; esac
	@"$(PYTHON)" -c 'import sys; assert sys.prefix != sys.base_prefix'

# Four passes from a clean extraction; no inherited auxiliaries are required.
paper:
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	@! grep -E 'Warning:|Overfull|Underfull|undefined references|undefined citations' paper/main.log

check: require-python
	"$(PYTHON)" scripts/check_paper.py

# Exact finite certificates for the 0.8 bound (a few minutes in total).
# Each script rewrites its certificate next to itself; compare with evidence/.
verify: require-python
	cd scripts && "$(PYTHON)" finite_check.py
	cd scripts && "$(PYTHON)" class4_check.py
	cd scripts && "$(PYTHON)" class4_check.py --finite
	cd scripts && "$(PYTHON)" finite_audit.py
	cd scripts && "$(PYTHON)" class4_examiner_proof.py
	"$(PYTHON)" scripts/compare_certificates.py

# Ball-arithmetic certificate for the minima: 666 fields, about one CPU-minute.
infimum: require-python
	cd scripts && "$(PYTHON)" infimum_check.py
	"$(PYTHON)" scripts/compare_certificates.py infimum

# Independent rebuild of the matrices (no FLINT) at q = 29, 37, 41, 49; seconds.
rebuild: require-python
	cd scripts && for a in "4 29 29 1" "56 29 29 1" "4 37 37 1" "56 37 37 1" "4 41 41 1" "56 41 41 1" "4 49 7 2" "56 49 7 2"; do \
	  "$(PYTHON)" independent_rebuild.py $$a; done
