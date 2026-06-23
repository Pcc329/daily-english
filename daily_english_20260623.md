---
layout: null
---
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>每日英文練習 | 2026-06-23 工作日誌 × Headway U4 句型</title>
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

.site-header {
  background: linear-gradient(120deg, var(--green) 0%, var(--green-dark) 100%);
  padding: 2.5rem 2rem 2rem; color: #fff;
}
.site-header h1 { font-size: 26px; font-weight: 700; letter-spacing: -0.01em; margin-bottom: 4px; }
.site-header p  { font-size: 14px; opacity: 0.82; margin-bottom: 14px; }
.badge-row { display:flex; gap:8px; flex-wrap:wrap; margin-bottom: 12px; }
.hdr-badge {
  font-size: 12px; font-weight: 600; padding: 3px 12px; border-radius: 999px;
  background: rgba(255,255,255,0.18); border: 1px solid rgba(255,255,255,0.35); color: #fff;
}
.btn-row { display:flex; gap:8px; flex-wrap:wrap; }
.gh-link {
  display: inline-flex; align-items: center; gap: 6px; font-size: 13px;
  color: rgba(255,255,255,0.85); text-decoration: none;
  border: 1px solid rgba(255,255,255,0.4); border-radius: 6px; padding: 4px 12px;
  transition: background 0.15s;
}
.gh-link:hover { background: rgba(255,255,255,0.15); }

.main-wrap { max-width: 820px; margin: 0 auto; padding: 2rem 1.25rem 4rem; }

.day-header {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 1.25rem 1.5rem; margin-bottom: 1.5rem;
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

.grammar-note {
  background: #eaf2ff; border: 1px solid #b3cfee; border-radius: var(--radius-lg);
  padding: 1rem 1.25rem; margin-bottom: 1.5rem; font-size: 13.5px; line-height: 1.8;
  color: #1a3a5c;
}
.grammar-note strong { font-weight: 700; }
.grammar-note .gn-title { font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #5080a0; margin-bottom: 8px; }

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
.btn-stop { font-size: 12px; padding: 4px 12px; border: 1px solid var(--border-em); border-radius: 6px; background: var(--surface); color: var(--ink-muted); cursor: pointer; }
.btn-stop:hover { background: var(--surface-alt); }

.sec-label {
  display: flex; align-items: center; gap: 10px;
  font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--ink-hint); margin: 2rem 0 1rem;
}
.sec-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }

