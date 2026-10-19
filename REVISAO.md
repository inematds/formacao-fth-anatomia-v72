Nota: 8.5/10

# Revisão independente — FTH 0 · O corpo do humanoide (PT) — 19/10/2026

## Resumo
- Curso sólido e honesto: os números medidos batem 100 % com `kit/saidas/` e com uma nova execução (MuJoCo 3.16.0, Menagerie 62ab00f). Todos os 24 "pronto quando" passaram. Os 13 blocos de terminal mostrados são idênticos a `kit/blocos/*.sh`, e as 17 saídas mostradas são idênticas a `kit/saidas/*.txt`.
- Os fatos de mercado seguem as pesquisas e quase sempre trazem a ressalva certa. Não achei fato inventado, preço sem versão nem menção desatualizada tratada como atual (Figure 01/02, K-Scale, "16 mil", Thor, Humble, ISO 25785 e Webots estão ausentes ou tratados como armadilha).
- Há 2 problemas graves, cada um corrigível em uma linha: (1) "punho 5 N·m" contradiz a própria saída medida; (2) os 50:26 da meia-maratona ([2ª]) aparecem sem ressalva no quiz. Há também 7 problemas menores de precisão ou ressalva.

## A) 15 afirmações factuais sorteadas

| # | Afirmação (trecho) | Aula | Onde está na fonte | Veredito |
|---|---|---|---|---|
| 1 | G1 base US$ 13,5 mil, "sem desenvolvimento secundário (sem SDK)"; EDU sob consulta; revendas US$ 43,5–73,9 mil (relatado) | 1 | PE §1.1 [FATO]/[2ª] | ok |
| 2 | G1 de competição a US$ 35 mil no programa da RoboCup 2026 | 1 | PE §1.2 [FATO] | ok |
| 3 | Optimus V3 sem aparição pública até ago/2026; Tesla promete início de produção antes do fim de 2026 em comunicado à SEC | 1 | VE §4 ([FATO] para a meta no 8-K) | ok (o "não mostrado até ago" vem de checagem secundária, mas o recorte temporal está explícito) |
| 4 | "meia-maratona … vencida em 50:26 … contra 2:40:42 em 2025" | 1 | PE §6.2 [2ª] | **ressalva faltando** no quiz P4 (ver Grave 2) |
| 5 | K-Scale Labs "fechou em 11/2025 … (relatado)" | 1 | PE §1.1 [2ª] | ok |
| 6 | "Material de 2024–25 ainda fala em Figure 01 e 02 com 'GPT-4 integrado'"; "O Atlas hidráulico foi aposentado" | 1 | não está em PE/VE/VM (ATUALIZACAO cita VE §4, que não diz isso) | **sem fonte** (menor: está enquadrado como material antigo) |
| 7 | MuJoCo "sai quase a cada duas semanas" | 2 | VE §2 [FATO] ("ritmo quase quinzenal") | ok |
| 8 | G1: nq=36 nv=35 nu=29, 33,3 kg, passo de 2 ms, keyframe stand | 2 | kit/saidas/a2b-abrir.txt; reexecutado | ok |
| 9 | "5 no punho" / "Os punhos do modelo aguentam só 5 N·m" | 3 | kit/saidas/a3-juntas.txt: wrist_roll **25**, wrist_pitch/yaw 5 | **errado** (Grave 1) |
| 10 | Joelho do G1 real: 90 N·m (base) / 120 N·m (EDU), "relatado" | 3, 4 | PE §1.1 [2ª] (robotshop, ifixit) | ok |
| 11 | Dex3-1 do G1 EDU com 7 GDL e matriz tátil opcional; F/T de 6 eixos ausente das fichas (incerto) | 5 | PE §2.2 [FATO]; §2.3 [incerto] | ok |
| 12 | 40 N por 0,2 s: CoM sai em t = 0,73 s e o robô cai; 15 N fica; 20–30 N sai e volta | 6 | kit/saidas/a6a, a6b; reexecutado | ok |
| 13 | Helix 02: S0 a 1 kHz e 10 M de parâmetros; S1 a 200 Hz; S2 a 7–9 Hz | 7 | VM §4 [FATO] | ok |
| 14 | Thor dev kit de US$ 3.499 (08/2025) para US$ 5.499 (07/2026); Orin Nano Super de 249 para 399 (relatado) | 7 | PE §2.3 / VE §4 [2ª] | ok |
| 15 | K1: 95 cm, 19,5 kg, 22 GDL, 117 TOPS, 1 h 10 min a 1,1 m/s; US$ 14.999 público na RoboCup | 8 | PE §1.1 [FATO], §1.2 [FATO] | ok |

