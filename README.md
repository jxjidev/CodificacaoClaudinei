Explicação do Código
Pré-processamento: Convertemos a mensagem para uma representação binária e adicionamos o padding necessário:

Adicionamos um único bit '1' após a mensagem original.
Preenchemos o restante com '0's até que o comprimento seja 448 bits (mod 512).
Finalmente, adicionamos o comprimento da mensagem original como um inteiro de 64 bits ao final.
Processamento em Blocos de 512 bits: Dividimos a mensagem em blocos de 512 bits e expandimos os blocos de 16 palavras de 32 bits para 80 palavras.

Loop Principal: Usamos 80 iterações para cada bloco, com diferentes funções e constantes de rotação em várias etapas.

Atualização dos Hashes: Combinamos os valores intermediários em cada bloco para formar o hash final.

