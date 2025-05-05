PLUGIN_UUID = com.canaryknight.macos-binings
PLUGIN_DIR = $(PLUGIN_UUID).sdPlugin
OUT_FILE = $(PLUGIN_UUID).streamDeckPlugin
MANIFEST = $(PLUGIN_DIR)/manifest.json

.PHONY: all build pack update-version install

all: build pack

build:
	yarn install
	yarn build

update-version:
	@echo "Auto-incrementing version..."
	@python3 scripts/bump_version.py $(MANIFEST)

pack: update-version
	cd $(PLUGIN_DIR) && streamdeck pack --force
	mv $(PLUGIN_DIR)/$(OUT_FILE) .

install: pack
	open $(OUT_FILE)

release:
	@VERSION=$$(jq -r .Version $(MANIFEST)); \
	if git rev-parse "v$$VERSION" >/dev/null 2>&1; then \
		echo "❌ Tag v$$VERSION already exists. Bump version before releasing."; \
		exit 1; \
	fi; \
	git tag v$$VERSION; \
	git push origin v$$VERSION
