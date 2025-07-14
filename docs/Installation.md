
# ⚙️ Installation Guide – Setup Playbook „Omul Viitorului”

> Ghid complet pentru implementarea practică a întregului sistem: Notion + GPT + Make (sau Zapier) + Metabase + Figma.

---

## 🧱 1. Notion – Structura Digitală

### 🔹 Pași:
1. Creează o bază de date „📦 Săptămâna în Derulare” (Kanban)
2. Creează template-uri:
   - „Content Card” (hook, carousel, video etc.)
   - „Remix Card”
   - „Sinteză Săptămânală”
3. Creează paginile statice:
   - `index.md`, `structura.md`, `kpis.md`, etc.
4. Activează Reminder-uri pentru:
   - Check-in zilnic
   - Raport KPI miercuri + vineri

---

## 🤖 2. GPT – Automatizarea Prompturilor

### 🔹 Pași:
1. Creează GPT Workspace separat: „Content Ops OV”
2. Încarcă prompturile din `omul_v_content_dep_ai_prompturi.md`
3. Creează un chain pentru fiecare funcție (ex: HookForge, ScriptSanctum)
4. Leagă Webhook GPT la Make/Zapier

---

## 🔁 3. Make (sau Zapier) – Flux Automatizat

### 🔹 Triggere și acțiuni recomandate:

| Scenariu | Trigger | Acțiune |
|----------|---------|---------|
| Task nou în Notion | New Entry | Trimite prompt la GPT |
| Output GPT valid | Webhook Response | Scrie în câmp Notion |
| Deadline apropiat | Time filter | Notificare Slack / Email |
| Nou conținut aprobat | Status = „Aprobat” | Trimite spre distribuție Buffer |

---

## 📊 4. KPI Dashboard – Metabase / GA4

### 🔹 Pași:
1. Creează colecție nouă „OV Content KPIs”
2. Setează următorii indicatori:
   - Hook CTR
   - Save Rate
   - Cost per Lead
   - VIP conversion rate
3. Exportă săptămânal PDF automat în Notion

---

## 🎨 5. Figma – Design Vizual

### 🔹 Setup:
1. Creează dosar comun „Omul Viitorului – Visuals”
2. Subfoldere: Glyphs, Carousels, Storyboards
3. Creează template Figma cu layout de carousel 10 slide

---

## 🔐 6. Recomandări de Securitate

- Accese GPT limitate per funcție
- Integrează Notion + Make + GPT prin webhook-uri cu token
- Folosește un workspace izolat pentru prompturi

---

## 🟢 Ready?

După setup, rulează prima săptămână:
- Planificare → Execuție → Distribuție → KPI → Remix

✅ Dacă rulează bine – ești gata pentru licențiere externă.

---

**Un sistem bun nu are nevoie să fie explicat zilnic. Se instalează o dată și decide în locul tău.**

