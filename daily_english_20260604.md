---
layout: null
---
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="資料庫工程師的英文口說復健 · Daily Speaking Practice">
<title>每日英文練習 | 2026-06-04 Strategy Guide・ROI 試算・統編批次補查</title>
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
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
  --font-ui:     -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono:   'Menlo', 'Courier New', monospace;
}
html { scroll-behavior: smooth; }
body { font-family: var(--font-ui); background: var(--surface-alt); color: var(--ink); min-height: 100vh; }

/* header */
.site-header {
  background: linear-gradient(120deg, var(--green) 0%, var(--green-dark) 100%);
  padding: 2.5rem 2rem 2rem;
  color: #fff;
}
.site-header h1 { font-size: 28px; font-weight: 700; letter-spacing: -0.01em; margin-bottom: 4px; }
.site-header p  { font-size: 15px; opacity: 0.82; margin-bottom: 14px; }
.gh-link {
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 13px; color: rgba(255,255,255,0.85); text-decoration: none;
  border: 1px solid rgba(255,255,255,0.4); border-radius: 6px; padding: 4px 12px;
  transition: background 0.15s;
}
.gh-link:hover { background: rgba(255,255,255,0.15); }

/* main */
.main-wrap { max-width: 820px; margin: 0 auto; padding: 2rem 1.25rem 4rem; }

/* day header */
.day-header {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 1.25rem 1.5rem; margin-bottom: 2rem;
  display: flex; align-items: flex-start; justify-content: space-between; gap: 1rem; flex-wrap: wrap;
}
.day-date { font-size: 12px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--green); margin-bottom: 4px; }
.day-title { font-size: 22px; font-weight: 700; color: var(--ink); line-height: 1.2; }
.day-sub   { font-size: 14px; color: var(--ink-muted); margin-top: 4px; }
.day-tags  { display: flex; gap: 6px; flex-wrap: wrap; align-items: flex-start; padding-top: 4px; }
.tag {
  font-size: 11px; font-weight: 500; padding: 3px 10px; border-radius: 999px;
  background: var(--green-light); color: var(--green-dark); border: 1px solid var(--green-mid); white-space: nowrap;
}

/* speed bar */
.speed-bar { display: flex; align-items: center; gap: 10px; margin-bottom: 1.5rem; flex-wrap: wrap; }
.speed-bar label { font-size: 13px; color: var(--ink-muted); }
.speed-bar input[type=range] {
  -webkit-appearance: none; width: 130px; height: 4px;
  background: var(--border-em); border-radius: 999px; outline: none;
}
.speed-bar input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none; width: 16px; height: 16px;
  border-radius: 50%; background: var(--green); cursor: pointer;
}
.speed-val { font-size: 13px; font-weight: 600; color: var(--green-dark); min-width: 36px; }
.btn-stop {
  font-size: 12px; padding: 4px 12px; border: 1px solid var(--border-em);
  border-radius: 6px; background: var(--surface); color: var(--ink-muted); cursor: pointer;
}
.btn-stop:hover { background: var(--surface-alt); }

/* section label */
.sec-label {
  display: flex; align-items: center; gap: 10px;
  font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--ink-hint); margin: 2rem 0 1rem;
}
.sec-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }

/* passage */
.passage {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 1.25rem 1.5rem 1rem; margin-bottom: 1rem;
}
.passage-title { font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-hint); margin-bottom: 0.75rem; }
.passage-zh { font-size: 13px; color: var(--ink-muted); margin-bottom: 8px; line-height: 1.6; padding-bottom: 8px; border-bottom: 1px dashed var(--border); }
.passage-en { font-size: 15.5px; line-height: 1.85; color: var(--ink); }

/* word buttons */
.w { background: none; border: none; cursor: pointer; font-size: inherit; color: inherit; font-family: inherit; padding: 0; line-height: inherit; display: inline; }
.w:hover { color: var(--green-dark); border-bottom: 1px dotted var(--green); }
.w.playing { color: var(--green); font-weight: 600; }

