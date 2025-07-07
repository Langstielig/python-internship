from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Указываем название модели
model_name = "sberbank-ai/rugpt3small_based_on_gpt2"

# Указываем путь, куда хотим сохранить файлы
save_directory = "./models"

# Загружаем и сохраняем токенизатор
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.save_pretrained(save_directory)

# Загружаем и сохраняем модель
model = GPT2LMHeadModel.from_pretrained(model_name)
model.save_pretrained(save_directory)

print(f"Модель и токенизатор сохранены в {save_directory}")
