---
layout: null
---
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="資料庫工程師的英文口說復健 · Daily Speaking Practice">
<title>每日英文練習 | 2026-06-03 測試缺口・語意搜尋・規格書範本</title>
<style>
/* ─── reset ─── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ─── tokens ─── */
:root {
  --green:       #157878;
  --green-dark:  #0f6e56;
  --green-light: #e8f5f1;
  --green-mid:   #9fd9c8;
  --ink:         #2c2c2a;
  --ink-muted:   #5f5e5a;
  --ink-hint:    #888780;
  --surface:     #ffffff;
  --surface-alt: #f7f6f2;
  --border:      rgba(44,44,42,.12);
  --border-em:   rgba(44,44,42,.25);
  --radius:      8px;
  --radius-lg:   14px;
  --font-body:   'Georgia', serif;
  --font-ui:     -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono:   'Menlo', 'Courier New', monospace;
}

/* ─── layout ─── */
html { scroll-behavior: smooth; }
body {
  font-family: var(--font-ui);
  background: var(--surface-alt);
  color: var(--ink);
  min-height: 100vh;
}

/* ─── site header (matches GitHub Pages Cayman theme) ─── */
.site-header {
  background: linear-gradient(120deg, var(--green) 0%, var(--green-dark) 100%);
  padding: 2.5rem 2rem 2rem;
  color: #fff;
}
.site-header h1 {
  font-size: 28px;
  font-weight: 700;
  letter-spacing: -0.01em;
  margin-bottom: 4px;
}
.site-header p {
  font-size: 15px;
  opacity: 0.82;
  margin-bottom: 14px;
}
.gh-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  border: 1px solid rgba(255,255,255,0.4);
  border-radius: 6px;
  padding: 4px 12px;
  transition: background 0.15s;
}
.gh-link:hover { background: rgba(255,255,255,0.15); }

/* ─── main ─── */
.main-wrap {
  max-width: 820px;
  margin: 0 auto;
  padding: 2rem 1.25rem 4rem;
}

/* ─── day header ─── */
.day-header {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 1.25rem 1.5rem;
  margin-bottom: 2rem;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}
.day-date {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--green);
  margin-bottom: 4px;
}
.day-title {
  font-size: 22px;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.2;
}
.day-sub {
  font-size: 14px;
  color: var(--ink-muted);
  margin-top: 4px;
}
.day-tags {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  align-items: flex-start;
  padding-top: 4px;
}
.tag {
  font-size: 11px;
  font-weight: 500;
  padding: 3px 10px;
  border-radius: 999px;
  background: var(--green-light);
  color: var(--green-dark);
  border: 1px solid var(--green-mid);
  white-space: nowrap;
}

/* ─── speed control ─── */
.speed-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}
.speed-bar label {
  font-size: 13px;
  color: var(--ink-muted);
}
.speed-bar input[type=range] {
  -webkit-appearance: none;
  width: 130px;
  height: 4px;
  background: var(--border-em);
  border-radius: 999px;
  outline: none;
}
.speed-bar input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 16px; height: 16px;
  border-radius: 50%;
  background: var(--green);
  cursor: pointer;
}
.speed-val {
  font-size: 13px;
  font-weight: 600;
  color: var(--green-dark);
  min-width: 36px;
}
.btn-stop {
  font-size: 12px;
  padding: 4px 12px;
  border: 1px solid var(--border-em);
  border-radius: 6px;
  background: var(--surface);
  color: var(--ink-muted);
  cursor: pointer;
}
.btn-stop:hover { background: var(--surface-alt); }

/* ─── section label ─── */
.sec-label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ink-hint);
  margin: 2rem 0 1rem;
}
.sec-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}

/* ─── passage blocks ─── */
.passage {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 1.25rem 1.5rem 1rem;
  margin-bottom: 1rem;
}
.passage-title {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink-hint);
  margin-bottom: 0.75rem;
}
.passage-zh {
  font-size: 13px;
  color: var(--ink-muted);
  margin-bottom: 8px;
  line-height: 1.6;
  padding-bottom: 8px;
  border-bottom: 1px dashed var(--border);
}
.passage-en {
  font-size: 15.5px;
  line-height: 1.85;
  color: var(--ink);
}

