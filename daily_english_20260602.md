<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>每日英文練習 — 2026/06/02</title>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=DM+Mono:wght@400;500&family=Noto+Sans+TC:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #f7f5f0;
    --bg-card: #ffffff;
    --bg-dark: #1a1917;
    --text: #1a1917;
    --text-muted: #6b6860;
    --text-light: #9b9890;
    --accent: #c84b2f;
    --accent-light: #f5ebe7;
    --accent2: #2d6a4f;
    --accent2-light: #e8f5ee;
    --border: #e8e4dc;
    --shadow: 0 2px 12px rgba(26,25,23,0.08);
    --radius: 10px;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Noto Sans TC', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    padding: 0 0 60px;
  }
  header {
    background: var(--text);
    color: #f7f5f0;
    padding: 28px 24px 22px;
    position: sticky;
    top: 0;
    z-index: 100;
  }
  header .meta {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #9b9890;
    letter-spacing: 0.08em;
    margin-bottom: 6px;
  }
  header h1 {
    font-family: 'Lora', serif;
    font-size: 20px;
    font-weight: 600;
    color: #f7f5f0;
  }
  .speed-bar {
    background: #2a2926;
    padding: 10px 24px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .speed-bar label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #9b9890;
    letter-spacing: 0.06em;
  }
  .speed-bar input[type=range] {
    flex: 1;
    accent-color: var(--accent);
    height: 3px;
    max-width: 160px;
  }
  .speed-bar span {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #f7f5f0;
    min-width: 32px;
  }
  .main { max-width: 680px; margin: 0 auto; padding: 24px 16px 0; }

  /* Section tabs */
  .tabs {
    display: flex;
    gap: 4px;
    margin-bottom: 20px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 4px;
  }
  .tab-btn {
    flex: 1;
    padding: 8px 4px;
    border: none;
    background: transparent;
    border-radius: 7px;
    font-family: 'Noto Sans TC', sans-serif;
    font-size: 13px;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.18s;
  }
  .tab-btn.active {
    background: var(--text);
    color: #f7f5f0;
    font-weight: 500;
  }

  /* Section panels */
  .panel { display: none; }
  .panel.active { display: block; }

  /* Paragraph cards */
  .para-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 18px 18px 14px;
    margin-bottom: 12px;
    box-shadow: var(--shadow);
  }
  .para-text {
    font-family: 'Lora', serif;
    font-size: 16px;
    line-height: 1.75;
    color: var(--text);
    margin-bottom: 12px;
  }
  .para-text .word {
    cursor: pointer;
    border-bottom: 1px dotted transparent;
    transition: border-color 0.15s, color 0.15s;
    border-radius: 2px;
    padding: 0 1px;
  }
  .para-text .word:hover {
    border-bottom-color: var(--accent);
    color: var(--accent);
  }
  .para-actions {
    display: flex;
    gap: 8px;
    align-items: center;
  }
  .btn-play {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border: 1px solid var(--accent);
    background: var(--accent-light);
    color: var(--accent);
    border-radius: 20px;
    font-size: 13px;
    font-family: 'DM Mono', monospace;
    cursor: pointer;
    transition: all 0.15s;
  }
  .btn-play:hover { background: var(--accent); color: white; }
  .btn-play.playing { background: var(--accent); color: white; }
  .btn-play svg { width: 14px; height: 14px; flex-shrink: 0; }
  .hint {
    font-size: 11px;
    color: var(--text-light);
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.04em;
  }

  /* Vocab cards */
  .vocab-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 16px 18px;
    margin-bottom: 12px;
    box-shadow: var(--shadow);
  }
  .vocab-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 8px;
    gap: 12px;
  }
  .vocab-word {
    font-family: 'Lora', serif;
    font-size: 20px;
    font-weight: 600;
    color: var(--text);
  }
  .vocab-pos {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--text-light);
    margin-top: 3px;
  }
  .vocab-phonetic {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--accent);
    background: var(--accent-light);
    padding: 4px 10px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.15s;
    white-space: nowrap;
  }
  .vocab-phonetic:hover { background: var(--accent); color: white; }
  .vocab-zh {
    font-size: 13px;
    color: var(--text-muted);
    margin-bottom: 6px;
  }
  .vocab-note {
    font-size: 13px;
    color: var(--text);
    line-height: 1.6;
    border-left: 2px solid var(--accent-light);
    padding-left: 10px;
  }
  .vocab-example {
    margin-top: 8px;
    font-family: 'Lora', serif;
    font-style: italic;
    font-size: 14px;
    color: var(--accent2);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }
  .vocab-example:hover { text-decoration: underline; }

  /* Key sentences */
  .sentence-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent2);
    border-radius: var(--radius);
    padding: 16px 18px;
    margin-bottom: 12px;
    box-shadow: var(--shadow);
  }
  .sentence-en {
    font-family: 'Lora', serif;
    font-size: 15px;
    line-height: 1.65;
    color: var(--text);
    margin-bottom: 6px;
    cursor: pointer;
  }
  .sentence-en:hover { color: var(--accent2); }
  .sentence-zh {
    font-size: 13px;
    color: var(--text-muted);
    margin-bottom: 10px;
  }
  .sentence-note {
    font-size: 12px;
    color: var(--text-light);
    line-height: 1.5;
  }

  /* Toast */
  .toast {
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%) translateY(20px);
    background: var(--text);
    color: #f7f5f0;
    padding: 8px 18px;
    border-radius: 20px;
    font-size: 13px;
    font-family: 'DM Mono', monospace;
    opacity: 0;
    transition: all 0.25s;
    pointer-events: none;
    z-index: 200;
  }
  .toast.show {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }

  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.1em;
    color: var(--text-light);
    margin-bottom: 14px;
    text-transform: uppercase;
  }
