---
layout: null
---
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>每日英文練習 | 2026-06-24 GitHub 工作流 × PR 流程 × Headway U4 延伸</title>
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --green: #157878;
  --green-dark: #0f6e56;
  --green-light: #e8f5f1;
  --green-mid: #9fd9c8;
  --ink: #2c2c2a;
  --ink-muted: #5f5e5a;
  --ink-hint: #888780;
  --surface: #ffffff;
  --surface-alt: #f7f6f2;
  --border: rgba(44,44,42,.12);
  --border-em: rgba(44,44,42,.25);
  --radius: 8px;
  --radius-lg: 14px;
  --font-ui: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'Menlo', 'Courier New', monospace;
}
html { scroll-behavior: smooth; }
body {
  font-family: var(--font-ui);
  background: var(--surface-alt);
  color: var(--ink);
  min-height: 100vh;
  overflow-x: hidden;
}
.site-header {
  background: linear-gradient(120deg, var(--green) 0%, var(--green-dark) 100%);
  padding: 2.5rem 2rem 2rem;
  color: #fff;
}
.site-header h1 { font-size: 26px; font-weight: 700; margin-bottom: 4px; }
.site-header p { font-size: 14px; opacity: .82; margin-bottom: 14px; }
.badge-row, .btn-row, .day-tags, .speed-bar {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.badge-row { margin-bottom: 12px; }
.hdr-badge, .tag {
  font-size: 12px;
  font-weight: 600;
  padding: 3px 12px;
  border-radius: 999px;
}
.hdr-badge {
  background: rgba(255,255,255,.18);
  border: 1px solid rgba(255,255,255,.35);
  color: #fff;
}
.gh-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: rgba(255,255,255,.85);
  text-decoration: none;
  border: 1px solid rgba(255,255,255,.4);
  border-radius: 6px;
  padding: 4px 12px;
}
.gh-link:hover { background: rgba(255,255,255,.15); }
.main-wrap {
  width: 100%;
  max-width: 820px;
  min-width: 0;
  margin: 0 auto;
  padding: 2rem 1.25rem 4rem;
  overflow: hidden;
}
.main-wrap > * { width: 100%; max-width: 100%; min-width: 0; }
.main-wrap p, .main-wrap div, .main-wrap span { overflow-wrap: anywhere; word-break: break-word; }
.day-header, .passage, .quiz-block, .practice-card, .summary-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
}
.day-header {
  padding: 1.25rem 1.5rem;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}
