# 🧬 E-OS Core

**Engineering Operating System Core** — чистое ядро инженерной операционной системы.

---

## 📋 СОДЕРЖАНИЕ

- [Архитектура](#архитектура)
- [Компоненты](#компоненты)
- [Паттерны Кассера](#паттерны-кассера)
- [Быстрый старт](#быстрый-старт)
- [Лицензия](#лицензия)

---

## 🏛️ АРХИТЕКТУРА

```
┌─────────────────────────────────────────────────────────────┐
│                    E-OS CORE                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LEVEL 0: SOL (Онтология)                                  │
│  ├── SOURCE      — Источник энергии/информации            │
│  ├── CONSTRAINT  — Ограничение/правило                    │
│  ├── DISSIPATE   — Рассеивание/потери                     │
│  └── COMPARE     — Сравнение                              │
│                                                             │
│  LEVEL 0.5: EEL (Инженерный язык обмена)                   │
│  ├── OBJ::       — Объекты                                │
│  ├── PAR::       — Параметры                              │
│  ├── CON::       — Связи                                  │
│  ├── CNS::       — Ограничения                            │
│  ├── ST::        — Состояния                             │
│  ├── EV::        — События                               │
│  └── OP::        — Операции                              │
│                                                             │
│  LEVEL 1: ISA (Типизация)                                  │
│  └── Инженерная грамматика + система типов                │
│                                                             │
│  LEVEL 2: EIR (Граф)                                       │
│  ├── NODE        — Вершины графа                          │
│  ├── EDGE        — Рёбра графа                            │
│  └── VALUE       — Значения                               │
│                                                             │
│  LEVEL 3: RUNTIME (Исполнение)                             │
│  ├── Calculate   — Вычисление                             │
│  ├── Validate    — Валидация                              │
│  ├── Compare     — Сравнение                              │
│  ├── Solve       — Решение                                │
│  └── Simulate    — Симуляция                              │
│                                                             │
│  LEVEL 4: ПАТТЕРНЫ КАССЕРА                                 │
│  ├── Systemic vs Systematic  — Мышление vs Исполнение    │
│  ├── Anticipatory Testing    — Опережающее тестирование  │
│  └── Lifecycle Framework     — Жизненный цикл             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧬 КОМПОНЕНТЫ

### SOL (Онтологические примитивы)

```python
SOURCE     # Источник потенциала
CONSTRAINT # Ограничение
DISSIPATE  # Рассеивание
COMPARE    # Сравнение
```

### EEL (Инженерный язык обмена)

```
OBJ::BEARING
PAR::CLEARANCE = 0.02 mm
CON::MOUNTS_ON_SHAFT
CNS::TOLERANCE = ISO 286
ST::VALIDATED
EV::ASSEMBLY_COMPLETE
OP::CALCULATE
```

### EIR (Инженерный граф)

```yaml
NODE: "Bearing_001"
EDGE: "Bearing_001 → Shaft_001 (MOUNTS_ON)"
VALUE: "CLEARANCE = 0.02 mm"
```

---

## 📚 ПАТТЕРНЫ КАССЕРА

### 1. Systemic vs Systematic

- **Systemic (Мышление):** анализ, поиск противоречий, синтез
- **Systematic (Исполнение):** вычисления, проверка ограничений

### 2. Anticipatory Testing (Опережающее тестирование)

- Pre-flight VALIDATE
- EXPECTED_STATE
- Deviation Handler

### 3. Lifecycle Framework (Жизненный цикл)

- ST::DRAFT → VALIDATED → OPERATIONAL → FAILED → ARCHIVED
- Реинкарнация (ARCHIVED → DRAFT)

---

## 🚀 БЫСТРЫЙ СТАРТ

```bash
# Установка
pip install eos-core

# Импорт
from eos import SOL, ISA, EIR, Runtime

# Создание объекта
bearing = SOL()
bearing.set_source("Механическая энергия")
bearing.set_constraint("Температура ≤ 80°C")
```

---

## 📄 ЛИЦЕНЗИЯ

Apache License 2.0

---

**💫 E-OS Core — инженерное ядро нового поколения.** 🧠⚙️