.passage {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 1.25rem 1.5rem 1rem; margin-bottom: 1rem;
}
.passage-title { font-size: 12px; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-hint); margin-bottom: 0.75rem; }
.passage-zh { font-size: 13px; color: var(--ink-muted); margin-bottom: 8px; line-height: 1.6; padding-bottom: 8px; border-bottom: 1px dashed var(--border); }
.passage-en { font-size: 15.5px; line-height: 1.9; color: var(--ink); }
.w { background: none; border: none; cursor: pointer; font-size: inherit; color: inherit; font-family: inherit; padding: 0; line-height: inherit; display: inline; }
.w:hover { color: var(--green-dark); border-bottom: 1px dotted var(--green); }
.w.playing { color: var(--green); font-weight: 600; }
.hl-past { color: #1a5276; font-weight: 700; }
.hl-neg  { color: #c0392b; font-weight: 700; }
.hl-q    { color: #7d6608; font-weight: 700; }
.hl-why  { color: var(--green-dark); font-weight: 600; }

.btn-read {
  display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-family: var(--font-ui);
  padding: 5px 14px; border-radius: 6px; border: 1px solid var(--border-em);
  background: var(--surface-alt); color: var(--ink-muted); cursor: pointer; margin-top: 10px; transition: all 0.12s;
}
.btn-read:hover { border-color: var(--green); color: var(--green-dark); background: var(--green-light); }
.btn-read.active { border-color: var(--green); color: var(--green); background: var(--green-light); }
.btn-read svg { width: 13px; height: 13px; fill: currentColor; flex-shrink: 0; }

.vocab-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(185px, 1fr)); gap: 10px; }
.vocab-card {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
  padding: 0.9rem 1rem; cursor: pointer; transition: border-color 0.15s, background 0.15s; user-select: none;
}
.vocab-card:hover { border-color: var(--green-mid); }
.vocab-card.playing { border-color: var(--green); background: var(--green-light); }
.vocab-en  { font-size: 13.5px; font-weight: 600; color: var(--ink); margin-bottom: 3px; }
.vocab-ipa { font-size: 11px; color: var(--ink-hint); font-family: var(--font-mono); margin-bottom: 4px; }
.vocab-zh  { font-size: 12px; color: var(--ink-muted); }

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

.quiz-block { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.25rem 1.5rem; margin-bottom: 1rem; }
.quiz-block-title { font-size: 13px; font-weight: 600; color: var(--ink-muted); margin-bottom: 14px; display:flex; align-items:center; gap:8px; }
.quiz-q { margin-bottom: 1.25rem; padding-bottom: 1.25rem; border-bottom: 1px dashed var(--border); }
.quiz-q:last-child { margin-bottom: 0; padding-bottom: 0; border-bottom: none; }
.quiz-q-num { display:inline-flex; align-items:center; justify-content:center; width:22px; height:22px; background:var(--green); color:#fff; font-size:11px; font-weight:700; border-radius:50%; flex-shrink:0; }
.quiz-q-row { display:flex; align-items:flex-start; gap:8px; margin-bottom:10px; }
.quiz-q-text { font-size:14.5px; color:var(--ink); line-height:1.55; padding-top:2px; }
.play-word-btn { display:inline-flex; align-items:center; gap:5px; font-size:12px; padding:4px 12px; border-radius:6px; border:1px solid var(--green); background:var(--green-light); color:var(--green-dark); cursor:pointer; font-family:var(--font-ui); white-space:nowrap; }
.play-word-btn:hover { background:var(--green-mid); }
.quiz-opts { display:grid; grid-template-columns:1fr 1fr; gap:7px; margin-top:8px; }
.quiz-opt { font-size:13px; padding:7px 12px; border-radius:var(--radius); border:1px solid var(--border-em); background:var(--surface-alt); color:var(--ink); cursor:pointer; text-align:left; font-family:var(--font-ui); transition:all 0.12s; }
.quiz-opt:hover:not(:disabled) { border-color:var(--green); background:var(--green-light); }
.quiz-opt.correct { border-color:#22a06b !important; background:#e3fcef !important; color:#1a6b45; font-weight:600; }
.quiz-opt.wrong   { border-color:#c9372c !important; background:#ffeceb !important; color:#c9372c; }
.fill-sentence { font-size:15px; line-height:2.3; color:var(--ink); margin-bottom:6px; }
.fill-input { font-size:15px; font-family:var(--font-ui); border:none; border-bottom:2px solid var(--green); background:transparent; color:var(--ink); min-width:100px; padding:0 4px; outline:none; text-align:center; vertical-align:middle; }
.fill-input.correct { border-color:#22a06b; color:#1a6b45; }
.fill-input.wrong   { border-color:#c9372c; color:#c9372c; }
.fill-hint { font-size:12px; color:var(--ink-hint); margin-bottom:8px; }
.quiz-check-btn { font-size:12px; padding:4px 12px; border-radius:6px; border:1px solid var(--border-em); background:var(--surface-alt); color:var(--ink-muted); cursor:pointer; font-family:var(--font-ui); margin-top:4px; }
.quiz-check-btn:hover { border-color:var(--green); color:var(--green-dark); background:var(--green-light); }
.quiz-feedback { font-size:12px; margin-top:5px; min-height:18px; }
.quiz-feedback.ok { color:#22a06b; font-weight:600; }
.quiz-feedback.ng { color:#c9372c; }
.quiz-submit-row { text-align:center; margin-top:1.25rem; }
.quiz-submit-btn { font-size:14px; font-weight:600; padding:9px 30px; border-radius:8px; border:none; background:var(--green); color:#fff; cursor:pointer; font-family:var(--font-ui); }
.quiz-submit-btn:hover { background:var(--green-dark); }
.quiz-score-card { background:var(--green-light); border:1px solid var(--green-mid); border-radius:var(--radius-lg); padding:1.5rem; text-align:center; margin-top:1rem; display:none; }
.score-big { font-size:40px; font-weight:700; color:var(--green-dark); line-height:1; }
.score-sub { font-size:14px; color:var(--ink-muted); margin-top:6px; margin-bottom:14px; }
.quiz-restart-btn { font-size:13px; padding:6px 20px; border-radius:6px; border:none; background:var(--green); color:#fff; cursor:pointer; font-family:var(--font-ui); }
.quiz-restart-btn:hover { background:var(--green-dark); }

.site-footer { border-top: 1px solid var(--border); padding-top: 1rem; margin-top: 2.5rem; font-size: 12px; color: var(--ink-hint); text-align: center; line-height: 1.7; }
.site-footer a { color: var(--green-dark); text-decoration: none; }
.hint-note { font-size: 12px; color: var(--ink-hint); text-align: center; margin-top: 1.5rem; }

@media (max-width: 520px) {
  .site-header { padding: 1.75rem 1.25rem 1.5rem; }
  .site-header h1 { font-size: 22px; }
  .day-header { flex-direction: column; }
  .vocab-grid { grid-template-columns: 1fr 1fr; }
  .quiz-opts { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<header class="site-header">
  <h1>每日英文練習</h1>
  <p>資料庫工程師的英文口說復健 · Daily Speaking Practice</p>
  <div class="badge-row">
    <span class="hdr-badge">Headway U4 句型</span>
    <span class="hdr-badge">Past Simple</span>
    <span class="hdr-badge">Why / Because</span>
    <span class="hdr-badge">We found that…</span>
  </div>
  <div class="btn-row">
    <a class="gh-link" href="./">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="currentColor"><path d="M9.78 4.22a.75.75 0 0 1 0 1.06L7.06 8l2.72 2.72a.75.75 0 1 1-1.06 1.06L5.47 8.53a.75.75 0 0 1 0-1.06l3.25-3.25a.75.75 0 0 1 1.06 0z"/></svg>
      返回目錄
    </a>
    <a class="gh-link" href="https://github.com/Pcc329/daily-english" target="_blank">
      <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
      View on GitHub
    </a>
  </div>
</header>

<main class="main-wrap">

  <div class="day-header">
    <div>
      <div class="day-date">2026.06.23 &nbsp;—&nbsp; Day 9</div>
      <div class="day-title">用過去式說我們今天發現了什麼</div>
      <div class="day-sub">交接盤點 · 資料品質調查 · 爬蟲研究 × Why / Because 句型</div>
    </div>
    <div class="day-tags">
      <span class="tag">we found that</span>
      <span class="tag">why / because</span>
      <span class="tag">43% missing</span>
      <span class="tag">Past Simple</span>
    </div>
  </div>

  <!-- grammar note -->
  <div class="grammar-note">
    <div class="gn-title">📖 今日文法重點 — Headway Elementary Unit 4 延伸</div>
    ✅ <strong>發現句</strong>：We <strong>found</strong> that 43% of the records <strong>had</strong> no company ID.<br>
    🔍 <strong>why / because</strong>：<strong>Why</strong> did you exclude them? &nbsp;→ <strong>Because</strong> the data was incomplete.<br>
    ⭐ <strong>不規則動詞</strong>：We <strong>found</strong> / We <strong>built</strong> / It <strong>went</strong> wrong<br>
    ❌ <strong>否定</strong>：We <strong>didn't</strong> add them to the database. &nbsp; It <strong>didn't</strong> work.<br>
    ❓ <strong>疑問</strong>：<strong>Did</strong> the crawler work? &nbsp;→ No, it <strong>didn't</strong>. The server <strong>blocked</strong> it.
  </div>

  <div class="speed-bar">
    <label>語速</label>
    <input type="range" id="speed" min="0.6" max="1.4" step="0.1" value="0.9">
    <span class="speed-val" id="speed-out">0.9×</span>
    <button class="btn-stop" onclick="stopAll()">■ 停止</button>
  </div>

  <div class="sec-label">朗讀練習</div>

  <div class="passage">
    <div class="passage-title">段落一 — 今天我們做了什麼？（Past Simple 肯定）</div>
    <div class="passage-zh">用過去式描述今天的交接盤點工作，把「整理、確認、移交」說成英文。</div>
    <div class="passage-en">
      <button class="w" onclick="say('Today I reviewed all the changes from last week')">Today I <span class="hl-past">reviewed</span> all the changes from last week</button>.
      <button class="w" onclick="say('I checked each item on the handover list')">I <span class="hl-past">checked</span> each item on the handover list</button>.
      <button class="w" onclick="say('Everything merged successfully into the main branch')">Everything <span class="hl-past">merged</span> successfully into the main branch</button>.
      <button class="w" onclick="say('I confirmed that the recommendation layout changed to top and bottom stacking')">I <span class="hl-past">confirmed</span> that the recommendation layout <span class="hl-past">changed</span> to top and bottom stacking</button>.
      <button class="w" onclick="say('We also moved the restart button next to the generate button')">We also <span class="hl-past">moved</span> the restart button next to the generate button</button>.
    </div>
    <button class="btn-read" onclick="readPara('Today I reviewed all the changes from last week. I checked each item on the handover list. Everything merged successfully into the main branch. I confirmed that the recommendation layout changed to top and bottom stacking. We also moved the restart button next to the generate button.', this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>聽整段
    </button>
  </div>

  <div class="passage">
    <div class="passage-title">段落二 — 我們發現了什麼問題？（We found that…）</div>
    <div class="passage-zh">用「We found that…」描述今天的資料品質調查發現，43% 的雲市集工業館方案缺少公司 ID。</div>
    <div class="passage-en">
      <button class="w" onclick="say('We found that 43 percent of the solutions had no company ID')">We <span class="hl-past">found</span> that 43 percent of the solutions <span class="hl-past">had</span> no company ID</button>.
      <button class="w" onclick="say('This was a big data quality problem')">This <span class="hl-past">was</span> a big data quality problem</button>.
      <button class="w" onclick="say('We checked the official government website for more data')">We <span class="hl-past">checked</span> the official government website for more data</button>.
      <button class="w" onclick="say('We found 225 solutions listed across three pages')">We <span class="hl-past">found</span> 225 solutions listed across three pages</button>.
      <button class="w" onclick="say('So we decided to exclude solutions with no company from the results')">So we <span class="hl-past">decided</span> to exclude solutions with no company from the results</button>.
    </div>
    <button class="btn-read" onclick="readPara('We found that 43 percent of the solutions had no company ID. This was a big data quality problem. We checked the official government website for more data. We found 225 solutions listed across three pages. So we decided to exclude solutions with no company from the results.', this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>聽整段
    </button>
  </div>

  <div class="passage">
    <div class="passage-title">段落三 — 爬蟲為什麼失敗？（Why / Because）</div>
    <div class="passage-zh">用 why / because 解釋爬蟲遇到的技術問題，練習原因句型。</div>
    <div class="passage-en">
      <button class="w" onclick="say('Why did the simple crawler fail?')"><span class="hl-q">Why</span> did the simple crawler fail?</button>
      <button class="w" onclick="say('Because the website used ASP.NET postback pagination')"><span class="hl-why">Because</span> the website <span class="hl-past">used</span> ASP.NET postback pagination</button>.
      <button class="w" onclick="say('The page URL did not change when we clicked next page')">The page URL <span class="hl-neg">did not</span> change when we <span class="hl-past">clicked</span> next page</button>.
      <button class="w" onclick="say('Why did it block us?')"><span class="hl-q">Why</span> did it block us?</button>
      <button class="w" onclick="say('Because the server required hidden form fields in each request')"><span class="hl-why">Because</span> the server <span class="hl-past">required</span> hidden form fields in each request</button>.
      <button class="w" onclick="say('So we built a postback-aware crawler instead')">So we <span class="hl-past">built</span> a postback-aware crawler instead</button>.
    </div>
    <button class="btn-read" onclick="readPara(`Why did the simple crawler fail? Because the website used ASP.NET postback pagination. The page URL did not change when we clicked next page. Why did it block us? Because the server required hidden form fields in each request. So we built a postback-aware crawler instead.`, this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>聽整段
    </button>
  </div>

  <div class="passage">
    <div class="passage-title">段落四 — 我們怎麼決定的？（Did you…? 疑問句）</div>
    <div class="passage-zh">用 Did you…? 模擬跟主管說明決策過程的對話練習。</div>
    <div class="passage-en">
      <button class="w" onclick="say('Did you add all 225 solutions to the database?')"><span class="hl-q">Did</span> you add all 225 solutions to the database?</button>
      <button class="w" onclick="say('No, we didn\\'t')">No, we <span class="hl-neg">didn't</span></button>.
      <button class="w" onclick="say('Why not?')"><span class="hl-q">Why</span> not?</button>
      <button class="w" onclick="say('Because we didn\\'t want to add incomplete data')"><span class="hl-why">Because</span> we <span class="hl-neg">didn't</span> want to add incomplete data</button>.
      <button class="w" onclick="say('Did you exclude the missing records from the frontend instead?')"><span class="hl-q">Did</span> you exclude the missing records from the frontend instead?</button>
      <button class="w" onclick="say('Yes, we did. It was the cleanest solution')">Yes, we did. It <span class="hl-past">was</span> the cleanest solution</button>.
    </div>
    <button class="btn-read" onclick="readPara(`Did you add all 225 solutions to the database? No, we didn't. Why not? Because we didn't want to add incomplete data. Did you exclude the missing records from the frontend instead? Yes, we did. It was the cleanest solution.`, this)">
      <svg viewBox="0 0 16 16"><path d="M3 2l10 6-10 6V2z"/></svg>聽整段
    </button>
  </div>

  <div class="sec-label">詞彙發音</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點卡片聽發音｜🟢 工作詞彙　🔵 U4 動詞</div>
  <div class="vocab-grid" id="vocabGrid"></div>

  <div class="sec-label">核心句型</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點句子聽完整朗讀</div>
  <div class="sent-list" id="sentList"></div>

  <div class="sec-label" style="margin-top:2.5rem">今日測驗</div>

  <div class="quiz-block">
    <div class="quiz-block-title"><span>📻</span> 第一關：聽音選答案（共 5 題）</div>
    <div id="listenQuiz"></div>
  </div>

  <div class="quiz-block">
    <div class="quiz-block-title"><span>✏️</span> 第二關：填空題（共 4 題）</div>
    <div id="fillQuiz"></div>
  </div>

  <div class="quiz-submit-row">
    <button class="quiz-submit-btn" onclick="submitQuiz()">交卷，看成績 →</button>
  </div>
  <div class="quiz-score-card" id="quizScore">
    <div class="score-big" id="scoreNum">—</div>
    <div class="score-sub" id="scoreSub"></div>
    <button class="quiz-restart-btn" onclick="restartQuiz()">再做一次</button>
  </div>

  <div class="hint-note">點單字聽發音 · 點卡片聽詞彙 · 點句子聽完整朗讀</div>

</main>

<footer class="site-footer">
  <a href="https://github.com/Pcc329/daily-english">daily-english</a> is maintained by
  <a href="https://github.com/Pcc329">Pcc329</a>.<br>
  工作日誌 × Headway Elementary U4 延伸 · Generated by Claude · 2026-06-23
</footer>

<script>
const vocab = [
  // 🟢 work vocab
  { en:"handover list",         ipa:"/ˈhænd.əʊ.vər lɪst/",            zh:"🟢 交接清冊" },
  { en:"data quality",          ipa:"/ˈdeɪ.tə ˈkwɒl.ɪ.ti/",           zh:"🟢 資料品質" },
  { en:"company ID",            ipa:"/ˈkʌm.pə.ni aɪ diː/",            zh:"🟢 公司識別碼" },
  { en:"postback pagination",   ipa:"/ˈpəʊst.bæk ˌpædʒ.ɪˈneɪ.ʃən/",  zh:"🟢 回傳式分頁" },
  { en:"hidden form fields",    ipa:"/ˈhɪd.ən fɔːm fiːldz/",          zh:"🟢 隱藏表單欄位" },
  { en:"exclude",               ipa:"/ɪkˈskluːd/",                     zh:"🟢 排除" },
  // 🔵 Headway U4 past-tense verbs
  { en:"found",                 ipa:"/faʊnd/",                         zh:"🔵 發現了（find，不規則）" },
  { en:"built",                 ipa:"/bɪlt/",                          zh:"🔵 建了（build，不規則）" },
  { en:"decided",               ipa:"/dɪˈsaɪ.dɪd/",                   zh:"🔵 決定了（decide）" },
  { en:"checked",               ipa:"/tʃekt/",                         zh:"🔵 確認了（check）" },
  { en:"merged",                ipa:"/mɜːdʒd/",                        zh:"🔵 合併了（merge）" },
  { en:"blocked",               ipa:"/blɒkt/",                         zh:"🔵 封鎖了（block）" },
  { en:"required",              ipa:"/rɪˈkwaɪəd/",                     zh:"🔵 要求了（require）" },
  { en:"didn't",                ipa:"/ˈdɪd.ənt/",                      zh:"🔵 沒有（過去否定）" },
];

const sentences = [
  { en:"We found that 43% of the solutions had no company ID.",            zh:"我們發現 43% 的方案沒有公司 ID。" },
  { en:"Why did the crawler fail? Because the server blocked it.",         zh:"爬蟲為什麼失敗？因為伺服器把它擋掉了。" },
  { en:"We decided to exclude solutions with no company from the results.", zh:"我們決定從結果中排除沒有公司的方案。" },
  { en:"Did you add all 225 solutions? No, we didn't.",                    zh:"你把所有 225 筆都加進去了嗎？沒有。" },
  { en:"Because we didn't want to add incomplete data.",                   zh:"因為我們不想加入不完整的資料。" },
  { en:"I reviewed all the changes and checked each item on the list.",    zh:"我回顧了所有改動，逐項確認清單。" },
  { en:"The URL did not change when we clicked next page.",                zh:"我們按下一頁時，URL 沒有改變。" },
  { en:"It was the cleanest solution — exclude from the frontend.",        zh:"這是最乾淨的做法——從前端直接排除。" },
];

const listenData = [
  { word:"found",             answer:"發現了（find，不規則）",   opts:["發現了（find，不規則）","建了（build，不規則）","決定了（decide）","確認了（check）"] },
  { word:"postback pagination",answer:"回傳式分頁",              opts:["回傳式分頁","隱藏表單欄位","資料品質","公司識別碼"] },
  { word:"exclude",           answer:"排除",                     opts:["排除","合併了（merge）","封鎖了（block）","交接清冊"] },
  { word:"didn't",            answer:"沒有（過去否定）",         opts:["沒有（過去否定）","發現了（find）","決定了（decide）","要求了（require）"] },
  { word:"built",             answer:"建了（build，不規則）",    opts:["建了（build，不規則）","合併了（merge）","確認了（check）","封鎖了（block）"] },
];

const fillData = [
  { before:"We",              blank:"found",    after:"that 43% of the solutions had no company ID.",  hint:"提示：find 的過去式（不規則）" },
  { before:"We",              blank:"didn't",   after:"want to add incomplete data.",                  hint:"提示：過去式否定助動詞縮寫" },
  { before:"Why did the crawler fail? Because the server", blank:"blocked", after:"it.",              hint:"提示：block 的過去式（規則 -ed）" },
  { before:"We",              blank:"decided",  after:"to exclude solutions with no company.",         hint:"提示：decide 的過去式（規則 -d）" },
];

/* build */
const vocabGrid = document.getElementById('vocabGrid');
vocab.forEach(v => {
  const c = document.createElement('div'); c.className = 'vocab-card';
  c.innerHTML = `<div class="vocab-en">${v.en}</div><div class="vocab-ipa">${v.ipa}</div><div class="vocab-zh">${v.zh}</div>`;
  c.addEventListener('click', () => speakVocab(v.en, c)); vocabGrid.appendChild(c);
});
const sentList = document.getElementById('sentList');
const playSVG = `<svg class="sent-icon" viewBox="0 0 16 16" fill="currentColor"><path d="M3 2l10 6-10 6V2z"/></svg>`;
sentences.forEach(s => {
  const item = document.createElement('div'); item.className = 'sent-item';
  item.innerHTML = `<div><div class="sent-en">${s.en}</div><div class="sent-zh">${s.zh}</div></div>${playSVG}`;
  item.addEventListener('click', () => readPara(s.en, item)); sentList.appendChild(item);
});
const lqDiv = document.getElementById('listenQuiz');
listenData.forEach((q, i) => {
  const opts = q.opts.map(o => `<button class="quiz-opt" onclick="pickOpt(this,${i},'${o}','${q.answer}')">${o}</button>`).join('');
  lqDiv.innerHTML += `<div class="quiz-q" id="lq${i}">
    <div class="quiz-q-row"><span class="quiz-q-num">${i+1}</span>
    <button class="play-word-btn" onclick="sayQuiz('${q.word}')">
      <svg width="11" height="11" viewBox="0 0 16 16" fill="currentColor"><path d="M3 2l10 6-10 6V2z"/></svg>聽單字
    </button></div>
    <div class="quiz-opts">${opts}</div>
    <div class="quiz-feedback" id="lf${i}"></div></div>`;
});
const fqDiv = document.getElementById('fillQuiz');
fillData.forEach((q, i) => {
  fqDiv.innerHTML += `<div class="quiz-q" id="fq${i}">
    <div class="quiz-q-row"><span class="quiz-q-num">${i+1}</span><div class="quiz-q-text">填入正確的英文單字</div></div>
    <div class="fill-sentence">${q.before} <input class="fill-input" id="fi${i}" type="text" autocomplete="off" spellcheck="false" placeholder="______"> ${q.after}</div>
    <div class="fill-hint">${q.hint}</div>
    <button class="quiz-check-btn" onclick="checkFill(${i},'${q.blank}')">確認</button>
    <div class="quiz-feedback" id="ff${i}"></div></div>`;
});
fillData.forEach((q, i) => {
  const inp = document.getElementById('fi'+i);
  if(inp) inp.addEventListener('keydown', e => { if(e.key==='Enter') checkFill(i, q.blank); });
});

/* speech */
let activeEl = null;
function clearActive(){ if(activeEl){activeEl.classList.remove('playing','active');activeEl=null;} }
function stopAll(){ window.speechSynthesis.cancel(); clearActive(); }
function getRate(){ return parseFloat(document.getElementById('speed').value); }
function utter(text,el){
  window.speechSynthesis.cancel(); clearActive();
  const u=new SpeechSynthesisUtterance(text); u.lang='en-US'; u.rate=getRate();
  if(el){el.classList.add('playing','active');activeEl=el;}
  u.onend=u.onerror=()=>{if(el)el.classList.remove('playing','active');if(activeEl===el)activeEl=null;};
  window.speechSynthesis.speak(u);
}
function say(t){utter(t,null);}
function sayQuiz(t){utter(t,null);}
function speakVocab(t,c){if(c.classList.contains('playing')){stopAll();return;}utter(t,c);}
function readPara(t,b){if(b&&b.classList.contains('active')){stopAll();return;}utter(t,b);}
document.getElementById('speed').addEventListener('input',function(){
  document.getElementById('speed-out').textContent=parseFloat(this.value).toFixed(1)+'×';
});

/* quiz */
let listenScore=0,fillScore=0;
let listenDone=new Array(listenData.length).fill(false);
let fillDone=new Array(fillData.length).fill(false);
function pickOpt(btn,idx,chosen,correct){
  if(listenDone[idx])return; listenDone[idx]=true;
  document.getElementById('lq'+idx).querySelectorAll('.quiz-opt').forEach(b=>{
    b.disabled=true; if(b.textContent===correct)b.classList.add('correct');
  });
  const fb=document.getElementById('lf'+idx);
  if(chosen===correct){btn.classList.add('correct');fb.textContent='✓ 正確！';fb.className='quiz-feedback ok';listenScore++;}
  else{btn.classList.add('wrong');fb.textContent='✗ 答案是：'+correct;fb.className='quiz-feedback ng';}
}
function checkFill(idx,answer){
  if(fillDone[idx])return; fillDone[idx]=true;
  const inp=document.getElementById('fi'+idx); inp.disabled=true;
  const val=inp.value.trim().toLowerCase();
  const fb=document.getElementById('ff'+idx);
  if(val===answer.toLowerCase()){inp.classList.add('correct');fb.textContent='✓ 正確！';fb.className='quiz-feedback ok';fillScore++;}
  else{inp.classList.add('wrong');fb.textContent='✗ 答案是：'+answer;fb.className='quiz-feedback ng';}
}
function submitQuiz(){
  fillData.forEach((q,i)=>{if(!fillDone[i])checkFill(i,q.blank);});
  const total=listenData.length+fillData.length,got=listenScore+fillScore;
  const pct=Math.round(got/total*100);
  const msgs=['繼續加油！','不錯，繼續練習！','很好！快掌握了！','太厲害！全對！'];
  const lvl=pct>=100?3:pct>=75?2:pct>=50?1:0;
  document.getElementById('scoreNum').textContent=got+' / '+total;
  document.getElementById('scoreSub').textContent=pct+'分　'+msgs[lvl];
  document.getElementById('quizScore').style.display='block';
  document.getElementById('quizScore').scrollIntoView({behavior:'smooth',block:'center'});
}
function restartQuiz(){
  listenScore=0;fillScore=0;listenDone.fill(false);fillDone.fill(false);
  document.querySelectorAll('.quiz-opt').forEach(b=>{b.disabled=false;b.className='quiz-opt';});
  document.querySelectorAll('.fill-input').forEach(i=>{i.disabled=false;i.value='';i.className='fill-input';});
  document.querySelectorAll('.quiz-feedback').forEach(f=>{f.textContent='';f.className='quiz-feedback';});
  document.getElementById('quizScore').style.display='none';
}
</script>
</body>
</html>
