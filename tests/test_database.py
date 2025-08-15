<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>GEMS9 — Quiz Sport & Motivation</title>
<style>
  :root{
    --bg:#0b0b0f;
    --panel:#121218;
    --gold:#d4af37;
    --gold-soft:#caa24b;
    --text:#f2f2f2;
    --muted:#b9b9c3;
    --accent:#8a6f1a;
    --ok:#2fbf71;
    --warn:#e08a2e;
  }
  *{box-sizing:border-box}
  body{
    margin:0; background:radial-gradient(1200px 600px at 70% -20%,#1a1a22 0%, var(--bg) 55%);
    color:var(--text); font:16px/1.5 "Inter",-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
  }
  .wrap{max-width:980px;margin:0 auto;padding:24px}
  header{display:flex;align-items:center;justify-content:space-between;padding:12px 0 20px 0}
  .brand{display:flex;align-items:center;gap:12px}
  .gem{
    width:28px;height:28px;background:conic-gradient(from 0deg, var(--gold), #997a1b, var(--gold));
    clip-path:polygon(50% 0%, 85% 20%, 100% 60%, 50% 100%, 0% 60%, 15% 20%);
    filter:drop-shadow(0 0 8px rgba(212,175,55,.35));
  }
  h1{font-weight:700;font-size:22px;margin:0}
  .card{
    background:linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,0));
    border:1px solid rgba(212,175,55,.18);
    border-radius:14px; padding:22px; box-shadow:0 10px 30px rgba(0,0,0,.4);
  }
  .hero{display:grid;grid-template-columns:1.2fr .8fr;gap:22px}
  .cta{display:inline-block;background:var(--gold);color:#1b1b1b;font-weight:700;border-radius:12px;padding:14px 18px;text-decoration:none}
  .cta:hover{background:var(--gold-soft)}
  .muted{color:var(--muted)}
  .progress{height:8px;background:#1b1b23;border-radius:999px;overflow:hidden;border:1px solid rgba(212,175,55,.25)}
  .bar{height:100%;width:0;background:linear-gradient(90deg,var(--gold),#ae8b2e);transition:width .25s ease}
  .question{
    font-size:20px; font-weight:600; margin:12px 0 6px 0;
  }
  .scale{display:flex;gap:10px;margin-top:10px;flex-wrap:wrap}
  .btn{
    flex:1 1 80px; min-width:70px; text-align:center; padding:12px 10px; border-radius:12px; cursor:pointer;
    border:1px solid rgba(212,175,55,.25); background:#14141b; color:var(--text);
  }
  .btn:hover{border-color:var(--gold)}
  .btn.small{padding:8px 10px;min-width:auto;flex:0 0 auto}
  .kbd{font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; background:#1b1b23; padding:2px 6px; border-radius:6px; border:1px solid #2c2c35}
  .row{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
  .hide{display:none}
  .pill{display:inline-flex;align-items:center;gap:8px;padding:8px 10px;border-radius:999px;border:1px solid rgba(212,175,55,.25);background:#121218}
  .grid{display:grid;gap:14px}
  .two{grid-template-columns:1fr 1fr}
  .tag{font-weight:700;color:var(--gold)}
  .result{
    display:grid; gap:18px; grid-template-columns:1.1fr .9fr;
  }
  .badge{
    display:flex; align-items:center; gap:10px; padding:10px 12px; border-radius:12px; border:1px solid rgba(212,175,55,.25);
    background:#101016;
  }
  .list{margin:0;padding-left:18px}
  .list li{margin:6px 0}
  .note{font-size:13px;color:var(--muted)}
  footer{margin:26px 0 10px 0;color:var(--muted);text-align:center}
  @media (max-width:900px){
    .hero,.result{grid-template-columns:1fr}
  }
</style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="brand"><div class="gem"></div><h1>GEMS9 — Sport & Motivation</h1></div>
      <div class="pill"><span class="muted">Palette</span><span class="tag">Noir & Or</span></div>
    </header>

    <section id="screen-start" class="card hero">
      <div>
        <h2 style="margin:0 0 10px 0">Votre parcours commence ici</h2>
        <p class="muted">En 6–8 minutes, découvrez votre combinaison unique Ennéagramme + GEMS de Dani Johnson. Recevez un plan d’entraînement et de nutrition aligné à votre psychologie — élégant, efficace, sans surcharge.</p>
        <div class="row" style="margin:14px 0">
          <div class="pill">Femmes cadres 30–40 ans</div>
          <div class="pill">Salle de fitness</div>
          <div class="pill">Séances ≤ 45 min</div>
        </div>
        <a class="cta" href="#" id="btn-start">Commencer le quiz</a>
        <p class="note" style="margin-top:10px">Astuce: répondez au feeling. Raccourcis clavier <span class="kbd">1</span> … <span class="kbd">5</span>.</p>
      </div>
      <div class="card">
        <h3 style="margin-top:0">Prise en compte des blessures</h3>
        <p class="muted">Sélectionnez si besoin. Nous adapterons vos recommandations.</p>
        <div class="row">
          <label class="pill"><input type="checkbox" id="inj-knee" /> Genou</label>
          <label class="pill"><input type="checkbox" id="inj-shoulder" /> Épaule</label>
          <label class="pill"><input type="checkbox" id="inj-back" /> Dos</label>
        </div>
        <div style="height:10px"></div>
        <div class="progress"><div class="bar" style="width:0%"></div></div>
        <p class="note">La progression s’affichera ici pendant le quiz.</p>
      </div>
    </section>

    <section id="screen-quiz" class="card hide">
      <div class="row" style="justify-content:space-between">
        <div class="pill"><strong>Étapes:</strong>&nbsp;<span id="step-label">1/30</span></div>
        <div class="pill"><strong>Temps:</strong>&nbsp;<span id="timer">00:00</span></div>
      </div>
      <div style="height:12px"></div>
      <div class="progress"><div class="bar" id="progress"></div></div>
      <div style="height:14px"></div>
      <div id="qcard">
        <div class="muted" id="qmeta">Ennéagramme</div>
        <div class="question" id="qtext">…</div>
        <div class="muted">Votre accord</div>
        <div class="scale">
          <button class="btn" data-v="1">1<br><span class="muted" style="font-size:12px">Pas du tout</span></button>
          <button class="btn" data-v="2">2</button>
          <button class="btn" data-v="3">3</button>
          <button class="btn" data-v="4">4</button>
          <button class="btn" data-v="5">5<br><span class="muted" style="font-size:12px">Tout à fait</span></button>
        </div>
      </div>
      <div style="height:12px"></div>
      <div class="row">
        <button class="btn small" id="prev">← Précédent</button>
        <div style="flex:1"></div>
        <button class="btn small" id="skip">Passer</button>
        <button class="btn small" id="next">Suivant →</button>
      </div>
      <p class="note">Raccourcis: <span class="kbd">1</span> … <span class="kbd">5</span> pour répondre, <span class="kbd">←</span>/<span class="kbd">→</span> pour naviguer.</p>
    </section>

    <section id="screen-result" class="card hide">
      <h2 style="margin:0 0 8px 0">Votre profil premium</h2>
      <p class="muted" id="profile-line">…</p>
      <div class="result">
        <div class="card">
          <h3 style="margin-top:0">Recommandations immédiates</h3>
          <div class="grid">
            <div class="badge"><div class="gem"></div><div><strong>Ennéagramme:</strong> <span id="ennea-badge"></span></div></div>
            <div class="badge"><div class="gem"></div><div><strong>GEMS:</strong> <span id="gems-badge"></span></div></div>
          </div>
          <div style="height:10px"></div>
          <div class="grid two">
            <div>
              <h4 style="margin:8px 0">Plan d’entraînement (semaine type)</h4>
              <ul class="list" id="train-plan"></ul>
              <div id="inj-tips"></div>
            </div>
            <div>
              <h4 style="margin:8px 0">Nutrition & habitudes</h4>
              <ul class="list" id="nutrition"></ul>
              <h4 style="margin:12px 0 6px 0">Anti-sabotage</h4>
              <ul class="list" id="habits"></ul>
            </div>
          </div>
        </div>
        <div class="card">
          <h3 style="margin-top:0">Leviers et vigilances</h3>
          <ul class="list" id="levers"></ul>
          <h4 style="margin:12px 0 6px 0">Vigilances</h4>
          <ul class="list" id="risks"></ul>
          <div style="height:12px"></div>
          <div class="badge">
            <span class="tag">Prochaines 72 h</span>
            <span class="muted">3 micro-missions ajoutées à votre agenda</span>
          </div>
          <ul class="list" id="quests"></ul>
        </div>
      </div>
      <div style="height:12px"></div>
      <div class="row">
        <button class="btn small" id="restart">Recommencer</button>
        <div style="flex:1"></div>
        <button class="btn small" id="export">Exporter le profil (JSON)</button>
      </div>
    </section>

    <footer>© GEMS9 — Guide Sport & Motivation. Design noir & or.</footer>
  </div>

<script>
/* ---------- Données ---------- */

// 18 items Ennéagramme (2 par type) + 12 items GEMS (3 par gemme) = 30
const QUESTIONS = [
  // Ennéagramme
  {id:"E1A", domain:"ennea", sub:"1", text:"Je me sens bien quand les choses sont faites « comme il faut »."},
  {id:"E1B", domain:"ennea", sub:"1", text:"Les règles m’aident à avancer."},
  {id:"E2A", domain:"ennea", sub:"2", text:"Je capte vite ce dont les autres ont besoin."},
  {id:"E2B", domain:"ennea", sub:"2", text:"Aider me donne de l’énergie."},
  {id:"E3A", domain:"ennea", sub:"3", text:"J’adore battre des objectifs."},
  {id:"E3B", domain:"ennea", sub:"3", text:"Je m’adapte pour réussir."},
  {id:"E4A", domain:"ennea", sub:"4", text:"Je cherche l’authenticité, même si c’est intense."},
  {id:"E4B", domain:"ennea", sub:"4", text:"Mes ressentis guident mes choix."},
  {id:"E5A", domain:"ennea", sub:"5", text:"Comprendre le « pourquoi » me motive."},
  {id:"E5B", domain:"ennea", sub:"5", text:"J’économise mon énergie sociale."},
  {id:"E6A", domain:"ennea", sub:"6", text:"J’aime avoir un plan B."},
  {id:"E6B", domain:"ennea", sub:"6", text:"J’avance mieux avec de la clarté."},
  {id:"E7A", domain:"ennea", sub:"7", text:"La variété me garde engagée."},
  {id:"E7B", domain:"ennea", sub:"7", text:"Je transforme tout en jeu."},
  {id:"E8A", domain:"ennea", sub:"8", text:"Je protège mon autonomie."},
  {id:"E8B", domain:"ennea", sub:"8", text:"J’avance franchement, sans détour."},
  {id:"E9A", domain:"ennea", sub:"9", text:"La paix intérieure est prioritaire."},
  {id:"E9B", domain:"ennea", sub:"9", text:"Je progresse par petites actions calmes."},
  // GEMS (Dani Johnson)
  {id:"GS1", domain:"gems", sub:"sapphire", text:"Si c’est fun, je suis à fond."},
  {id:"GS2", domain:"gems", sub:"sapphire", text:"L’ambiance compte autant que le résultat."},
  {id:"GS3", domain:"gems", sub:"sapphire", text:"Je brille en groupe."},
  {id:"GR1", domain:"gems", sub:"ruby", text:"Donnez-moi un défi chiffré, je décolle."},
  {id:"GR2", domain:"gems", sub:"ruby", text:"J’aime prendre les rênes."},
  {id:"GR3", domain:"gems", sub:"ruby", text:"La compétition me stimule."},
  {id:"GE1", domain:"gems", sub:"emerald", text:"Un plan détaillé me rassure."},
  {id:"GE2", domain:"gems", sub:"emerald", text:"J’adore mesurer et optimiser."},
  {id:"GE3", domain:"gems", sub:"emerald", text:"Je préfère la précision à l’improvisation."},
  {id:"GP1", domain:"gems", sub:"pearl", text:"Aider ou inspirer me porte."},
  {id:"GP2", domain:"gems", sub:"pearl", text:"Le sens avant la vitesse."},
  {id:"GP3", domain:"gems", sub:"pearl", text:"J’aime des rituels qui comptent."}
];

// Leviers et risques Ennéagramme
const ENNEA_META = {
  "1": {name:"Type 1 — Perfectionniste", levers:["Routines claires","Critères de qualité","Checklist"], risks:["Rigidité","Autocritique excessive"]},
  "2": {name:"Type 2 — Serviable", levers:["Partenaire d’entraînement","Dimension relationnelle","Feedback bienveillant"], risks:["S’oublier","Difficulté à dire non"]},
  "3": {name:"Type 3 — Performeur", levers:["Objectifs chiffrés","Tableaux de bord","Feedback rapide"], risks:["Sur-identification aux résultats","Surmenage"]},
  "4": {name:"Type 4 — Créatif", levers:["Esthétique/playlist","Journal post-séance","Variété expressive"], risks:["Tout-ou-rien selon l’humeur","Isolement"]},
  "5": {name:"Type 5 — Investigateur", levers:["Protocoles précis","Logique/expérimentation","Limites de décision"], risks:["Rester dans la théorie","Économie d’énergie excessive"]},
  "6": {name:"Type 6 — Prévoyant", levers:["Plan B prêt","Binôme fixe","Checklists rassurantes"], risks:["Suranalyse","Inquiétude"]},
  "7": {name:"Type 7 — Épicurien", levers:["Variété planifiée","Sessions courtes et fun","Gamification"], risks:["Dispersion","Sur-accumulation de projets"]},
  "8": {name:"Type 8 — Protecteur", levers:["Objectifs ambitieux","Autonomie","Intensité cadrée"], risks:["Ignorer les signaux du corps","Conflit avec la récupération"]},
  "9": {name:"Type 9 — Pacificateur", levers:["Micro-démarrages","Environnement apaisant","Rituels doux"], risks:["Inertie","Procrastination douce"]}
};

// Leviers et risques GEMS
const GEMS_META = {
  sapphire:{name:"Sapphire (jeu & social)", levers:["Cours collectifs","Circuits fun","Playlists"], risks:["Dispersion","Inconstance si ambiance faible"]},
  ruby:{name:"Ruby (résultats & défi)", levers:["KPIs/PR","Intervalles structurés","Badges progrès"], risks:["Surintensité","Récup insuffisante"]},
  emerald:{name:"Emerald (structure & précision)", levers:["Programme écrit","Suivi métrique","Technique"], risks:["Paralysie par analyse","Rigidité"]},
  pearl:{name:"Pearl (valeurs & contribution)", levers:["Rituels","Groupe de soutien","Sens"], risks:["S’ignorer soi-même","Culpabilité"]}
};

/* ---------- État ---------- */
let idx=0;
const answers = {}; // id -> 1..5
let startedAt = null;

/* ---------- Helpers ---------- */
function $(sel){return document.querySelector(sel)}
function show(id){["#screen-start","#screen-quiz","#screen-result"].forEach(s=>$(s).classList.add("hide")); $(id).classList.remove("hide")}
function fmt(n){return n<10? "0"+n:n}
function updateTimer(){
  if(!startedAt) return;
  const s=Math.floor((Date.now()-startedAt)/1000);
  $("#timer").textContent = `${fmt(Math.floor(s/60))}:${fmt(s%60)}`
}
setInterval(updateTimer, 500);

/* ---------- Navigation ---------- */
function renderQuestion(){
  const q = QUESTIONS[idx];
  $("#step-label").textContent = `${idx+1}/${QUESTIONS.length}`;
  $("#qmeta").textContent = q.domain==="ennea" ? "Ennéagramme" : "GEMS";
  $("#qtext").textContent = q.text;
  const progress = Math.round(((idx)/QUESTIONS.length)*100);
  $("#progress").style.width = progress + "%";
  document.querySelectorAll(".scale .btn").forEach(b=>{
    const v = parseInt(b.dataset.v,10);
    const chosen = answers[q.id]===v;
    b.style.borderColor = chosen ? "var(--gold)" : "rgba(212,175,55,.25)";
    b.style.background = chosen ? "#181820" : "#14141b";
  });
}
function next(){
  if(idx < QUESTIONS.length-1){ idx++; renderQuestion(); }
  else finalize();
}
function prev(){
  if(idx>0){ idx--; renderQuestion(); }
}

/* ---------- Scoring ---------- */
function computeProfile(){
  const ennea = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0};
  const gems = {sapphire:0,ruby:0,emerald:0,pearl:0};
  QUESTIONS.forEach(q=>{
    const v = answers[q.id]||0;
    if(q.domain==="ennea") ennea[q.sub]+=v;
    else gems[q.sub]+=v;
  });
  const enneaSorted = Object.entries(ennea).sort((a,b)=>b[1]-a[1]);
  const gemsSorted = Object.entries(gems).sort((a,b)=>b[1]-a[1]);
  const enneaTop = enneaSorted[0][0], enneaWing = enneaSorted[1][0];
  const gemTop = gemsSorted[0][0], gemSecond = gemsSorted[1][0];
  return {
    enneaScores: ennea, gemsScores: gems,
    enneaTop, enneaWing,
    gemTop, gemSecond
  };
}

/* ---------- Recommandations ---------- */
function planForGems(g, minutes=40){
  // 4 gabarits, adaptés pour ≤45 min
  if(g==="ruby") return [
    "Force bas du corps (30–35 min) + finisher intervalles 8–10 min",
    "Cardio intervalles: 6 × 2 min RPE 7, récup 2 min",
    "Force haut du corps (30–35 min) + gainage 8 min",
    "Cardio zone 2 (30–40 min) ou 8–12k pas"
  ];
  if(g==="emerald") return [
    "Full body technique: 4 mouvements fondamentaux, 4×6–10, tempo contrôlé",
    "Cardio zone 2 (35–45 min), respiration nasale si possible",
    "Haut du corps + mobilité épaules 15 min",
    "Bas du corps + stabilité hanches/genoux 10 min"
  ];
  if(g==="sapphire") return [
    "Circuit fun: 6 mouvements, 30\"/30\", 4 tours",
    "Cours collectif (vélo/danse/boxing) 30–40 min",
    "Renfo minimaliste 3×8–12 (pousser/tirer/charnière/squat)",
    "Rando/steps 45–60 min avec podcast/musique"
  ];
  // pearl
  return [
    "Full body fondations + 1 rituel (2 min gratitude/sens)",
    "Cardio doux en nature 35–45 min, marche consciente",
    "Fonctionnel: farmer carry, sled, marches",
    "Séance communautaire avec une amie/coach"
  ];
}
function nutritionForGems(g){
  if(g==="ruby") return [
    "Objectif protéines: 1,6–2,2 g/kg/jour, 3–4 prises",
    "Suivi simple: poids hebdo, pas/jour, macro approximatives",
    "Assiette: 1/2 légumes, 1/4 protéines, 1/4 féculents complets"
  ];
  if(g==="emerald") return [
    "Template repas hebdo + liste de courses standard",
    "Traquer portion/structure plutôt que calories millimétrées",
    "Hydratation: 1 grand verre d’eau avant chaque repas"
  ];
  if(g==="sapphire") return [
    "Recettes colorées prêtes en ≤15 min, batch-cooking musical",
    "Dîners sociaux « light »: priorité protéines + légumes",
    "1–2 repas flex/sem., retour au plan dès le repas suivant"
  ];
  return [
    "Relier chaque choix à une valeur (santé, exemple pour proches)",
    "Cuisiner pour/avec quelqu’un 2×/sem.",
    "Marche digestive 10–15 min après le dîner"
  ];
}
function habitsUniversal(){
  return [
    "Règle des 2: jamais 2 jours off d’affilée",
    "Si–Alors: « Si je rate ma séance, alors 20 min de marche + 30 pompes réparties »",
    "Tenue prête la veille; snacks protéinés visibles"
  ];
}
function injuryTips({knee,shoulder,back}){
  const tips=[];
  if(knee) tips.push("Genou: privilégiez vélo/rameur; fentes arrière plutôt qu’avant; limiter flexion profonde et impacts.");
  if(shoulder) tips.push("Épaule: évitez développés au-dessus de la tête au début; favorisez tirages horizontaux; charge légère, amplitude sans douleur.");
  if(back) tips.push("Dos: charnière de hanche technique; gainage (plank, bird-dog); évitez crunchs dynamiques lourds.");
  return tips;
}

/* ---------- UI Binding ---------- */
function finalize(){
  const prof = computeProfile();
  // Titre
  const eMeta = ENNEA_META[prof.enneaTop];
  const eWing = ENNEA_META[prof.enneaWing];
  const gMeta = GEMS_META[prof.gemTop];
  const gSecond = GEMS_META[prof.gemSecond];
  $("#profile-line").textContent = `Ennéagramme: ${eMeta.name} (aile ${prof.enneaWing}) · GEMS: ${gMeta.name} (+ ${gSecond.name})`;
  $("#ennea-badge").textContent = `${eMeta.name} (aile ${prof.enneaWing})`;
  $("#gems-badge").textContent = `${gMeta.name} + ${gSecond.name}`;

  // Plan entraînement
  const basePlan = planForGems(prof.gemTop);
  $("#train-plan").innerHTML = basePlan.map(x=>`<li>${x}</li>`).join("");

  // Blessures
  const inj = {
    knee: $("#inj-knee").checked,
    shoulder: $("#inj-shoulder").checked,
    back: $("#inj-back").checked
  };
  const it = injuryTips(inj);
  $("#inj-tips").innerHTML = it.length ? `<h4 style="margin:12px 0 6px 0">Adaptations blessures</h4><ul class="list">${it.map(x=>`<li>${x}</li>`).join("")}</ul>` : "";

  // Nutrition & habitudes
  const nut = nutritionForGems(prof.gemTop);
  $("#nutrition").innerHTML = nut.map(x=>`<li>${x}</li>`).join("");
  $("#habits").innerHTML = habitsUniversal().map(x=>`<li>${x}</li>`).join("");

  // Leviers et risques (fusion Ennéagramme+GEMS)
  const levers = [...eMeta.levers.slice(0,2), ...GEMS_META[prof.gemTop].levers.slice(0,2)];
  const risks = [...eMeta.risks.slice(0,2), ...GEMS_META[prof.gemTop].risks.slice(0,1)];
  $("#levers").innerHTML = levers.map(x=>`<li>${x}</li>`).join("");
  $("#risks").innerHTML = risks.map(x=>`<li>${x}</li>`).join("");

  // Quêtes 72 h
  const quests = [
    "Bloquez 2 créneaux de 45 min dans l’agenda (non négociables).",
    "Faites votre première séance selon le plan ci-dessus.",
    "Préparez 2 repas protéinés simples pour les 48 prochaines heures."
  ];
  $("#quests").innerHTML = quests.map(x=>`<li>${x}</li>`).join("");

  // Progress finale
  document.querySelectorAll(".bar").forEach(b=>b.style.width="100%");
  show("#screen-result");
}

function startQuiz(){
  startedAt = Date.now();
  idx=0;
  renderQuestion();
  show("#screen-quiz");
}

function exportJSON(){
  const prof = computeProfile();
  const inj = {
    knee: $("#inj-knee").checked,
    shoulder: $("#inj-shoulder").checked,
    back: $("#inj-back").checked
  };
  const payload = {
    timestamp: new Date().toISOString(),
    answers, profile: prof, injuries: inj
  };
  const blob = new Blob([JSON.stringify(payload,null,2)],{type:"application/json"});
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "gems9-profil.json";
  a.click();
  URL.revokeObjectURL(a.href);
}

/* ---------- Events ---------- */
$("#btn-start").addEventListener("click",(e)=>{e.preventDefault(); startQuiz();});
document.querySelectorAll(".scale .btn").forEach(b=>{
  b.addEventListener("click",()=>{
    const v = parseInt(b.dataset.v,10);
    const q = QUESTIONS[idx];
    answers[q.id]=v;
    // auto next after slight delay
    renderQuestion();
    setTimeout(next, 120);
  });
});
$("#next").addEventListener("click", next);
$("#prev").addEventListener("click", prev);
$("#skip").addEventListener("click", ()=>{ next(); });
$("#restart").addEventListener("click", ()=>{ Object.keys(answers).forEach(k=>delete answers[k]); startedAt=null; document.querySelectorAll("input[type=checkbox]").forEach(i=>i.checked=false); document.querySelectorAll(".bar").forEach(b=>b.style.width="0%"); show("#screen-start");});
$("#export").addEventListener("click", exportJSON);

window.addEventListener("keydown",(e)=>{
  if($("#screen-quiz").classList.contains("hide")) return;
  if(e.key>="1" && e.key<="5"){
    const v=parseInt(e.key,10);
    const q=QUESTIONS[idx];
    answers[q.id]=v;
    renderQuestion();
    setTimeout(next, 100);
  } else if(e.key==="ArrowRight"){ next(); }
    else if(e.key==="ArrowLeft"){ prev(); }
});

document.addEventListener("DOMContentLoaded", ()=>{
  // Seed progress bar on start card
  document.querySelector("#screen-start .bar").style.width="0%";
});
</script>
</body>
</html>
