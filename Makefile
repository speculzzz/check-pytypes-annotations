all: local

.PHONY: local
local:
	@echo "==========================="
	@echo "Check the types annotations"
	@echo "==========================="
	@pyright

.PHONY: typing
typing:
	docker-compose up --build --abort-on-container-exit
	docker-compose down
