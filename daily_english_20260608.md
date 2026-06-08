<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>每日英文練習 | 2026-06-08</title>
  <style>
    :root {
      --green: #157878;
      --light-green: #00d084;
      --bg: #f4f8f6;
      --card: #ffffff;
      --text: #1a2e2a;
      --muted: #5a7a72;
      --border: #d4e8e0;
      --accent: #e8f5f0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: Georgia, "Times New Roman", serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.7;
    }

    /* Header */
    .site-header {
      background: linear-gradient(135deg, #155757 0%, #157878 60%, #1a9a9a 100%);
      color: white;
      padding: 2rem 1.5rem 1.5rem;
      text-align: center;
    }
    .site-header h1 { font-size: 1.6rem; font-weight: bold; letter-spacing: 0.05em; }
    .site-header p { font-size: 0.9rem; opacity: 0.8; margin-top: 0.3rem; font-style: italic; }
    .site-header a { color: #b2f0e8; font-size: 0.82rem; text-decoration: none; display: inline-block; margin-top: 0.6rem; }

    /* Date Banner */
    .date-banner {
      background: var(--green);
      color: white;
      text-align: center;
      padding: 1.2rem 1rem;
    }
    .date-banner .day-label { font-size: 0.8rem; opacity: 0.75; letter-spacing: 0.12em; text-transform: uppercase; }
    .date-banner .date-main { font-size: 1.4rem; font-weight: bold; margin: 0.2rem 0; }
    .date-banner .subtitle { font-size: 0.85rem; opacity: 0.85; }
    .date-banner .keywords { margin-top: 0.5rem; font-size: 0.78rem; opacity: 0.7; font-style: italic; letter-spacing: 0.05em; }

    /* Main */
    main { max-width: 760px; margin: 0 auto; padding: 1.5rem 1rem 4rem; }

    /* Speed Control */
    .speed-control {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 0.8rem 1.2rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }
    .speed-control label { font-size: 0.82rem; color: var(--muted); font-family: sans-serif; }
    .speed-btn {
      background: var(--accent);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 0.3rem 0.7rem;
      font-size: 0.8rem;
      cursor: pointer;
      color: var(--green);
      font-weight: bold;
      font-family: sans-serif;
    }
    .speed-btn.active { background: var(--green); color: white; border-color: var(--green); }
    .stop-btn {
      margin-left: auto;
      background: #fff0f0;
      border: 1px solid #ffc0c0;
      border-radius: 6px;
      padding: 0.3rem 0.8rem;
      font-size: 0.8rem;
      cursor: pointer;
      color: #cc4444;
      font-family: sans-serif;
    }

    /* Section Card */
    .section-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      margin-bottom: 1.5rem;
      overflow: hidden;
    }
    .section-header {
      background: var(--accent);
      border-bottom: 1px solid var(--border);
      padding: 0.8rem 1.2rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }
    .section-num {
      background: var(--green);
      color: white;
      border-radius: 50%;
      width: 26px;
      height: 26px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: bold;
      font-family: sans-serif;
      flex-shrink: 0;
    }
    .section-title { font-size: 1rem; font-weight: bold; color: var(--green); font-family: sans-serif; }
    .section-body { padding: 1.2rem; }

    /* Chinese Text */
    .zh-text {
      font-size: 0.95rem;
      color: var(--muted);
      margin-bottom: 1rem;
      line-height: 1.8;
      border-left: 3px solid var(--border);
      padding-left: 0.8rem;
    }

    /* English Chunks */
    .en-chunks { display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 1rem; }
    .chunk {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
    }
    .chunk-text {
      font-size: 1rem;
      color: var(--text);
      cursor: pointer;
      border-bottom: 1px dashed var(--border);
      transition: color 0.15s;
    }
    .chunk-text:hover { color: var(--green); border-bottom-color: var(--green); }
    .chunk-icon { font-size: 0.7rem; color: var(--light-green); }

    /* Listen Button */
    .listen-btn {
      background: var(--green);
      color: white;
      border: none;
      border-radius: 8px;
      padding: 0.5rem 1.1rem;
      font-size: 0.82rem;
      cursor: pointer;
      font-family: sans-serif;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: background 0.15s;
    }
    .listen-btn:hover { background: #0f5f5f; }

    /* Vocabulary */
    .vocab-section { margin-top: 2rem; }
    .vocab-title {
      font-size: 1rem;
      font-weight: bold;
      color: var(--green);
      font-family: sans-serif;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .vocab-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 0.8rem; }
    .vocab-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 0.9rem 1rem;
      cursor: pointer;
      transition: transform 0.15s, box-shadow 0.15s;
      text-align: center;
    }
    .vocab-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(21,120,120,0.1); }
    .vocab-en { font-size: 0.92rem; font-weight: bold; color: var(--green); }
    .vocab-zh { font-size: 0.78rem; color: var(--muted); margin-top: 0.25rem; font-family: sans-serif; }

    /* Key Sentences */
    .sentences-section { margin-top: 2rem; }
    .sentence-item {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1rem 1.1rem;
      margin-bottom: 0.8rem;
      cursor: pointer;
      transition: border-color 0.15s;
    }
    .sentence-item:hover { border-color: var(--green); }
    .sentence-en { font-size: 0.95rem; color: var(--text); }
    .sentence-zh { font-size: 0.82rem; color: var(--muted); margin-top: 0.3rem; font-family: sans-serif; }

    /* Footer hint */
    .hint-bar {
      text-align: center;
      font-size: 0.78rem;
      color: var(--muted);
      font-family: sans-serif;
      margin: 1.5rem 0 0.5rem;
    }

    /* Site Footer */
    .site-footer {
      background: var(--green);
      color: rgba(255,255,255,0.75);
      text-align: center;
      padding: 1.2rem;
      font-size: 0.78rem;
      font-family: sans-serif;
    }
    .site-footer a { color: #b2f0e8; }
  </style>
</head>
<body>

<header class="site-header">
  <h1>每日英文練習</h1>
  <p>資料庫工程師的英文口說復健 · Daily Speaking Practice</p>
  <a href="https://github.com/Pcc329/daily-english">View on GitHub</a>
</header>

<div class="date-banner">
  <div class="day-label">2026.06.08 — Day 10</div>
  <div class="date-main">搜尋升級、資料品質與篩選修復</div>
  <div class="subtitle">Semantic Search · Data Quality · Filter Fixes</div>
  <div class="keywords">AI classification · industry keyword · merge conflict · filter alignment</div>
</div>

<main>
  <!-- Speed Control -->
  <div class="speed-control">
    <label>語速</label>
    <button class="speed-btn" onclick="setRate(0.8)">0.8×</button>
    <button class="speed-btn active" onclick="setRate(0.9)">0.9×</button>
    <button class="speed-btn" onclick="setRate(1.0)">1.0×</button>
    <span style="font-size:0.78rem;color:#999;font-family:sans-serif;">■</span>
    <button class="stop-btn" onclick="stopAll()">停止</button>
    <span style="font-size:0.75rem;color:var(--muted);font-family:sans-serif;">朗讀練習</span>
  </div>

  <!-- Section 1 -->
  <div class="section-card">
    <div class="section-header">
      <div class="section-num">1</div>
      <div class="section-title">段落一 — AI 批次分類 564 筆方案</div>
    </div>
    <div class="section-body">
      <div class="zh-text">
        針對資料庫中 564 筆沒有服務類別的方案，用 Claude Haiku API 做批次自動分類。每筆方案把方案名稱、描述和原始類別標籤餵給模型，讓它從 9 個類別中選出最適合的一個，花費約 0.27 美元，暫無法分類從 172 筆降到 15 筆。
      </div>
      <div class="en-chunks">
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">We used the Claude Haiku API to batch-classify 564 solution records</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">that were missing their service category labels</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">For each record, we fed the solution name, description, and original category tag to the model</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">and asked it to pick the best fit from nine predefined categories</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">The total cost was about 0.27 US dollars</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">and the unclassified count dropped from 172 down to just 15</span></div>
      </div>
      <button class="listen-btn" onclick="speakAll(1)">▶ 聽整段</button>
    </div>
  </div>

  <!-- Section 2 -->
  <div class="section-card">
    <div class="section-header">
      <div class="section-num">2</div>
      <div class="section-title">段落二 — 語意搜尋全面升級</div>
    </div>
    <div class="section-body">
      <div class="zh-text">
        升級了 Claude 的語意解析邏輯，新增兩個篩選欄位：category 精確對應服務類別，讓「醫療照護系統」從回傳全部 2322 筆降到 44 筆；industryKeyword 則讓「餐飲業」和「製造業」搜尋相同需求時，能回傳不同的排序結果。
      </div>
      <div class="en-chunks">
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">We upgraded the semantic parsing logic in Claude's API</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">by adding two new filter fields</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">The category field maps queries to exact service categories</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">so searching "healthcare system" now returns 44 results instead of all 2,322</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">The industryKeyword field enables industry-specific soft ranking</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">so the food service industry and the manufacturing industry get different top results</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">even when they search for the same need</span></div>
      </div>
      <button class="listen-btn" onclick="speakAll(2)">▶ 聽整段</button>
    </div>
  </div>

  <!-- Section 3 -->
  <div class="section-card">
    <div class="section-header">
      <div class="section-num">3</div>
      <div class="section-title">段落三 — Merge Conflict 修復</div>
    </div>
    <div class="section-body">
      <div class="zh-text">
        語意搜尋升級的 PR 因為和另一個分支都改了 index.html 的排序邏輯，產生 merge conflict。前端保留新版的 industryKeyword 加權排序邏輯，刪除舊版衝突區塊後重新 push，成功 merge。
      </div>
      <div class="en-chunks">
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">The semantic search pull request had a merge conflict</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">because two branches both modified the sorting logic in index.html</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">We resolved it by keeping the new version</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">which includes the industryKeyword weighted ranking logic</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">removed all conflict markers, pushed again, and successfully merged the PR</span></div>
      </div>
      <button class="listen-btn" onclick="speakAll(3)">▶ 聽整段</button>
    </div>
  </div>

  <!-- Section 4 -->
  <div class="section-card">
    <div class="section-header">
      <div class="section-num">4</div>
      <div class="section-title">段落四 — 篩選功能對齊與修復</div>
    </div>
    <div class="section-body">
      <div class="zh-text">
        發現前端篩選標籤的名稱和資料庫實際值不一致，例如「雲市集」對應資料庫的「臺灣雲市集」，「SMEI」對應「SEMI」。同時補上了遺漏的領域篩選條件（industry_vertical），讓旅宿觀光、製造業等領域篩選正式生效。
      </div>
      <div class="en-chunks">
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">We found a mismatch between the filter button labels and the actual database values</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">For example, the button said "Cloud Marketplace" but the database stored "Taiwan Cloud Marketplace"</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">We aligned all seven program type labels to match the database exactly</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">We also added the missing industry vertical filter condition</span></div>
        <div class="chunk"><span class="chunk-icon">▶</span><span class="chunk-text" onclick="speak(this)">so filtering by sectors like hospitality and manufacturing now works correctly</span></div>
      </div>
      <button class="listen-btn" onclick="speakAll(4)">▶ 聽整段</button>
    </div>
  </div>

  <!-- Vocabulary -->
  <div class="vocab-section">
    <div class="vocab-title">🔤 術語發音 <span style="font-size:0.75rem;font-weight:normal;color:var(--muted);">點卡片聽發音</span></div>
    <div class="vocab-grid">
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">batch classification</div>
        <div class="vocab-zh">批次分類</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">semantic parsing</div>
        <div class="vocab-zh">語意解析</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">industry keyword</div>
        <div class="vocab-zh">產業關鍵字</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">soft ranking</div>
        <div class="vocab-zh">軟性加權排序</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">merge conflict</div>
        <div class="vocab-zh">合併衝突</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">filter alignment</div>
        <div class="vocab-zh">篩選對齊</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">conflict marker</div>
        <div class="vocab-zh">衝突標記</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">weighted score</div>
        <div class="vocab-zh">加權分數</div>
      </div>
    </div>
  </div>

  <!-- Key Sentences -->
  <div class="sentences-section">
    <div class="vocab-title">💬 核心句型 <span style="font-size:0.75rem;font-weight:normal;color:var(--muted);">點句子聽完整朗讀</span></div>
    <div class="sentence-item" onclick="speak(this.querySelector('.sentence-en'))">
      <div class="sentence-en">The unclassified count dropped from 172 down to just 15 after the batch classification run.</div>
      <div class="sentence-zh">批次分類執行後，暫無法分類的筆數從 172 降到只剩 15 筆。</div>
    </div>
    <div class="sentence-item" onclick="speak(this.querySelector('.sentence-en'))">
      <div class="sentence-en">Searching for a healthcare system now returns 44 results instead of the entire database of 2,322.</div>
      <div class="sentence-zh">搜尋醫療照護系統現在回傳 44 筆，而不是整個資料庫的 2322 筆。</div>
    </div>
    <div class="sentence-item" onclick="speak(this.querySelector('.sentence-en'))">
      <div class="sentence-en">The industry keyword enables soft ranking so different industries see different top results for the same query.</div>
      <div class="sentence-zh">產業關鍵字啟用軟性排序，讓不同產業對相同查詢看到不同的 top 結果。</div>
    </div>
    <div class="sentence-item" onclick="speak(this.querySelector('.sentence-en'))">
      <div class="sentence-en">We resolved the merge conflict by keeping the new version and removing all conflict markers before pushing again.</div>
      <div class="sentence-zh">我們保留新版並移除所有衝突標記後重新 push，解決了 merge conflict。</div>
    </div>
  </div>

  <div class="hint-bar">點單字聽發音 · 點卡片聽術語 · 點句子聽完整朗讀</div>
</main>

<footer class="site-footer">
  <a href="https://github.com/Pcc329/daily-english">daily-english</a> is maintained by
  <a href="https://github.com/Pcc329">Pcc329</a>.<br>
  This page was generated by Claude · 2026-06-08
</footer>

<script>
  let currentRate = 0.9;
  let currentUtterance = null;

  function setRate(r) {
    currentRate = r;
    document.querySelectorAll('.speed-btn').forEach(btn => {
      btn.classList.toggle('active', btn.textContent === r.toFixed(1) + '×');
    });
  }

  function speak(el) {
    if (!el) return;
    stopAll();
    const text = el.textContent.trim();
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = 'en-US';
    utter.rate = currentRate;
    currentUtterance = utter;
    speechSynthesis.speak(utter);
  }

  function stopAll() {
    speechSynthesis.cancel();
    currentUtterance = null;
  }

  const paragraphs = {
    1: "We used the Claude Haiku API to batch-classify 564 solution records that were missing their service category labels. For each record, we fed the solution name, description, and original category tag to the model and asked it to pick the best fit from nine predefined categories. The total cost was about 0.27 US dollars, and the unclassified count dropped from 172 down to just 15.",
    2: "We upgraded the semantic parsing logic in Claude's API by adding two new filter fields. The category field maps queries to exact service categories, so searching healthcare system now returns 44 results instead of all 2,322. The industryKeyword field enables industry-specific soft ranking, so the food service industry and the manufacturing industry get different top results, even when they search for the same need.",
    3: "The semantic search pull request had a merge conflict, because two branches both modified the sorting logic in index.html. We resolved it by keeping the new version, which includes the industryKeyword weighted ranking logic, removed all conflict markers, pushed again, and successfully merged the PR.",
    4: "We found a mismatch between the filter button labels and the actual database values. For example, the button said Cloud Marketplace but the database stored Taiwan Cloud Marketplace. We aligned all seven program type labels to match the database exactly. We also added the missing industry vertical filter condition, so filtering by sectors like hospitality and manufacturing now works correctly."
  };

  function speakAll(num) {
    stopAll();
    const utter = new SpeechSynthesisUtterance(paragraphs[num]);
    utter.lang = 'en-US';
    utter.rate = currentRate;
    currentUtterance = utter;
    speechSynthesis.speak(utter);
  }
</script>
</body>
</html>