/* read button */
.btn-read {
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 12px; font-family: var(--font-ui); padding: 5px 14px; border-radius: 6px;
  border: 1px solid var(--border-em); background: var(--surface-alt); color: var(--ink-muted);
  cursor: pointer; margin-top: 10px; transition: all 0.12s;
}
.btn-read:hover { border-color: var(--green); color: var(--green-dark); background: var(--green-light); }
.btn-read.active { border-color: var(--green); color: var(--green); background: var(--green-light); }
.btn-read svg { width: 13px; height: 13px; fill: currentColor; flex-shrink: 0; }

/* vocab */
.vocab-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 10px; }
.vocab-card {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 0.9rem 1rem; cursor: pointer; transition: border-color 0.15s, background 0.15s; user-select: none;
}
.vocab-card:hover { border-color: var(--green-mid); }
.vocab-card.playing { border-color: var(--green); background: var(--green-light); }
.vocab-en  { font-size: 14px; font-weight: 600; color: var(--ink); margin-bottom: 3px; }
.vocab-ipa { font-size: 12px; color: var(--ink-hint); font-family: var(--font-mono); margin-bottom: 5px; }
.vocab-zh  { font-size: 12px; color: var(--ink-muted); }

/* sentences */
.sent-list { display: flex; flex-direction: column; gap: 9px; }
.sent-item {
  background: var(--surface); border: 1px solid var(--border);
  border-left: 3px solid var(--green); border-radius: 0 var(--radius) var(--radius) 0;
  padding: 0.8rem 1rem 0.8rem 1.1rem; cursor: pointer;
  display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; transition: background 0.12s;
}
.sent-item:hover { background: var(--green-light); }
.sent-item.playing { border-left-color: var(--green-dark); background: var(--green-light); }
.sent-en { font-size: 14.5px; color: var(--ink); line-height: 1.55; }
.sent-zh { font-size: 12px; color: var(--ink-muted); margin-top: 3px; }
.sent-icon { flex-shrink: 0; margin-top: 3px; color: var(--ink-hint); width: 18px; height: 18px; }
.sent-item.playing .sent-icon { color: var(--green); }

/* footer */
.site-footer { border-top: 1px solid var(--border); padding-top: 1rem; margin-top: 2.5rem; font-size: 12px; color: var(--ink-hint); text-align: center; line-height: 1.7; }
.site-footer a { color: var(--green-dark); text-decoration: none; }
.site-footer a:hover { text-decoration: underline; }
.hint-note { font-size: 12px; color: var(--ink-hint); text-align: center; margin-top: 1.5rem; }

@media (max-width: 520px) {
  .site-header { padding: 1.75rem 1.25rem 1.5rem; }
  .site-header h1 { font-size: 22px; }
  .day-header { flex-direction: column; }
  .vocab-grid { grid-template-columns: 1fr 1fr; }
}
</style>
</head>
<body>

<header class="site-header">
  <h1>每日英文練習</h1>
  <p>資料庫工程師的英文口說復健 · Daily Speaking Practice</p>
  <a class="gh-link" href="https://github.com/Pcc329/daily-english" target="_blank">
    <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
    View on GitHub
  </a>
</header>

