from tokenizer import TextTokenizer #Импортируем, что написали в tokenization.py

def main():
    tokenizer = TextTokenizer() #вводим переменную, чтобы применить к ней метод, и сразу использовать 3 варианта
    
  
    sample_text = "Hello, world! This is a test sentence. How are you today?" #Даем текст
    
    print("Текст из задания:", sample_text) #Ну тут просто оформление
    print("\nРезультаты токенизации:")
    print("-" * 40)
    
    results = tokenizer.tokenize_all(sample_text) #Применяем метод
    
    for method, tokens in results.items():#Блаагодаря циклу for каждый из 3 методов выводит свои токены
        print(f"{method}: {tokens}")

if __name__ == "__main__": 
    main()