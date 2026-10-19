# ATUALIZACAO — FTH 0 · O corpo do humanoide (19/10/2026)

Conferência "atualizar, não copiar": cada afirmação das fontes antigas usadas neste curso foi comparada com as pesquisas da formação (`~/projetos/wifi/longrun/2026-10-19-formacao-fth-v72/PESQUISA-ESTADO-DA-ARTE.md` = **PE**, `../2026-10-19-vla-v72/PESQUISA-ECOSSISTEMA.md` = **VE**, `PESQUISA-MODELOS.md` = **VM**) e com o que o MJCF do MuJoCo Menagerie (commit `62ab00f`, 15/10/2026) declara, medido nesta máquina em 19/10/2026 com `mujoco 3.16.0` (= **MJCF**).
Fontes antigas (intocadas): HG1 `5ee0596` (`docs/tier1/*`, `docs/tier1.1/*`, conteúdo de 22–25/11/2025) e FTH `26fe21c` (`niveis/nivel-1/modulo-1.md`, `modulo-2.md`, 29/10/2025).
Legenda da coluna "curso diz agora": **fato** (fonte primária), **relatado** (fonte secundária, dito como tal no texto), **fora** (não entra por falta de fonte).

## Mercado e estágio (aula 1)

| fonte antiga | o que dizia | o que o curso diz agora | fonte (URL/data) |
|---|---|---|---|
| HG1 tier1/03 | Unitree G1 "$16,000 (versão básica)", lançado 05/2024 | G1 base **US$ 13,5 mil sem desenvolvimento secundário (sem SDK)**; EDU sob consulta; revendas EDU US$ 43,5–73,9 mil (relatado); preço de programa RoboCup US$ 35 mil público. Explica que são 3 SKUs. "16 mil" não aparece | https://www.unitree.com/g1 (lido 19/10/2026) · https://robotprogram.robocup.org/ (19/10/2026) · PE §1.1 |
| HG1 tier1/03 | Unitree H1 por US$ 90.000, "vendendo"; 180 cm, 47 kg, 21/31 GDL | H1 só como modelo do Menagerie (19 GDL acionados, 51,4 kg no MJCF); a Unitree vende hoje o **H2** (US$ 29.900; 1,82 m, ~70 kg, 31 GDL) | https://www.unitree.com/H2 (19/10/2026) · MJCF |
| HG1 tier1/03, 09, 10 | Figure 01 (2023) e Figure 02 (2024), "GPT-4 integrado", meta de 1.000 robôs até 2026, BMW 2024 | **Figure 03** (10/2025) + **Helix 02** (27/01/2026, S0 a 1 kHz); na BMW Spartanburg desde ~06/2026, **piloto, relatado**; sem venda ao consumidor. Figure 01/02 não aparecem | https://www.figure.ai/news/helix-02 (27/01/2026) · VE §4 · VM §4 |
| HG1 tier1/03, specs-comparacao | Atlas elétrico "2024, ~60 kg estimado", "> US$ 1 milhão", não comercial | Atlas de produto lançado na **CES 2026 (05/01/2026)**: 56 GDL, carga de 50 kg, lote de 2026 comprometido com Hyundai e Google DeepMind (**relatado**) → estágio **piloto** | https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/ · VE §4 |
| HG1 tier1/03, 09, 10 | Optimus Gen 3 "comercial previsto para 2026", meta < US$ 30 mil, "100 na Gigafactory em 2025" | Optimus V3 **não foi mostrado publicamente até ago/2026**; a Tesla mantém, em comunicado à SEC, início de produção antes do fim de 2026 → estágio **demo** | SEC 8-K Tesla 2026 (VE §4; o link da SEC recusa acesso automático, por isso não vai como link na aula) |
| HG1 tier1/09, 10 | Digit "piloto avançado na Amazon 2023–24", "Amazon: 500+ Digit" em 2025 | Digit em GXO (100 mil+ caixas), Schaeffler, Toyota, Mercado Libre; SPAC de 06/2026 (**relatado**). Os "500+" saem | VE §4 / §6 |
| — (ausente) | — | **1X NEO**: pré-venda US$ 20 mil, fábrica em produção desde 30/04/2026, entrega a cliente não confirmada → **demo** (relatado) | https://www.1x.tech/discover/neo-factory · VE §4 |
| — (ausente) | — | **Unitree R1** US$ 4.900 / 5.900 (fato); **Booster K1** 95 cm, 22 GDL, 117 TOPS (fato); **UBTech Walker S2** entrega em massa desde 11/2025 (relatado); **Unitree 5.511 humanoides embarcados em 2025**, IPO na STAR em 19/08/2026 (relatado) | https://www.unitree.com/R1 · https://www.booster.tech/booster-k1/ · PE §1.1, §6.3 |
| FTH 1.2 / pesquisa | plataformas abertas; K-Scale não citada no antigo, mas é armadilha comum | **K-Scale Labs fechou em 11/2025** (relatado); dito como fechado, nunca como fornecedor | PE §1.1 |
| HG1 tier1/09, 10 | projeções de frota e mercado (2026 ~50.000; 2030 ~1 milhão; US$ 50 bi em 2030) | **fora** (sem fonte; mercado é dono do vla-v72 aula 8) | — |
| FTH 1.1 | "2025 – NOETIX BUMI (Brasil!)", "desenvolvido nacionalmente" | **fora** (não está nas pesquisas; não confirmado) | — |
| FTH 1.1 | "sim-to-real funciona 80–90% bem" | **fora** (sem fonte; sim-to-real é dono do curso 2) | — |
| PE §6.2 | competições 2026 | meia-maratona de Pequim 19/04/2026 em 50:26 e WHRG 2026 com 2.056 robôs **só como relatado** | PE §6.2 |

