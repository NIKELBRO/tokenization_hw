import re

class TextTokenizer:
    def __init__(self):
        # Флаги для отслеживания доступности библиотек
        self.nltk_available = False
        self.spacy_available = False
        
        #Проверяем доступность NLTK и загружаем необходимые данные
        try:
            import nltk
            try:
                #Проверяем, установлен ли уже токенизатор punkt
                nltk.data.find('tokenizers/punkt')
            except LookupError:
                # Если нет - скачиваем его автоматически
                nltk.download('punkt', quiet=True)
            self.nltk_available = True  # Устанавливаем флаг доступности
        except ImportError:
            #NLTK не установлен, пропускаем без ошибки
            pass
        
        #
        try:
            import spacy
            try:
            
                self.nlp = spacy.load("en_core_web_sm")
                self.spacy_available = True  #Если все Получилось, меня False на True
            except OSError:
                #Кроме когда Модель не найдена, нужно скачать отдельно
                pass
        except ImportError:
            #кроме когда spaCy не установлен, пропускаем без ошибки
            pass

    def simple_tokenize(self, text):
        #Возвращаем пустой список для пустого текста или пробелов
        if not text.strip():
            return []
        
        #Регулярное выражение для поиска токенов:
        # - \b\w+\b: слова (буквенно-цифровые последовательности между границами слов)
        # - [^\w\s]: отдельные символы, которые не являются буквами/цифрами/пробелами (знаки препинания)
        tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
        
        #Фильтруем результат, убирая пустые строки
        return [token for token in tokens if token.strip()]

    def nltk_tokenize(self, text):
        #Проверяем, доступна ли библиотека NLTK
        if not self.nltk_available:
            return "NLTK not available"
        
        #Проверяем, не пустой ли текст
        if not text.strip():
            return []
        
        try:
            #Импортируем функцию токенизации из NLTK
            from nltk.tokenize import word_tokenize
            #Используем встроенный токенизатор NLTK
            return word_tokenize(text)
        except Exception:
            #Или Возвращаем сообщение об
            return "NLTK error"

    def spacy_tokenize(self, text):
        #Проверяем spaCy
        if not self.spacy_available:
            return "spaCy not available"
        
        #Проверяем, не пустой ли текст
        if not text.strip():
            return []
        
        try:
            #Обрабатываем текст через spaCy pipeline
            doc = self.nlp(text)
            #Извлекаем текст каждого токена, исключая пробелы
            return [token.text for token in doc if not token.is_space]
        except Exception:
            #Возвращаем сообщение об ошибке при проблемах с токенизацией
            return "spaCy error"

    def tokenize_all(self, text):
        #Применяем все три метода токенизации к тексту
        #Возвращаем словарь с результатами для сравнения
        return {
            'simple': self.simple_tokenize(text),  #Простая токенизация
            'nltk': self.nltk_tokenize(text),      #Токенизация NLTK
            'spacy': self.spacy_tokenize(text)     #Токенизация spaCy
        }

def demo():
    #Создаем экземпляр токенизатора
    tokenizer = TextTokenizer()
    
    #Тестовый текст для демонстрации
    sample_text = "Hello, world! This is a test sentence."
    
    #Получаем результаты всех методов токенизации
    results = tokenizer.tokenize_all(sample_text)
    
    #Выводим результаты каждого метода
    for method, tokens in results.items():
        print(f"{method}: {tokens}")

if __name__ == "__main__":
    #Запускаем демонстрацию при прямом выполнении файла
    demo()