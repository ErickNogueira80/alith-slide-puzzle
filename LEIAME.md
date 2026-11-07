# Alith Yngvirld · Slide Puzzle (18+)

## O que é
Quebra-cabeça deslizante (estilo 15-puzzle) com a arte da personagem **Alith Yngvirld**, paladina de
Atraídes. Cinco capítulos de dificuldade crescente; cada um, ao ser resolvido, revela um trecho da
história da personagem. Classificação 18+ (nudez sugerida, sangue, temas sombrios), com portão de idade.

- **Cliente/área:** pessoal (lazer). Fora do assistente por decisão do Erick (2026-11-07).
- **Arte:** @marknogart. Uso pessoal; não publicar sem autorização do artista.

## Onde está
- Pasta: `D:\Erick\Jogos\alith-slide-puzzle`
- Repositório: https://github.com/ErickNogueira80/alith-slide-puzzle (**privado**; acesso só do Erick e de Mark666DooM, convidado como colaborador, que em conta pessoal sempre tem escrita)
- Jogo pronto: `alith-puzzle.html` (arquivo único, imagem embutida; abre em qualquer navegador e no celular)
- Fontes: `src/template.html` (código) + `src/alith.png` (arte original)

## Como rodar
- Jogar: abrir `alith-puzzle.html`.
- Depois de editar o template ou trocar a arte: `python build.py` (precisa de Pillow) gera o HTML de novo.

## Como joga
- Toque/clique numa peça na mesma linha ou coluna do vazio (move a fileira inteira), deslize, ou use setas/WASD.
- **Espiar** (segurar o botão ou Espaço) mostra a imagem completa; conta no resultado.
- **Números** mostra a ordem das peças.
- Recordes e capítulos liberados ficam no `localStorage` do navegador.

| Cap. | Título | Grade |
|---|---|---|
| I | Aletheia | 3×3 |
| II | Yngvihildr | 3×4 |
| III | A Voz | 4×5 |
| IV | As Cicatrizes | 5×6 |
| V | A Paladina | 5×7 |

## Decisões
- 2026-11-07: HTML único e local, por ser arte de terceiro com nudez.
- 2026-11-07: repositório privado no GitHub, compartilhado só com Mark666DooM. Sem GitHub Pages: o site do Pages seria público. Para jogar, baixar o `alith-puzzle.html` e abrir no navegador.
- Embaralhamento por passeio aleatório a partir da solução, então toda partida tem solução.
- Textos dos capítulos adaptados do background da personagem escrito pelo Erick.
