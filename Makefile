RUNTIME_TAG='bie/text-tokenizer'

all:
	@echo command missing

update: \
	update-code-only \
	build

update-code-only:
	git reset --hard
	git pull

build: \
	runtime-build \

runtime-build:
	docker build \
		--tag ${RUNTIME_TAG} \
		./env/docker/runtime