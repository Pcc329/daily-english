<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>每日英文練習 | 2026-08-14 Case Collection × 讓步句型 × 字首字根</title>
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --green: #157878; --green-dark: #0f6e56; --green-light: #e8f5f1; --green-mid: #9fd9c8;
  --ink: #2c2c2a; --ink-muted: #5f5e5a; --ink-hint: #888780;
  --surface: #ffffff; --surface-alt: #f7f6f2;
  --border: rgba(44,44,42,.12); --border-em: rgba(44,44,42,.25);
  --radius: 8px; --radius-lg: 14px;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'Menlo', 'Courier New', monospace;
}
html { scroll-behavior: smooth; }
body { font-family: var(--font-ui); background: var(--surface-alt); color: var(--ink); min-height: 100vh; overflow-x: hidden; }
.site-header { background: linear-gradient(120deg, var(--green) 0%, var(--green-dark) 100%); padding: 2.5rem 2rem 2rem; color: #fff; }
.site-header h1 { font-size: 26px; font-weight: 700; margin-bottom: 4px; }
.site-header p { font-size: 14px; opacity: .82; margin-bottom: 14px; }
.badge-row, .btn-row, .day-tags, .speed-bar { display: flex; gap: 8px; flex-wrap: wrap; }
.badge-row { margin-bottom: 12px; }
.hdr-badge { font-size: 12px; font-weight: 600; padding: 3px 12px; border-radius: 999px; background: rgba(255,255,255,.18); border: 1px solid rgba(255,255,255,.35); color: #fff; }
.gh-link { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; color: rgba(255,255,255,.85); text-decoration: none; border: 1px solid rgba(255,255,255,.4); border-radius: 6px; padding: 4px 12px; }
.gh-link:hover { background: rgba(255,255,255,.15); }
.main-wrap { width: 100%; max-width: 820px; min-width: 0; margin: 0 auto; padding: 2rem 1.25rem 4rem; overflow: hidden; }
.main-wrap > * { width: 100%; max-width: 100%; min-width: 0; }
.day-header, .passage, .quiz-block, .practice-card, .summary-card, .root-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg); }
.day-header { padding: 1.25rem 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: flex-start; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }
.day-date { font-size: 12px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: var(--green); margin-bottom: 4px; }
.day-title { font-size: 22px; font-weight: 700; line-height: 1.2; }
.day-sub { font-size: 14px; color: var(--ink-muted); margin-top: 4px; }
.tag { font-size: 11px; font-weight: 500; padding: 3px 10px; border-radius: 999px; background: var(--green-light); color: var(--green-dark); border: 1px solid var(--green-mid); white-space: nowrap; }
.grammar-note { background: #eaf2ff; border: 1px solid #b3cfee; border-radius: var(--radius-lg); padding: 1rem 1.25rem; margin-bottom: 1.5rem; font-size: 13.5px; line-height: 1.8; color: #1a3a5c; }
.gn-title { font-size: 11px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #5080a0; margin-bottom: 8px; }
.speed-bar { align-items: center; margin-bottom: 1.5rem; }
.speed-bar label { font-size: 13px; color: var(--ink-muted); }
.speed-bar input[type=range] { width: 130px; accent-color: var(--green); }
.speed-val { font-size: 13px; font-weight: 600; color: var(--green-dark); min-width: 36px; }
.btn-stop, .btn-read, .quiz-check-btn { font-family: var(--font-ui); border: 1px solid var(--border-em); border-radius: 6px; background: var(--surface); color: var(--ink-muted); cursor: pointer; touch-action: manipulation; }
.btn-stop { font-size: 12px; padding: 4px 12px; }
.sec-label { display: flex; align-items: center; gap: 10px; font-size: 11px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: var(--ink-hint); margin: 2rem 0 1rem; }
.sec-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }
.passage { padding: 1.25rem 1.5rem 1rem; margin-bottom: 1rem; }
.passage-title { font-size: 12px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-hint); margin-bottom: 4px; }
.word-hint { font-size: 11px; color: var(--green); margin-bottom: .75rem; }
.passage-en { font-size: 15.5px; line-height: 1.9; color: var(--ink); overflow-wrap: anywhere; }
.passage-en p + p { margin-top: .75rem; }