/* ─── word buttons inside passage ─── */
.w {
  background: none;
  border: none;
  cursor: pointer;
  font-size: inherit;
  color: inherit;
  font-family: inherit;
  padding: 0;
  line-height: inherit;
  display: inline;
}
.w:hover { color: var(--green-dark); border-bottom: 1px dotted var(--green); }
.w.playing { color: var(--green); font-weight: 600; }

/* ─── read button ─── */
.btn-read {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-family: var(--font-ui);
  padding: 5px 14px;
  border-radius: 6px;
  border: 1px solid var(--border-em);
  background: var(--surface-alt);
  color: var(--ink-muted);
  cursor: pointer;
  margin-top: 10px;
  transition: all 0.12s;
}
.btn-read:hover { border-color: var(--green); color: var(--green-dark); background: var(--green-light); }
.btn-read.active { border-color: var(--green); color: var(--green); background: var(--green-light); }
.btn-read svg { width: 13px; height: 13px; fill: currentColor; flex-shrink: 0; }

/* ─── vocab grid ─── */
.vocab-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
  gap: 10px;
}
.vocab-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 0.9rem 1rem;
  cursor: pointer;
  transition: border-color 0.15s, background 0.15s;
  user-select: none;
}
.vocab-card:hover { border-color: var(--green-mid); }
.vocab-card.playing { border-color: var(--green); background: var(--green-light); }
.vocab-en  { font-size: 14px; font-weight: 600; color: var(--ink); margin-bottom: 3px; }
.vocab-ipa { font-size: 12px; color: var(--ink-hint); font-family: var(--font-mono); margin-bottom: 5px; }
.vocab-zh  { font-size: 12px; color: var(--ink-muted); }

/* ─── sentence list ─── */
.sent-list { display: flex; flex-direction: column; gap: 9px; }
.sent-item {
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 3px solid var(--green);
  border-radius: 0 var(--radius) var(--radius) 0;
  padding: 0.8rem 1rem 0.8rem 1.1rem;
  cursor: pointer;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  transition: background 0.12s;
}
.sent-item:hover { background: var(--green-light); }
.sent-item.playing { border-left-color: var(--green-dark); background: var(--green-light); }
.sent-en { font-size: 14.5px; color: var(--ink); line-height: 1.55; }
.sent-zh { font-size: 12px; color: var(--ink-muted); margin-top: 3px; }
.sent-icon {
  flex-shrink: 0;
  margin-top: 3px;
  color: var(--ink-hint);
  width: 18px; height: 18px;
}
.sent-item.playing .sent-icon { color: var(--green); }

/* ─── footer ─── */
.site-footer {
  border-top: 1px solid var(--border);
  padding-top: 1rem;
  margin-top: 2.5rem;
  font-size: 12px;
  color: var(--ink-hint);
  text-align: center;
  line-height: 1.7;
}
.site-footer a { color: var(--green-dark); text-decoration: none; }
.site-footer a:hover { text-decoration: underline; }

/* ─── helper note ─── */
.hint-note {
  font-size: 12px;
  color: var(--ink-hint);
  text-align: center;
  margin-top: 1.5rem;
}

@media (max-width: 520px) {
  .site-header { padding: 1.75rem 1.25rem 1.5rem; }
  .site-header h1 { font-size: 22px; }
  .day-header { flex-direction: column; }
  .vocab-grid { grid-template-columns: 1fr 1fr; }
}
</style>
</head>
<body>

<!-- site header -->
<header class="site-header">
  <h1>每日英文練習</h1>
  <p>資料庫工程師的英文口說復健 · Daily Speaking Practice</p>
  <a class="gh-link" href="https://github.com/Pcc329/daily-english" target="_blank">
    <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
    View on GitHub
  </a>
</header>