Também conferi (todos ok): R1 com 1,23 m, 27–29 kg e 20–40 GDL (PE §1.1); H2 com 0,972 kWh, 15 Ah e 75,6 V (PE §1.1); G1 com 9.000 mAh, 13S e ~2 h; Atlas na CES 2026 com lote comprometido (VE §4, relatado); 1X NEO a US$ 20 mil e fábrica desde 30/04/2026 (VE §4, relatado); Unitree com 5.511 em 2025 e IPO (PE §6.3, relatado); H1 com ctrlrange ±200/±300 (h1.xml); OP3 com 3,15 kg; pé do G1 com 0,608 kg; sítio imu_in_torso existe.

## B) "Pronto quando" (24 exercícios)

Rodei todos no venv (MuJoCo 3.16.0 + Menagerie 62ab00f), com timeout, e conferi contra `kit/saidas/`. **Não há divergência literal.** Observações:
- Aula 1 E1: o rc real é 1 (`saída: 1`), como no texto. Aula 1 E3: testei com uma 7ª linha válida e saiu `7 robôs, 7 com fonte e data`.
- Aula 2 E3: `nq=50 nv=49 nu=43`, ok. Aula 3 E3: `juntas.py` sem argumento usa o G1 por padrão e `-15     15` bate.
- Aula 4 E2: o texto diz que "a linha de 120° começa com `ATENÇÃO`", mas a linha real começa com `joelho 120°: ATENÇÃO: …` (menor, só a redação).
- Aula 5 E3: o rótulo do script é dinâmico (`{m.nsensor - 4} acrescentados`), então `8 sensores (4 do arquivo + 4 acrescentados)` sai como esperado.
- Aula 6 E2: `queda: não` é prefixo de `queda: não (pelve a 0.79 m em t = 3 s)`; aceitável.
- Aula 8 E3: `apptronik_apollo/scene.xml` e `pal_talos/scene_position.xml` existem no commit 62ab00f (`git ls-tree`), mas estão fora do sparse-checkout, por isso não rodei. Rodei `comparar.py` com booster_t1 e robotis_op3 (este sem keyframe) e os dois deram `FICHA: 7 itens comparados`, então o script é robusto.

## C) Problemas GRAVES

1. **Número medido contradito pelo texto.** Em `conteudo/pt/aulas/03-juntas.json`:
   - em `secoes[0].nos[3].detalhe`: "Os punhos do modelo aguentam só 5 N·m: servem para orientar a mão, não para carregar peso.";
   - em `secoes[1].passos[2].texto[0]`: "… 25 no ombro, 5 no punho.".
   
   A saída da própria aula (`kit/saidas/a3-juntas.txt`) mostra `wrist_roll_joint … 25`; só pitch e yaw têm 5. A mesma imprecisão aparece em ATUALIZACAO.md ("punho 5 N·m").
   **Correção:** "Pitch e yaw do punho aguentam só 5 N·m (o roll, 25 N·m): servem para orientar a mão…" e "… 25 no ombro e no roll do punho, 5 no pitch e yaw do punho.".
2. **Fato [2ª] sem ressalva.** Em `conteudo/pt/aulas/01-cenario.json`, `secoes[5].perguntas[3].p`: "A meia-maratona de Pequim de 2026 foi vencida em 50:26." PE §6.2 marca o dado como [2ª]. Em `secoes[1].passos[3].texto[0]`, o "(relatado)" fica no fim da frase, depois do número da WHRG, e não cobre claramente o 50:26.
   **Correção:** "Segundo a imprensa, a meia-maratona de Pequim de 2026 foi vencida em 50:26." No passo: "…foi vencida em 50:26 por um robô autônomo, contra 2:40:42 em 2025 (relatado); …".

## Problemas menores

