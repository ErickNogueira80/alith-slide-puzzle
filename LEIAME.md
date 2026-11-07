# Alith Yngvirld · Quebra-cabeças (18+)

## O que é
Dois jogos com a arte da personagem **Alith Yngvirld**, paladina de
Atraídes. **Deslizante** (slide puzzle, estilo 15-puzzle) e **Encaixe** (jigsaw: peças com encaixes arrastadas de uma bandeja). Cada jogo tem cinco capítulos de dificuldade crescente; cada um, ao ser resolvido, revela um trecho da
história da personagem. Classificação 18+ (nudez sugerida, sangue, temas sombrios), com portão de idade.

- **Cliente/área:** pessoal (lazer). Fora do assistente por decisão do Erick (2026-11-07).
- **Arte:** @marknogart. Uso pessoal; não publicar sem autorização do artista.

## Onde está
- Pasta: `D:\Erick\Jogos\alith-slide-puzzle`
- Repositório: https://github.com/ErickNogueira80/alith-slide-puzzle (**PÚBLICO temporariamente** desde 2026-11-07 para teste no celular; Erick vai voltar para privado. Colaborador: Mark666DooM)
- Jogo online (temporário): deslizante https://ericknogueira80.github.io/alith-slide-puzzle/app/ · encaixe https://ericknogueira80.github.io/alith-slide-puzzle/app/jigsaw.html (GitHub Pages; some ao voltar para privado)
- Jogos prontos: `alith-puzzle.html` (deslizante) e `alith-jigsaw.html` (encaixe) (arquivo único, imagem embutida; abre em qualquer navegador e no celular)
- PWA: pasta `app/` (index.html, manifest, service worker offline, ícones). Só instala servida por HTTPS; hoje **não hospedado** (decisão de 2026-11-07), fica pronta para o futuro.
- Fontes: `src/template.html` (deslizante), `src/jigsaw.html` (encaixe) + `src/alith.png` (arte original)

## Como rodar
- Jogar no PC: abrir `alith-puzzle.html`.
- Jogar no celular (Android): baixar `alith-puzzle.html` do repositório (logado no GitHub), abrir pelo app Arquivos e escolher o Chrome. No iPhone a pré-visualização de arquivos não roda o jogo; usar um app com navegador de arquivos locais (ex.: Documents, da Readdle).
- Depois de editar o template ou trocar a arte: `python build.py` (precisa de Pillow) gera o HTML avulso e a pasta `app/`. Ao mudar o jogo, suba `VERSION` no `build.py` para o PWA instalado se atualizar.

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

### Encaixe (jigsaw)
- Arraste a peça da bandeja (lateral no PC, embaixo no celular, puxando para cima) até o lugar dela; perto do certo ela encaixa, senão volta e conta erro.
- **Sombra**: imagem fraca no fundo do tabuleiro. **Só bordas**: filtra a bandeja. **Espiar**: imagem inteira.
- Recorde por tempo. Progresso salvo em `alith-jigsaw-v1` (aceite do 18+ é compartilhado com o deslizante).

| Cap. | Peças (C×R) |
|---|---|
| I | 3×4 = 12 |
| II | 4×5 = 20 |
| III | 5×7 = 35 |
| IV | 6×8 = 48 |
| V | 7×10 = 70 |

## Decisões
- 2026-11-07: HTML único e local, por ser arte de terceiro com nudez.
- 2026-11-07: repositório privado no GitHub, compartilhado só com Mark666DooM. Sem GitHub Pages: o site do Pages seria público. Para jogar, baixar o `alith-puzzle.html` e abrir no navegador.
- Embaralhamento por passeio aleatório a partir da solução, então toda partida tem solução.
- Textos dos capítulos adaptados do background da personagem escrito pelo Erick.
- 2026-11-07: versão PWA gerada pelo mesmo build. Para manter o acesso só entre os dois, a hospedagem precisa de login (ex.: Cloudflare Pages + Cloudflare Access), não link público.
- 2026-11-07: Erick escolheu não hospedar; no celular o jogo é aberto como arquivo. Recordes podem não persistir quando aberto como arquivo.
- 2026-11-07: repositório tornado público e GitHub Pages ligado, temporariamente, a pedido do Erick para testar no celular. Para encerrar: Settings → Pages → desligar e voltar a visibilidade para privado.
- 2026-11-07: criada a versão de encaixe (jigsaw), com mesmos capítulos e textos; os dois jogos têm link um para o outro. PWA v1.2.0.
