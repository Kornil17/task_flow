.PHONY: generate-api-routers-models

OPENAPI_FILE := docs/architecture/api/openapi.yaml
OUTPUT_DIR := src/presentation
MODEL_FILE := dtos/models.py

generate-api-routers-models:
	fastapi-codegen --input $(OPENAPI_FILE) \
		--output $(OUTPUT_DIR) \
		--output-model-type pydantic_v2.BaseModel \
		--model-file $(MODEL_FILE) \
		--python-version 3.13 \
		--use-annotated \
		--reuse-model \
		--enable-faux-immutability

	@if [ -f $(OUTPUT_DIR)/main.py ]; then \
		rm $(OUTPUT_DIR)/main.py; \
		echo "Removed routers in main.py"; \
	else \
		echo "Warning: main.py not found, skipping routers remove"; \
	fi