<main class="main-wrap">

  <div class="day-header">
    <div>
      <div class="day-date">2026.06.04 &nbsp;—&nbsp; Day 6</div>
      <div class="day-title">前端上線、資料清洗與系統備份</div>
      <div class="day-sub">Strategy Guide · ROI 試算 · 統編批次補查 · 自動備份</div>
    </div>
    <div class="day-tags">
      <span class="tag">ROI calculator</span>
      <span class="tag">batch lookup</span>
      <span class="tag">automated backup</span>
    </div>
  </div>

  <div class="speed-bar">
    <label>語速</label>
    <input type="range" id="speed" min="0.6" max="1.4" step="0.1" value="0.9">
    <span class="speed-val" id="speed-out">0.9×</span>
    <button class="btn-stop" onclick="stopAll()">■ 停止</button>
  </div>

  <!-- ── 朗讀練習 ── -->
  <div class="sec-label">朗讀練習</div>

  <div class="passage">
    <div class="passage-title">段落一 — Strategy Guide 完整上線</div>
    <div class="passage-zh">今天最重要的里程碑是策略智庫從無到有完整上線。它包含七種計畫類型的服務分類、泡泡圖公司圖譜、AI 方案推薦、市場現況分布，以及 ROI 試算功能。</div>
    <div class="passage-en">
      <button class="w" onclick="say('Today\'s most important milestone')">Today's most important milestone</button>
      <button class="w" onclick="say('was the full launch of the Strategy Guide')">was the full launch of the Strategy Guide</button>.
      <button class="w" onclick="say('It went from zero to fully operational')">It went from zero to fully operational</button>.
      <button class="w" onclick="say('The guide includes seven service categories')">The guide includes seven service categories</button>,
      <button class="w" onclick="say('a circle packing company map')">a circle packing company map</button>,
      <button class="w" onclick="say('AI-powered solution recommendations')">AI-powered solution recommendations</button>,
      <button class="w" onclick="say('a market overview section')">a market overview section</button>,
      <button class="w" onclick="say('and an ROI calculator')">and an ROI calculator</button>.
    </div>
    <button class="btn-read" onclick="readPara(`Today's most important milestone was the full launch of the Strategy Guide. It went from zero to fully operational. The guide includes seven service categories, a circle packing company map, AI-powered solution recommendations, a market overview section, and an ROI calculator.`, this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>聽整段
    </button>
  </div>

  <div class="passage">
    <div class="passage-title">段落二 — ROI 試算串接搜尋結果</div>
    <div class="passage-zh">新功能讓顧問可以從搜尋結果直接進入 ROI 試算。勾選一到四筆方案後，點擊底部比較列的「試算 ROI」按鈕，月費就會自動帶入，填入人力數據後即可得出回收期。</div>
    <div class="passage-en">
      <button class="w" onclick="say('We added a new feature')">We added a new feature</button>
      <button class="w" onclick="say('that connects the search results directly to the ROI calculator')">that connects the search results directly to the ROI calculator</button>.
      <button class="w" onclick="say('A consultant can select one to four solutions from the search page')">A consultant can select one to four solutions from the search page</button>,
      <button class="w" onclick="say('click the Calculate ROI button in the comparison bar')">click the Calculate ROI button in the comparison bar</button>,
      <button class="w" onclick="say('and the monthly fee is automatically filled in')">and the monthly fee is automatically filled in</button>.
      <button class="w" onclick="say('They just enter the headcount data and get the payback period')">They just enter the headcount data and get the payback period</button>.
    </div>
    <button class="btn-read" onclick="readPara('We added a new feature that connects the search results directly to the ROI calculator. A consultant can select one to four solutions from the search page, click the Calculate ROI button in the comparison bar, and the monthly fee is automatically filled in. They just enter the headcount data and get the payback period.', this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>聽整段
    </button>
  </div>

  <div class="passage">
    <div class="passage-title">段落三 — 公司統編批次補查</div>
    <div class="passage-zh">針對 103 筆缺少統一編號的公司，用 g0v 台灣公司查詢 API 做批次補查，成功找到 87 筆，覆蓋率達 84.5%。查無結果的包含財團法人、外國品牌和名稱截斷的公司。</div>
    <div class="passage-en">
      <button class="w" onclick="say('We ran a batch lookup')">We ran a batch lookup</button>
      <button class="w" onclick="say('for 103 companies that were missing their business registration number')">for 103 companies that were missing their business registration number</button>.
      <button class="w" onclick="say('Using the g0v Taiwan company API')">Using the g0v Taiwan company API</button>,
      <button class="w" onclick="say('we found registration numbers for 87 of them')">we found registration numbers for 87 of them</button>,
      <button class="w" onclick="say('an 84.5 percent coverage rate')">an 84.5 percent coverage rate</button>.
      <button class="w" onclick="say('The remaining 16 were foundations, foreign brands, or companies with truncated names')">The remaining 16 were foundations, foreign brands, or companies with truncated names</button>.
    </div>
    <button class="btn-read" onclick="readPara('We ran a batch lookup for 103 companies that were missing their business registration number. Using the g0v Taiwan company API, we found registration numbers for 87 of them, an 84.5 percent coverage rate. The remaining 16 were foundations, foreign brands, or companies with truncated names.', this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>聽整段
    </button>
  </div>

  <div class="passage">
    <div class="passage-title">段落四 — 資料清理與自動備份上線</div>
    <div class="passage-zh">移除了 7 筆確認無法補齊資料的公司，Companies 表清理後剩 842 家。同時上線了 Airtable 自動週備份系統，每週日自動備份全部 12 張資料表，首次執行 27 秒完成。</div>
    <div class="passage-en">
      <button class="w" onclick="say('We removed seven companies')">We removed seven companies</button>
      <button class="w" onclick="say('that had incomplete and unrecoverable data')">that had incomplete and unrecoverable data</button>.
      <button class="w" onclick="say('The Companies table now stands at 842 records')">The Companies table now stands at 842 records</button>.
      <button class="w" onclick="say('We also launched an automated weekly backup system for Airtable')">We also launched an automated weekly backup system for Airtable</button>.
      <button class="w" onclick="say('It backs up all twelve tables every Sunday at midnight UTC')">It backs up all twelve tables every Sunday at midnight UTC</button>,
      <button class="w" onclick="say('and the first run completed in 27 seconds')">and the first run completed in 27 seconds</button>.
    </div>
    <button class="btn-read" onclick="readPara('We removed seven companies that had incomplete and unrecoverable data. The Companies table now stands at 842 records. We also launched an automated weekly backup system for Airtable. It backs up all twelve tables every Sunday at midnight UTC, and the first run completed in 27 seconds.', this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>聽整段
    </button>
  </div>

  <!-- ── 術語發音 ── -->
  <div class="sec-label">術語發音</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點卡片聽發音</div>
  <div class="vocab-grid" id="vocabGrid"></div>

  <!-- ── 核心句型 ── -->
  <div class="sec-label">核心句型</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點句子聽完整朗讀</div>
  <div class="sent-list" id="sentList"></div>

  <div class="hint-note">點單字聽發音 · 點卡片聽術語 · 點句子聽完整朗讀</div>