<main class="main-wrap">

  <!-- day header -->
  <div class="day-header">
    <div>
      <div class="day-date">2026.06.03 &nbsp;—&nbsp; Day 5</div>
      <div class="day-title">資料庫工程師的一天</div>
      <div class="day-sub">測試缺口 · 語意搜尋 · 規格書範本</div>
    </div>
    <div class="day-tags">
      <span class="tag">simulation test</span>
      <span class="tag">gap analysis</span>
      <span class="tag">spec template</span>
    </div>
  </div>

  <!-- speed control -->
  <div class="speed-bar">
    <label>語速</label>
    <input type="range" id="speed" min="0.6" max="1.4" step="0.1" value="0.9">
    <span class="speed-val" id="speed-out">0.9×</span>
    <button class="btn-stop" onclick="stopAll()">■ 停止</button>
  </div>

  <!-- SECTION: 朗讀練習 -->
  <div class="sec-label">朗讀練習</div>

  <div class="passage">
    <div class="passage-title">段落一 — 第二輪模擬測試</div>
    <div class="passage-zh">今天我跑了第二輪模擬測試。第一輪有一個關鍵缺陷：不管輸入什麼查詢，搜尋 API 都回傳全部 2,169 筆，所以結果毫無意義。</div>
    <div class="passage-en" id="p1">
      <button class="w" onclick="say('Today')">Today</button>
      <button class="w" onclick="say('I ran')">I ran</button>
      <button class="w" onclick="say('the second round of simulation tests')">the second round of simulation tests</button>
      <button class="w" onclick="say('for our solution finder database')">for our solution finder database</button>.
      <button class="w" onclick="say('The first round had a critical flaw')">The first round had a critical flaw</button> —
      <button class="w" onclick="say('the search API was returning all 2,169 records')">the search API was returning all 2,169 records</button>
      <button class="w" onclick="say('regardless of the query')">regardless of the query</button>.
      <button class="w" onclick="say('So the results were completely meaningless')">So the results were completely meaningless</button>.
    </div>
    <button class="btn-read" onclick="readPara('Today I ran the second round of simulation tests for our solution finder database. The first round had a critical flaw. The search API was returning all 2,169 records regardless of the query. So the results were completely meaningless.', this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>
      聽整段
    </button>
  </div>

  <div class="passage">
    <div class="passage-title">段落二 — 修正語意搜尋邏輯</div>
    <div class="passage-zh">第二版改走語意解析 API。Claude 先從查詢中擷取篩選條件，再對快取的方案清單做過濾，搜尋結果因此有了真實的參考價值。</div>
    <div class="passage-en" id="p2">
      <button class="w" onclick="say('In version two')">In version two</button>,
      <button class="w" onclick="say('I rewrote the search function')">I rewrote the search function</button>
      <button class="w" onclick="say('to go through the semantic parsing API first')">to go through the semantic parsing API first</button>.
      <button class="w" onclick="say('Claude extracts filter conditions from the natural language query')">Claude extracts filter conditions from the natural language query</button>,
      <button class="w" onclick="say('then we apply them to a cached list of solutions')">then we apply them to a cached list of solutions</button>.
      <button class="w" onclick="say('This way, the search results are actually meaningful')">This way, the search results are actually meaningful</button>.
    </div>
    <button class="btn-read" onclick="readPara('In version two, I rewrote the search function to go through the semantic parsing API first. Claude extracts filter conditions from the natural language query, then we apply them to a cached list of solutions. This way, the search results are actually meaningful.', this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>
      聽整段
    </button>
  </div>

  <div class="passage">
    <div class="passage-title">段落三 — 發現真實資料缺口</div>
    <div class="passage-zh">修正後，100 個測試情境中有 20 個回傳 0 筆結果。最大的缺口集中在「提升辦公室效率」和「吸引人才」，幾乎每個產業都沒有對應方案。</div>
    <div class="passage-en" id="p3">
      <button class="w" onclick="say('After fixing the logic')">After fixing the logic</button>,
      <button class="w" onclick="say('the results became genuinely useful')">the results became genuinely useful</button>.
      <button class="w" onclick="say('Out of 100 test scenarios')">Out of 100 test scenarios</button>,
      <button class="w" onclick="say('twenty returned zero results')">twenty returned zero results</button>.
      <button class="w" onclick="say('That reveals where our database has real gaps')">That reveals where our database has real gaps</button>.
      <button class="w" onclick="say('The biggest gaps are in office productivity tools and HR recruitment solutions')">The biggest gaps are in office productivity tools and HR recruitment solutions</button> —
      <button class="w" onclick="say('almost no industry has matching records')">almost no industry has matching records</button>.
    </div>
    <button class="btn-read" onclick="readPara('After fixing the logic, the results became genuinely useful. Out of 100 test scenarios, twenty returned zero results. That reveals where our database has real gaps. The biggest gaps are in office productivity tools and HR recruitment solutions. Almost no industry has matching records.', this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>
      聽整段
    </button>
  </div>

  <div class="passage">
    <div class="passage-title">段落四 — 規格書範本與防呆機制</div>
    <div class="passage-zh">我也整理了給 Codex 用的規格書範本，涵蓋背景說明、需求、驗收標準和防呆規則。最重要的是「不准動的東西」那一節，用來保護核心搜尋邏輯。</div>
    <div class="passage-en" id="p4">
      <button class="w" onclick="say('I also finalized a spec template for working with Codex')">I also finalized a spec template for working with Codex</button>.
      <button class="w" onclick="say('It covers background context, requirements, acceptance criteria, and guardrails')">It covers background context, requirements, acceptance criteria, and guardrails</button>.
      <button class="w" onclick="say('The most critical section is what Codex is NOT allowed to touch')">The most critical section is what Codex is NOT allowed to touch</button> —
      <button class="w" onclick="say('we call it the off-limits section')">we call it the off-limits section</button>.
      <button class="w" onclick="say('It prevents unintended changes to the core search logic')">It prevents unintended changes to the core search logic</button>.
    </div>
    <button class="btn-read" onclick="readPara('I also finalized a spec template for working with Codex. It covers background context, requirements, acceptance criteria, and guardrails. The most critical section is what Codex is NOT allowed to touch. We call it the off-limits section. It prevents unintended changes to the core search logic.', this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>
      聽整段
    </button>
  </div>

  <!-- SECTION: 術語發音 -->
  <div class="sec-label">術語發音</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點卡片聽發音</div>
  <div class="vocab-grid" id="vocabGrid"></div>

  <!-- SECTION: 核心句型 -->
  <div class="sec-label">核心句型</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點句子聽完整朗讀</div>
  <div class="sent-list" id="sentList"></div>

  <div class="hint-note">點單字聽發音 · 點卡片聽術語 · 點句子聽完整朗讀</div>

