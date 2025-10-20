.PHONY: help setup test dash zip_all zip_folders zip_target

help:
	@echo "Available targets:"
	@echo "  setup   - create venv, install dev deps"
	@echo "  test    - run pytest"
	@echo "  dash    - run the example dashboard script"

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements-dev.txt

test:
	pytest -q

dash:
	python tools/hello_core.py


filetree: ## Emit an abbreviated project tree
	@mkdir -p meta
	@echo "OughtCore/" > meta/file_structure.txt
	@tree --noreport --charset utf-8 -F -I '.git|.venv|.pytest_cache|node_modules|__pycache__|z_notes' . \
		| tail -n +2 \
		| sed 's/\*$$//' >> meta/file_structure.txt
	@echo "📁 Wrote meta/file_structure.txt"


# -----------------------------------------------------------------------------
# Packaging helpers (universal)
# -----------------------------------------------------------------------------

# Adjust these lists as your repos evolve
ZIP_EXCLUDES := .git .venv __pycache__ .pytest_cache node_modules out/*.zip
ZIP_INCLUDE_DIRS := docs tools meta  # default subset for partial zips
REPO_NAME := $(notdir $(CURDIR))
TIMESTAMP := $(shell date +"%Y%m%dT%H%M")

# Expand the exclude globs so zip sees both root-level and nested matches.
ZIP_EXCLUDE_DIRS := $(filter-out %*%,$(ZIP_EXCLUDES))
ZIP_EXCLUDE_GLOBS := $(filter %*%,$(ZIP_EXCLUDES))
ZIP_EXCLUDE_ARGS := \
	$(foreach dir,$(ZIP_EXCLUDE_DIRS),"$(dir)" "$(dir)/*" "./$(dir)" "./$(dir)/*" "*/$(dir)" "*/$(dir)/*") \
	$(foreach glob,$(ZIP_EXCLUDE_GLOBS),"$(glob)" "./$(glob)" "*/$(glob)")

# Whole-repo zip (minus exclusions)
zip_all: ## Build full repo archive under out/
	@mkdir -p out
	@echo "📦 Creating full repo zip..."
	@zip -r out/$(REPO_NAME)_$(TIMESTAMP)_full.zip . \
		-x $(ZIP_EXCLUDE_ARGS)
	@echo "✅ Wrote out/$(REPO_NAME)_$(TIMESTAMP)_full.zip"

# Selected folders only
zip_folders: ## Zip only selected folders (edit ZIP_INCLUDE_DIRS)
	@mkdir -p out
	@echo "📦 Zipping folders: $(ZIP_INCLUDE_DIRS)"
	@zip -r out/$(REPO_NAME)_$(TIMESTAMP)_partial.zip $(ZIP_INCLUDE_DIRS)
	@echo "✅ Wrote out/$(REPO_NAME)_$(TIMESTAMP)_partial.zip"

# Cross-repo target (optional)
zip_target: ## TARGET_REPO=<path> zip another repo using this makefile
	@[ -n "$(TARGET_REPO)" ] || (echo "❌ TARGET_REPO not set"; exit 1)
	@mkdir -p out
	@name=$$(basename $(TARGET_REPO)); \
	echo "📦 Zipping $$name..."; \
	zip -r out/$${name}_$(TIMESTAMP)_full.zip $$TARGET_REPO \
		-x "*/.git/*" "*/.venv/*" "*/__pycache__/*" "*/.pytest_cache/*" "*/node_modules/*" "*/out/*.zip"; \
	echo "✅ Wrote out/$${name}_$(TIMESTAMP)_full.zip"