</main>

<footer class="site-footer">
  <a href="https://github.com/Pcc329/daily-english">daily-english</a> is maintained by
  <a href="https://github.com/Pcc329">Pcc329</a>.<br>
  This page was generated by Claude · 2026-06-04
</footer>

<script>
const vocab = [
  { en:"ROI calculator",             ipa:"/ˌɑːr.oʊ.ˈaɪ ˈkælkjʊleɪtər/",   zh:"投資報酬試算器" },
  { en:"payback period",             ipa:"/ˈpeɪbæk ˈpɪəriəd/",              zh:"投資回收期" },
  { en:"sticky navigation bar",      ipa:"/ˈstɪki ˌnævɪˈɡeɪʃən bɑːr/",     zh:"固定導航列" },
  { en:"circle packing",             ipa:"/ˈsɜːrkl ˈpækɪŋ/",                zh:"圓形填充圖（泡泡圖）" },
  { en:"batch lookup",               ipa:"/bætʃ ˈlʊkʌp/",                   zh:"批次查詢" },
  { en:"business registration number",ipa:"/ˈbɪznɪs ˌredʒɪˈstreɪʃən ˈnʌmbər/",zh:"統一編號" },
  { en:"coverage rate",              ipa:"/ˈkʌvərɪdʒ reɪt/",               zh:"覆蓋率" },
  { en:"automated backup",           ipa:"/ˈɔːtəmeɪtɪd ˈbækʌp/",           zh:"自動備份" },
  { en:"Content Security Policy",    ipa:"/ˈkɒntent sɪˈkjʊərɪti ˈpɒlɪsi/", zh:"內容安全策略（CSP）" },
  { en:"product roadmap",            ipa:"/ˈprɒdʌkt ˈrəʊdmæp/",            zh:"產品路線圖" },
  { en:"foundation",                 ipa:"/faʊnˈdeɪʃən/",                   zh:"財團法人" },
  { en:"headcount",                  ipa:"/ˈhedkaʊnt/",                     zh:"人力數量" },
];

