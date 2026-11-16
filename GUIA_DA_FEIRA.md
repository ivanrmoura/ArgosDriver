# 🚗 ArgosDriver AI: Guia da Feira de Ciências & Segurança Viária

Guia prático para a equipe montar o estande mais impactante e cinematográfico da feira!

---

## 🎯 1. O Problema e a Conexão Social

O **ArgosDriver AI** combate um dos fatores mais letais nas rodovias mundiais: **o sono ao volante e a distração com o celular**.

- **Dados da Polícia Rodoviária Federal (PRF) & ABRAMET:** A sonolência e o cansaço são a **segunda maior causa de mortes** no trânsito brasileiro.
- **O Cálculo do Risco:** A **80 km/h**, um motorista percorre **22 metros por segundo**. Fechar os olhos por apenas 2 segundos significa atravessar **44 metros às cegas** — mais do que o comprimento de uma quadra poliesportiva!
- **Conexão ODS da ONU:** **Meta 3.6** (Reduzir pela metade as mortes e os ferimentos globais por acidentes em estradas).

---

## 🚦 2. As 8 Situações de Risco Monitoradas pelo Sistema

| Situação | Algoritmo / Parâmetro | Reação do Cockpit |
| :--- | :--- | :--- |
| **1. Micro-Sono** | $EAR < 0.20$ por > 0.8s | 🚨 Pára-brisa vermelho + Buzina automotiva + Metros às cegas |
| **2. Bocejo de Fadiga** | $MAR > 0.50$ sustentado | 🥱 Aviso amarelo + Bips + Contador de bocejos incrementado |
| **3. Distração Lateral** | $|Yaw| > 0.16$ (olhando pros lados) | 👀 Aviso de retorno de atenção à pista |
| **4. Celular no Ouvido** | Mão na região auricular por > 2s | 📱 Alarme de infração gravíssima (DETRAN) |
| **5. Cabeça Desabando** | $\Delta Y_{nariz} > 0.045$ brusco | ⚡ Alerta de cochilo profundo (Head Nodding) |
| **6. Condutor Ausente** | 0 marcos faciais por > 1s em movimento | 👤 Protocolo de parada de emergência / Mal súbito |
| **7. Fadiga Acumulada** | Tempo contínuo de direção > limite | ☕ Alerta da Lei do Motorista (Lei nº 13.103) sugerindo parada |
| **8. Condutor Alerta** | EAR alto, MAR baixo, olhar centrado | 🟢 Painel verde holográfico com 100% de prontidão |

---

## 🏎️ 3. Montagem Física do Estande (O "Cockpit do Carro")

Para chamar a atenção de todos os visitantes:
1. **O Volante Real ou Simulador:**
   - Coloque um **volante de brinquedo** ou um volante de videogame preso à mesa em frente à cadeira do visitante.
2. **O "Pára-Brisa":**
   - O monitor fica logo atrás do volante com o **ArgosDriver AI** aberto em tela cheia (**F11**).
   - O visual holográfico azul/ciano simula o painel de um carro autônomo moderno (como Tesla ou Volvo).
3. **A Cadeira do Motorista:**
   - Uma cadeira confortável onde os jurados possam se sentar e "dirigir".
4. **Um Celular Cenográfico:**
   - Deixe um smartphone na mesa para o jurado fingir que está atendendo ou olhando mensagem para disparar os sensores!

---

## 🎤 4. Roteiro de Fala para os Jurados (Dividido em 3 Alunos)

### Aluno 1: O Impacto e a Realidade das Estradas (1 minuto)
> *"Boa tarde, jurados! Vocês sabiam que dormir ao volante mata mais do que a ingestão de álcool em diversas rodovias do Brasil? A 80 por hora, se você piscar mais demorado ou fechar o olho por 2 segundos, seu carro vira um projétil de duas toneladas desgovernado por quase 50 metros. Para salvar vidas utilizando a Inteligência Artificial e alinhados à Meta 3.6 da ONU, desenvolvemos o **ArgosDriver AI**."*

### Aluno 2: Demonstração Prática no Cockpit (1 a 2 minutos)
> *(Convida o jurado para segurar o volante ou o aluno senta na cadeira)*
> *"Observem: nossa câmera monitora 8 situações críticas de segurança viária em tempo real.
> - Se eu estiver dirigindo normalmente, o painel fica verde com 100% de atenção.
> - Se eu bocejar, a IA registra a abertura dos lábios e orienta uma parada para descanso.
> - Se eu fechar os olhos entrando em micro-sono ou se minha cabeça desabar para frente num tranco de sono, o sistema dispara a buzina do carro e calcula os metros percorridos às cegas!
> - E se o motorista sofrer um mal súbito ou desmaiar, o sistema percebe a ausência na direção e ativa o protocolo de emergência!"*

### Aluno 3: A Engenharia de Visão Computacional (1 a 2 minutos)
> *"Tecnicamente, como funciona por trás dos panos?
> - Utilizamos a malha **MediaPipe Face Mesh**, rastreando 468 marcos tridimensionais do rosto humano a 30 FPS.
> - Para os olhos, implementamos a equação científica **EAR (Eye Aspect Ratio)**, calculando a razão entre a abertura das pálpebras e a largura dos olhos.
> - Para a boca, usamos o **MAR (Mouth Aspect Ratio)** para distinguir fala de bocejos reais.
> - Para a cabeça, medimos a aceleração vertical da cervical para flagrar o reflexo de queda (*head nodding*).
> - E tudo isso roda 100% no computador local pelo navegador, garantindo a privacidade total do motorista e conformidade com a LGPD!"*

---

## 🚀 5. Como Executar

1. **No Navegador (Aplicação Principal):**
   - Abra [`index.html`](file:///C:/Users/ivanr/.gemini/antigravity/scratch/safedriver-ai/index.html) no Chrome ou Edge.
   - Pressione **F11** para tela cheia e ligue as caixas de som!
2. **Em Python (Para demonstração de código aos professores):**
   - Execute:
     ```bash
     python safedriver_detector.py
     ```