</style>
</head>
<body>

<header>
  <div class="meta">2026.06.02 — TOEIC 700 — Day 4</div>
  <h1>資料庫工程師的一天</h1>
</header>

<div class="speed-bar">
  <label>語速</label>
  <input type="range" id="speedRange" min="0.5" max="1.5" step="0.1" value="0.9">
  <span id="speedVal">0.9×</span>
</div>

<div class="main">
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('reading')">朗讀練習</button>
    <button class="tab-btn" onclick="switchTab('vocab')">術語發音</button>
    <button class="tab-btn" onclick="switchTab('sentences')">核心句型</button>
  </div>

  <!-- Panel 1: Reading -->
  <div class="panel active" id="panel-reading">
    <p class="section-label">點單字聽發音 · 點按鈕聽整段</p>

    <div class="para-card">
      <div class="para-text" id="p1"></div>
      <div class="para-actions">
        <button class="btn-play" onclick="playPara(0)">
          <svg viewBox="0 0 16 16" fill="currentColor"><polygon points="3,2 13,8 3,14"/></svg>
          聽整段
        </button>
        <span class="hint">或點單字單獨聽</span>
      </div>
    </div>

    <div class="para-card">
      <div class="para-text" id="p2"></div>
      <div class="para-actions">
        <button class="btn-play" onclick="playPara(1)">
          <svg viewBox="0 0 16 16" fill="currentColor"><polygon points="3,2 13,8 3,14"/></svg>
          聽整段
        </button>
      </div>
    </div>

    <div class="para-card">
      <div class="para-text" id="p3"></div>
      <div class="para-actions">
        <button class="btn-play" onclick="playPara(2)">
          <svg viewBox="0 0 16 16" fill="currentColor"><polygon points="3,2 13,8 3,14"/></svg>
          聽整段
        </button>
      </div>
    </div>

    <div class="para-card">
      <div class="para-text" id="p4"></div>
      <div class="para-actions">
        <button class="btn-play" onclick="playPara(3)">
          <svg viewBox="0 0 16 16" fill="currentColor"><polygon points="3,2 13,8 3,14"/></svg>
          聽整段
        </button>
      </div>
    </div>

    <div class="para-card">
      <div class="para-text" id="p5"></div>
      <div class="para-actions">
        <button class="btn-play" onclick="playPara(4)">
          <svg viewBox="0 0 16 16" fill="currentColor"><polygon points="3,2 13,8 3,14"/></svg>
          聽整段
        </button>
      </div>
    </div>
  </div>

  <!-- Panel 2: Vocab -->
  <div class="panel" id="panel-vocab">
    <p class="section-label">點音標聽發音 · 點例句聽完整句</p>

    <div id="vocab-list"></div>
  </div>

  <!-- Panel 3: Sentences -->
  <div class="panel" id="panel-sentences">
    <p class="section-label">點英文句子聽朗讀</p>
    <div id="sentence-list"></div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
