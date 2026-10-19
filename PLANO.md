# PLANO — FTH 0 · O corpo do humanoide (formacao-fth-anatomia-v72)

Curso 0 de 5 da **FTH — Formação Tecnológica em Humanoides** (v7.2, PT/EN/ES). Piloto da formação. Público: quem programa em Python, já viu ROS 2 e quer trabalhar com humanoides sem ter um. Toda prática roda em CPU, em segundos, com saída determinística.

## Versões testadas nesta máquina (19/10/2026, aarch64 / NVIDIA GB10, Ubuntu, Python 3.12.3)
| item | versão | como |
|---|---|---|
| MuJoCo | **3.16.0** (wheel aarch64 do PyPI) | `pip install -q mujoco==3.16.0 numpy` num venv novo |
| numpy | 2.5.4 | idem |
| MuJoCo Menagerie | commit **62ab00f** (15/10/2026) | `git clone --filter=blob:none --sparse` + `sparse-checkout set unitree_g1 unitree_h1 robotis_op3 booster_t1` + `git checkout 62ab00f` (153 MB) |
| Modelos medidos | G1 `nq=36 nv=35 nu=29`, 33,3 kg, keyframe `stand` · H1 `nu=19`, 51,4 kg · OP3 `nu=20` · Booster T1 `nu=23` | `kit/abrir.py`, `kit/comparar.py` |

Determinismo: todos os blocos rodados duas vezes seguidas com `kit/capturar.sh` → `diff -r` sem diferença (19/10/2026). Números impressos arredondados (N·m inteiro, cm com 1 casa) para reduzir diferença entre CPUs.
**Não testado aqui (só mostrado):** mjlab, MuJoCo Playground, Isaac Lab/Sim (GPU NVIDIA, cursos 1–2). Visualizador `python -m mujoco.viewer` precisa de tela: opcional, sem "pronto quando".

## Pasta do aluno
`~/fth/` (variável `FTH` muda o lugar) com `.venv/`, `mujoco_menagerie/` e `anatomia/` (clone deste repo). Os blocos começam com `F=${FTH:-$HOME/fth}`; a captura roda o mesmo texto com `FTH=<scratchpad>` e troca o caminho por `~/fth` na saída.

## Aulas (objetivo · diagrama · prática "pronto quando", já testada)
| # | slug | objetivo (≤ 160) | diagrama | pronto quando (comando → saída) |
|---|---|---|---|---|
| 1 | cenario | classificar 6 humanoides em demo, piloto ou produção com fonte e data, sem repetir preço velho | escada demo → piloto → produção → escala | `python3 kit/conferir_fichas.py ~/fth/fichas.csv; echo "saída: $?"` → `6 robôs, 6 com fonte e data` + `saída: 0` (antes: `6 robôs, 0 com fonte e data`, `saída: 1`) |
| 2 | mjcf | instalar MuJoCo 3.16 e o Menagerie e abrir o G1 lendo nq, nv e nu do próprio arquivo | MJCF → compilador → MjModel/MjData → passo | `python3 kit/abrir.py unitree_g1/scene.xml` → `nq=36 nv=35 nu=29` |
| 3 | juntas | listar as juntas do G1 com limites em graus e conferir que o número bate com os atuadores | árvore de corpos: pelve → pernas, cintura → braços | `python3 kit/juntas.py` → `RESUMO: 29 juntas articuladas + 1 base flutuante · nu=29 · bate com nu: sim` + `saída: 0` |
| 4 | atuadores | medir o torque de cada junta do G1 agachado e comparar com o limite declarado no MJCF | mapa do corpo: QDD, harmônico, planetário, linear | `python3 kit/torque_agachado.py --joelho 90` → `maior torque: left_knee_joint 31 N·m` e mj_inverse `31 N·m` |
| 5 | sensores | ler IMU e força dos pés do G1 parado e conferir que a soma dos contatos bate com o peso | IMU, encoder, força no tornozelo, contato, (tato) | `python3 kit/sensores.py` → `soma dos contatos / peso do robô (327 N): 1.00` |
| 6 | equilibrio | empurrar o G1 e dizer quando o centro de massa sai do polígono de apoio e se ele cai | CoM → polígono de apoio → CoP/ZMP → queda | `python3 kit/equilibrio.py --empurrao 40` → `CoM dentro do apoio: não · saiu em t = 0.73 s` + `queda: sim`; com 15 N `sim (o tempo todo)` + `queda: não` |
| 7 | computacao-energia | calcular a autonomia e o orçamento de tempo de cada camada de controle a partir da ficha do fabricante | camadas S0/PD 1 kHz–500 Hz → política 50 Hz → VLA 5–10 Hz + bateria | `python3 kit/autonomia.py --pack-s 13 --ah 9 --w 216` → `autonomia: 120 min (2.0 h), sem reserva` |
| 8 | ficha | comparar dois humanoides do Menagerie por script e montar a sua ficha técnica com o plano de estudo | mapa (4 degraus) + gerador | `python3 kit/comparar.py unitree_g1/scene.xml unitree_h1/scene.xml; echo "saída: $?"` → `FICHA: 7 itens comparados` + `saída: 0` |

Saídas de erro comum capturadas: `e1-ficha-erro` (aula 1), `e2-sem-menagerie` (2), `e7-unidade` (7, mAh no lugar de Ah), `e8-fora-do-sparse` (8, pasta fora do sparse-checkout). Nas aulas 3–6 o "erro comum" vem de saídas capturadas dos próprios blocos (contar `njnt` como GDL; ler torque de robô caído a 120°; CoM fora do apoio ≠ queda).

## Simulação de ciclo
Não há `simfila`/`simconversa`: este curso não ensina ciclo (é anatomia). O ciclo treino → avaliação → ajuste entra no curso 1.

## Links fixos
- Curso seguinte (aula 8, `links`): https://inematds.github.io/formacao-fth-locomocao-v72/ (ainda não publicado em 19/10/2026 — 404 esperado no `validar --links`).
- Donos externos: vla-v72 (mercado, VLA), robot (ROS 2, PID, URDF).