.w { cursor: pointer; border-bottom: 1.5px dotted var(--green-mid); border-radius: 3px; padding: 0 1px; transition: background 0.12s; }
.w:hover { background: var(--green-light); border-bottom-color: var(--green); }
.w.playing { background: var(--green-light); color: var(--green-dark); font-weight: 600; border-bottom-color: var(--green); }

.hl-cause { color: #c0392b; font-weight: 700; }
.hl-result { color: #1a5276; font-weight: 700; }
.hl-key { color: var(--green-dark); font-weight: 600; }
.hl-perf { color: #6c3483; font-weight: 700; }
.btn-read { display: inline-flex; align-items: center; gap: 6px; font-size: 12px; padding: 5px 14px; background: var(--surface-alt); margin-top: 10px; }
.btn-read:hover, .btn-read.active { border-color: var(--green); color: var(--green-dark); background: var(--green-light); }
.vocab-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(185px, 1fr)); gap: 10px; }
.vocab-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: .9rem 1rem; cursor: pointer; touch-action: manipulation; }
.vocab-card:hover, .vocab-card.playing { border-color: var(--green); background: var(--green-light); }
.vocab-en { font-size: 13.5px; font-weight: 600; margin-bottom: 3px; }
.vocab-ipa { font-size: 11px; color: var(--ink-hint); font-family: var(--font-mono); margin-bottom: 4px; }
.vocab-zh { font-size: 12px; color: var(--ink-muted); }
.root-list { display: flex; flex-direction: column; gap: 12px; }
.root-card { padding: 1rem 1.25rem; cursor: pointer; touch-action: manipulation; }
.root-card:hover, .root-card.playing { border-color: var(--green); background: var(--green-light); }
.root-morph { font-size: 15px; font-weight: 700; color: var(--green-dark); margin-bottom: 4px; }
.root-morph .part { background: #fff4d6; border-radius: 4px; padding: 0 5px; }
.root-mean { font-size: 12.5px; color: var(--ink-muted); margin-bottom: 8px; }
.root-family { font-size: 13px; line-height: 1.9; color: var(--ink); }
.root-family b { color: var(--green-dark); }
.sent-list { display: flex; flex-direction: column; gap: 9px; }
.sent-item { background: var(--surface); border: 1px solid var(--border); border-left: 3px solid var(--green); border-radius: 0 var(--radius) var(--radius) 0; padding: .8rem 1rem .8rem 1.1rem; cursor: pointer; touch-action: manipulation; }
.sent-item:hover, .sent-item.playing { background: var(--green-light); }
.sent-en { font-size: 14.5px; line-height: 1.55; overflow-wrap: anywhere; }
.sent-zh { font-size: 12px; color: var(--ink-muted); margin-top: 3px; }
.hint-note { font-size: 12px; color: var(--ink-hint); text-align: center; margin-top: 1.5rem; }
.quiz-block { padding: 1.25rem 1.5rem; margin-bottom: 1rem; }
.quiz-block-title { font-size: 13px; font-weight: 600; color: var(--ink-muted); margin-bottom: 14px; }
.quiz-q { margin-bottom: 1.25rem; padding-bottom: 1.25rem; border-bottom: 1px dashed var(--border); }
.quiz-q:last-child { margin-bottom: 0; padding-bottom: 0; border-bottom: 0; }
.quiz-q-text { font-size: 14.5px; line-height: 1.55; margin-bottom: 8px; }
.quiz-opts { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; }
.quiz-opt { font-size: 13px; padding: 7px 12px; border-radius: var(--radius); border: 1px solid var(--border-em); background: var(--surface-alt); cursor: pointer; text-align: left; touch-action: manipulation; }
.quiz-opt.correct { border-color: #22a06b; background: #e3fcef; color: #1a6b45; font-weight: 600; }
.quiz-opt.wrong { border-color: #c9372c; background: #ffeceb; color: #c9372c; }
.fill-sentence { font-size: 15px; line-height: 2.3; overflow-wrap: anywhere; }
.fill-input { font-size: 15px; border: 0; border-bottom: 2px solid var(--green); background: transparent; min-width: 120px; padding: 0 4px; text-align: center; }
.fill-input.correct { border-color: #22a06b; color: #1a6b45; }
.fill-input.wrong { border-color: #c9372c; color: #c9372c; }
.quiz-check-btn { font-size: 12px; padding: 4px 12px; margin-top: 6px; }
.quiz-feedback { font-size: 12px; margin-top: 5px; min-height: 18px; }
.quiz-feedback.ok { color: #22a06b; font-weight: 600; }
.quiz-feedback.ng { color: #c9372c; }
.practice-card, .summary-card { padding: 1.25rem 1.5rem; line-height: 1.8; }
.practice-card p + p, .summary-card p + p { margin-top: .8rem; }
.practice-card .advanced { background: var(--green-light); border-left: 3px solid var(--green); padding: .75rem 1rem; margin-top: 1rem; }
.summary-card { background: #fffdf4; border-color: #e5d9a8; }
.summary-card .english-summary { background: var(--surface); border-left: 3px solid #c6a94b; padding: .75rem 1rem; margin: 1rem 0; }
.site-footer { border-top: 1px solid var(--border); padding: 1.25rem; font-size: 12px; color: var(--ink-hint); text-align: center; line-height: 1.7; }
.site-footer a { color: var(--green-dark); text-decoration: none; }
@media (max-width: 520px) {
  .site-header { padding: 1.75rem 1.25rem 1.5rem; }
  .day-header { flex-direction: column; }
  .main-wrap { padding-left: .75rem; padding-right: .75rem; }
  .vocab-grid { grid-template-columns: minmax(0, 1fr); }
  .quiz-opts { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<header class="site-header">
  <h1>每日英文練習</h1>
  <p>資料庫工程師的英文口說復健 · Daily Speaking Practice</p>
  <div class="badge-row">
    <span class="hdr-badge">Concession</span>
    <span class="hdr-badge">even though / despite / although</span>
    <span class="hdr-badge">Case Collection Day</span>
    <span class="hdr-badge">Word Roots</span>
    <span class="hdr-badge">點詞聽音</span>
  </div>
  <div class="btn-row">
    <a class="gh-link" href="./">← 返回目錄</a>
    <a class="gh-link" href="https://github.com/Pcc329/daily-english" target="_blank">View on GitHub</a>
  </div>
</header>

<main class="main-wrap">

  <div class="day-header">
    <div>
      <div class="day-date">2026.08.14 &nbsp;—&nbsp; Day 16</div>
      <div class="day-title">Case Collection Wrap-up × 讓步句型 × 字首字根</div>
      <div class="day-sub">Ambiguous matches · Foreign key fixes · API filter bug found</div>
    </div>
    <div class="day-tags">
      <span class="tag">even though</span>
      <span class="tag">despite</span>
      <span class="tag">although</span>
      <span class="tag">legacy filter</span>
    </div>
  </div>

  <div class="grammar-note">
    <div class="gn-title">📖 今日文法重點 — 讓步句型 Concession</div>
    今天的工作充滿「雖然遇到阻礙，但還是完成了」的情境，這正是讓步句型的主場。<br /><br />
    ✅ <strong>Even though + 完整句子</strong>：Even though the GCIS search returned ten candidates, only one was a reliable match.<br />
    ✅ <strong>Despite + 名詞/動名詞</strong>：Despite the ambiguous company name, the correct tax ID was confirmed.<br />
    ✅ <strong>Although + 完整句子</strong>：Although the transaction failed once, the second attempt succeeded.<br />
    ✅ <strong>對比但不否定</strong>：讓步句型不是說「這件事沒發生」，是說「儘管有阻礙，結果依然成立」。<br /><br />
    <strong>口訣：</strong><em>even though / although</em> 後面接<strong>完整句子</strong>；<em>despite / in spite of</em> 後面接<strong>名詞</strong>。
  </div>

  <div class="speed-bar">
    <label for="speed">語速</label>
    <input type="range" id="speed" min="0.6" max="1.4" step="0.1" value="0.9" />
    <span class="speed-val" id="speed-out">0.9×</span>
    <button class="btn-stop" onclick="stopAll()">■ 停止</button>
  </div>

  <div class="sec-label">朗讀練習</div>

  <div class="passage">
    <div class="passage-title">段落一 — 今天做了什麼？</div>
    <div class="word-hint">💡 底線單字可點擊單獨發音</div>
    <div class="passage-en" data-speech="Today we continued the case collection task. Even though most companies were confirmed yesterday, seven records still needed manual verification. Despite the ambiguous company names, five were resolved through official registration data. As a result, twenty-one out of twenty-three cases are now complete.">
      <p>Today we continued the <span class="w" onclick="speakWord('case collection')">case collection</span> task.<br />
      <span class="hl-cause">Even though</span> most companies were confirmed yesterday, seven records still needed
      <span class="w" onclick="speakWord('manual verification')">manual verification</span>.<br />
      <span class="hl-cause">Despite</span> the <span class="w" onclick="speakWord('ambiguous')">ambiguous</span> company names, five were resolved through official
      <span class="w" onclick="speakWord('registration data')">registration data</span>.<br />
      As a result, twenty-one out of twenty-three cases are now complete.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落二 — 太多同名公司</div>
    <div class="word-hint">💡 底線單字可點擊單獨發音</div>
    <div class="passage-en" data-speech="Two company names turned out to be too common to verify. Even though we searched the official registry, nearly ten candidates shared the same name. Since the source article gave no address or tax ID, there was no reliable way to pick the right one. Although we asked the colleague who provided the article, the information chain had already run out. We decided to shelve these two records rather than guess.">
      <p>Two company names turned out to be too <span class="w" onclick="speakWord('common')">common</span> to verify.<br />
      <span class="hl-cause">Even though</span> we searched the official registry, nearly ten
      <span class="w" onclick="speakWord('candidates')">candidates</span> shared the same name.<br />
      Since the source article gave no address or tax ID, there was no reliable way to pick the right one.<br />
      <span class="hl-cause">Although</span> we asked the colleague who provided the article, the
      <span class="w" onclick="speakWord('information chain')">information chain</span> had already run out.<br />
      We decided to <span class="w" onclick="speakWord('shelve')">shelve</span> these two records rather than guess.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落三 — 外鍵擋下了第一次寫入</div>
    <div class="word-hint">💡 底線單字可點擊單獨發音</div>
    <div class="passage-en" data-speech="The first insert attempt failed. Even though the case records looked correct, they referenced companies that did not exist yet. This violated a foreign key constraint. Despite the setback, the fix was simple: insert the companies first, then the cases. After the correction, all eleven records were written successfully.">
      <p>The first <span class="w" onclick="speakWord('insert attempt')">insert attempt</span> failed.<br />
      <span class="hl-cause">Even though</span> the case records looked correct, they referenced companies that did not exist yet.<br />
      This violated a <span class="w" onclick="speakWord('foreign key constraint')">foreign key constraint</span>.<br />
      <span class="hl-cause">Despite</span> the <span class="w" onclick="speakWord('setback')">setback</span>, the fix was simple: insert the companies first, then the cases.<br />
      After the correction, all eleven records were written successfully.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落四 — 一個過濾規則，兩條路徑</div>
    <div class="word-hint">💡 底線單字可點擊單獨發音</div>
    <div class="passage-en" data-speech="We found a real bug today. Even though the record status filter had been written correctly, it only applied to the old Airtable path. Since production had switched to Supabase after the cutover, the filter was never actually running. Although the rule existed on paper, it had no effect in practice. We fixed it by adding the same filter to the Supabase query, and the retired records disappeared from search results.">
      <p>We found a real bug today.<br />
      <span class="hl-cause">Even though</span> the <span class="w" onclick="speakWord('record status filter')">record status filter</span> had been written correctly, it only applied to the old Airtable path.<br />
      Since production had switched to Supabase after the cutover, the filter was never actually running.<br />
      <span class="hl-cause">Although</span> the rule existed on paper, it had no effect in practice.<br />
      We fixed it by adding the same filter to the Supabase query, and the
      <span class="w" onclick="speakWord('retired records')">retired records</span> disappeared from search results.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落五 — 為什麼要提前建治理表？（主管問答）</div>
    <div class="word-hint">💡 底線單字可點擊單獨發音</div>
    <div class="passage-en" data-speech="Why did you build a new table for something so small? Because we discovered that one data source program had already ended in June. Even though only one source is affected right now, the same problem could happen again. Despite the extra effort, we built a lightweight table to track the status of every source. As a result, future changes only require one row update, not a rewrite of thousands of records.">
      <p>Why did you build a new table for something so small?<br />
      Because we discovered that one data source program had already ended in June.<br />
      <span class="hl-cause">Even though</span> only one source is affected right now, the same problem could happen again.<br />
      <span class="hl-cause">Despite</span> the extra effort, we built a lightweight table to track the
      <span class="w" onclick="speakWord('status')">status</span> of every source.<br />
      As a result, future changes only require one row update, not a rewrite of thousands of records.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="sec-label">詞彙發音</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點卡片聽發音</div>
  <div class="vocab-grid" id="vocabGrid"></div>

  <div class="sec-label">字首字根延伸記憶</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點卡片聽字根單字 · 拆解一次記一串</div>
  <div class="root-list" id="rootList"></div>

  <div class="sec-label">核心句型</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點句子聽完整朗讀</div>
  <div class="sent-list" id="sentList"></div>

  <div class="sec-label">今日測驗</div>
  <div class="quiz-block">
    <div class="quiz-block-title">📻 第一關：聽音選答案</div>
    <div id="listenQuiz"></div>
  </div>
  <div class="quiz-block">
    <div class="quiz-block-title">✏️ 第二關：讓步句型填空</div>
    <div id="fillQuiz"></div>
  </div>

  <div class="sec-label">今日口說任務</div>
  <div class="practice-card">
    <p><strong>請跟讀三次：</strong></p>
    <p data-speech="Even though two company names were too ambiguous to verify, we completed twenty-one out of twenty-three cases today. Despite a foreign key error on the first attempt, the fix was straightforward. Although the retired-record filter existed on paper, it was never applied to the new database path — until today.">
      Even though two company names were too ambiguous to verify, we completed twenty-one out of twenty-three cases today.<br />
      Despite a foreign key error on the first attempt, the fix was straightforward.<br />
      Although the retired-record filter existed on paper, it was never applied to the new database path — until today.
    </p>
    <button class="btn-read">▶ 聽整段</button>
    <div class="advanced">
      <strong>進階版：</strong><br />
      <span data-speech="Even though the program had ended two months earlier, no one had recorded that fact anywhere in the system. Despite the small scope of the fix, we chose to build a governance table so the same gap would not repeat itself. In spite of tight time pressure, row-level security was enabled by default.">
        Even though the program had ended two months earlier, no one had recorded that fact anywhere in the system.<br />
        Despite the small scope of the fix, we chose to build a governance table so the same gap would not repeat itself.<br />
        In spite of tight time pressure, row-level security was enabled by default.
      </span>
    </div>
  </div>

  <div class="sec-label">今日總結</div>
  <div class="summary-card">
    <p>今天英文主題是用讓步句型描述「儘管遇到阻礙，工作依然完成」的邏輯。</p>
    <p>中文你說的是：<br />
    「雖然兩家公司名字太菜市場、查不出來，我們還是完成了 21/23 家案例。中間外鍵擋了一次，補建公司之後就寫進去了。順便發現一個 bug：下架過濾條件其實早就寫好了，只是遷移到 Supabase 之後沒有跟著搬過去。」</p>
    <div class="english-summary">
      Even though two companies could not be reliably identified, twenty-one out of twenty-three cases were completed today.<br />
      Despite a foreign key error on the first insert, the companies were added first and the fix worked.<br />
      Although the filter logic existed before the cutover, it had not been applied to the Supabase path — until today.
    </div>
    <p>讓步句型是報告「困難與結果」最自然的骨架：先承認<strong>阻礙（even though / despite）</strong>，再說出<strong>結果依然成立</strong>。這樣講,主管聽得出來你不是隱藏問題,是解決了問題。</p>
  </div>

</main>

<footer class="site-footer">
  <a href="https://github.com/Pcc329/daily-english">daily-english</a> is maintained by Pcc329.<br />
  Case Collection Day × 讓步句型 × 字首字根 · 2026-08-14
</footer>

<script>
function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

const vocab = [
  { en:"ambiguous",           ipa:"/æmˈbɪɡjuəs/",             zh:"模糊不清的；難以判斷的" },
  { en:"foreign key",         ipa:"/ˈfɒrən kiː/",             zh:"外鍵（資料庫關聯約束）" },
  { en:"constraint",          ipa:"/kənˈstreɪnt/",            zh:"限制條件" },
  { en:"legacy",              ipa:"/ˈleɡəsi/",                zh:"舊有的；歷史遺留的" },
  { en:"deprecate",           ipa:"/ˈdeprəkeɪt/",             zh:"棄用；不再建議使用" },
  { en:"row-level security",  ipa:"/roʊ ˈlevəl sɪˈkjʊərəti/", zh:"列層級安全性（RLS）" },
  { en:"provenance",          ipa:"/ˈprɒvənəns/",             zh:"來源；出處" },
  { en:"shelve",              ipa:"/ʃelv/",                   zh:"擱置；暫緩處理" },
  { en:"redundant",           ipa:"/rɪˈdʌndənt/",             zh:"冗餘的；多餘的" },
  { en:"audit trail",         ipa:"/ˈɔːdɪt treɪl/",           zh:"稽核軌跡" },
  { en:"placeholder",         ipa:"/ˈpleɪshoʊldər/",          zh:"佔位值" },
  { en:"governance",          ipa:"/ˈɡʌvərnəns/",             zh:"治理" },
];

const roots = [
  {
    morph: [["ambi-","兩者、雙方"],["ig/ag","趕、驅動（拉丁 agere）"]],
    means: "ambiguous = 被兩個方向拉扯 → 模糊不清的",
    family: "同根 <b>ambi-</b>（雙方）：<b>ambi</b>guous(模糊)、<b>ambi</b>dextrous(左右手皆靈巧)、<b>ambi</b>valent(矛盾的)、<b>ambi</b>ent(周遭的)",
    say: "ambiguous, ambidextrous, ambivalent, ambient"
  },
  {
    morph: [["strain/strict","拉緊、束緊（拉丁 stringere）"]],
    means: "constraint = 被綁緊的狀態 → 限制條件",
    family: "同根 <b>strain/strict</b>（束緊）：con<b>strain</b>t(限制)、re<b>strict</b>(限制)、<b>strict</b>(嚴格的)、<b>strain</b>(拉緊)、con<b>strict</b>(壓縮)",
    say: "constraint, restrict, strict, strain, constrict"
  },
  {
    morph: [["leg","法律、指定（拉丁 lex/legare）"]],
    means: "legacy = 依法傳承下來的東西 → 舊有的、遺留的",
    family: "同根 <b>leg</b>（法律）：<b>leg</b>acy(遺產/舊有)、<b>leg</b>al(合法的)、<b>leg</b>islate(立法)、de<b>leg</b>ate(委派)、<b>leg</b>itimate(正當的)",
    say: "legacy, legal, legislate, delegate, legitimate"
  },
  {
    morph: [["prov/pro-","向前"],["ven","來（拉丁 venire）"]],
    means: "provenance = 從哪裡來的紀錄 → 來源、出處",
    family: "同根 <b>ven</b>（來）：pro<b>ven</b>ance(來源)、con<b>ven</b>e(召集)、inter<b>ven</b>e(介入)、<b>ven</b>ue(場地)、re<b>ven</b>ue(收入)",
    say: "provenance, convene, intervene, venue, revenue"
  },
  {
    morph: [["aud","聽（拉丁 audire）"]],
    means: "audit trail = 可被聽審、追查的軌跡 → 稽核軌跡",
    family: "同根 <b>aud</b>（聽）：<b>aud</b>it(稽核)、<b>aud</b>ience(聽眾)、<b>aud</b>ible(聽得見的)、<b>aud</b>io(音訊)",
    say: "audit, audience, audible, audio"
  },
];

const sentences = [
  { en:"Even though the search returned ten candidates, only one was reliable.", zh:"雖然搜尋出十個候選，只有一個可信。" },
  { en:"Despite the ambiguous name, the tax ID was confirmed through official records.", zh:"儘管名稱模糊，統編還是透過官方紀錄確認了。" },
  { en:"Although the first insert failed, the second attempt succeeded.", zh:"雖然第一次寫入失敗，第二次就成功了。" },
  { en:"The filter existed on paper, but it was never applied to the new path.", zh:"這個過濾條件寫在文件裡，但從未套用到新路徑上。" },
  { en:"We shelved the two records rather than guessing.", zh:"我們選擇擱置這兩筆記錄，而不是用猜的。" },
  { en:"In spite of the small scope, a governance table was built for long-term safety.", zh:"儘管範圍很小，還是建了一張治理表以求長期安全。" },
  { en:"Row-level security was enabled by default, even under time pressure.", zh:"即使時間緊迫，列層級安全性仍預設開啟。" },
  { en:"The two counts differ, despite both being technically correct.", zh:"儘管兩者技術上都正確，這兩個計數依然不同。" },
  { en:"Although the program had ended in June, nothing in the system reflected that.", zh:"雖然計畫六月就結束了，系統裡卻沒有任何紀錄反映這件事。" },
  { en:"We fixed the root cause instead of patching the symptom.", zh:"我們修的是根本原因，而不是表面症狀。" },
];

const listenData = [
  { word:"ambiguous",          answer:"模糊不清的；難以判斷的", opts:["模糊不清的；難以判斷的","冗餘的","來源；出處","擱置"] },
  { word:"constraint",         answer:"限制條件",               opts:["限制條件","治理","稽核軌跡","舊有的"] },
  { word:"legacy",             answer:"舊有的；歷史遺留的",     opts:["舊有的；歷史遺留的","模糊不清的","佔位值","限制條件"] },
  { word:"provenance",         answer:"來源；出處",             opts:["來源；出處","冗餘的","擱置","治理"] },
  { word:"row-level security", answer:"列層級安全性（RLS）",    opts:["列層級安全性（RLS）","稽核軌跡","佔位值","舊有的"] },
];

const fillData = [
  { before:"",                          blank:"Even though", after:"ten candidates were found, only one was reliable.", hint:"雖然（後接完整句子）" },
  { before:"",                          blank:"Despite",     after:"the ambiguous name, the tax ID was confirmed.",      hint:"儘管（後接名詞）" },
  { before:"The filter existed on paper,", blank:"but",       after:"it was never applied to the new path.",             hint:"但是（轉折連接詞）" },
  { before:"",                          blank:"Although",    after:"the program had ended, nothing reflected that.",     hint:"雖然（後接完整句子）" },
];

let activeEl = null;
function stopAll() {
  window.speechSynthesis.cancel();
  if (activeEl) activeEl.classList.remove('playing', 'active');
  activeEl = null;
}
function speak(text, el) {
  stopAll();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US';
  u.rate = parseFloat(document.getElementById('speed').value);
  if (el) { el.classList.add('playing', 'active'); activeEl = el; }
  u.onend = u.onerror = () => {
    if (el) el.classList.remove('playing', 'active');
    activeEl = null;
  };
  window.speechSynthesis.speak(u);
}

function speakWord(text) {
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US';
  u.rate = parseFloat(document.getElementById('speed').value);
  window.speechSynthesis.speak(u);
}

document.getElementById('speed').addEventListener('input', function () {
  document.getElementById('speed-out').textContent = Number(this.value).toFixed(1) + '×';
});
document.querySelectorAll('.btn-read').forEach(button => {
  button.addEventListener('click', () => {
    const container = button.previousElementSibling;
    const target = container && container.dataset.speech ? container
      : button.parentElement.querySelector('[data-speech]');
    if (target) speak(target.dataset.speech, button);
  });
});

const vocabGrid = document.getElementById('vocabGrid');
vocab.forEach(item => {
  const card = document.createElement('div');
  card.className = 'vocab-card';
  card.innerHTML = `<div class="vocab-en">${item.en}</div><div class="vocab-ipa">${item.ipa}</div><div class="vocab-zh">${item.zh}</div>`;
  card.addEventListener('click', () => speak(item.en, card));
  vocabGrid.appendChild(card);
});

const rootList = document.getElementById('rootList');
roots.forEach(item => {
  const card = document.createElement('div');
  card.className = 'root-card';
  const morphHtml = item.morph.map(m => `<span class="part">${m[0]}</span> <span style="font-size:11px;color:var(--ink-hint)">${m[1]}</span>`).join(' &nbsp;+&nbsp; ');
  card.innerHTML = `<div class="root-morph">${morphHtml}</div><div class="root-mean">${item.means}</div><div class="root-family">${item.family}</div>`;
  card.addEventListener('click', () => speak(item.say, card));
  rootList.appendChild(card);
});

const sentList = document.getElementById('sentList');
sentences.forEach(item => {
  const row = document.createElement('div');
  row.className = 'sent-item';
  row.innerHTML = `<div class="sent-en">${item.en}</div><div class="sent-zh">${item.zh}</div>`;
  row.addEventListener('click', () => speak(item.en, row));
  sentList.appendChild(row);
});

const listenQuiz = document.getElementById('listenQuiz');
listenData.forEach((q, index) => {
  const block = document.createElement('div');
  block.className = 'quiz-q';
  block.innerHTML = `<div class="quiz-q-text">${index + 1}. What does "<strong>${q.word}</strong>" mean? <button class="quiz-check-btn play-word">▶ 聽單字</button></div><div class="quiz-opts"></div><div class="quiz-feedback"></div>`;
  block.querySelector('.play-word').addEventListener('click', () => speakWord(q.word));
  const optsDiv = block.querySelector('.quiz-opts');
  shuffle(q.opts).forEach(option => {
    const btn = document.createElement('button');
    btn.className = 'quiz-opt';
    btn.textContent = option;
    btn.addEventListener('click', () => {
      optsDiv.querySelectorAll('button').forEach(b => { b.disabled = true; if (b.textContent === q.answer) b.classList.add('correct'); });
      const fb = block.querySelector('.quiz-feedback');
      if (option === q.answer) { btn.classList.add('correct'); fb.textContent = '✓ 正確！'; fb.className = 'quiz-feedback ok'; }
      else { btn.classList.add('wrong'); fb.textContent = '✗ 答案：' + q.answer; fb.className = 'quiz-feedback ng'; }
    });
    optsDiv.appendChild(btn);
  });
  listenQuiz.appendChild(block);
});

const fillQuiz = document.getElementById('fillQuiz');
fillData.forEach((q, index) => {
  const block = document.createElement('div');
  block.className = 'quiz-q';
  block.innerHTML = `<div class="quiz-q-text">${index + 1}. Fill in the correct concession word. <span style="font-size:12px;color:var(--ink-hint)">（${q.hint}）</span></div><div class="fill-sentence">${q.before} <input class="fill-input" type="text" autocomplete="off" placeholder="______"> ${q.after}</div><button class="quiz-check-btn">確認</button><div class="quiz-feedback"></div>`;
  const input = block.querySelector('input');
  const validate = () => {
    const fb = block.querySelector('.quiz-feedback');
    if (input.value.trim().toLowerCase() === q.blank.toLowerCase()) {
      input.classList.add('correct'); fb.textContent = '✓ 正確！'; fb.className = 'quiz-feedback ok';
    } else {
      input.classList.add('wrong'); fb.textContent = '✗ 答案：' + q.blank; fb.className = 'quiz-feedback ng';
    }
  };
  block.querySelector('button').addEventListener('click', validate);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') validate(); });
  fillQuiz.appendChild(block);
});
</script>
</body>
</html>
