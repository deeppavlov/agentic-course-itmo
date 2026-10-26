# Заготовка целей. Реализация — своя.
.PHONY: up down test-ci test-ui test-infra baf bench-fs bench-sandbox
up:            ; docker compose up --build -d
down:          ; docker compose down -v
test-ci:       test-ui test-infra baf-smoke
test-ui:       ; @echo "TODO: UI-микросценарии"
test-infra:    ; @echo "TODO: инфраструктурные тесты (mock LLM)"
baf-smoke:     ; @echo "TODO: по одной простой задаче на БАФ, 1 повтор"
baf:           ; @echo "TODO: полный БАФ для PAIR=$(PAIR), 3 повтора"
bench-fs:      ; @echo "TODO: замеры ФС через монтирование"
bench-sandbox: ; @echo "TODO: замеры сандбокса"
