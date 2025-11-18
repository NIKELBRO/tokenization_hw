tokenization_hw/
├── tokenizer.py      # Основной модуль токенизации
├── demo.py          # Демонстрационный скрипт
├── requirements.txt # Зависимости
└── README.md        # Инструкции



# Создание виртуального окружения (рекомендуется)
python -m venv tokenizer_env
source tokenizer_env/bin/activate  # Linux/Mac (также работает в VS Code на Windows)

# Установка зависимостей
pip install -r requirements.txt
pip install nltk
pip install spacy

# Если есть другие missing imports, установите их тоже
pip install tokenizer

# Дополнительно для spaCy (после установки spaCy)
python3 -m spacy download en_core_web_sm

# Тестирование модуля
python3 demo.py

# Использование
python
from tokenizer import TextTokenizer
tokenizer = TextTokenizer()
text = "Hello, world! This is a test."
results = tokenizer.tokenize_all(text)
print(results) 