const paragraphs = [
  "Today is Tuesday, but it was a pivotal day for the project, because I made a decision to hit the brakes.",
  "In the morning, I completed the fifth round of simulation testing. It was the best round so far: across 100 scenarios, zero gaps, zero filtering failures, 98 valid answers, and an average answer length of 696 characters. I also upgraded the test script to v3, adding an AI scoring feature — it lets Claude grade each answer across three dimensions, relevance, actionability, and completeness, and writes the scores back to the database.",
  "But the truly important thing today was a discovery. I had originally planned to spend a week tagging every solution in the database with the industries it fits, so the search could return different results per industry. But before diving in, I ran a database diagnostic first — and it turned out my assumption was wrong.",
  "The data showed that most solutions are inherently generic: a cloud antivirus tool for small businesses is the same product whether you sell it to a restaurant or a bank. The database simply does not contain anything like a finance-specific security solution. So even if I tagged the industries, hard-filtering by them would only empty out the search results and create gaps instead.",
  "So I decided to hit the brakes, abandon the original tagging plan, and take a different path: keep the same pool of candidate solutions, but apply a soft ranking based on each industry's concerns — floating the relevant solutions to the top without removing any. The lesson I took away: spending one hour on diagnosis before committing to heavy engineering can save you an entire week of wasted work. Knowing when to pull back is more professional than stubbornly pushing forward."
];

const vocabData = [
  {
    word: "Diagnostic",
    pos: "n. / adj.",
    zh: "診斷 / 診斷的",
    phonetic: "dye-ag-NOS-tik",
    ipa: "/ˌdaɪ.əɡˈnɒs.tɪk/",
    note: "在投入開發前先檢查資料或系統現況。展現嚴謹的關鍵字。",
    example: "I ran a diagnostic first."
  },
  {
    word: "Assumption",
    pos: "n.",
    zh: "假設",
    phonetic: "uh-SUMP-shun",
    ipa: "/əˈsʌmp.ʃən/",
    note: "尚未驗證的前提。願意承認假設錯誤是資深工程師的特質。",
    example: "My assumption was wrong."
  },
  {
    word: "Inherently",
    pos: "adv.",
    zh: "本質上、天生地",
    phonetic: "in-HAIR-ent-lee",
    ipa: "/ɪnˈhɪə.rənt.li/",
    note: "強調事物的根本性質，比 simply 更精確有力。",
    example: "Most solutions are inherently generic."
  },
  {
    word: "Hard-filter",
    pos: "v.",
    zh: "硬篩",
    phonetic: "HARD FIL-ter",
    ipa: "/hɑːrd ˈfɪl.tər/",
    note: "會「移除」不符合條件的資料，風險是清空結果。",
    example: "Hard-filtering would empty out the results."
  },
  {
    word: "Soft ranking",
    pos: "n.",
    zh: "軟性排序",
    phonetic: "SOFT RANK-ing",
    ipa: "/sɒft ˈræŋ.kɪŋ/",
    note: "只「重排」順序、不移除資料。搜尋系統設計的核心概念。",
    example: "Apply a soft ranking based on industry concerns."
  },
  {
    word: "Candidate pool",
    pos: "n.",
    zh: "候選池",
    phonetic: "KAN-di-dut POOL",
    ipa: "/ˈkæn.dɪ.dət puːl/",
    note: "經初步篩選後待排序的資料集合。",
    example: "Keep the same candidate pool but re-rank it."
  },
  {
    word: "Hand off",
    pos: "phrasal v.",
    zh: "交付、轉交",
    phonetic: "HAND OFF",
    ipa: "/hænd ɒf/",
    note: "把工作成果轉交給下一個人或系統，比 give 更專業。",
    example: "I handed off the spec to Codex."
  }
];

