# Pesquisa Binaria
- Pesquisa binaria
  - Uma maneira melhor de buscar
  - Tempo de Execução

- Notação Big O
  - Tempo de execução dos algoritioms crece a taxas diferentes
  - Vendo diferentes tempos de execução Big O
  - A notação Big O estabelece o tempo de execução para a pior hipótese
  - Alguns exemplos comuns de tempo de execução Big O
  - O caixeiro-viajante

- Recaptulando


## Busca binaria se resume a log₂n
diferença de Pesquisa Simples e Pesquisa Binaria

- Simples
  - O(n) tempo de execução linear
- Binaria
  - O (log n) tempo de execução logaritimico

## Notação Big O
é uma notação especial que diz o quão rápido é um algoritimo.

### Tempo de execução dos algoritimos crece a taxas diferentes.
usando de exemplo Bob que está escrevendo um algoritimo para NASA. O algoritimo dele entrara em ação quando o foguete estiver prestes a pousar na lua, e ele o ajudará a calcular o local do pouso.

Esse é um exemplo de como o tempo de execução de dois algoritimos pode crescer a taxas diferentes. ele está tentando se decidir entre usar pesquisa simples ou binaria, na pesquisa binaria é mais rapida, pois ele tem apenas 10 segundos para descobrir onde pousar, ou o foguete saira de seu curso. <br/>
Por outro lado, é mais facil escrever a pesquisa simples, oque gera menor risco de erros. Bob não quer mesmo erros no seu código! <br/>
Para ser ainda mais cuidadoso. Bob decide cronometrar ambos os algoritimos com uma lista de 100 elementos.

Vamos presumir que leva-se 1 milisegundo para verificar um elemento. Com a pesquisa simples. Bob precisa verificar 100 elementos,então a busca pode levar até o maximo de 100ms para rodar. Em contra partida ele precisa verificar apenas sete(7) elementos na pesquisa binária (log₂ 100 é aproximadamente 7), logo, a pesquisa binária leva 7ms para ser executada. Porém, realisticamente falando, a lista provavelmente terá entrono de 1 bilhão de elementos. Se a lista iver esse numero, quanto tempo a pesquisa simples levará para ser executada? E a pesquisa binária? Tenha certeza de que sabe a resposta para essa pergunta antes de continuar lendo.

Bob executa a pesquisa binária com 1bi de elementos e leva 30ms (log₂ 1.000.000.000 é aproximadamente 30). "30 ms!" - ele pensa.<br/>
"A pesquisa binária é aproximadamente 15 vezes mais rápida do que a pesquisa simples, porque a pesquisa simples levou 100ms para uma lista de 100 elementos e a pesquisa binaria levou só 7ms. Logo, a pesquisa simples levará 30 x 15 = 450ms. certo? Bem abaixo do meu limite de 10 segundos." Bob decide utilizar a pesquisa simples. Ele fez a escolha certa?

Não. Bob está errado. Muito errado. O tempo de execução para a pesquisa simples para 1 bilhão de itens é 1 bilhão  ms, ou seja, 11 dias!
O problema é que o tempo de execução da pesquisa simples e da pesquisa binária cresce com taxas diferentes.

- Simples
  - 100ms -------> 100 elementos
  - 10 segundos -> 10000 elementos
  - 11 dias -------> 1bi elementos

- Binária
  - 7ms --> 100 elementos
  - 14ms -> 10000 elementos
  - 32 ----> 1bi elementos

Bob esperava que a pesquisa binaria fosse 15 vezes mais rápida que a simples, mas isso está incorreto. Se a lista possui 1bi de itens. o tempo de execução é aproximadamente 33milhões devezes mais rápido. Por isso, não basta saber quanto tempo um algoritimo leva pra ser executado - voce precisa saber se o tempo de execução aumenta conforme a lista aumenta. É ai que a notação Big O entra.

A notação Big O informa o quão rápido é um algoritimo. por exemplo imagine que você tem uma lista de tamanho n, O tempo de execução na notação Big O é O(n). Onde estão os segundos? eles não existem - a notação Big O não fornece o tempo em segundos. A notação Big O permite que você compara o número de operações. Ela informa o quão rapidamente um algoritimo cresce.

Temos outro exemplo disso. A pesquisa binária precisa de log n operações para verificar uma lista de tamanho n. Qual é o tempo de execução na notação Big O? É O(log n). De maneira geral, a notação Big O é escrita da seguinte forma: O(n)<br/>
O sendo de "Big O" e (n) sendo número de operações

Isso fornece o número de operações que um algoritimo realiza. é chamado de notação Big O porque coloca-se um "grande O" na frente do número de operações (parece piada, mas é verdade!).

Pesando em um algoritimo utilizando uma folha de papel onde tenha de dezenhar uma grade com 16 divizões, uma das formas "algoritimo 1" seria desenhando unitariamente cada grade. a outra "algoritimo 2" seria dobra o papel de novo e denovo quatro vezes e assim já teriamos as 16 divizões apenas com quatro operações.


no caso o algoritimo 1 tem tempo de execução O(n) enquanto o algoritimo 2 tem tempo de execução O(log n)

A notação Big O estabelece o tempo de execução para a pior hipótese

### Alguns exemploes comuns de tempo de execução Big O
aqui temos cinco tempos de execução Big O que você encontrará bastante, ordenados do mais rápido para o mais lento.
- O(log n), também conhecido como tempo logarítimico. Exemplo: pesquisa binária.
- O(n), conhecido como tempo linear. Exemplo: pesquisa simples.
- O(n * log n). Exemplo: um algoritmo rápido de ordenação, como a ordenação quicksort.
- O(n²). Exemplo: um algoritimo lento de ordenação, como a ordenação por seleção.
- O(n!). Exemplo: um algoritimo bastante lento, como o do caixeiro-viajante.

#### principais pontos são os seguintes
- A rapidez de um algoritimo não é medida em segundos, mas pelo crescimento do número de operações.
- Em vez disso, discutimos sobre o quão rapidamente o tempo de execução de um algoritimo aumenta conforme o número de elementos aumenta.
- O tempo de execução em algoritimos é expresso na notação Big O.
- O(log n) é mais rápido do que O(n), e O(log n) fica ainda mais rapido conforme a lista aumenta.