</main>

<!-- site footer -->
<footer class="site-footer">
  <a href="https://github.com/Pcc329/daily-english">daily-english</a> is maintained by
  <a href="https://github.com/Pcc329">Pcc329</a>.<br>
  This page was generated by Claude · 2026-06-03
</footer>

<script>
/* ─── data ─── */
const vocab = [
  { en:"simulation test",      ipa:"/ˌsɪmjʊˈleɪʃən test/",        zh:"模擬測試" },
  { en:"semantic search",      ipa:"/sɪˈmæntɪk sɜːrtʃ/",           zh:"語意搜尋" },
  { en:"gap analysis",         ipa:"/ɡæp əˈnæləsɪs/",              zh:"缺口分析" },
  { en:"spec template",        ipa:"/spek ˈtempleɪt/",              zh:"規格書範本" },
  { en:"acceptance criteria",  ipa:"/əkˈseptəns kraɪˈtɪəriə/",     zh:"驗收標準" },
  { en:"guardrails",           ipa:"/ˈɡɑːrdreɪlz/",                zh:"防呆規則" },
  { en:"filter condition",     ipa:"/ˈfɪltər kənˈdɪʃən/",          zh:"篩選條件" },
  { en:"zero-result scenario", ipa:"/ˈzɪərəʊ rɪˈzʌlt sɪˈnɑːriəʊ/",zh:"無結果情境" },
  { en:"off-limits section",   ipa:"/ɒf ˈlɪmɪts ˈsekʃən/",        zh:"禁止修改區" },
  { en:"cached dataset",       ipa:"/kæʃt ˈdeɪtəset/",             zh:"快取資料集" },
  { en:"diversity metric",     ipa:"/daɪˈvɜːrsəti ˈmetrɪk/",       zh:"多樣性指標" },
  { en:"system prompt",        ipa:"/ˈsɪstəm prɒmpt/",             zh:"系統提示詞" },
];