## Corpo, juntas e atuadores (aulas 2–4)

| fonte antiga | o que dizia | o que o curso diz agora | fonte (URL/data) |
|---|---|---|---|
| HG1 tier1.1/specs-comparacao | G1 "1.32m, 55kg, 35 GDL (standard)" | G1 1,32 m / ~35 kg; **23 GDL no base, 23–43 no EDU** (fato); o MJCF do Menagerie traz a versão de **29 GDL** e **33,3 kg** (medido) — a diferença para "~35 kg" é ensinada | https://www.unitree.com/g1 · MJCF (`abrir.py`) |
| HG1 tier1/03 | G1 "127 cm, 35 kg" (diverge do próprio HG1) | resolvido acima: 1,32 m (fato) | idem |
| HG1 tier1.1/hardware-anatomia | motores do G1: "quadril 180 Nm, 1:50 harmonic drive; joelho 250 Nm, 1:60; tornozelo 100 Nm" | o MJCF declara **joelho 139 N·m, quadril 88/139, tornozelo 50, ombro 25, punho 25 (roll) e 5 (pitch, yaw) N·m** (medido); fontes de revenda citam joelho 90 N·m (base) / 120 N·m (EDU) (**relatado**). Redução harmônica no G1: **fora** (a Unitree fala em PMSM de rotor interno + rolamento de rolos cruzados) | MJCF (`juntas.py`) · https://www.unitree.com/g1 · PE §1.1 |
| HG1 tier1/05 | QDD 5:1–10:1, "MIT Cheetah Motor usado no Unitree H1" | QDD ~5:1 a 20:1, um estágio, backdrivable (**relatado**, relatório da humanoid.guide); classificar o motor da Unitree como QDD é **incerto** e dito assim; "MIT Cheetah no H1": **fora** | https://humanoid.guide/humanoid-robot-actuation-report/ · PE §2.1 |
| HG1 tier1/05 | não fala de harmônico, planetário nem fuso de rolos | **mapa do corpo**: QDD (pernas de robôs de pesquisa), harmônico (braço/punho), planetário (meio-termo; Schaeffler CES 2026, 60–250 N·m), linear de fuso de rolos (joelho/tornozelo de humanoide grande, ex. Optimus) — tudo **relatado** | PE §2.1 |
| HG1 tier1/05 | faixas de torque "tornozelo 80–150, joelho 150–250, quadril 200–360 N·m" | substituído por números **lidos do MJCF** (G1 e H1) e pela medição do agachamento: joelho a 90° pede **31 N·m** por perna (22 % do limite do modelo) | MJCF (`torque_agachado.py`, 19/10/2026) |
| HG1 tier1/05 | Atlas hidráulico, 28 juntas, autonomia 20 min | só como história em uma linha (hidráulico aposentado; Atlas atual é elétrico) | VE §4 |

## Sensores e equilíbrio (aulas 5–6)

| fonte antiga | o que dizia | o que o curso diz agora | fonte (URL/data) |
|---|---|---|---|
| HG1 tier1.1/hardware-anatomia | G1: "sensores de força no pé 0–500 N, 1000 Hz"; IMU "BMI088 a 400 Hz" | a ficha oficial lista câmera de profundidade + LiDAR 3D, 4 microfones, encoder duplo; **sensor de força 6 eixos no pé não aparece** nas fichas lidas (**incerto**). O MJCF declara só **4 sensores (IMU no tronco e na pelve)**; a aula acrescenta força no tornozelo pela API e mostra a diferença para o contato | https://www.unitree.com/g1 · PE §2.3 · MJCF (`sensores.py`) |
| HG1 tier1/04 | "Optimus: sensores de torque nas 28 juntas", "só câmeras" | **fora** (sem fonte primária; PE §2.2 marca Optimus como incerto) | — |
| HG1 tier1/04 | pele tátil 20k sensores; preços de IMU/LiDAR de hobby | **fora**; tato só com fonte: Dex3-1 com matriz tátil opcional (fato), Sharpa Wave 1.000+ sensores por ponta (relatado) | PE §2.2 |
| — (HG1 só citava) | ZMP/CoM sem cálculo | CoM, polígono de apoio e CoP (= ZMP no chão plano) calculados no MJCF com empurrão: **15 N fica, 20–30 N sai do apoio e volta, 35–40 N cai** (empurrão de 0,2 s; medido) | `equilibrio.py` (19/10/2026) |

