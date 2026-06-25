---
layout: null
---
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>每日英文練習 | 2026-06-25 方案摘要 × 斷字修正 × 手機短句發音</title>
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
  touch-action: manipulation;
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
  touch-action: manipulation;
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
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}
.sent-item:hover, .sent-item:focus-visible, .sent-item.playing {
  background: var(--green-light);
  outline: none;
}
.sent-item:focus-visible { box-shadow: 0 0 0 3px rgba(21,120,120,.22); }
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
  touch-action: manipulation;
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
    <span class="hdr-badge">Headway U4 延伸</span>
    <span class="hdr-badge">We found that</span>
    <span class="hdr-badge">Because / So</span>
    <span class="hdr-badge">We changed</span>
    <span class="hdr-badge">Mobile Speaking</span>
  </div>
  <div class="btn-row">
    <a class="gh-link" href="./">← 返回目錄</a>
    <a class="gh-link" href="https://github.com/Pcc329/daily-english" target="_blank">View on GitHub</a>
  </div>
</header>

<main class="main-wrap">
  <div class="day-header">
    <div>
      <div class="day-date">2026.06.25 &nbsp;—&nbsp; Day 11</div>
      <div class="day-title">產業資料庫方案介紹斷字問題 × 短摘要策略 × 手機短句發音</div>
      <div class="day-sub">Solution descriptions · Word wrapping · Short summaries × Mobile sentence audio</div>
    </div>
    <div class="day-tags">
      <span class="tag">word wrapping</span>
      <span class="tag">short summary</span>
      <span class="tag">mobile layout</span>
      <span class="tag">speech synthesis</span>
      <span class="tag">tap to speak</span>
    </div>
  </div>

  <div class="grammar-note">
    <div class="gn-title">📖 今日文法重點 — Headway Elementary Unit 4 延伸</div>
    ✅ <strong>發現問題</strong>：We <strong>found that</strong> long solution descriptions broke awkwardly on mobile screens.<br>
    ✅ <strong>說明原因</strong>：The cards were difficult to scan <strong>because</strong> each description contained too much detail.<br>
    ✅ <strong>說明結果</strong>：We shortened the summaries, <strong>so</strong> users could understand the key value faster.<br>
    ✅ <strong>描述修改</strong>：We <strong>changed</strong> each introduction to a concise problem–solution–benefit format.<br>
    ✅ <strong>手機操作</strong>：Tap a sentence card and the browser <strong>will read</strong> the English sentence aloud.
  </div>

  <div class="speed-bar">
    <label for="speed">語速</label>
    <input type="range" id="speed" min="0.6" max="1.4" step="0.1" value="0.9">
    <span class="speed-val" id="speed-out">0.9×</span>
    <button class="btn-stop" onclick="stopAll()">■ 停止</button>
  </div>

  <div class="sec-label">朗讀練習</div>

  <div class="passage">
    <div class="passage-title">段落一 — 我們發現了什麼？（We found that…）</div>
    <div class="passage-en" data-speech="Today I reviewed the solution cards in our industry database. We found that some introductions broke awkwardly on mobile screens. Long Chinese and English text created uneven lines. Important information was pushed too far down the card. The page still worked, but it was difficult to scan.">
      <p>Today I <span class="hl-past">reviewed</span> the solution cards in our industry database.<br>
      We <span class="hl-past">found</span> that some introductions broke awkwardly on mobile screens.<br>
      Long Chinese and English text <span class="hl-past">created</span> uneven lines.<br>
      Important information <span class="hl-past">was pushed</span> too far down the card.<br>
      The page still worked, but it was difficult to scan.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落二 — 為什麼需要短摘要？（Because / So）</div>
    <div class="passage-en" data-speech="The cards were hard to read because each description tried to explain everything at once. Users only needed the main problem, the proposed solution, and the key benefit. So we decided to create a short summary for every solution. The full description can remain available on the detail page.">
      <p>The cards were hard to read <span class="hl-why">because</span> each description tried to explain everything at once.<br>
      Users only needed the main problem, the proposed solution, and the key benefit.<br>
      <span class="hl-why">So</span> we <span class="hl-past">decided</span> to create a short summary for every solution.<br>
      The full description can remain available on the detail page.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落三 — 我們採用了什麼摘要策略？（We changed…）</div>
    <div class="passage-en" data-speech="We changed the introduction to a three-part structure. First, state the business problem. Second, explain what the solution does. Third, describe the expected benefit. Each summary should stay concise and avoid unnecessary technical details. This makes the cards easier to compare.">
      <p>We <span class="hl-past">changed</span> the introduction to a three-part structure.<br>
      First, state the business problem.<br>
      Second, explain what the solution does.<br>
      Third, describe the expected benefit.<br>
      Each summary should stay concise and avoid unnecessary technical details.<br>
      This makes the cards easier to compare.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落四 — 手機短句發音怎麼運作？（Tap to speak）</div>
    <div class="passage-en" data-speech="The page already supports full paragraph reading. Today we added direct audio to the short sentence cards. On a phone, users can tap any sentence to hear it immediately. When they tap a new sentence, the previous audio stops first. The active card stays highlighted until the speech ends.">
      <p>The page already supports full paragraph reading.<br>
      Today we <span class="hl-past">added</span> direct audio to the short sentence cards.<br>
      On a phone, users can tap any sentence to hear it immediately.<br>
      When they tap a new sentence, the previous audio stops first.<br>
      The active card stays highlighted until the speech ends.</p>
    </div>
    <button class="btn-read">▶ 聽整段</button>
  </div>

  <div class="passage">
    <div class="passage-title">段落五 — 模擬主管問答（Did you…?）</div>
    <div class="passage-en" data-speech="Did you remove the full solution descriptions? No, we didn’t. Did you shorten the text shown on the cards? Yes, we did. Why did you change it? Because users needed a faster way to understand and compare solutions. Did the sentence audio work on mobile? Yes, it did.">
      <p><span class="hl-q">Did</span> you remove the full solution descriptions?<br>
      No, we <span class="hl-neg">didn’t</span>.</p>
      <p><span class="hl-q">Did</span> you shorten the text shown on the cards?<br>
      Yes, we did.</p>
      <p><span class="hl-q">Why</span> did you change it?<br>
      <span class="hl-why">Because</span> users needed a faster way to understand and compare solutions.</p>
      <p><span class="hl-q">Did</span> the sentence audio work on mobile?<br>
      Yes, it did.</p>
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
    <p data-speech="We found a word-wrapping problem in the solution cards. We replaced long introductions with concise summaries. This made the mobile layout easier to read and compare.">
      We found a word-wrapping problem in the solution cards.<br>
      We replaced long introductions with concise summaries.<br>
      This made the mobile layout easier to read and compare.
    </p>
    <button class="btn-read">▶ 聽整段</button>
    <div class="advanced">
      <strong>進階版：</strong><br>
      <span data-speech="Our summary strategy uses three parts: the business problem, the proposed solution, and the expected benefit. On mobile, users can also tap a short sentence card to hear the English sentence immediately.">
        Our summary strategy uses three parts: the business problem, the proposed solution, and the expected benefit.<br>
        On mobile, users can also tap a short sentence card to hear the English sentence immediately.
      </span>
    </div>
  </div>

  <div class="sec-label">今日總結</div>
  <div class="summary-card">
    <p>今天的英文主題是如何把介面問題、內容策略和手機互動說清楚。</p>
    <p>中文裡你說的是：<br>
    「方案介紹在手機上斷字不好看，所以我們改用短摘要，並讓短句卡片可以直接點擊發音。」</p>
    <div class="english-summary">
      The solution descriptions were difficult to scan on mobile.<br>
      We changed them to concise summaries.<br>
      We also made each short sentence card directly playable with speech synthesis.
    </div>
    <p>這就是你的每日英文資料庫真正有價值的地方：<br>
    不只記錄做了什麼，也練習如何解釋問題、設計決策與使用者體驗。</p>
  </div>
