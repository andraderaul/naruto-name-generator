# naruto-name-generator 
Primeiramente, foi necessário realizar uma raspagem de dados(scraping) do seguinte site [leafninja](http://www.leafninja.com/), pois não encontrei nenhuma API de Naruto. Em seguida, os dados coletados foram tratados/limpados depois convertidos de forma que a rede neural conseguisse utilizar.

O próximo passo é treinar a rede neural recorrente com uma camada LSTM nos dados. 
Segue alguns exemplos de nomes:
* obuta
* onaha
* atsuni
* uzuna
* oiho
* ashiri
* orei
* yuuraku
* kuronba
* ouso
* mokaku
* enda

Até que o resultado não foi ruim, dado a quantidade de dados, boa parte dos nomes são querentes.

Referências: 
* [Keras LSTM text generation](https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py)
* [RNN for Pokemon names](https://towardsdatascience.com/generating-pok%C3%A9mon-names-using-rnns-f41003143333)
* [RNN for Dinosaur names](https://datascience-enthusiast.com/DL/Dinosaurus_Island_Character_level_language_model.html)
