
# Prompturi GPT – Departamentul Content Marketing „Omul Viitorului”

> Acest fișier conține lanțurile de prompturi GPT standardizate, organizate pe roluri și funcții. Ele permit execuția automată a conținutului, fără pierdere de stil, tensiune sau conversie.

---

## 📍 C1 – SCRIPTORIUM (Conținut Scris)

### 🔹 HS – Manager Engagement & Hook-uri
**Prompt:**  
> `Avatar tension: {X}`  
> „Generează 10 hook-uri sub 15 cuvinte, bazate pe paradox, în stil Retorică Fără Anestezie.”

---

### 🔹 CA – Strateg Senior Conținut  
**Prompt Chain:**  
1. `Input: hook aprobat + temă`  
2. `Transformă în manifest de 700–800 cuvinte, cu 1 paradox, 1 trădare, 1 verdict.`  
3. `Formatează în: Cover – Declanșator – Conținut – Verdict – Întrebare.`

---

### 🔹 AO – Manager Arhivă & Reciclare  
**Prompt:**  
> `Transcript: {X}`  
> „Extrage 3 replici cu potențial viral, max. 20 cuvinte, care provoacă identitate.”

---

## 🎨 C2 – VISUARION (Conținut Vizual)

### 🔹 GA – Identitate Vizuală  
**Prompt DALL·E / MJ:**  
> „Symbolic glyph, gas mask, post-apocalyptic, neon green/red, black background, minimalist geometry.”

---

### 🔹 CE – Storytelling Vizual  
**Prompt Chain:**  
1. `Input: manifest aprobat`  
2. `Construiește 10 slide-uri în format Cover – Conflict – Paradox – Verdict – CTA`  
3. `Livrare: JSON pt. Figma Import`

---

### 🔹 VR – Video Manager  
**Prompt Chain:**  
1. `Input: articol lung`  
2. `Scrie scenariu video 90 sec – 5 scene, fiecare cu simbol + emoție + voce interioară.`  
3. `Output: storyboard descriptiv + voiceover text`

---

## 📡 C3 – PULSARIUM (Distribuție & KPI)

### 🔹 PD – Distribuție  
**Prompt:**  
> `Livrabile săptămânale`  
> „Asociază fiecare postare cu canalul optim: Instagram, Telegram, YouTube Shorts etc.”

---

### 🔹 DA – Insights  
**Prompt:**  
> `Raw KPI data`  
> „Extrage insight principal + 2 recomandări strategice în 200 cuvinte.”

---

### 🔹 ER – Repurposing  
**Prompt Chain:**  
1. `Input: top 3 postări`  
2. `Transformă: articol → reel, carousel → newsletter, hook → short email.`

---

### 🔹 CS – Community Response  
**Prompt:**  
> `Comentariu critic: {X}`  
> „Răspunde în 30 cuvinte, ton ferm, fără scuze, stil Cușnir. Include subtext de control.”

---

## ⚙️ Configurare Tehnică

- Toate prompturile se livrează prin Make → Webhook → GPT → Notion Output
- Variantele de failover includ fallback GPT completat de om
- Prompturile pot fi încorporate în GPT Workspace dedicat: `Omul Viitorului GPT Ops`

---

**Promptul nu e text. E vector de comandă.**

