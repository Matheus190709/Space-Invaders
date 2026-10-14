# Space Invaders

## Integrantes

Matheus de Araujo Proença e Kaylane Yasmin Fernandes de Paiva

## 1. Apresentação

O Space Invaders é um jogo desenvolvido em Python utilizando a biblioteca Pygame, inspirado no clássico jogo de arcade de mesmo nome. O projeto foi elaborado com o objetivo de aplicar conceitos de programação, lógica computacional, orientação a objetos e desenvolvimento de jogos.

O jogador controla uma nave espacial e deve eliminar os alienígenas que se movimentam pela tela, evitando seus disparos e utilizando barreiras como proteção. O jogo apresenta um sistema de pontuação e progressão por fases, com aumento gradual da dificuldade.

## 2. Objetivos do projeto

O desenvolvimento deste projeto tem como principais objetivos:

- Aplicar os fundamentos da linguagem Python.
- Compreender a organização de um projeto em módulos.
- Utilizar classes e objetos na representação dos elementos do jogo.
- Implementar sistemas de movimentação, disparos e detecção de colisões.
- Trabalhar com eventos de teclado, controle de tempo e elementos gráficos.
- Utilizar recursos de áudio e gerenciamento de arquivos.
- Aplicar o controle de versão por meio do Git e do GitHub.

## 3. Funcionalidades

O jogo apresenta as seguintes funcionalidades:

- Movimentação horizontal da nave controlada pelo jogador.
- Sistema de disparos do jogador e dos alienígenas.
- Alienígenas com diferentes valores de pontuação.
- Movimentação e descida dos grupos de alienígenas.
- Barreiras que interagem com os disparos e com os alienígenas.
- Sistema de pontuação e gerenciamento de vidas.
- Possibilidade de obter uma vida extra ao atingir 1.600 pontos.
- Três fases com níveis progressivos de dificuldade.
- Reprodução de música de fundo e efeitos sonoros.
- Tela de encerramento por derrota e tela de vitória.
- Possibilidade de reiniciar a partida após o encerramento.

## 4. Controles

| Tecla | Função |
|---|---|
| Seta para a esquerda | Movimentar a nave para a esquerda |
| Seta para a direita | Movimentar a nave para a direita |
| Espaço | Disparar contra os alienígenas |
| Enter | Reiniciar a partida após o encerramento |
| Esc | Encerrar o jogo |

## 5. Tecnologias utilizadas

**Python:** linguagem utilizada para implementar a lógica e as funcionalidades do jogo.

**Pygame:** biblioteca utilizada para gerenciamento da janela, eventos, elementos gráficos, movimentação, colisões e reprodução de áudio.

**Git:** sistema de controle de versão utilizado para registrar as alterações realizadas durante o desenvolvimento.

**GitHub:** plataforma utilizada para hospedar o repositório e disponibilizar o código-fonte do projeto.

## 6. Estrutura do projeto

```text
space_invaders_etec/
├── assets/
│   ├── audio/
│   │   ├── Soundtrack.mp3
│   │   ├── tiro-nave.wav
│   │   └── tiro-aliens.wav
│   └── images/
│       ├── Green.png
│       ├── Yellow.png
│       ├── Red.png
│       └── Space-Invaders-Ship-PNG-Images.png
├── src/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── config.py
│   │   └── entities.py
│   └── main.py
├── tests/
│   └── README.md
├── .gitignore
├── requirements.txt
└── README.md
```

### Descrição dos diretórios e arquivos

- **assets/:** armazena os recursos gráficos e sonoros utilizados pelo jogo.
- **src/:** contém os arquivos responsáveis pela execução e implementação do jogo.
- **main.py:** ponto de entrada da aplicação.
- **app.py:** contém a lógica principal da partida, incluindo atualização e desenho dos elementos.
- **config.py:** reúne constantes e configurações utilizadas pelo jogo.
- **entities.py:** define as entidades, como nave, alienígenas, disparos e barreiras.
- **__init__.py:** identifica o pacote Python e pode conter sua documentação inicial.
- **tests/:** diretório reservado para a documentação e futura implementação de testes automatizados.
- **requirements.txt:** registra as dependências Python necessárias para executar o projeto.
- **.gitignore:** define arquivos e diretórios que não devem ser incluídos no controle de versão.

## 7. Requisitos para execução

Para executar o projeto, é necessário possuir:

- Python instalado em uma versão compatível com as dependências.
- Biblioteca Pygame instalada.
- Arquivos de recursos presentes nos diretórios correspondentes.

## 8. Instalação e execução

### 8.1. Obtenção do projeto

Clone o repositório utilizando o comando:

```bash
git clone https://github.com/Matheus190709/Space-Invaders.git
```

Em seguida, acesse a pasta do projeto:

```bash
cd Space-Invaders
```

### 8.2. Instalação das dependências

Execute o comando abaixo no terminal, a partir da pasta raiz do projeto:

```bash
python -m pip install -r requirements.txt
```

### 8.3. Inicialização

Para iniciar o jogo, execute:

```bash
python src/main.py
```

No Windows, caso necessário, utilize o inicializador do Python:

```powershell
py -3.13 src/main.py
```

## 9. Testes

O diretório `tests/` está reservado para a implementação de testes automatizados. No estado atual, os testes ainda não foram implementados.

A implementação futura poderá contemplar verificações relacionadas ao sistema de pontuação, movimentação, colisões, gerenciamento de vidas e progressão das fases.

## 10. Considerações finais

O desenvolvimento do Space Invaders possibilitou a aplicação prática de conceitos fundamentais da programação, incluindo estruturas condicionais, repetição, funções, classes, objetos e manipulação de eventos.

A organização modular do código e a utilização de recursos gráficos e sonoros contribuíram para a construção de uma aplicação interativa, além de proporcionar experiência com ferramentas de desenvolvimento e controle de versão.

## 11. Material utilizado

Imagem da Nave : https://www.pngall.com/space-invaders-png/download/114436/#google_vignette
Imagem dos Aliens ( vermelho, verde, amarelo ) : https://opengameart.org/content/assets-for-a-space-invader-like-game
Som da música de fundo :  https://youtu.be/7y92E-CaJzs?si=D8WiSF5JcGKwgWbv
Som dos tiros : https://samplefocus.com/samples?search=shot%20game

## 12. Repositório

O código-fonte do projeto está disponível no GitHub:

https://github.com/Matheus190709/Space-Invaders