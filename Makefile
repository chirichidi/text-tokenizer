RUNTIME_TAG='bie/text-tokenizer'
RUNTIME_KR_TAG='bie/text-tokenizer-kr'

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
	docker build \
		--tag ${RUNTIME_KR_TAG} \
		./env/docker/runtime_ko