</main>

<footer class="site-footer">
  <a href="https://github.com/Pcc329/daily-english">daily-english</a> is maintained by Pcc329.<br>
  工作日誌 × Headway Elementary U4 延伸 · Generated by ChatGPT · 2026-06-25
</footer>

<script>
const vocab = [
  { en:"word wrapping", ipa:"/wɜːrd ˈræpɪŋ/", zh:"文字換行、斷字" },
  { en:"solution description", ipa:"/səˈluːʃən dɪˈskrɪpʃən/", zh:"方案介紹" },
  { en:"short summary", ipa:"/ʃɔːrt ˈsʌməri/", zh:"短摘要" },
  { en:"concise", ipa:"/kənˈsaɪs/", zh:"簡潔的" },
  { en:"key benefit", ipa:"/kiː ˈbenɪfɪt/", zh:"核心效益" },
  { en:"readability", ipa:"/ˌriːdəˈbɪləti/", zh:"可讀性" },
  { en:"mobile layout", ipa:"/ˈmoʊbaɪl ˈleɪaʊt/", zh:"手機版面" },
  { en:"tap target", ipa:"/tæp ˈtɑːrɡɪt/", zh:"觸控點擊目標" },
  { en:"speech synthesis", ipa:"/spiːtʃ ˈsɪnθəsɪs/", zh:"語音合成" },
  { en:"active state", ipa:"/ˈæktɪv steɪt/", zh:"播放中狀態" },
  { en:"scan", ipa:"/skæn/", zh:"快速瀏覽" },
  { en:"compare", ipa:"/kəmˈper/", zh:"比較" }
];
const sentences = [
  { en:"We found that long descriptions broke awkwardly on mobile screens.", zh:"我們發現長篇介紹在手機畫面上斷字不自然。" },
  { en:"The cards were difficult to scan because they contained too much detail.", zh:"卡片很難快速瀏覽，因為內容包含太多細節。" },
  { en:"We changed each introduction to a concise three-part summary.", zh:"我們把每段介紹改成簡潔的三段式摘要。" },
  { en:"The summary explains the problem, the solution, and the key benefit.", zh:"摘要說明問題、解法與核心效益。" },
  { en:"The full description remains available on the detail page.", zh:"完整介紹仍保留在詳細頁面。" },
  { en:"Users can tap a sentence card to hear it immediately.", zh:"使用者可以點擊短句卡片立即聽取發音。" },
  { en:"The previous audio stops before the new sentence begins.", zh:"新句子開始前，上一段語音會先停止。" },
  { en:"The active card stays highlighted while the sentence is playing.", zh:"句子播放期間，作用中的卡片會維持高亮。" },
  { en:"This improves readability without removing useful information.", zh:"這在不刪除實用資訊的情況下改善可讀性。" },
  { en:"Short summaries make solutions easier to understand and compare.", zh:"短摘要讓方案更容易理解與比較。" }
];
const listenData = [
  { word:"word wrapping", answer:"文字換行、斷字", opts:["文字換行、斷字","資料排序","語音速度","程式部署"] },
  { word:"short summary", answer:"短摘要", opts:["短摘要","完整報告","搜尋結果","原始資料"] },
  { word:"readability", answer:"可讀性", opts:["可讀性","可靠性","相容性","擴充性"] },
  { word:"speech synthesis", answer:"語音合成", opts:["語音合成","文字辨識","影像生成","資料清理"] },
  { word:"active state", answer:"播放中狀態", opts:["播放中狀態","登入狀態","錯誤訊息","備份版本"] }
];
const fillData = [
  { before:"We found that long descriptions broke awkwardly on", blank:"mobile", after:"screens." },
  { before:"We changed each introduction to a concise", blank:"summary", after:"." },
  { before:"Users can", blank:"tap", after:"a sentence card to hear it immediately." },
  { before:"The previous audio", blank:"stops", after:"before the new sentence begins." }
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
  row.setAttribute('role', 'button');
  row.setAttribute('tabindex', '0');
  row.setAttribute('aria-label', '播放短句：' + item.en);
  row.innerHTML = `<div class="sent-en">${item.en}</div><div class="sent-zh">${item.zh}</div>`;
  const playSentence = () => speak(item.en, row);
  row.addEventListener('click', playSentence);
  row.addEventListener('keydown', event => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      playSentence();
    }
  });
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
