# Space Invaders — Projeto Python

## Objetivo
Criar uma versão educacional do clássico Space Invaders usando Python e Pygame, com código separado por responsabilidade e sprites em uma pasta de recursos.

## Funcionalidades
- Nave controlada pelas setas esquerda e direita; disparo com a barra de espaço.
- Seis fileiras de invasores: duas verdes (10 pontos), duas amarelas (20 pontos) e duas vermelhas (30 pontos).
- Invasores se movem em grupo na horizontal, descem apenas quando alcançam uma borda e aceleram gradualmente.
- Disparos inimigos em intervalos aleatórios.
- Quatro barreiras em formato de U invertido, danificadas por tiros e corroídas quando os invasores chegam até elas.
- Uma vida: qualquer tiro inimigo que acerte a nave ou invasor que alcance a zona da nave encerra a partida.
- Tela de Game Over em estilo retrô e opção de reiniciar com Enter.
- Tela de vitória quando todos os invasores forem derrotados.

## Tecnologias
- Python 3.13 (recomendado para esta configuração)
- Pygame

## Estrutura de pastas
```text
space_invaders_etec/
├── assets/
│   └── images/                 # Sprites da nave e dos invasores
├── src/
│   ├── main.py                 # Ponto de entrada
│   └── game/
│       ├── __init__.py
│       ├── app.py              # Loop, regras e desenho
│       ├── config.py           # Constantes e cores
│       └── entities.py         # Nave, invasores, tiros e barreiras
├── tests/                      # Espaço para testes automatizados
├── .gitignore
├── README.md
└── requirements.txt
```

## Como executar no Windows
Abra o terminal na pasta principal do projeto e execute:

```powershell
py -3.13 -m pip install -r requirements.txt
py -3.13 src/main.py
```

Se usar outra versão de Python compatível com Pygame, substitua `py -3.13` pelo comando correspondente.

## Controles
- **Seta esquerda / seta direita:** mover a nave.
- **Barra de espaço:** atirar.
- **Enter:** reiniciar após Game Over ou vitória.
- **Esc:** fechar o jogo.

## Integrantes
- Matheus de Araujo Proença e Kaylane Yasmin Fernandes de Paiva

## Créditos dos recursos
Os sprites de nave e invasores foram fornecidos pelo grupo para este projeto. Os arquivos são mantidos em `assets/images/` para que o jogo funcione sem depender de caminhos externos.
