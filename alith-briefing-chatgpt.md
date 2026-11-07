# Alith Yngvirld · Slide Puzzle 18+

> Briefing completo do projeto para um assistente de IA. Contém a personagem, o design do jogo, a parte técnica, o estado atual e o código-fonte completo. A arte original não vai neste arquivo: ela será anexada à parte (`alith.png`, 663×941, retrato).

## 1. Resumo

Jogo web de **quebra-cabeça deslizante** (estilo 15-puzzle) com a arte da personagem de RPG **Alith Yngvirld**, uma paladina demoníaca criada pelo Erick. São cinco capítulos de dificuldade crescente. Cada capítulo resolvido revela a imagem completa e um trecho da história da personagem. Classificação **18+**: nudez sugerida (da própria arte), sangue e tom sombrio. Não há conteúdo sexual explícito além do que já está na arte.

- Idioma da interface e dos textos: português do Brasil.
- Uso: pessoal, compartilhado com um amigo (usuário do GitHub `Mark666DooM`).
- Arte: **@marknogart** (artista terceiro). Uso pessoal; não comercializar nem redistribuir sem autorização.

## 2. A personagem

**Nome:** Alith Yngvirld. Ela não lembra o nome de nascença e escolheu este.
- **Alith**, de *Aletheia*/*Alithea* (grego): o não-oculto, o não-dissimulado. A verdade é a manifestação daquilo que é, tal como é.
- **Yngvi**: nome mais antigo do deus nórdico Freyr (prosperidade, colheita, fertilidade, casamento, alegria e paz), irmão gêmeo de Freyja.
- **Hildr**: batalha, guerra. A palavra que deu origem a *hell*.
- **Yngvihildr → Yngvirld**: uma adaptação entre a origem, a história e a superação dela.

**Ficha:**
- Aparenta 40 a 50 anos; deve estar perto dos 150. Não confirma.
- 2,10 m de altura e cerca de 120 kg estimados (está sempre de armadura, armada ou carregando a armadura).
- **Classe:** Paladina. **Divindade:** Atraídes. Os votos dela são ao bem maior e à verdade, acima de divindades presas à ordem e ao caos.
- **Aparência no background:** cabelo ondulado até o meio das costas, grisalho e de um rosa natural estranho, às vezes em trança para exibir as cicatrizes; chifres de carneiro negros; esclera preta com íris pêssego que flameja; pele roxa acinzentada e pálida; maquiagem roxo-escura forte e metálica (sombra manchada, batom desenhado); tatuagens no pescoço, no rosto e no corpo; cicatrizes no rosto; corpo curvilíneo, força extrema, mãos de artesã; unhas pontudas roxo-metálicas.
- **Aparência na arte usada no jogo** (difere do background): pele branco-pálida, cabelo lilás com reflexos turquesa, chifres de carneiro marrom-dourados, orelhas élficas com alargador, olhos rosa com maquiagem preta escorrendo como lágrimas, piercing no septo, batom escuro, tatuagem preta ornamental no pescoço e no peito, mãos com garras vermelho-sangue. Fundo escuro com iluminação rosa e turquesa. Nudez sugerida (mãos cobrindo o peito).
- **Voz:** madura, aveludada, agridoce; uma dança entre o medo e a inspiração. "Basta saber de qual lado da batalha você escolhe estar: junto, ou contra."
- **Personalidade:** coleciona espólios das conquistas (às vezes materiais, sempre na memória). Desapegada de quem não agrega. Busca a verdade e o bem, mesmo que custe cicatrizes. Tem orgulho das cicatrizes, mas nunca contou como as ganhou.
- **Objetivo:** buscar a origem, o "eu interior" e o futuro, com o mesmo peso.
- **Memória:** esqueceu boa parte da vida, inclusive a infância. Acredita que lembrar seria só mais um espólio.
- **Lar:** tem uma casa no campo, não se sabe onde. Quando alguém se aproxima do íntimo dela, fala de um lindo horizonte com ilhas ao fundo. Nunca voltou desde que partiu. Lugares silenciosos não lhe trazem más recordações.
- **Família:** fala dos pais (e de parentes) sempre com carinho e sempre do mesmo jeito; parecem fortes e imponentes como ela. Pouco se sabe.
- **Estilo de vida:** simples e minimalista. "Para quem já dormiu somente com as estrelas como teto, é fácil viver com o minimalismo da realidade."

## 3. O jogo

### Mecânica
- Tabuleiro com a imagem cortada em `C×R` peças (a proporção da imagem é mantida, então as peças não são quadradas). Uma peça (canto inferior direito) começa vazia.
- Tocar ou clicar numa peça na mesma linha ou coluna do vazio desliza a fileira inteira. Cada peça deslocada conta 1 movimento.
- Também funciona com deslizar o dedo no tabuleiro e com setas ou WASD (a peça vizinha desliza para o vazio na direção indicada).
- **Espiar** (segurar o botão ou a barra de espaço) mostra a imagem completa por cima; o número de espiadas aparece no resultado.
- **Números** mostra a ordem das peças.
- Embaralhamento por passeio aleatório a partir do estado resolvido (60×N movimentos válidos), então toda partida tem solução. O vazio volta ao canto inferior direito no fim.
- O tempo começa no primeiro movimento.
- Ao resolver, a última peça aparece com fade, e uma janela mostra a imagem completa, o resultado, o recorde e o texto do capítulo.
- Portão 18+ na primeira abertura.
- Persistência em `localStorage` (chave `alith-puzzle-v1`): capítulos liberados, recorde por capítulo (menos movimentos, desempate por tempo), aceite do 18+ e preferência de números. Todo acesso fica em try/catch.

### Capítulos

| Cap. | Título | Subtítulo | Grade (C×R) | Frase final |
|---|---|---|---|---|
| I | Aletheia | o nome escolhido | 3×3 | "A verdade é a manifestação daquilo que é, tal como é." |
| II | Yngvihildr | paz e guerra no mesmo sangue | 3×4 | "Uma adaptação entre a origem, a história e a sua superação." |
| III | A Voz | dois metros e dez de aço | 4×5 | "Basta saber de qual lado da batalha você escolhe estar: junto, ou contra." |
| IV | As Cicatrizes | espólios que não se contam | 5×6 | "Em algum lugar da sua história alguém as conheceu. Nunca saberemos quem." |
| V | A Paladina | a lua cheia na noite mais escura | 5×7 | "Os objetivos são claros como a luz da lua cheia, dentro da mais escura noite." |

Ao terminar o capítulo V aparece um epílogo (as estrelas como teto). Os textos completos estão no código, na constante `CHAPTERS`.

### Visual
- Tema escuro fixo: fundo `#0b0710` com brilhos radiais turquesa e rosa e poeira de estrelas.
- Paleta: rosa `#ff4f8b`, sangue `#9b0f25`, turquesa `#36c9c6`, violeta `#8f5cc2`, pêssego `#ffb38a`, texto `#efe4f2`.
- Fontes (Google Fonts): **Cinzel** (títulos, números) e **Cormorant Garamond** (texto).
- O tabuleiro tem um brilho que pulsa em rosa e sangue. As janelas têm uma borda superior com "gotas de sangue" feitas em CSS.
- Tamanho do tabuleiro: `min(92vw, 460px, (100dvh − 250px) × 0,7046)`, para caber no celular sem rolar.

## 4. Parte técnica

- HTML, CSS e JavaScript puros, sem framework e sem dependências além das fontes.
- A imagem é embutida no HTML como JPEG em base64 (qualidade 90), por isso o jogo é um arquivo só (~158 KB).

```
alith-slide-puzzle/
├── src/
│   ├── template.html   # código do jogo, com marcadores __IMG__, __PWA_HEAD__ e __PWA_SW__
│   └── alith.png       # arte original
├── build.py            # gera as duas saídas abaixo (Python + Pillow)
├── alith-puzzle.html   # saída 1: arquivo único para abrir direto no navegador
├── app/                # saída 2: PWA
│   ├── index.html
│   ├── manifest.webmanifest
│   ├── sw.js           # service worker: rede primeiro, cache como reserva (funciona offline)
│   └── icons/          # 192, 512, maskable 512 e apple-touch 180 (recorte do rosto)
└── LEIAME.md
```

- **Build:** `python build.py`. Ao mudar o jogo, suba a constante `VERSION` no `build.py` para o service worker trocar o cache do app instalado.
- O PWA só instala quando servido por HTTPS.

## 5. Publicação e estado atual (2026-11-07)

- Repositório: https://github.com/ErickNogueira80/alith-slide-puzzle. Está **público temporariamente** para teste no celular; o plano é voltar para privado. Colaborador convidado: `Mark666DooM`.
- Jogo online (GitHub Pages, temporário): https://ericknogueira80.github.io/alith-slide-puzzle/app/. Some quando o repositório voltar a ser privado (o Pages de repositório privado exige plano pago e ficaria público mesmo assim).
- Alternativa privada já considerada e não adotada por ora: Cloudflare Pages com Cloudflare Access (login por e-mail só para os dois).
- Funcionalidades prontas: os 5 capítulos, controles por toque, deslize e teclado, espiar, números, recordes, portão 18+, PWA instalável e offline.
- Ainda não testado num celular de verdade no momento deste briefing.

## 6. Restrições e decisões

- A arte é de terceiro (@marknogart): uso pessoal, com crédito no rodapé do jogo.
- Manter o tom 18+ sombrio (sangue, morte, guerra, sensualidade sugerida) sem conteúdo sexual explícito.
- Textos em português do Brasil, em frases curtas e no tom das frases entre aspas do background.
- A lore vem do background do Erick. Quando inventar algo novo, deixe claro que é sugestão, porque o passado dela é propositalmente misterioso (memória perdida, cicatrizes sem explicação).

## 7. Ideias de próximos passos

- Mais capítulos ou grades maiores (6×8), modo contra o relógio, contador de movimentos ótimos.
- Trilha sonora ambiente e sons das peças (com botão de mudo).
- Novas artes para outros capítulos (ex.: Alith de armadura, a casa com ilhas no horizonte).
- Conquistas (resolver sem espiar, abaixo de X movimentos) e um "baú de espólios" que guarda as vitórias, combinando com a personagem.
- Hospedagem privada (Cloudflare Access) quando o repositório voltar a ser privado.

## 8. Código-fonte completo

O marcador `__IMG__` é substituído pela imagem em base64 no build. `__PWA_HEAD__` e `__PWA_SW__` ficam vazios no arquivo único e recebem as tags do PWA e o registro do service worker no `app/index.html`.

### src/template.html

````html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Alith Yngvirld</title>
__PWA_HEAD__
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#0b0710; --bg2:#160d1d; --ink:#efe4f2; --muted:#a893b0;
  --rose:#ff4f8b; --blood:#9b0f25; --teal:#36c9c6; --violet:#8f5cc2; --peach:#ffb38a;
  --line:rgba(255,255,255,.09);
  --ar:0.7046;
  --bw:min(92vw, 460px, calc((100dvh - 250px) * var(--ar)));
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{
  background:
    radial-gradient(ellipse 60% 45% at 15% 20%, rgba(54,201,198,.13), transparent 70%),
    radial-gradient(ellipse 55% 50% at 90% 85%, rgba(255,79,139,.16), transparent 70%),
    radial-gradient(ellipse 80% 60% at 50% 50%, var(--bg2), var(--bg));
  background-color:var(--bg);
  color:var(--ink);
  font-family:"Cormorant Garamond", Georgia, serif;
  font-size:18px;
  min-height:100dvh;
  overflow-x:hidden;
  -webkit-tap-highlight-color:transparent;
}
body::before{ /* poeira de estrelas */
  content:"";position:fixed;inset:0;pointer-events:none;opacity:.5;
  background-image:
    radial-gradient(1px 1px at 12% 30%, #fff8, transparent),
    radial-gradient(1px 1px at 72% 12%, #fff6, transparent),
    radial-gradient(1px 1px at 40% 80%, #fff5, transparent),
    radial-gradient(1px 1px at 88% 55%, #fff7, transparent),
    radial-gradient(1px 1px at 25% 65%, #fff4, transparent),
    radial-gradient(1px 1px at 58% 40%, #fff3, transparent);
}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
.wrap{max-width:980px;margin:0 auto;padding:calc(14px + env(safe-area-inset-top)) 16px calc(28px + env(safe-area-inset-bottom));display:flex;flex-direction:column;align-items:center;gap:12px}

header{text-align:center}
h1{
  font-family:Cinzel, serif;font-weight:700;letter-spacing:.14em;
  font-size:clamp(22px,5vw,34px);
  background:linear-gradient(180deg,#f6e9ff 0%, #d9a6e6 55%, var(--rose) 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent;
  text-shadow:0 0 28px rgba(255,79,139,.25);
}
.sub{color:var(--muted);font-style:italic;font-size:16px;margin-top:2px}

.chapters{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
.ch{
  font-family:Cinzel,serif;font-size:13px;letter-spacing:.08em;
  padding:7px 12px;border:1px solid var(--line);border-radius:999px;
  background:rgba(255,255,255,.03);transition:.2s;min-width:44px;
}
.ch:hover:not(:disabled){border-color:rgba(255,79,139,.5)}
.ch.on{border-color:var(--rose);background:rgba(255,79,139,.14);box-shadow:0 0 16px rgba(255,79,139,.25)}
.ch:disabled{opacity:.35;cursor:not-allowed}
.ch .done{color:var(--teal);margin-left:4px}

.title-ch{font-family:Cinzel,serif;font-size:15px;letter-spacing:.18em;color:var(--peach);text-align:center}
.title-ch small{display:block;font-family:"Cormorant Garamond",serif;letter-spacing:0;color:var(--muted);font-style:italic;font-size:15px}

.stats{display:flex;gap:18px;font-size:15px;color:var(--muted)}
.stats b{color:var(--ink);font-family:Cinzel,serif;font-weight:500;font-size:15px;margin-left:4px}

.stage{position:relative;width:var(--bw);height:calc(var(--bw) / var(--ar))}
.board{
  position:absolute;inset:0;border-radius:6px;overflow:hidden;
  background:#07040a;touch-action:none;user-select:none;
  box-shadow:0 0 0 1px rgba(255,79,139,.35), 0 0 40px rgba(255,79,139,.18), 0 0 80px rgba(54,201,198,.08);
  animation:pulse 3.2s ease-in-out infinite;
}
@keyframes pulse{50%{box-shadow:0 0 0 1px rgba(255,79,139,.55), 0 0 55px rgba(155,15,37,.35), 0 0 90px rgba(54,201,198,.10)}}
.tile{
  position:absolute;left:0;top:0;
  background-repeat:no-repeat;
  transition:transform .14s cubic-bezier(.3,.7,.3,1), opacity .5s;
  box-shadow:inset 0 0 0 1px rgba(0,0,0,.55), inset 0 0 12px rgba(0,0,0,.25);
  cursor:pointer;
}
.tile .n{
  position:absolute;left:4px;top:3px;font-family:Cinzel,serif;font-size:12px;
  color:#fff;text-shadow:0 0 4px #000,0 0 2px #000;opacity:0;transition:opacity .2s;
}
.shownum .tile .n{opacity:.85}
.tile.ok{box-shadow:inset 0 0 0 1px rgba(54,201,198,.0), inset 0 0 12px rgba(0,0,0,.15)}
.solved .tile{box-shadow:none;transition:transform .14s, box-shadow .6s}
.ghost{
  position:absolute;inset:0;border-radius:6px;pointer-events:none;
  background-size:100% 100%;opacity:0;transition:opacity .2s;
}
.peeking .ghost{opacity:.92}

.controls{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
.btn{
  font-family:Cinzel,serif;font-size:13px;letter-spacing:.1em;
  padding:10px 16px;border-radius:4px;border:1px solid var(--line);
  background:rgba(255,255,255,.04);transition:.15s;
}
.btn:hover{border-color:rgba(255,255,255,.25)}
.btn.primary{border-color:var(--blood);background:linear-gradient(180deg,#b3173a,#6d0a1b);box-shadow:0 0 18px rgba(155,15,37,.4)}
.btn.primary:hover{filter:brightness(1.15)}
.btn[aria-pressed="true"]{border-color:var(--teal);color:var(--teal)}
.hint{font-size:14px;color:var(--muted);font-style:italic;text-align:center}
footer{font-size:13px;color:var(--muted);opacity:.7;text-align:center}

/* overlays */
.ov{
  position:fixed;inset:0;z-index:10;display:none;
  background:rgba(6,3,9,.86);backdrop-filter:blur(6px);
  overflow-y:auto;padding:24px 16px;
}
.ov.show{display:flex;align-items:flex-start;justify-content:center}
.card{
  margin:auto;max-width:720px;width:100%;
  border:1px solid rgba(255,79,139,.3);border-radius:8px;
  background:linear-gradient(180deg,#1a0f22,#0e0813);
  box-shadow:0 0 60px rgba(155,15,37,.35);
  padding:22px;
}
.gate{text-align:center;max-width:460px}
.gate .age{
  display:inline-block;font-family:Cinzel,serif;font-size:30px;font-weight:700;
  border:2px solid var(--blood);color:var(--rose);border-radius:6px;padding:2px 14px;margin-bottom:12px;
}
.gate p{margin:10px 0;color:#d7c6dd}
.gate .row{display:flex;gap:10px;justify-content:center;margin-top:16px}
.win{display:grid;grid-template-columns:minmax(0,240px) 1fr;gap:20px;align-items:start}
.win img{width:100%;border-radius:6px;box-shadow:0 0 30px rgba(255,79,139,.35);display:block}
.win h2{font-family:Cinzel,serif;font-size:22px;letter-spacing:.12em;color:var(--peach)}
.win .kicker{font-family:Cinzel,serif;font-size:12px;letter-spacing:.2em;color:var(--rose)}
.win .lore p{margin:10px 0;line-height:1.45;color:#e2d4e7}
.win blockquote{
  margin:14px 0;padding:8px 14px;border-left:2px solid var(--blood);
  font-style:italic;color:var(--peach);
}
.win .res{font-size:15px;color:var(--muted);margin:8px 0 14px}
.win .res b{color:var(--ink)}
.win .new{color:var(--teal);font-family:Cinzel,serif;font-size:12px;letter-spacing:.12em;margin-left:6px}
.win .row{display:flex;gap:8px;flex-wrap:wrap}
@media (max-width:600px){
  .win{grid-template-columns:1fr}
  .win img{max-width:220px;margin:0 auto}
}
.drip{height:10px;margin:-22px -22px 14px;border-radius:8px 8px 0 0;
  background:
    radial-gradient(circle at 10% 0, var(--blood) 6px, transparent 7px),
    radial-gradient(circle at 31% 0, var(--blood) 9px, transparent 10px),
    radial-gradient(circle at 57% 0, var(--blood) 5px, transparent 6px),
    radial-gradient(circle at 78% 0, var(--blood) 8px, transparent 9px),
    linear-gradient(var(--blood),var(--blood)) top/100% 3px no-repeat;
}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>ALITH YNGVIRLD</h1>
    <div class="sub">o quebra-cabeça do não-oculto</div>
  </header>

  <nav class="chapters" id="chapters" aria-label="Capítulos"></nav>
  <div class="title-ch" id="chTitle"></div>

  <div class="stats">
    <span>Movimentos<b id="sMoves">0</b></span>
    <span>Tempo<b id="sTime">0:00</b></span>
    <span>Recorde<b id="sBest">—</b></span>
  </div>

  <div class="stage" id="stage">
    <div class="board" id="board" aria-label="Tabuleiro"></div>
    <div class="ghost" id="ghost"></div>
  </div>

  <div class="controls">
    <button class="btn primary" id="bShuffle">Embaralhar</button>
    <button class="btn" id="bPeek">Espiar (segure)</button>
    <button class="btn" id="bNum" aria-pressed="false">Números</button>
  </div>
  <div class="hint">Toque numa peça na mesma linha ou coluna do espaço vazio. Setas, WASD ou deslize também funcionam. Espaço = espiar.</div>
  <footer>Arte: @marknogart · Uso pessoal</footer>
</div>

<div class="ov" id="gate">
  <div class="card gate">
    <div class="drip"></div>
    <div class="age">18+</div>
    <p><b>Conteúdo adulto.</b> Nudez sugerida, sangue e temas sombrios.</p>
    <p style="font-style:italic;color:var(--muted)">"Basta saber de qual lado da batalha você escolhe estar, junto ou contra."</p>
    <div class="row">
      <button class="btn primary" id="gYes">Tenho 18 anos ou mais</button>
      <button class="btn" id="gNo">Sair</button>
    </div>
  </div>
</div>

<div class="ov" id="winOv">
  <div class="card">
    <div class="drip"></div>
    <div class="win">
      <img id="wImg" alt="Alith Yngvirld">
      <div>
        <div class="kicker" id="wKick"></div>
        <h2 id="wTitle"></h2>
        <div class="res" id="wRes"></div>
        <div class="lore" id="wLore"></div>
        <div class="row" id="wBtns"></div>
      </div>
    </div>
  </div>
</div>

<script>
const IMG = "__IMG__";

const CHAPTERS = [
  { n:"I", t:"Aletheia", s:"o nome escolhido", c:3, r:3,
    lore:[
      "Ela não se lembra do nome com que nasceu. Então escolheu um.",
      "<b>Alith</b>, de <i>Aletheia</i>: o não-oculto, o não-escondido, o não-dissimulado. A verdade é aquilo que se mostra como é, aos olhos do corpo e do espírito.",
      "E ela nunca se escondeu de ninguém."
    ],
    quote:"A verdade é a manifestação daquilo que é, tal como é." },
  { n:"II", t:"Yngvihildr", s:"paz e guerra no mesmo sangue", c:3, r:4,
    lore:[
      "<b>Yngvi</b> é o nome mais antigo de Freyr, irmão gêmeo de Freyja: colheita, fertilidade, casamento, alegria e paz.",
      "<b>Hildr</b> é a batalha. A palavra que o tempo arrastou até virar <i>hell</i>.",
      "Yngvihildr. Yngvirld. A origem, a história e tudo o que ela atravessou para continuar de pé."
    ],
    quote:"Uma adaptação entre a origem, a história e a sua superação." },
  { n:"III", t:"A Voz", s:"dois metros e dez de aço", c:4, r:5,
    lore:[
      "Dois metros e dez. Uns cento e vinte quilos, se alguém um dia a visse sem armadura. Ninguém viu.",
      "Aparenta entre quarenta e cinquenta anos. Deve estar perto dos cento e cinquenta. Ela não confirma.",
      "Mas o que rende os homens não é o tamanho. É a voz: madura, aveludada, agridoce. Uma dança estreita entre o medo e a inspiração."
    ],
    quote:"Basta saber de qual lado da batalha você escolhe estar: junto, ou contra." },
  { n:"IV", t:"As Cicatrizes", s:"espólios que não se contam", c:5, r:6,
    lore:[
      "Ela coleciona o que conquista. Às vezes num baú. Sempre na memória.",
      "Busca a verdade e o bem, mesmo quando o preço é sangue, o dela ou o de quem estiver no caminho.",
      "Prende o cabelo em trança para que ninguém deixe de ver as cicatrizes do rosto. Tem orgulho delas. Nunca disse como as ganhou."
    ],
    quote:"Em algum lugar da sua história alguém as conheceu. Nunca saberemos quem." },
  { n:"V", t:"A Paladina", s:"a lua cheia na noite mais escura", c:5, r:7,
    lore:[
      "Paladina de Atraídes. Os votos dela vão para o bem maior e para a verdade, acima de deuses presos à ordem e ao caos.",
      "Esqueceu boa parte da vida: a infância, os traços que a moldaram, talvez o caminho de casa. Uma casa no campo, um horizonte com ilhas ao fundo. Nunca voltou.",
      "Por ora coleciona vitórias. Lembrar seria só mais um espólio."
    ],
    quote:"Os objetivos são claros como a luz da lua cheia, dentro da mais escura noite." }
];
const EPILOGUE = "Para quem já dormiu com as estrelas como único teto, é fácil viver com o minimalismo da realidade. Ela segue firme.";

/* ---------- persistência (tolerante a falhas) ---------- */
const KEY = "alith-puzzle-v1";
function load(){ try{ return JSON.parse(localStorage.getItem(KEY)) || {}; }catch(e){ return {}; } }
function save(){ try{ localStorage.setItem(KEY, JSON.stringify(store)); }catch(e){} }
const store = Object.assign({ unlocked:1, best:{}, adult:false, nums:false }, load());

/* ---------- estado ---------- */
const $ = id => document.getElementById(id);
const board = $("board"), stage = $("stage");
let ch = 0, C = 3, R = 3, grid = [], empty = 0, tiles = [];
let moves = 0, t0 = 0, elapsed = 0, timer = null, playing = false, peeks = 0;

$("ghost").style.backgroundImage = `url(${IMG})`;
$("wImg").src = IMG;

function fmt(s){ const m = Math.floor(s/60); return m + ":" + String(s%60).padStart(2,"0"); }

function renderChapters(){
  const nav = $("chapters"); nav.innerHTML = "";
  CHAPTERS.forEach((c,i)=>{
    const b = document.createElement("button");
    b.className = "ch" + (i===ch ? " on" : "");
    b.disabled = i >= store.unlocked;
    b.title = b.disabled ? "Bloqueado" : `${c.t} (${c.c}×${c.r})`;
    b.innerHTML = (b.disabled ? "🔒 " : "") + c.n + (store.best[i] ? '<span class="done">✦</span>' : "");
    b.onclick = () => { if(!b.disabled){ ch = i; start(); } };
    nav.appendChild(b);
  });
}

function bestText(){
  const b = store.best[ch];
  return b ? `${b.moves} · ${fmt(b.time)}` : "—";
}

function build(){
  board.innerHTML = ""; tiles = [];
  const N = C*R;
  for(let id=0; id<N-1; id++){
    const el = document.createElement("div");
    el.className = "tile";
    el.style.width = (100/C) + "%";
    el.style.height = (100/R) + "%";
    el.style.backgroundImage = `url(${IMG})`;
    el.style.backgroundSize = `${C*100}% ${R*100}%`;
    const x = id % C, y = Math.floor(id / C);
    el.style.backgroundPosition = `${C>1 ? x/(C-1)*100 : 0}% ${R>1 ? y/(R-1)*100 : 0}%`;
    el.innerHTML = `<span class="n">${id+1}</span>`;
    board.appendChild(el);
    tiles[id] = el;
  }
}

function place(){
  grid.forEach((id,pos)=>{
    if(id === C*R-1) return;
    const el = tiles[id];
    el.style.transform = `translate(${(pos%C)*100}%, ${Math.floor(pos/C)*100}%)`;
    el.classList.toggle("ok", id === pos);
  });
}

function neighbors(p){
  const x = p % C, y = Math.floor(p / C), out = [];
  if(x>0) out.push(p-1); if(x<C-1) out.push(p+1);
  if(y>0) out.push(p-C); if(y<R-1) out.push(p+C);
  return out;
}

function shuffle(){
  const N = C*R;
  grid = [...Array(N).keys()]; empty = N-1;
  let prev = -1, steps = 60*N;
  do{
    for(let i=0;i<steps;i++){
      const opts = neighbors(empty).filter(p => p !== prev);
      const p = opts[Math.floor(Math.random()*opts.length)];
      grid[empty] = grid[p]; grid[p] = N-1; prev = empty; empty = p;
    }
  }while(isSolved());
  // devolve o vazio ao canto inferior direito para começar como o clássico
  while(empty % C !== C-1){ const p = empty+1; grid[empty]=grid[p]; grid[p]=N-1; empty=p; }
  while(Math.floor(empty/C) !== R-1){ const p = empty+C; grid[empty]=grid[p]; grid[p]=N-1; empty=p; }
  if(isSolved()) return shuffle();
}

function isSolved(){ return grid.every((id,pos)=>id===pos); }

function start(){
  const c = CHAPTERS[ch];
  C = c.c; R = c.r;
  stopTimer(); moves = 0; elapsed = 0; playing = true; peeks = 0;
  board.classList.remove("solved");
  $("chTitle").innerHTML = `CAPÍTULO ${c.n} · ${c.t.toUpperCase()}<small>${c.s} · ${C}×${R}</small>`;
  build(); shuffle(); place();
  updStats(); renderChapters();
}

function updStats(){
  $("sMoves").textContent = moves;
  $("sTime").textContent = fmt(elapsed);
  $("sBest").textContent = bestText();
}

function startTimer(){
  if(timer) return;
  t0 = Date.now() - elapsed*1000;
  timer = setInterval(()=>{ elapsed = Math.floor((Date.now()-t0)/1000); updStats(); }, 250);
}
function stopTimer(){ clearInterval(timer); timer = null; }

/* move a peça em p (e as que estiverem entre ela e o vazio) */
function tryMove(p){
  if(!playing || p === empty || p < 0) return;
  const px = p % C, py = Math.floor(p/C), ex = empty % C, ey = Math.floor(empty/C);
  if(px !== ex && py !== ey) return;
  const step = px === ex ? (py > ey ? C : -C) : (px > ex ? 1 : -1);
  startTimer();
  while(empty !== p){
    const n = empty + step;
    grid[empty] = grid[n]; grid[n] = C*R-1; empty = n; moves++;
  }
  place(); updStats();
  if(isSolved()) win();
}

/* direção: para onde a peça desliza */
function slide(dx, dy){
  const ex = empty % C, ey = Math.floor(empty/C);
  const tx = ex - dx, ty = ey - dy;
  if(tx<0||tx>=C||ty<0||ty>=R) return;
  tryMove(ty*C + tx);
}

function win(){
  playing = false; stopTimer();
  // última peça aparece
  const last = document.createElement("div");
  last.className = "tile";
  Object.assign(last.style, {
    width:(100/C)+"%", height:(100/R)+"%", backgroundImage:`url(${IMG})`,
    backgroundSize:`${C*100}% ${R*100}%`, backgroundPosition:"100% 100%",
    transform:`translate(${(C-1)*100}%, ${(R-1)*100}%)`, opacity:0
  });
  board.appendChild(last);
  requestAnimationFrame(()=>{ last.style.opacity = 1; board.classList.add("solved"); });

  const prev = store.best[ch];
  const isNew = !prev || moves < prev.moves || (moves === prev.moves && elapsed < prev.time);
  if(isNew) store.best[ch] = { moves, time: elapsed };
  const firstClear = store.unlocked === ch+1 && ch+1 < CHAPTERS.length;
  if(store.unlocked < ch+2) store.unlocked = Math.min(CHAPTERS.length, ch+2);
  save(); renderChapters(); updStats();

  setTimeout(()=>showWin(isNew, firstClear), 900);
}

function showWin(isNew, firstClear){
  const c = CHAPTERS[ch];
  const lastCh = ch === CHAPTERS.length-1;
  $("wKick").textContent = `CAPÍTULO ${c.n} REVELADO`;
  $("wTitle").textContent = c.t;
  $("wRes").innerHTML = `<b>${moves}</b> movimentos em <b>${fmt(elapsed)}</b>` +
    (peeks ? ` · espiou ${peeks}×` : "") + (isNew ? '<span class="new">NOVO RECORDE</span>' : "");
  $("wLore").innerHTML = c.lore.map(p=>`<p>${p}</p>`).join("") +
    `<blockquote>“${c.quote}”</blockquote>` +
    (lastCh ? `<p style="color:var(--peach)">${EPILOGUE}</p>` : "") +
    (firstClear ? `<p style="color:var(--teal);font-size:15px">Capítulo ${CHAPTERS[ch+1].n} desbloqueado.</p>` : "");
  const btns = $("wBtns"); btns.innerHTML = "";
  if(!lastCh){
    const nx = document.createElement("button");
    nx.className = "btn primary"; nx.textContent = "Próximo capítulo";
    nx.onclick = ()=>{ closeWin(); ch++; start(); };
    btns.appendChild(nx);
  }
  const again = document.createElement("button");
  again.className = "btn" + (lastCh ? " primary" : ""); again.textContent = "Jogar de novo";
  again.onclick = ()=>{ closeWin(); start(); };
  const look = document.createElement("button");
  look.className = "btn"; look.textContent = "Contemplar";
  look.onclick = closeWin;
  btns.append(again, look);
  $("winOv").classList.add("show");
}
function closeWin(){ $("winOv").classList.remove("show"); }

/* ---------- entrada ---------- */
let pd = null;
board.addEventListener("pointerdown", e=>{ pd = {x:e.clientX, y:e.clientY}; });
board.addEventListener("pointerup", e=>{
  if(!pd) return;
  const dx = e.clientX - pd.x, dy = e.clientY - pd.y; pd = null;
  if(Math.hypot(dx,dy) > 28){
    if(Math.abs(dx) > Math.abs(dy)) slide(Math.sign(dx), 0); else slide(0, Math.sign(dy));
    return;
  }
  const r = board.getBoundingClientRect();
  const x = Math.floor((e.clientX - r.left) / r.width * C);
  const y = Math.floor((e.clientY - r.top) / r.height * R);
  if(x>=0 && x<C && y>=0 && y<R) tryMove(y*C + x);
});
board.addEventListener("pointercancel", ()=>{ pd = null; });

const KEYS = { ArrowLeft:[-1,0], a:[-1,0], ArrowRight:[1,0], d:[1,0], ArrowUp:[0,-1], w:[0,-1], ArrowDown:[0,1], s:[0,1] };
document.addEventListener("keydown", e=>{
  if($("gate").classList.contains("show")) return;
  if(e.key === " "){ e.preventDefault(); if(!e.repeat) peek(true); return; }
  if($("winOv").classList.contains("show")){ if(e.key==="Escape") closeWin(); return; }
  const k = KEYS[e.key] || KEYS[e.key.toLowerCase()];
  if(k){ e.preventDefault(); slide(k[0], k[1]); }
});
document.addEventListener("keyup", e=>{ if(e.key === " ") peek(false); });

function peek(on){
  if(on && !stage.classList.contains("peeking") && playing) peeks++;
  stage.classList.toggle("peeking", on);
}
const bp = $("bPeek");
bp.addEventListener("pointerdown", e=>{ e.preventDefault(); peek(true); });
["pointerup","pointerleave","pointercancel"].forEach(ev=>bp.addEventListener(ev, ()=>peek(false)));
bp.addEventListener("contextmenu", e=>e.preventDefault());

$("bShuffle").onclick = start;
function setNums(v){ store.nums = v; save(); board.classList.toggle("shownum", v); $("bNum").setAttribute("aria-pressed", v); }
$("bNum").onclick = ()=> setNums(!store.nums);
setNums(store.nums);

/* ---------- portão 18+ ---------- */
$("gYes").onclick = ()=>{ store.adult = true; save(); $("gate").classList.remove("show"); };
$("gNo").onclick = ()=>{ document.body.innerHTML = '<p style="padding:40px;text-align:center;color:#a893b0;font-style:italic">Volte quando estiver pronto.</p>'; };
if(!store.adult) $("gate").classList.add("show");

ch = Math.max(0, store.unlocked - 1);
start();
__PWA_SW__
</script>
</body>
</html>
````

### build.py

````python
"""Gera o jogo a partir de src/:
- alith-puzzle.html : arquivo único para abrir direto no navegador
- app/              : versão PWA (instalável quando servida por HTTPS)
"""
import base64, io, json, pathlib
from PIL import Image

root = pathlib.Path(__file__).parent
VERSION = "1.1.0"

img = Image.open(root / "src" / "alith.png").convert("RGB")
buf = io.BytesIO()
img.save(buf, "JPEG", quality=90, optimize=True, progressive=True)
data = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
tpl = (root / "src" / "template.html").read_text(encoding="utf-8").replace("__IMG__", data)

# 1) arquivo único
(root / "alith-puzzle.html").write_text(
    tpl.replace("__PWA_HEAD__", "").replace("__PWA_SW__", ""), encoding="utf-8")

# 2) PWA
app = root / "app"; (app / "icons").mkdir(parents=True, exist_ok=True)
BG = (11, 7, 16)
face = img.crop((195, 95, 575, 475))          # rosto e chifres
for size in (192, 512):
    face.resize((size, size), Image.LANCZOS).save(app / "icons" / f"icon-{size}.png")
face.resize((180, 180), Image.LANCZOS).save(app / "icons" / "apple-touch-icon.png")
m = Image.new("RGB", (512, 512), BG)           # maskable: margem de segurança
m.paste(face.resize((410, 410), Image.LANCZOS), (51, 51))
m.save(app / "icons" / "icon-maskable-512.png")

head = """<meta name="theme-color" content="#0b0710">
<meta name="robots" content="noindex, nofollow">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Alith">"""
sw_reg = """if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
  navigator.serviceWorker.register('sw.js').catch(()=>{});
}"""
(app / "index.html").write_text(
    tpl.replace("__PWA_HEAD__", head).replace("__PWA_SW__", sw_reg), encoding="utf-8")

manifest = {
    "name": "Alith Yngvirld",
    "short_name": "Alith",
    "description": "Slide puzzle 18+ da paladina Alith Yngvirld",
    "lang": "pt-BR",
    "start_url": "./",
    "scope": "./",
    "display": "standalone",
    "orientation": "portrait",
    "background_color": "#0b0710",
    "theme_color": "#0b0710",
    "icons": [
        {"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}
(app / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

sw = f"""const CACHE = 'alith-{VERSION}';
const FILES = ['./', 'index.html', 'manifest.webmanifest',
  'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png', 'icons/apple-touch-icon.png'];
self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
}});
self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
}});
self.addEventListener('fetch', e => {{
  if (e.request.method !== 'GET') return;
  e.respondWith(
    fetch(e.request).then(r => {{
      if (r.ok && new URL(e.request.url).origin === location.origin) {{
        const copy = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copy));
      }}
      return r;
    }}).catch(() => caches.match(e.request).then(r => r || caches.match('index.html')))
  );
}});
"""
(app / "sw.js").write_text(sw, encoding="utf-8")
print("ok:", sorted(str(p.relative_to(root)) for p in app.rglob("*") if p.is_file()))
````
