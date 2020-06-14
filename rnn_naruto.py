from keras.callbacks import LambdaCallback
from keras.layers import LSTM, Dense
from keras.models import Sequential
import numpy as np
import scraping
from manage_file import read_file

names = read_file()
if(len(names[0]) == 0):
    names = scraping.get_all_names()

# names to one-hot encode
char_to_index = dict((chr(i+96), i) for i in range(1, 27))
char_to_index[' '] = 0
char_to_index['.'] = 27

index_to_char = dict((i, chr(i+96)) for i in range(1, 27))
index_to_char[0] = ' '
index_to_char[27] = '.'

max_char = len(max(names, key=len))
m = len(names)
char_dim = len(char_to_index)

X = np.zeros((m, max_char, char_dim))
Y = np.zeros((m, max_char, char_dim))

for i in range(m):
    name = list(names[i])
    for j in range(len(name)):
        X[i, j, char_to_index[name[j]]] = 1
        if j < len(name)-1:
            Y[i, j, char_to_index[name[j+1]]] = 1

# build the model: a single LSTM


def build_model():
    print('Build model...')
    model = Sequential()
    model.add(LSTM(128, input_shape=(max_char, char_dim), return_sequences=True))
    model.add(Dense(char_dim, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model


def make_name(model):
    name = []
    x = np.zeros((1, max_char, char_dim))
    end = False
    i = 0

    while end == False:
        probs = list(model.predict(x)[0, i])
        probs = probs / np.sum(probs)
        index = np.random.choice(range(char_dim), p=probs)
        if i == max_char-2:
            character = '.'
            end = True
        else:
            character = index_to_char[index]
        name.append(character)
        x[0, i+1, index] = 1
        i += 1
        if character == '.':
            end = True

    return ''.join(name)


# def generate_name_loop(epoch, _):
#     if epoch % 25 == 0:

#         print('Names generated after epoch %d:' % epoch)

#         for i in range(3):
#             make_name(model)
#         print()


def fit_model():
    #name_generator = LambdaCallback(on_epoch_end=generate_name_loop)
    model = build_model()
    model.fit(X, Y, batch_size=64, epochs=300, verbose=0)
    return model


def get_names(model):
    names = [make_name(model) for i in range(50)]
    names_more = list(filter(lambda name: len(name) > 4, names))
    return names_more