## Computação e energia (aula 7)

| fonte antiga | o que dizia | o que o curso diz agora | fonte (URL/data) |
|---|---|---|---|
| HG1 tier1.1/sistema-computacional, hardware-anatomia | "Jetson Orin NX como cérebro principal" do G1; versões EDU/Standard/Advanced com Orin Nano/NX/AGX | G1 vem com **CPU de 8 núcleos**; "módulo de alta computação" (Orin etc.) **só no EDU, opcional**; H2 traz Intel i5 (PC1) e i7 (PC2, EDU); K1 117 TOPS | https://www.unitree.com/g1 · https://www.unitree.com/H2 · https://www.booster.tech/booster-k1/ |
| HG1 tier1/10 | "Jetson Thor (2025): 2000 TOPS, 20 W, US$ 500–800" | Thor: ~2.070 TFLOPS FP4, 128 GB; dev kit US$ 3.499 (08/2025) → **US$ 5.499 em 07/2026** (relatado); Thor de catálogo só no **Booster T2** (relatado) | PE §2.3 · VM §3 |
| HG1 tier1.1/sistema-computacional | Ubuntu 20.04 + JetPack 5.1.2 + ROS 2 + Gazebo 11 + PyTorch 1.13 no G1 | **fora** (versões velhas e sem fonte atual; software de bordo é dono do curso 4) | — |
| HG1 tier1/05, 06 | hierarquia "Jetson 30 Hz, MCU 1000 Hz, driver 20 kHz" | camadas com fonte: Helix 02 **S0 1 kHz, S1 200 Hz, S2 7–9 Hz** (fato, Figure); PD 500 Hz–1 kHz no robô e política ~50 Hz como **típico nos repositórios citados** (síntese da PE §5); VLA 5–10 Hz | https://www.figure.ai/news/helix-02 · https://www.figure.ai/news/helix · PE §5 |
| HG1 tier1.1/energia-bateria | G1 "LiPo 12S, 48 V, 9000 mAh, 432 Wh", autonomias por modo (80 W/5 h…) | G1: **9.000 mAh, 13S, ~2 h** (fato); Wh = **conta derivada** 13 × 3,7 V × 9 Ah ≈ 433 Wh; potência média implícita ≈ 216 W. As autonomias por modo saem (sem fonte) | https://www.unitree.com/g1 · `autonomia.py` |
| HG1 tier1/07 | H1 "13S5P 48 V 15 Ah 720 Wh", "Unitree usa LFP" | H2: **15 Ah, 0,972 kWh, 75,6 V máx.** (fato), ~3 h (relatado); química da bateria Unitree: **fora** (não confirmada) | https://www.unitree.com/H2 · PE §1.1 |

## Simulação (aulas 2, 8 e todas as práticas)

| fonte antiga | o que dizia | o que o curso diz agora | fonte (URL/data) |
|---|---|---|---|
| FTH 1.2 | Webots R2023b + robô NAO como "primeiros passos" | **MuJoCo 3.16.0** (pip, 14/10/2026) + **MuJoCo Menagerie** (G1 29, H1 19, OP3 20, Booster T1 23 acionados — medidos); Webots/NAO não aparecem | https://mujoco.readthedocs.io/en/stable/changelog.html · https://github.com/google-deepmind/mujoco_menagerie |
| HG1 tier2 | "Gazebo Fortress" com saída do Gazebo Classic 11; Isaac Sim sem versão | não citado aqui; Isaac Sim 6.1 / Isaac Lab 3.0 EA / mjlab / MuJoCo Playground **só mostrados** como "o que se usa em escala" (GPU NVIDIA) com link | VE §2 · PE §3.4 |
| HG1 tier1.1 (ficha técnica) | copiar especificação do fabricante | ler o **MJCF**: `nq/nv/nu`, juntas, `actuatorfrcrange`, sensores, keyframes; comparar dois modelos por script | `abrir.py`, `juntas.py`, `comparar.py` |

## Ficou de fora por falta de fonte
- Torques e reduções por junta do G1 e do Optimus vindos do HG1; química das baterias Unitree; autonomia por modo de operação.
- Sensor de força/torque de 6 eixos no pé ou punho do G1 (as fichas lidas não citam).
- Projeções de frota e de mercado (2026–2030) e preços futuros.
- NOETIX Bumi; "MIT Cheetah no H1"; "G1+" (14/09/2026, fonte única).
- Comparação quantitativa MPC × RL em 2026 (PE: incerto) — a aula 6 só cita MPC como conceito.