const sentences = [
  { en:"The search API was returning all 2,169 records regardless of the query.", zh:"不管輸入什麼，搜尋 API 都回傳全部 2,169 筆記錄。" },
  { en:"Twenty out of a hundred test scenarios returned zero results.", zh:"100 個測試情境中，有 20 個回傳 0 筆結果。" },
  { en:"That reveals where our database has real gaps.", zh:"這讓我們清楚看到資料庫的真實缺口在哪裡。" },
  { en:"The biggest gap is in office productivity tools and HR solutions.", zh:"最大缺口在辦公室效率工具和人力資源類方案。" },
  { en:"Claude extracts filter conditions from the natural language query.", zh:"Claude 從自然語言查詢中擷取篩選條件。" },
  { en:"The off-limits section prevents unintended changes to the core logic.", zh:"防呆區段避免核心邏輯被意外修改。" },
  { en:"We need to add more data before running Round 03.", zh:"在跑第三輪測試之前，我們需要補充更多資料。" },
  { en:"Four scenarios returned the full dataset because the parser got no filters.", zh:"有 4 個情境因語意解析器沒有產出篩選條件，所以回傳了全庫資料。" },
];

/* ─── build DOM ─── */
const vocabGrid = document.getElementById('vocabGrid');
vocab.forEach(v => {
  const card = document.createElement('div');
  card.className = 'vocab-card';
  card.innerHTML = `<div class="vocab-en">${v.en}</div><div class="vocab-ipa">${v.ipa}</div><div class="vocab-zh">${v.zh}</div>`;
  card.addEventListener('click', () => speakVocab(v.en, card));
  vocabGrid.appendChild(card);
});

const sentList = document.getElementById('sentList');
sentences.forEach(s => {
  const item = document.createElement('div');
  item.className = 'sent-item';
  const playIcon = `<svg class="sent-icon" viewBox="0 0 16 16" fill="currentColor"><path d="M3 2l10 6-10 6V2z"/></svg>`;
  item.innerHTML = `<div><div class="sent-en">${s.en}</div><div class="sent-zh">${s.zh}</div></div>${playIcon}`;
  item.addEventListener('click', () => readPara(s.en, item));
  sentList.appendChild(item);
});

/* ─── speech ─── */
let activeEl = null;

function clearActive() {
  if (activeEl) {
    activeEl.classList.remove('playing', 'active');
    activeEl = null;
  }
}

function stopAll() {
  window.speechSynthesis.cancel();
  clearActive();
}

function getRate() {
  return parseFloat(document.getElementById('speed').value);
}

function utter(text, el, onEnd) {
  window.speechSynthesis.cancel();
  clearActive();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US';
  u.rate = getRate();
  if (el) { el.classList.add('playing', 'active'); activeEl = el; }
  u.onend = u.onerror = () => {
    if (el) el.classList.remove('playing', 'active');
    if (activeEl === el) activeEl = null;
    if (onEnd) onEnd();
  };
  window.speechSynthesis.speak(u);
}

function say(text) { utter(text, null); }

function speakVocab(text, card) {
  if (card.classList.contains('playing')) { stopAll(); return; }
  utter(text, card);
}

function readPara(text, btn) {
  if (btn && btn.classList.contains('active')) { stopAll(); return; }
  utter(text, btn);
}

/* ─── speed slider ─── */
document.getElementById('speed').addEventListener('input', function() {
  document.getElementById('speed-out').textContent = parseFloat(this.value).toFixed(1) + '×';
});
</script>
</body>
</html>
