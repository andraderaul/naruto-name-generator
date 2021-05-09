# naruto-name-generator
Nesse repositório contém a implementação de um [Bot](https://twitter.com/rnn_narubot) para o twitter, a ideia principal do Bot é realizar tweets com base nos nomes de personagens do anime Naruto.

Primeiramente, foi necessário realizar uma raspagem de dados(scraping) do seguinte site [leafninja](http://www.leafninja.com/), pois não encontrei nenhuma API de Naruto. Em seguida, os dados coletados foram tratados/limpados depois convertidos de forma que a rede neural conseguisse utilizar.

O próximo passo é treinar a rede neural recorrente com uma camada LSTM nos dados, isso será utilizado para gerar novos nomes.

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

Agora é utilizar os nomes gerados pela RNN para fazer os tweets e para isso foi necessário consumir a [api de desenvolvedores](https://developer.twitter.com/) do twitter. Por último o deploy do Bot foi feito na plataforma de nuvem [Heroku](https://www.heroku.com/) para que fique disponível 24/7.

Referências: 
* [Keras LSTM text generation](https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py)
* [RNN for Pokemon names](https://towardsdatascience.com/generating-pok%C3%A9mon-names-using-rnns-f41003143333)
* [RNN for Dinosaur names](https://datascience-enthusiast.com/DL/Dinosaurus_Island_Character_level_language_model.html)
* [How To Create a Twitterbot with Python 3 and the Tweepy Library](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library)
* [Building a Twitter Bot with Python](https://towardsdatascience.com/building-a-twitter-bot-with-python-89959ef2607f)