1. **Aula 1 sem fonte.** `01-cenario.json` `secoes[1].passos[1]`: "'GPT-4 integrado'" e "O Atlas hidráulico foi aposentado" não estão em PE/VE/VM. **Correção:** tirar o "GPT-4 integrado" (basta "Figure 01 e 02") e escrever "o Atlas atual é elétrico (CES 2026)", sem afirmar a aposentadoria. Ou registrar a fonte.
2. **Aula 1, preço do R1 inconsistente.** O diagrama diz "R1 (US$ 4.900 / 5.900)", `passos[2].texto[1]` diz "Unitree R1 (US$ 5.900)" e o quiz P3 diz "R1 a partir de US$ 4.900". Logo a aula do "preço por versão" deixa a versão sem nome. **Correção:** "R1 AIR US$ 4.900 / R1 US$ 5.900" nos três lugares.
3. **Aula 1, gabarito do Figure 03.** Na saída `a1b-conferir`, a linha "Figure 03 piloto 27/01/2026" usa a data do anúncio do Helix 02 (uma demo) como data da evidência de piloto. A evidência de piloto é a BMW, ~06/2026 (relatado). **Correção:** data 06/2026 e fonte VE (time.com/humanoidsdaily), ou nota no texto: "a data é a da fonte usada, não a do piloto".
4. **Aula 7 [incerto] como fato.** Em `07-computacao-energia.json`, `secoes[0].nos[2].detalhe` diz "Roda no robô, no software do fabricante." e "Cerca de 50 Hz é o típico". PE §5 marca isso como síntese [incerto]. **Correção:** "Nos robôs comerciais, em geral roda no SDK do fabricante (síntese da pesquisa da formação)".
5. **Aula 7, camada S0 = PD.** No mesmo nó, "PD / S0" mistura o PD de junta com o S0 do Helix 02, que é um controlador de corpo inteiro aprendido. **Correção:** "O equivalente na Figure é o S0 do Helix 02, um controlador aprendido a 1 kHz…".
6. **Aula 8, Booster T1.** Em `08-ficha.json`, `secoes[1].passos[2].texto[1]`: "O T1, da mesma empresa, tem modelo no Menagerie". PE §1.1 diz que a página do T1 redireciona e que a linha atual é T2 + K1. **Correção:** acrescentar "(a linha atual da Booster é T2 e K1; o T1 pode ter saído de linha — incerto)".
7. **Detalhes de redação e comando:**
   - Aula 4 E2: trocar "a linha de 120° começa com" por "a linha de 120° mostra".
   - Aula 2 `secoes[2].saida.abas[1]`: a saída de erro mostra `/tmp/sem-menagerie/…`, caminho da captura; trocar por `~/fth/…`, como no e8.
   - Aula 2 `secoes[3].blocos[3]` usa `~/fth` fixo, ignorando `FTH`.
   - A saída "1 robôs" (e1) pede singular no script.
   - Aula 4 usa queda com pelve < 0,4 m e a aula 6, < 0,5 m. Dizer que são critérios de scripts diferentes.

## D) Didática e tom

Técnico, sem hype e com texto curto. Cada aula mede algo no próprio modelo e confronta com a ficha, e a coluna "diferença" fecha bem o curso. Os "erros comuns" são reais e capturados (njnt como GDL, robô caído a 120°, CoM fora ≠ queda, mAh × Ah). Os quizzes têm resposta certa correta e explicação coerente com o texto em todas as 8 aulas. Os distratores são plausíveis, com exceção de alguns caricatos (ex.: "o MuJoCo regrava o g1.xml"). A progressão aula 2 → 8 é clara, e a bancada fixada em versão torna tudo reproduzível.

## Correções do autor depois da revisão (19/10/2026)
- Graves 1 e 2 corrigidos: punho (pitch/yaw 5 N·m, roll 25) na aula 3 e no ATUALIZACAO.md; meia-maratona com "segundo a imprensa" no quiz e "(relatado)" logo após o 50:26.
- Menores corrigidos: "GPT-4 integrado" e "Atlas hidráulico aposentado" retirados; preços do R1 iguais nos 3 lugares (R1 AIR 4.900 / R1 5.900); data da ficha do Figure 03 explicada; PD × S0 do Helix 02 separados e "em geral no SDK do fabricante (síntese)"; T1 com ressalva de linha atual; "mostra" no E2 da aula 4; critério de queda 0,4 × 0,5 m explicado; visualizador respeita FTH; singular "1 robô" (saída recapturada).
- Mantido: caminho /tmp/sem-menagerie na saída de erro (é o caminho real que o bloco usa).
