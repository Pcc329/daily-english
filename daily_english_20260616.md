<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>每日英文練習 | 2026-06-16 工作日誌 × Headway U8 句型</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, 'Microsoft JhengHei', sans-serif; background: #f5f7fa; color: #333; }
    header { background: linear-gradient(135deg, #157878, #0BA08C); color: white; padding: 32px 24px 24px; text-align: center; }
    header h1 { font-size: 1.6rem; font-weight: 700; margin-bottom: 6px; }
    header p { font-size: 0.9rem; opacity: 0.85; }
    .day-badge { display: inline-block; background: rgba(255,255,255,0.2); border-radius: 20px; padding: 4px 16px; font-size: 0.85rem; margin: 12px 0 4px; }
    .grammar-tag { display: inline-block; background: rgba(255,255,255,0.15); border-radius: 12px; padding: 3px 12px; font-size: 0.78rem; margin: 2px; }
    nav { text-align: center; padding: 12px; background: #fff; border-bottom: 1px solid #e5e7eb; }
    nav a { color: #157878; text-decoration: none; font-size: 0.85rem; margin: 0 12px; }
    .container { max-width: 720px; margin: 0 auto; padding: 24px 16px 48px; }
    .grammar-box { background: #fff; border-radius: 12px; padding: 20px 24px; margin-bottom: 24px; border-left: 4px solid #0BA08C; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
    .grammar-box h2 { font-size: 1rem; color: #0BA08C; margin-bottom: 12px; }
    .grammar-box p { font-size: 0.9rem; line-height: 1.8; margin-bottom: 6px; }
    .section { background: #fff; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
    .section-label { font-size: 0.75rem; color: #6b7280; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 4px; }
    .section h3 { font-size: 1.05rem; color: #111827; margin-bottom: 6px; }
    .section .zh { font-size: 0.82rem; color: #6b7280; margin-bottom: 14px; }
    .chunk { display: inline; }
    .chunk span { display: inline; cursor: pointer; border-radius: 4px; padding: 1px 2px; transition: background 0.15s; }
    .chunk span:hover { background: #d1fae5; }
    .chunk span.playing { background: #6ee7b7; }
    p.en { font-size: 1rem; line-height: 2; color: #1f2937; margin-bottom: 10px; }
    .listen-btn { display: inline-flex; align-items: center; gap: 6px; background: #f0fdf4; border: 1px solid #86efac; color: #166534; border-radius: 20px; padding: 5px 14px; font-size: 0.82rem; cursor: pointer; margin-top: 6px; transition: background 0.15s; }
    .listen-btn:hover { background: #dcfce7; }
    .speed-control { display: flex; align-items: center; gap: 10px; background: #fff; border-radius: 10px; padding: 10px 16px; margin-bottom: 20px; box-shadow: 0 1px 4px rgba(0,0,0,0.06); font-size: 0.85rem; }
    .speed-control label { color: #374151; }
    input[type=range] { flex: 1; accent-color: #0BA08C; }
    #speed-val { color: #0BA08C; font-weight: 600; min-width: 36px; }
    .vocab-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; margin-top: 12px; }
    .vocab-card { background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 10px; padding: 10px 12px; cursor: pointer; transition: border-color 0.15s; }
    .vocab-card:hover { border-color: #0BA08C; }
    .vocab-card.work { border-left: 3px solid #0BA08C; }
    .vocab-card.grammar { border-left: 3px solid #6366f1; }
    .vocab-card .word { font-weight: 700; font-size: 0.95rem; color: #111827; }
    .vocab-card .pron { font-size: 0.75rem; color: #6b7280; margin: 2px 0; }
    .vocab-card .zh-word { font-size: 0.78rem; color: #374151; }
    .pattern-list { list-style: none; margin-top: 10px; }
    .pattern-list li { padding: 8px 12px; border-radius: 8px; background: #f9fafb; margin-bottom: 8px; cursor: pointer; font-size: 0.9rem; color: #1f2937; transition: background 0.15s; }
    .pattern-list li:hover { background: #d1fae5; }
    footer { text-align: center; font-size: 0.78rem; color: #9ca3af; padding: 24px; }
  </style>
</head>
<body>

<header>
  <h1>每日英文練習</h1>
  <p>資料庫工程師的英文口說復健 · Daily Speaking Practice</p>
  <div class="day-badge">2026.06.16 — Day 19</div><br>
  <span class="grammar-tag">Past Simple</span>
  <span class="grammar-tag">What did you do?</span>
  <span class="grammar-tag">I built / I designed / We decided</span>
</header>

<nav>
  <a href="https://pcc329.github.io/daily-english/">返回目錄</a>
  <a href="https://github.com/Pcc329/daily-english">View on GitHub</a>
</nav>

<div class="container">

  <p style="font-size:0.88rem;color:#6b7280;text-align:center;margin-bottom:16px;">
    用 Past Simple 說今天的工作<br>
    AI Agent 設計 · 命名討論 · 資料庫分析 × What did you do today?
  </p>

  <!-- 語速 -->
  <div class="speed-control">
    <label>語速</label>
    <input type="range" id="speed" min="0.6" max="1.2" step="0.1" value="0.9">
    <span id="speed-val">0.9×</span>
    <span style="color:#9ca3af;font-size:0.78rem;">■ <span id="stop-btn" style="cursor:pointer;">停止</span></span>
  </div>

  <!-- 文法重點 -->
  <div class="grammar-box">
    <h2>📖 今日文法重點 — Past Simple（過去式）</h2>
    <p>✅ <strong>規則動詞</strong>：I <strong>designed</strong> a new interface. We <strong>decided</strong> on a name.</p>
    <p>✅ <strong>不規則動詞</strong>：I <strong>built</strong> a spec. We <strong>ran</strong> tests. I <strong>wrote</strong> the document.</p>
    <p>❌ <strong>否定</strong>：I <strong>didn't modify</strong> the core API. We <strong>didn't merge</strong> without review.</p>
    <p>❓ <strong>疑問</strong>：<strong>What did</strong> you build today? <strong>Did</strong> it work? → Yes, it <strong>did</strong>.</p>
    <p>🕐 <strong>時間標記</strong>：<em>today / this morning / just now / yesterday / earlier</em></p>
  </div>

  <!-- 段落一 -->
  <div class="section">
    <div class="section-label">段落一 — 今天建了什麼？（Past Simple 肯定）</div>
    <h3>What did I build today?</h3>
    <div class="zh">用過去式描述今天完成的功能，把工作動詞變成過去式練習。</div>
    <p class="en">
      <span class="chunk" onclick="speak(this)"><span>Today I designed a conversational AI agent</span></span>
      <span class="chunk" onclick="speak(this)"><span>to replace the old form-based interface</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>I wrote a specification document</span></span>
      <span class="chunk" onclick="speak(this)"><span>and sent it to Codex for implementation</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>Codex built the chat interface</span></span>
      <span class="chunk" onclick="speak(this)"><span>and I reviewed the pull request</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>We merged it into production after testing</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
    </p>
    <button class="listen-btn" onclick="speakAll('p1')">▶ 聽整段</button>
    <div id="p1" style="display:none;">Today I designed a conversational AI agent to replace the old form-based interface. I wrote a specification document and sent it to Codex for implementation. Codex built the chat interface and I reviewed the pull request. We merged it into production after testing.</div>
  </div>

  <!-- 段落二 -->
  <div class="section">
    <div class="section-label">段落二 — 我們決定了什麼？（Past Simple 決策動詞）</div>
    <h3>What decisions did we make?</h3>
    <div class="zh">用過去式說明今天做了哪些設計決策，練習決策類動詞。</div>
    <p class="en">
      <span class="chunk" onclick="speak(this)"><span>We decided to use two different AI models</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>I chose Claude Haiku for the conversation</span></span>
      <span class="chunk" onclick="speak(this)"><span>because it is fast and cheap</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>I selected Claude Sonnet for recommendations</span></span>
      <span class="chunk" onclick="speak(this)"><span>because quality matters more there</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>We also renamed the tool</span></span>
      <span class="chunk" onclick="speak(this)"><span>from "Consultant Assistant" to "Smart Solution Explorer"</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
    </p>
    <button class="listen-btn" onclick="speakAll('p2')">▶ 聽整段</button>
    <div id="p2" style="display:none;">We decided to use two different AI models. I chose Claude Haiku for the conversation because it is fast and cheap. I selected Claude Sonnet for recommendations because quality matters more there. We also renamed the tool from Consultant Assistant to Smart Solution Explorer.</div>
  </div>

  <!-- 段落三 -->
  <div class="section">
    <div class="section-label">段落三 — 遇到什麼問題？（Past Simple 問題描述）</div>
    <h3>What problems did I encounter?</h3>
    <div class="zh">用過去式描述今天踩到的坑，練習問題描述與解決方案句型。</div>
    <p class="en">
      <span class="chunk" onclick="speak(this)"><span>Codex didn't follow the spec exactly</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>It changed the title to the wrong name twice</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>The budget field also showed "undefined"</span></span>
      <span class="chunk" onclick="speak(this)"><span>when the user typed Chinese numbers like "three thousand"</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>I wrote a fix specification</span></span>
      <span class="chunk" onclick="speak(this)"><span>and added a conversion rule to the prompt</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>After the fix, it worked correctly</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
    </p>
    <button class="listen-btn" onclick="speakAll('p3')">▶ 聽整段</button>
    <div id="p3" style="display:none;">Codex didn't follow the spec exactly. It changed the title to the wrong name twice. The budget field also showed undefined when the user typed Chinese numbers like three thousand. I wrote a fix specification and added a conversion rule to the prompt. After the fix, it worked correctly.</div>
  </div>

  <!-- 段落四 -->
  <div class="section">
    <div class="section-label">段落四 — 今天學到了什麼？（Past Simple 反思）</div>
    <h3>What did I learn today?</h3>
    <div class="zh">用過去式反思今天的收穫，練習學習與成長相關的動詞。</div>
    <p class="en">
      <span class="chunk" onclick="speak(this)"><span>I learned that Airtable API is free</span></span>
      <span class="chunk" onclick="speak(this)"><span>but Anthropic API costs money per token</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>I calculated the cost for one session</span></span>
      <span class="chunk" onclick="speak(this)"><span>— it was only about two cents</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>I also analysed the database coverage</span></span>
      <span class="chunk" onclick="speak(this)"><span>and found that industry vertical only covered ten percent</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
      <span class="chunk" onclick="speak(this)"><span>So I ran a batch classification job</span></span>
      <span class="chunk" onclick="speak(this)"><span>to fill in five hundred and sixty-eight missing records</span></span>
      <span class="chunk" onclick="speak(this)"><span>.</span></span>
    </p>
    <button class="listen-btn" onclick="speakAll('p4')">▶ 聽整段</button>
    <div id="p4" style="display:none;">I learned that Airtable API is free but Anthropic API costs money per token. I calculated the cost for one session — it was only about two cents. I also analysed the database coverage and found that industry vertical only covered ten percent. So I ran a batch classification job to fill in five hundred and sixty-eight missing records.</div>
  </div>

  <!-- 詞彙發音 -->
  <div class="section">
    <div class="section-label">詞彙發音</div>
    <h3>點卡片聽發音｜🟢 工作詞彙 🔵 文法詞彙</h3>
    <div class="vocab-grid">
      <div class="vocab-card work" onclick="speakWord('conversational')">
        <div class="word">conversational</div>
        <div class="pron">/ˌkɒnvəˈseɪʃənl/</div>
        <div class="zh-word">對話式的</div>
      </div>
      <div class="vocab-card work" onclick="speakWord('specification')">
        <div class="word">specification</div>
        <div class="pron">/ˌspesɪfɪˈkeɪʃən/</div>
        <div class="zh-word">規格書</div>
      </div>
      <div class="vocab-card work" onclick="speakWord('implementation')">
        <div class="word">implementation</div>
        <div class="pron">/ˌɪmplɪmenˈteɪʃən/</div>
        <div class="zh-word">實作</div>
      </div>
      <div class="vocab-card work" onclick="speakWord('recommendation')">
        <div class="word">recommendation</div>
        <div class="pron">/ˌrekəmenˈdeɪʃən/</div>
        <div class="zh-word">推薦</div>
      </div>
      <div class="vocab-card work" onclick="speakWord('classification')">
        <div class="word">classification</div>
        <div class="pron">/ˌklæsɪfɪˈkeɪʃən/</div>
        <div class="zh-word">分類</div>
      </div>
      <div class="vocab-card work" onclick="speakWord('coverage')">
        <div class="word">coverage</div>
        <div class="pron">/ˈkʌvərɪdʒ/</div>
        <div class="zh-word">覆蓋率</div>
      </div>
      <div class="vocab-card grammar" onclick="speakWord('decided')">
        <div class="word">decided</div>
        <div class="pron">/dɪˈsaɪdɪd/</div>
        <div class="zh-word">決定（過去式）</div>
      </div>
      <div class="vocab-card grammar" onclick="speakWord('encountered')">
        <div class="word">encountered</div>
        <div class="pron">/ɪnˈkaʊntəd/</div>
        <div class="zh-word">遇到（過去式）</div>
      </div>
    </div>
  </div>

  <!-- 核心句型 -->
  <div class="section">
    <div class="section-label">核心句型</div>
    <h3>點句子聽完整朗讀</h3>
    <ul class="pattern-list">
      <li onclick="speakWord(this.dataset.text)" data-text="Today I designed a conversational AI agent.">Today I <strong>designed</strong> a conversational AI agent.</li>
      <li onclick="speakWord(this.dataset.text)" data-text="I chose Haiku for speed and Sonnet for quality.">I <strong>chose</strong> Haiku for speed and Sonnet for quality.</li>
      <li onclick="speakWord(this.dataset.text)" data-text="Codex didn't follow the spec exactly.">Codex <strong>didn't follow</strong> the spec exactly.</li>
      <li onclick="speakWord(this.dataset.text)" data-text="I wrote a fix and it worked correctly after that.">I <strong>wrote</strong> a fix and it <strong>worked</strong> correctly after that.</li>
      <li onclick="speakWord(this.dataset.text)" data-text="I ran a batch job to fill in five hundred and sixty-eight missing records.">I <strong>ran</strong> a batch job to fill in 568 missing records.</li>
      <li onclick="speakWord(this.dataset.text)" data-text="What did you build today? I built an AI agent interface."><strong>What did</strong> you build today? → I <strong>built</strong> an AI agent interface.</li>
    </ul>
  </div>

</div>

<footer>
  <a href="https://github.com/Pcc329/daily-english">daily-english</a> is maintained by
  <a href="https://github.com/Pcc329">Pcc329</a>.<br>
  工作日誌 × Past Simple · Generated by Claude · 2026-06-16
</footer>

<script>
  let currentUtterance = null;
  const speedInput = document.getElementById('speed');
  const speedVal = document.getElementById('speed-val');

  speedInput.addEventListener('input', () => {
    speedVal.textContent = speedInput.value + '×';
  });

  document.getElementById('stop-btn').addEventListener('click', () => {
    speechSynthesis.cancel();
    document.querySelectorAll('.chunk span').forEach(s => s.classList.remove('playing'));
  });

  function speak(el) {
    const span = el.querySelector('span');
    const text = span.textContent.trim().replace(/[。，、]/g, '');
    if (!text || text === '.') return;
    speechSynthesis.cancel();
    document.querySelectorAll('.chunk span').forEach(s => s.classList.remove('playing'));
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = 'en-US';
    utter.rate = parseFloat(speedInput.value);
    span.classList.add('playing');
    utter.onend = () => span.classList.remove('playing');
    speechSynthesis.speak(utter);
  }

  function speakAll(id) {
    const text = document.getElementById(id).textContent.trim();
    speechSynthesis.cancel();
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = 'en-US';
    utter.rate = parseFloat(speedInput.value);
    speechSynthesis.speak(utter);
  }

  function speakWord(text) {
    speechSynthesis.cancel();
    const utter = new SpeechSynthesisUtterance(typeof text === 'string' ? text : text);
    utter.lang = 'en-US';
    utter.rate = parseFloat(speedInput.value);
    speechSynthesis.speak(utter);
  }
</script>
</body>
</html>
