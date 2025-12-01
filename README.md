# Projeto-Introducao-a-IA
Projeto elaborado para a disciplina de Introdução à Inteligência Artificial.

A ideia é desenvolver um labirinto percorrido pelo jogador, em que um monstro controlado por IA deverá, a cada movimento do usuário, buscar sempre a rota mais otimizada para alcançá-lo. O jogador deve encontrar a saída ou possíveis objetivos ao longo do caminho, sempre recorrendo ao pensamento estratégico para evitar que o monstro o alcance antes do objetivo ser concluído.

Inicialmente, criaremos nosso próprio labirinto e testaremos pelo terminal. Caso sobre tempo, faremos uma interface gráfica. Por último, podemos idealizar um novo algoritmo que gere labirintos aleatórios, sempre garantindo que é possível percorrê-lo.

Ideias adicionais, caso sobre tempo:

    - Criação de outros modos de jogo: A utilização do algoritmo A* nos dá a liberdade de expandir ainda mais. Por exemplo, no modo que iremos desenvolver como prioridade, o monstro sempre sabe aonde o jogador está, sendo esse o desafio. Um outro modo poderia incluir um detector de proximidade, possível através do A*, em que vários monstros são posicionados pelo labirinto e o jogador deve evitá-los sabendo que eles só irão perseguí-lo se ele chegar perto o suficiente.

    - Portas e coletáveis através do mapa: Para o modo mencionado anteriormente (ou até mesmo o modo padrão) ficar mais interessante, poderiam haver paredes que podem ser fechadas pelo jogador, dando a ele uma nova chance caso o monstro esteja muito perto. Isso deixa o modo com vários monstros mais justo, pois ao fechar a porta, o monstro poderia parar de detectar o jogador, cortando a detecção dele por estar muito distante. Os coletáveis incentivariam o jogador a percorrer diferentes áreas do labirinto à fim de abrir a saída final, tornando o jogo mais desafiador.