.day-header > div { min-width: 0; max-width: 100%; }
.day-date {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--green);
  margin-bottom: 4px;
}
.day-title { font-size: 22px; font-weight: 700; line-height: 1.2; overflow-wrap: anywhere; }
.day-sub { font-size: 14px; color: var(--ink-muted); margin-top: 4px; overflow-wrap: anywhere; }
.tag {
  font-size: 11px;
  font-weight: 500;
  background: var(--green-light);
  color: var(--green-dark);
  border: 1px solid var(--green-mid);
  white-space: nowrap;
}
.grammar-note {
  background: #eaf2ff;
  border: 1px solid #b3cfee;
  border-radius: var(--radius-lg);
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
  font-size: 13.5px;
  line-height: 1.8;
  color: #1a3a5c;
  overflow-wrap: anywhere;
}
.gn-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: #5080a0;
  margin-bottom: 8px;
}
.speed-bar { align-items: center; margin-bottom: 1.5rem; }
.speed-bar label { font-size: 13px; color: var(--ink-muted); }
.speed-bar input[type=range] { width: 130px; accent-color: var(--green); }
.speed-val { font-size: 13px; font-weight: 600; color: var(--green-dark); min-width: 36px; }
.btn-stop, .btn-read, .quiz-check-btn, .quiz-restart-btn {
  font-family: var(--font-ui);
  border: 1px solid var(--border-em);
  border-radius: 6px;
  background: var(--surface);
  color: var(--ink-muted);
  cursor: pointer;
}
.btn-stop { font-size: 12px; padding: 4px 12px; }
.sec-label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink-hint);
  margin: 2rem 0 1rem;
}
.sec-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }
.passage { padding: 1.25rem 1.5rem 1rem; margin-bottom: 1rem; }
.passage-title {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--ink-hint);
  margin-bottom: .75rem;
}
.passage-en { min-width: 0; font-size: 15.5px; line-height: 1.9; color: var(--ink); overflow-wrap: anywhere; }
.passage-en p + p { margin-top: .75rem; }
.hl-past { color: #1a5276; font-weight: 700; }
.hl-neg { color: #c0392b; font-weight: 700; }
.hl-q { color: #7d6608; font-weight: 700; }
.hl-why { color: var(--green-dark); font-weight: 600; }
.btn-read {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  padding: 5px 14px;
  background: var(--surface-alt);
  margin-top: 10px;
}
.btn-read:hover, .btn-read.active {
  border-color: var(--green);
  color: var(--green-dark);
  background: var(--green-light);
}
.vocab-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(185px, 1fr));
  gap: 10px;
}
.vocab-card {
  min-width: 0;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: .9rem 1rem;
  cursor: pointer;
}
.vocab-card:hover, .vocab-card.playing {
  border-color: var(--green);
  background: var(--green-light);
}
.vocab-en { font-size: 13.5px; font-weight: 600; margin-bottom: 3px; }
.vocab-ipa {
  font-size: 11px;
  color: var(--ink-hint);
  font-family: var(--font-mono);
  margin-bottom: 4px;
}
.vocab-zh { font-size: 12px; color: var(--ink-muted); }
.sent-list { display: flex; flex-direction: column; gap: 9px; }
.sent-item {
  min-width: 0;
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 3px solid var(--green);
  border-radius: 0 var(--radius) var(--radius) 0;
  padding: .8rem 1rem .8rem 1.1rem;
  cursor: pointer;
}
.sent-item:hover, .sent-item.playing { background: var(--green-light); }
.sent-en { font-size: 14.5px; line-height: 1.55; overflow-wrap: anywhere; }
.sent-zh { font-size: 12px; color: var(--ink-muted); margin-top: 3px; }
.hint-note {
  font-size: 12px;
  color: var(--ink-hint);
  text-align: center;
  margin-top: 1.5rem;
}
.quiz-block { padding: 1.25rem 1.5rem; margin-bottom: 1rem; }
.quiz-block-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--ink-muted);
  margin-bottom: 14px;
}
.quiz-q { margin-bottom: 1.25rem; padding-bottom: 1.25rem; border-bottom: 1px dashed var(--border); }
.quiz-q:last-child { margin-bottom: 0; padding-bottom: 0; border-bottom: 0; }
.quiz-q-text { font-size: 14.5px; line-height: 1.55; margin-bottom: 8px; }
.quiz-opts { display: grid; grid-template-columns: 1fr 1fr; gap: 7px; }
.quiz-opt {
  font-size: 13px;
  padding: 7px 12px;
  border-radius: var(--radius);
  border: 1px solid var(--border-em);
  background: var(--surface-alt);
  cursor: pointer;
  text-align: left;
}
.quiz-opt.correct { border-color: #22a06b; background: #e3fcef; color: #1a6b45; font-weight: 600; }
.quiz-opt.wrong { border-color: #c9372c; background: #ffeceb; color: #c9372c; }
.fill-sentence { font-size: 15px; line-height: 2.3; }
.fill-input {
  font-size: 15px;
  border: 0;
  border-bottom: 2px solid var(--green);
  background: transparent;
  min-width: 110px;
  padding: 0 4px;
  text-align: center;
}
.quiz-check-btn { font-size: 12px; padding: 4px 12px; margin-top: 6px; }
.quiz-feedback { font-size: 12px; margin-top: 5px; min-height: 18px; }
.quiz-feedback.ok { color: #22a06b; font-weight: 600; }
.quiz-feedback.ng { color: #c9372c; }
.practice-card, .summary-card { padding: 1.25rem 1.5rem; line-height: 1.8; }
.practice-card p + p, .summary-card p + p { margin-top: .8rem; }
.practice-card .advanced {
  background: var(--green-light);
  border-left: 3px solid var(--green);
  padding: .75rem 1rem;
  margin-top: 1rem;
}
.summary-card { background: #fffdf4; border-color: #e5d9a8; }
.summary-card .english-summary {
  background: var(--surface);
  border-left: 3px solid #c6a94b;
  padding: .75rem 1rem;
  margin: 1rem 0;
}
.site-footer {
  border-top: 1px solid var(--border);
  padding: 1.25rem;
  font-size: 12px;
  color: var(--ink-hint);
  text-align: center;
  line-height: 1.7;
}
.site-footer a { color: var(--green-dark); text-decoration: none; }
@media (max-width: 520px) {
  .site-header { padding: 1.75rem 1.25rem 1.5rem; }
  .site-header h1 { font-size: 22px; }
  .day-header { flex-direction: column; }
  .main-wrap { padding-left: .75rem; padding-right: .75rem; }
  .day-title { font-size: 20px; }
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
    <span class="hdr-badge">Headway U4 句型</span>
    <span class="hdr-badge">Past Simple</span>
    <span class="hdr-badge">Why / Because</span>
    <span class="hdr-badge">We decided to</span>
    <span class="hdr-badge">Did you…?</span>
  </div>
  <div class="btn-row">
    <a class="gh-link" href="./">← 返回目錄</a>
    <a class="gh-link" href="https://github.com/Pcc329/daily-english" target="_blank">View on GitHub</a>
  </div>
</header>

<main class="main-wrap">
  <div class="day-header">
    <div>
      <div class="day-date">2026.06.24 &nbsp;—&nbsp; Day 10</div>
      <div class="day-title">用英文說明：我今天如何把內容整理成網站、建立入口，並確認未來維持 PR 流程。</div>
      <div class="day-sub">GitHub workflow · Daily English branch · PR review × Why / Because 句型</div>
    </div>
    <div class="day-tags">
      <span class="tag">branch workflow</span>
      <span class="tag">pull request</span>
      <span class="tag">review</span>
      <span class="tag">publish</span>
      <span class="tag">daily practice</span>
    </div>
  </div>

  <div class="grammar-note">
    <div class="gn-title">📖 今日文法重點 — Headway Elementary Unit 4 延伸</div>
    ✅ <strong>過去式工作句</strong>：I <strong>created</strong> a new HTML page for the report.<br>
    ✅ <strong>決策句</strong>：We <strong>decided to</strong> keep the same workflow.<br>
    ✅ <strong>Why / Because</strong>：<strong>Why</strong> did we use a pull request? <strong>Because</strong> we wanted to review the changes before merging them.<br>
    ✅ <strong>否定句</strong>：We <strong>didn’t</strong> push directly to main.<br>
    ✅ <strong>疑問句</strong>：<strong>Did</strong> Codex finish the task? Yes, it <strong>did</strong>.
  </div>

  <div class="speed-bar">
    <label for="speed">語速</label>
    <input type="range" id="speed" min="0.6" max="1.4" step="0.1" value="0.9">
    <span class="speed-val" id="speed-out">0.9×</span>
    <button class="btn-stop" onclick="stopAll()">■ 停止</button>
  </div>

  <div class="sec-label">朗讀練習</div>

  <div class="passage">
    <div class="passage-title">段落一 — 今天我做了什麼？（Past Simple 肯定句）</div>
    <div class="passage-en" data-speech="Today I reviewed the new GitHub update. Codex created a new HTML page for the report. It also added a new entry to the index page. The entry name was clear and professional. After that, the changes were pushed to the main branch.">
      <p>Today I <span class="hl-past">reviewed</span> the new GitHub update.<br>
      Codex <span class="hl-past">created</span> a new HTML page for the report.<br>
      It also <span class="hl-past">added</span> a new entry to the index page.<br>
      The entry name <span class="hl-past">was</span> clear and professional.<br>
      After that, the changes <span class="hl-past">were pushed</span> to the main branch.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落二 — 我們確認了什麼流程？（We confirmed that…）</div>
    <div class="passage-en" data-speech="We confirmed that this workflow should continue. Claude and I plan the structure first. Codex executes the code changes. Then Claude and I review the result again. Finally, I decide whether to merge the pull request.">
      <p>We <span class="hl-past">confirmed</span> that this workflow should continue.<br>
      Claude and I plan the structure first.<br>
      Codex executes the code changes.<br>
      Then Claude and I review the result again.<br>
      Finally, I decide whether to merge the pull request.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落三 — 為什麼要保留 PR？（Why / Because）</div>
    <div class="passage-en" data-speech="Why should we keep using pull requests? Because a pull request gives us one more review checkpoint. It helps us catch layout problems before publishing. It also makes the change history easier to track. So we should not push directly to main unless I clearly ask for it.">
      <p><span class="hl-q">Why</span> should we keep using pull requests?<br>
      <span class="hl-why">Because</span> a pull request gives us one more review checkpoint.<br>
      It helps us catch layout problems before publishing.<br>
      It also makes the change history easier to track.<br>
      So we should <span class="hl-neg">not push directly to main</span> unless I clearly ask for it.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落四 — 每日英文網站要做什麼？（Daily practice）</div>
    <div class="passage-en" data-speech="This website turns my daily work into English practice. I do not only memorize words. I practice how to explain real tasks in English. Each page becomes a small speaking script. Over time, these pages will become my personal English database.">
      <p>This website turns my daily work into English practice.<br>
      I do not only memorize words.<br>
      I practice how to explain real tasks in English.<br>
      Each page becomes a small speaking script.<br>
      Over time, these pages will become my personal English database.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落五 — 模擬主管問答（Did you…?）</div>
    <div class="passage-en" data-speech="Did Codex create the new page? Yes, it did. Did we review the index entry? Yes, we did. Did we decide to keep the PR workflow? Yes, we did. Did we push every future change directly to main? No, we didn’t. We decided to use pull requests first.">
      <p><span class="hl-q">Did</span> Codex create the new page?<br>
      Yes, it did.</p>
      <p><span class="hl-q">Did</span> we review the index entry?<br>
      Yes, we did.</p>
      <p><span class="hl-q">Did</span> we decide to keep the PR workflow?<br>
      Yes, we did.</p>
      <p><span class="hl-q">Did</span> we push every future change directly to main?<br>
      No, we <span class="hl-neg">didn’t</span>.<br>
      We <span class="hl-past">decided</span> to use pull requests first.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="sec-label">詞彙發音</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點卡片聽發音</div>
  <div class="vocab-grid" id="vocabGrid"></div>

  <div class="sec-label">核心句型</div>
  <div class="hint-note" style="margin-bottom:12px;margin-top:-4px">點句子聽完整朗讀</div>
  <div class="sent-list" id="sentList"></div>

  <div class="sec-label">今日測驗</div>
  <div class="quiz-block">
    <div class="quiz-block-title">📻 第一關：聽音選答案</div>
    <div id="listenQuiz"></div>
  </div>
  <div class="quiz-block">
    <div class="quiz-block-title">✏️ 第二關：填空題</div>
    <div id="fillQuiz"></div>
  </div>

  <div class="sec-label">今日口說任務</div>
  <div class="practice-card">
    <p><strong>請跟讀三次：</strong></p>
    <p data-speech="I use this website to practice real work English. I turn my daily tasks into short English scripts. This helps me explain my work more clearly.">
      I use this website to practice real work English.<br>
      I turn my daily tasks into short English scripts.<br>
      This helps me explain my work more clearly.
    </p>
    <button class="btn-read">▶ 聽整段</button>
    <div class="advanced">
      <strong>進階版：</strong><br>
      <span data-speech="My workflow is simple. I plan the structure with Claude, Codex executes the code changes, and I review the result before merging the pull request.">
        My workflow is simple.<br>
        I plan the structure with Claude, Codex executes the code changes, and I review the result before merging the pull request.
      </span>
    </div>
  </div>

  <div class="sec-label">今日總結</div>
  <div class="summary-card">
    <p>今天的英文主題不是背單字，而是把真實工作流程說清楚。</p>
    <p>中文裡你說的是：<br>
    「我和 Claude 規劃，Codex 執行，我再檢查，最後決定要不要合併 PR。」</p>
    <div class="english-summary">
      Claude and I plan the structure first.<br>
      Codex executes the code changes.<br>
      Then I review the result and decide whether to merge the pull request.
    </div>
    <p>這就是你的每日英文資料庫真正有價值的地方：<br>
    不是寫漂亮英文，而是把每天的工作，變成未來面試、會議、交接都能直接使用的語料。</p>
  </div>
</main>

<footer class="site-footer">
  <a href="https://github.com/Pcc329/daily-english">daily-english</a> is maintained by Pcc329.<br>
  工作日誌 × Headway Elementary U4 延伸 · Generated by ChatGPT · 2026-06-24
</footer>

<script>
const vocab = [
  { en:"branch", ipa:"/bræntʃ/", zh:"分支" },
  { en:"pull request", ipa:"/pʊl rɪˈkwest/", zh:"合併請求" },
  { en:"review", ipa:"/rɪˈvjuː/", zh:"檢查、審查" },
  { en:"merge", ipa:"/mɜːrdʒ/", zh:"合併" },
  { en:"push", ipa:"/pʊʃ/", zh:"推送" },
  { en:"publish", ipa:"/ˈpʌblɪʃ/", zh:"發布" },
  { en:"update", ipa:"/ˈʌpdeɪt/", zh:"更新" },
  { en:"entry", ipa:"/ˈentri/", zh:"入口、項目" },
  { en:"workflow", ipa:"/ˈwɜːrkfloʊ/", zh:"工作流程" },
  { en:"checkpoint", ipa:"/ˈtʃekpɔɪnt/", zh:"檢查點" },
  { en:"execute", ipa:"/ˈeksɪkjuːt/", zh:"執行" },
  { en:"confirm", ipa:"/kənˈfɜːrm/", zh:"確認" }
];
const sentences = [
  { en:"I created a new HTML page for the report.", zh:"我為報告新增了一個 HTML 頁面。" },
  { en:"Codex added a new entry to the index page.", zh:"Codex 在首頁加入了一個新的入口。" },
  { en:"We confirmed that the workflow should continue.", zh:"我們確認這個工作流程應該維持下去。" },
  { en:"Claude and I plan the structure first.", zh:"Claude 和我會先規劃架構。" },
  { en:"Codex executes the code changes.", zh:"Codex 執行程式碼修改。" },
  { en:"I review the result before merging it.", zh:"我會在合併前檢查結果。" },
  { en:"We didn’t push directly to main.", zh:"我們沒有直接推到 main。" },
  { en:"Why did we use a pull request?", zh:"我們為什麼使用 PR？" },
  { en:"Because we wanted one more review checkpoint.", zh:"因為我們想多一個檢查點。" },
  { en:"This website turns my daily work into English practice.", zh:"這個網站把我的日常工作轉成英文練習。" }
];
const listenData = [
  { word:"branch", answer:"分支", opts:["分支","錯誤","按鈕","表格"] },
  { word:"pull request", answer:"合併請求", opts:["合併請求","公司資料","瀏覽器","伺服器"] },
  { word:"review", answer:"檢查、審查", opts:["檢查、審查","刪除","阻擋","下載"] },
  { word:"workflow", answer:"工作流程", opts:["工作流程","網頁標題","錯誤訊息","會員資料"] },
  { word:"checkpoint", answer:"檢查點", opts:["檢查點","密碼","欄位","圖片"] }
];
const fillData = [
  { before:"Codex", blank:"created", after:"a new HTML page for the report." },
  { before:"We", blank:"confirmed", after:"that the workflow should continue." },
  { before:"We didn’t push directly to", blank:"main", after:"." },
  { before:"Why did we use a pull request?", blank:"Because", after:"we wanted one more review checkpoint." }
];

let activeEl = null;
function stopAll() {
  window.speechSynthesis.cancel();
  if (activeEl) activeEl.classList.remove('playing', 'active');
  activeEl = null;
}
function speak(text, el) {
  stopAll();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'en-US';
  utterance.rate = parseFloat(document.getElementById('speed').value);
  if (el) {
    el.classList.add('playing', 'active');
    activeEl = el;
  }
  utterance.onend = utterance.onerror = () => {
    if (el) el.classList.remove('playing', 'active');
    activeEl = null;
  };
  window.speechSynthesis.speak(utterance);
}
document.getElementById('speed').addEventListener('input', function () {
  document.getElementById('speed-out').textContent = Number(this.value).toFixed(1) + '×';
});
document.querySelectorAll('.btn-read').forEach(button => {
  button.addEventListener('click', () => {
    const container = button.previousElementSibling;
    const speechTarget = container && container.dataset.speech
      ? container
      : button.parentElement.querySelector('[data-speech]');
    if (speechTarget) speak(speechTarget.dataset.speech, button);
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
const sentList = document.getElementById('sentList');
sentences.forEach(item => {
  const row = document.createElement('div');
  row.className = 'sent-item';
  row.innerHTML = `<div class="sent-en">${item.en}</div><div class="sent-zh">${item.zh}</div>`;
  row.addEventListener('click', () => speak(item.en, row));
  sentList.appendChild(row);
});

const listenQuiz = document.getElementById('listenQuiz');
listenData.forEach((question, index) => {
  const block = document.createElement('div');
  block.className = 'quiz-q';
  block.innerHTML = `<div class="quiz-q-text">${index + 1}. What does “${question.word}” mean? <button class="quiz-check-btn play-word">▶ 聽單字</button></div><div class="quiz-opts"></div><div class="quiz-feedback"></div>`;
  block.querySelector('.play-word').addEventListener('click', () => speak(question.word));
  const options = block.querySelector('.quiz-opts');
  question.opts.forEach(option => {
    const button = document.createElement('button');
    button.className = 'quiz-opt';
    button.textContent = option;
    button.addEventListener('click', () => {
      options.querySelectorAll('button').forEach(item => {
        item.disabled = true;
        if (item.textContent === question.answer) item.classList.add('correct');
      });
      const feedback = block.querySelector('.quiz-feedback');
      if (option === question.answer) {
        feedback.textContent = '✓ Answer: ' + question.answer;
        feedback.className = 'quiz-feedback ok';
      } else {
        button.classList.add('wrong');
        feedback.textContent = '✗ Answer: ' + question.answer;
        feedback.className = 'quiz-feedback ng';
      }
    });
    options.appendChild(button);
  });
  listenQuiz.appendChild(block);
});

const fillQuiz = document.getElementById('fillQuiz');
fillData.forEach((question, index) => {
  const block = document.createElement('div');
  block.className = 'quiz-q';
  block.innerHTML = `<div class="quiz-q-text">${index + 1}. Fill in the blank.</div><div class="fill-sentence">${question.before} <input class="fill-input" type="text" autocomplete="off" placeholder="______"> ${question.after}</div><button class="quiz-check-btn">確認</button><div class="quiz-feedback"></div>`;
  const input = block.querySelector('input');
  const check = block.querySelector('button');
  const validate = () => {
    const feedback = block.querySelector('.quiz-feedback');
    if (input.value.trim().toLowerCase() === question.blank.toLowerCase()) {
      feedback.textContent = '✓ Answer: ' + question.blank;
      feedback.className = 'quiz-feedback ok';
    } else {
      feedback.textContent = '✗ Answer: ' + question.blank;
      feedback.className = 'quiz-feedback ng';
    }
  };
  check.addEventListener('click', validate);
  input.addEventListener('keydown', event => { if (event.key === 'Enter') validate(); });
  fillQuiz.appendChild(block);
});
</script>
</body>
</html>
