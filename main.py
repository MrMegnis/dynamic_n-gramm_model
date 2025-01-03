from models import DynamicNGramModel
from data_holder import DictDataHolder
from tokenizers import SimpleTokenizer

tokenizer = SimpleTokenizer(1)
data_holder = DictDataHolder()
model = DynamicNGramModel(3, data_holder, tokenizer)

# Обучение (обновление распределений)
model.update("<BOS> hello world this is a test hello world <EOS>")

# Предсказание
prediction = model.predict("hello world")
print(prediction)  # Вернет вероятности для следующего слова
print(tokenizer.token2item(sorted(list(prediction.items()), reverse=True, key=lambda x: x[-1])[0][0]))

# print(model.data_holder.data_holder.items())
# print(tokenizer.token2item_vocab)
# print(tokenizer.item2token_vocab)

model.update("<BOS> hello world <EOS>")

# Предсказание
prediction = model.predict("hello world")
print(prediction.items())  # Вернет вероятности для следующего слова

print(tokenizer.token2item(sorted(list(prediction.items()), reverse=True, key=lambda x: x[-1])[0][0]))

# print(model.data_holder.data_holder.items())
# print(tokenizer.token2item_vocab)
# print(tokenizer.item2token_vocab)