const sentenceData = [
  {
    en: "Before diving in, I ran a diagnostic first — and my assumption turned out to be wrong.",
    zh: "在動手之前，我先做了診斷——結果發現我的假設是錯的。",
    note: "展現嚴謹工作流程的黃金句型。面試或 review 說出來，代表你會先驗證假設再執行。"
  },
  {
    en: "Hard-filtering would only empty out the results, so I switched to soft ranking instead.",
    zh: "硬篩只會清空結果，所以我改用軟性排序。",
    note: "說明技術權衡（trade-off）的標準句。點出副作用，再說明替代方案。"
  },
  {
    en: "Knowing when to pull back is more professional than stubbornly pushing forward.",
    zh: "懂得何時收手，比硬著頭皮做下去更專業。",
    note: "適合週報結語、retro 會議、面試談「你最近一個好決定」。"
  }
];

let currentRate = 0.9;
let currentUtterance = null;

document.getElementById('speedRange').addEventListener('input', function() {
  currentRate = parseFloat(this.value);
  document.getElementById('speedVal').textContent = currentRate.toFixed(1) + '×';
});

function speak(text, onEnd) {
  if (!('speechSynthesis' in window)) {
    showToast('此瀏覽器不支援語音合成');
    return;
  }
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US';
  u.rate = currentRate;
  u.pitch = 1;
  if (onEnd) u.onend = onEnd;
  currentUtterance = u;
  window.speechSynthesis.speak(u);
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 1800);
}

function buildClickableText(text) {
  return text.split(/(\s+)/).map(part => {
    const clean = part.replace(/[^a-zA-Z'-]/g, '');
    if (clean.length > 0) {
      return `<span class="word" onclick="speak('${clean.replace(/'/g,"\\'")}'); showToast('${clean}')">${part}</span>`;
    }
    return part;
  }).join('');
}

paragraphs.forEach((p, i) => {
  const el = document.getElementById('p' + (i + 1));
  if (el) el.innerHTML = buildClickableText(p);
});

function playPara(idx) {
  const btns = document.querySelectorAll('.btn-play');
  btns.forEach(b => b.classList.remove('playing'));
  const btn = document.querySelectorAll('#panel-reading .btn-play')[idx];
  if (btn) btn.classList.add('playing');
  speak(paragraphs[idx], () => {
    if (btn) btn.classList.remove('playing');
  });
}

const vocabList = document.getElementById('vocab-list');
vocabData.forEach(v => {
  vocabList.innerHTML += `
    <div class="vocab-card">
      <div class="vocab-header">
        <div>
          <div class="vocab-word">${v.word}</div>
          <div class="vocab-pos">${v.pos} &nbsp;·&nbsp; ${v.ipa}</div>
        </div>
        <div class="vocab-phonetic" onclick="speak('${v.word}'); showToast('${v.word}')">${v.phonetic} ▶</div>
      </div>
      <div class="vocab-zh">${v.zh}</div>
      <div class="vocab-note">${v.note}</div>
      <div class="vocab-example" onclick="speak('${v.example.replace(/'/g,"\\'")}'); showToast('playing...')">
        ▶ "${v.example}"
      </div>
    </div>`;
});

const sentenceList = document.getElementById('sentence-list');
sentenceData.forEach(s => {
  sentenceList.innerHTML += `
    <div class="sentence-card">
      <div class="sentence-en" onclick="speak('${s.en.replace(/'/g,"\\'")}'); showToast('playing...')">${s.en} ▶</div>
      <div class="sentence-zh">${s.zh}</div>
      <div class="sentence-note">${s.note}</div>
    </div>`;
});

function switchTab(name) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.getElementById('panel-' + name).classList.add('active');
  event.target.classList.add('active');
  window.speechSynthesis.cancel();
}
</script>
</body>
</html>
