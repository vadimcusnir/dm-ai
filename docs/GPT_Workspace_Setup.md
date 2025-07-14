
# 🧠 GPT Workspace Setup – Playbook „Omul Viitorului”

> Ghid complet pentru configurarea unui spațiu GPT personalizat care execută sarcini pe fiecare funcție din departament: de la hook la KPI report.

---

## ⚙️ Setup General

### 1. Creează GPT dedicat
- Nume: `Omul Viitorului – Content Ops`
- Identitate: Stil direct, semiotic, Retorică Fără Anestezie
- Voice: Provocator, simbolic, orientat pe conversie

### 2. Activează următoarele funcționalități:
- Browsing (dacă folosești date externe)
- Code interpreter (pentru KPI)
- File upload (pentru rulare prompturi pe fișiere Notion/CSV)
- Memory (pentru păstrare context per rol)

---

## 🔁 Structura GPT pe Roluri

### 🔹 HookForge (HS)
- Prompt principal: paradoxuri, tensionare, captare atenție
- Output: 10 hook-uri sub 15 cuvinte
- Format: listă brută + variantă în stilul Cușnir

---

### 🔹 ScriptSanctum (CA)
- Prompt: outline → manifest (700–800c) + format Cover–Verdict
- Output: articol, email sau text pentru carousel

---

### 🔹 ArchiveOracle (AO)
- Prompt: transcript brut → citate cu impact
- Output: 3 replici max 20 cuvinte cu tensiune narativă

---

### 🔹 GlyphLab (GA)
- Prompt: text-to-image prompt creator
- Output: comenzi pentru DALL·E / Midjourney (stil OV)

---

### 🔹 CarouselForge (CE)
- Prompt: transformă articol → 10 slide-uri JSON
- Output: Figma import-ready structure

---

### 🔹 VideoRitualist (VR)
- Prompt: manifest → scenariu 90s → storyboard descriptiv
- Output: script narativ + voiceover + scene breakdown

---

### 🔹 PulseDispatcher (PD)
- Prompt: conținut → canal optim
- Output: tabel content-type x platform x CTA

---

### 🔹 CommentSentinel (CS)
- Prompt: comentariu → replică tăioasă în max 30 cuvinte
- Output: ton Cușnir, fără scuze, cu subtext

---

### 🔹 KPI Narrator (DA)
- Prompt: metrici brute → insight + acțiune recomandată
- Output: raport de 200 cuvinte

---

### 🔹 EchoRecomposer (ER)
- Prompt: conținut performant → 3 remixuri alternative
- Output: tip remix, format, canal, CTA

---

## 🧱 Recomandări Tehnice

- Fiecare funcție = prompt preset separat în GPT
- Păstrează un `.md` pentru fiecare rol ca documentație
- Leagă GPT Workspace la Make pentru execuție în lanț

---

**GPT-ul nu e asistent. E membru de echipă. Dă-i sarcină, ton, format, și va livra.**