const sentences = [
  { en:"The Strategy Guide went from zero to fully operational today.",           zh:"策略智庫今天從無到有完整上線。" },
  { en:"The monthly fee is automatically filled in when you enter from the search page.", zh:"從搜尋頁進入時，月費會自動帶入。" },
  { en:"We ran a batch lookup for 103 companies missing their registration number.", zh:"我們針對 103 筆缺少統編的公司做了批次補查。" },
  { en:"The coverage rate came out to 84.5 percent.",                            zh:"覆蓋率達到 84.5%。" },
  { en:"The remaining 16 were foundations, foreign brands, or truncated entries.", zh:"剩下 16 筆是財團法人、外國品牌或名稱截斷的資料。" },
  { en:"We upgraded from a single backup to an automated weekly backup system.",  zh:"備份機制從「唯一備份」升級為自動週備份系統。" },
  { en:"The first run completed all twelve tables in 27 seconds.",               zh:"首次執行 27 秒就完成了全部 12 張資料表的備份。" },
  { en:"Tomorrow we will build a 10-by-10 industry needs matrix heatmap.",       zh:"明天我們要製作 10×10 的產業需求矩陣熱力圖。" },
];

/* build DOM */
const vocabGrid = document.getElementById('vocabGrid');
vocab.forEach(v => {
  const c = document.createElement('div');
  c.className = 'vocab-card';
  c.innerHTML = `<div class="vocab-en">${v.en}</div><div class="vocab-ipa">${v.ipa}</div><div class="vocab-zh">${v.zh}</div>`;
  c.addEventListener('click', () => speakVocab(v.en, c));
  vocabGrid.appendChild(c);
});

const sentList = document.getElementById('sentList');
const playSVG = `<svg class="sent-icon" viewBox="0 0 16 16" fill="currentColor"><path d="M3 2l10 6-10 6V2z"/></svg>`;
sentences.forEach(s => {
  const item = document.createElement('div');
  item.className = 'sent-item';
  item.innerHTML = `<div><div class="sent-en">${s.en}</div><div class="sent-zh">${s.zh}</div></div>${playSVG}`;
  item.addEventListener('click', () => readPara(s.en, item));
  sentList.appendChild(item);
});

/* speech */
let activeEl = null;
function clearActive() { if (activeEl) { activeEl.classList.remove('playing','active'); activeEl = null; } }
function stopAll() { window.speechSynthesis.cancel(); clearActive(); }
function getRate() { return parseFloat(document.getElementById('speed').value); }
function utter(text, el) {
  window.speechSynthesis.cancel(); clearActive();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US'; u.rate = getRate();
  if (el) { el.classList.add('playing','active'); activeEl = el; }
  u.onend = u.onerror = () => { if (el) el.classList.remove('playing','active'); if (activeEl===el) activeEl=null; };
  window.speechSynthesis.speak(u);
}
function say(text) { utter(text, null); }
function speakVocab(text, card) { if (card.classList.contains('playing')) { stopAll(); return; } utter(text, card); }
function readPara(text, btn)  { if (btn && btn.classList.contains('active'))  { stopAll(); return; } utter(text, btn); }

document.getElementById('speed').addEventListener('input', function() {
  document.getElementById('speed-out').textContent = parseFloat(this.value).toFixed(1) + '×';
});
</script>
</body>
</html>
