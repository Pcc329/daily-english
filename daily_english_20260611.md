<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>每日英文練習 | 2026-06-11</title>
  <style>
    :root {
      --green: #157878; --light-green: #00d084; --bg: #f4f8f6;
      --card: #ffffff; --text: #1a2e2a; --muted: #5a7a72;
      --border: #d4e8e0; --accent: #e8f5f0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: Georgia, "Times New Roman", serif; background: var(--bg); color: var(--text); line-height: 1.7; }

    .site-header { background: linear-gradient(135deg, #155757 0%, #157878 60%, #1a9a9a 100%); color: white; padding: 2rem 1.5rem 1.5rem; text-align: center; }
    .site-header h1 { font-size: 1.6rem; font-weight: bold; letter-spacing: 0.05em; }
    .site-header p { font-size: 0.9rem; opacity: 0.8; margin-top: 0.3rem; font-style: italic; }
    .site-header a { color: #b2f0e8; font-size: 0.82rem; text-decoration: none; display: inline-block; margin-top: 0.6rem; }

    .date-banner { background: var(--green); color: white; text-align: center; padding: 1.2rem 1rem; }
    .date-banner .day-label { font-size: 0.8rem; opacity: 0.75; letter-spacing: 0.12em; text-transform: uppercase; }
    .date-banner .date-main { font-size: 1.4rem; font-weight: bold; margin: 0.2rem 0; }
    .date-banner .subtitle { font-size: 0.85rem; opacity: 0.85; }
    .date-banner .keywords { margin-top: 0.5rem; font-size: 0.78rem; opacity: 0.7; font-style: italic; letter-spacing: 0.05em; }

    main { max-width: 760px; margin: 0 auto; padding: 1.5rem 1rem 4rem; }

    .speed-control { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 0.8rem 1.2rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }
    .speed-control label { font-size: 0.82rem; color: var(--muted); font-family: sans-serif; white-space: nowrap; }
    .speed-btn { background: none; border: 1px solid var(--border); border-radius: 6px; padding: 0.3rem 0.7rem; font-size: 0.8rem; cursor: pointer; font-family: sans-serif; color: var(--muted); transition: all 0.15s; }
    .speed-btn:hover { background: var(--accent); }
    .speed-btn.active { background: var(--green); color: white; border-color: var(--green); }
    .stop-btn { background: none; border: 1px solid #e88; border-radius: 6px; padding: 0.3rem 0.7rem; font-size: 0.8rem; cursor: pointer; font-family: sans-serif; color: #c44; }
    .stop-btn:hover { background: #fee; }

    .section-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 1.4rem 1.5rem; margin-bottom: 1.4rem; }
    .section-num { display: inline-block; background: var(--green); color: white; font-size: 0.72rem; font-family: sans-serif; letter-spacing: 0.08em; padding: 0.2rem 0.6rem; border-radius: 4px; margin-bottom: 0.6rem; }
    .section-title { font-size: 1.05rem; font-weight: bold; margin-bottom: 0.8rem; color: var(--text); }

    .zh-summary { background: var(--accent); border-left: 3px solid var(--green); border-radius: 0 8px 8px 0; padding: 0.8rem 1rem; margin-bottom: 1rem; font-size: 0.9rem; color: var(--muted); line-height: 1.7; }

    .chunk-group { display: flex; flex-direction: column; gap: 0.4rem; margin-bottom: 1rem; }
    .chunk { display: inline-flex; align-items: center; gap: 0.5rem; }
    .chunk-text { background: #f0faf6; border: 1px solid var(--border); border-radius: 20px; padding: 0.35rem 0.9rem; font-size: 0.92rem; cursor: pointer; transition: all 0.15s; line-height: 1.5; }
    .chunk-text:hover { background: var(--green); color: white; border-color: var(--green); }

    .speak-all-btn { display: inline-flex; align-items: center; gap: 0.4rem; background: none; border: 1px solid var(--green); color: var(--green); border-radius: 8px; padding: 0.4rem 1rem; font-size: 0.82rem; font-family: sans-serif; cursor: pointer; transition: all 0.15s; }
    .speak-all-btn:hover { background: var(--green); color: white; }
    .speak-all-btn::before { content: "▶"; font-size: 0.7rem; }

    .vocab-section { margin-top: 2rem; }
    .vocab-section h2 { font-size: 1rem; color: var(--green); border-bottom: 2px solid var(--border); padding-bottom: 0.4rem; margin-bottom: 1rem; font-family: sans-serif; letter-spacing: 0.05em; }
    .vocab-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 0.7rem; }
    .vocab-card { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 0.8rem 1rem; cursor: pointer; transition: all 0.15s; text-align: center; }
    .vocab-card:hover { border-color: var(--green); background: var(--accent); }
    .vocab-en { font-size: 0.88rem; font-weight: bold; color: var(--text); }
    .vocab-zh { font-size: 0.78rem; color: var(--muted); margin-top: 0.2rem; font-family: sans-serif; }

    .sentences-section { margin-top: 2rem; }
    .sentences-section h2 { font-size: 1rem; color: var(--green); border-bottom: 2px solid var(--border); padding-bottom: 0.4rem; margin-bottom: 1rem; font-family: sans-serif; letter-spacing: 0.05em; }
    .sentence-item { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.8rem; cursor: pointer; transition: all 0.15s; }
    .sentence-item:hover { border-color: var(--green); background: var(--accent); }
    .sentence-en { font-size: 0.95rem; color: var(--text); line-height: 1.6; }
    .sentence-zh { font-size: 0.82rem; color: var(--muted); margin-top: 0.3rem; font-family: sans-serif; }

    .hint { text-align: center; font-size: 0.78rem; color: var(--muted); margin-top: 1.8rem; font-family: sans-serif; font-style: italic; }

    .site-footer { background: #1a3d3d; color: #ccc; text-align: center; padding: 2rem 1rem; font-size: 0.82rem; font-family: sans-serif; }
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
  <div class="day-label">2026.06.11 — Day 13</div>
  <div class="date-main">資料除錯・儀表板換色・簡報製作</div>
  <div class="subtitle">BOM Debug · Dashboard Recolor · Presentation + Progress Bar</div>
  <div class="keywords">bom character, color palette, discrimination, standard deviation, progress indicator</div>
</div>

<main>
  <div class="speed-control">
    <label>語速</label>
    <button class="speed-btn" onclick="setRate(0.7)">0.7×</button>
    <button class="speed-btn active" onclick="setRate(0.9)">0.9×</button>
    <button class="speed-btn" onclick="setRate(1.0)">1.0×</button>
    <button class="speed-btn" onclick="setRate(1.2)">1.2×</button>
    <button class="stop-btn" onclick="stopAll()">■ 停止</button>
  </div>

  <h2 style="font-size:1rem; color:var(--muted); font-family:sans-serif; margin-bottom:1rem; letter-spacing:0.05em;">朗讀練習</h2>

  <!-- Section 1 -->
  <div class="section-card">
    <div class="section-num">段落一</div>
    <div class="section-title">BOM 除錯 + is_startup 批次同步</div>
    <div class="zh-summary">
      在補全 Companies 屬性時，發現 Airtable API 回傳的欄位名稱前有一個隱藏的 BOM 字元，導致所有 company_id 查詢都回傳 None。用一行 replace 清除後，成功批次同步了 112 家公司的新創狀態。
    </div>
    <div class="chunk-group">
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">While filling in company attributes,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">we discovered a hidden BOM character</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">prepended to the field name in the API response.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">This caused every company ID lookup to return None.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">After stripping the BOM with a one-line replace,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">we ran the batch sync successfully</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">and updated the startup status for 112 companies in Airtable.</span></div>
    </div>
    <button class="speak-all-btn" onclick="speakAll(1)">聽整段</button>
  </div>

  <!-- Section 2 -->
  <div class="section-card">
    <div class="section-num">段落二</div>
    <div class="section-title">儀表板色系升級完成並 Merge</div>
    <div class="zh-summary">
      儀表板換色系任務完成並合併上線。Codex 按照規格書將全站色系從單色綠升級為 IT Product Warehouse 風格：深海軍藍 header、Teal 主色、九色 categorical palette、KPI 語意分色。截圖驗收三個關鍵畫面後確認 PR 可以 merge。
    </div>
    <div class="chunk-group">
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">The dashboard color scheme upgrade was completed and merged.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">Codex updated the entire color system</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">from a single-color green to the IT Product Warehouse style.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">This includes a deep navy header,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">teal as the primary brand color,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">a nine-color categorical palette for the charts,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">and semantic accent colors for the KPI numbers.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">We approved the merge after checking three key screenshots.</span></div>
    </div>
    <button class="speak-all-btn" onclick="speakAll(2)">聽整段</button>
  </div>

  <!-- Section 3 -->
  <div class="section-card">
    <div class="section-num">段落三</div>
    <div class="section-title">0615 報告簡報製作 + 雙層進度列</div>
    <div class="zh-summary">
      為 0615 報告製作了六頁新投影片，涵蓋建置歷程、系統現況、AI 評分系統、鑑別度分析、模擬測試流程與顧問價值。另外為 V6 版本的每一頁加上雙層進度列：上層顯示六大段落，下層顯示當前段落的子頁。
    </div>
    <div class="chunk-group">
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">We created six new slides for the June 15th presentation.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">They cover the build journey, system overview,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">the AI scoring system, discrimination analysis,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">the simulation test walkthrough, and consultant value.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">We also added a two-level progress indicator to every content slide.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">The top row shows the six main sections,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">and the second row shows the sub-pages within the current section.</span></div>
    </div>
    <button class="speak-all-btn" onclick="speakAll(3)">聽整段</button>
  </div>

  <!-- Section 4 -->
  <div class="section-card">
    <div class="section-num">段落四</div>
    <div class="section-title">AI 評分系統：鑑別度與標準差分析</div>
    <div class="zh-summary">
      深入討論了四維度評分系統的鑑別度問題。標準差分析顯示，創新力（1.14）鑑別度最佳，支援度（0.57）趨同最嚴重。根本原因是欄位資料填寫不足：資訊不完整時，模型傾向給安全分 4 分，導致分布集中，無法區分好壞。
    </div>
    <div class="chunk-group">
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">We did a deep dive into the discrimination quality of the four-dimension scoring system.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">Standard deviation measures how spread out the scores are.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">Innovation has the best discrimination with a standard deviation of 1.14,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">while Support is the most concentrated at 0.57.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">The root cause is insufficient field data.</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">When information is incomplete,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">the model defaults to a safe score of four,</span></div>
      <div class="chunk"><span class="chunk-text" onclick="speak(this)">which causes the scores to cluster and lose their ranking power.</span></div>
    </div>
    <button class="speak-all-btn" onclick="speakAll(4)">聽整段</button>
  </div>

  <!-- Vocab -->
  <div class="vocab-section">
    <h2>術語發音</h2>
    <div class="vocab-grid">
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">BOM character</div>
        <div class="vocab-zh">位元組順序標記</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">field key</div>
        <div class="vocab-zh">欄位鍵名</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">color palette</div>
        <div class="vocab-zh">色票 / 配色方案</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">categorical palette</div>
        <div class="vocab-zh">類別配色</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">discrimination</div>
        <div class="vocab-zh">鑑別度</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">standard deviation</div>
        <div class="vocab-zh">標準差</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">progress indicator</div>
        <div class="vocab-zh">進度列</div>
      </div>
      <div class="vocab-card" onclick="speak(this.querySelector('.vocab-en'))">
        <div class="vocab-en">safe score</div>
        <div class="vocab-zh">安全分（中庸評分）</div>
      </div>
    </div>
  </div>

  <!-- Sentences -->
  <div class="sentences-section">
    <h2>核心句型</h2>
    <div class="sentence-item" onclick="speak(this.querySelector('.sentence-en'))">
      <div class="sentence-en">The bug was caused by a hidden BOM character prepended to the field name, which made every lookup return None.</div>
      <div class="sentence-zh">這個 bug 是由附在欄位名稱前的隱藏 BOM 字元所造成的，導致每次查詢都回傳 None。</div>
    </div>
    <div class="sentence-item" onclick="speak(this.querySelector('.sentence-en'))">
      <div class="sentence-en">We verified the merge by checking three screenshots: the header color, the chart palette, and the Taiwan density map gradient.</div>
      <div class="sentence-zh">我們透過確認三個截圖來驗收 merge：header 顏色、圖表配色，以及台灣密度地圖的漸層。</div>
    </div>
    <div class="sentence-item" onclick="speak(this.querySelector('.sentence-en'))">
      <div class="sentence-en">A low standard deviation means most solutions receive the same score, which reduces the indicator's usefulness for ranking.</div>
      <div class="sentence-zh">標準差低代表大多數方案得到相同分數，這會降低該指標的排序效用。</div>
    </div>
    <div class="sentence-item" onclick="speak(this.querySelector('.sentence-en'))">
      <div class="sentence-en">The data can be collected by scrapers, but a consultant's on-site insight cannot be automated — interview records are what will make this knowledge base a true competitive moat.</div>
      <div class="sentence-zh">資料可以爬蟲取得，但顧問在客戶現場的洞察無法自動化——訪談記錄才是讓這個智庫成為真正護城河的關鍵。</div>
    </div>
  </div>

  <p class="hint">點單字聽發音 · 點卡片聽術語 · 點句子聽完整朗讀</p>
</main>

<footer class="site-footer">
  <p><a href="https://github.com/Pcc329/daily-english">daily-english</a> is maintained by <a href="https://github.com/Pcc329">Pcc329</a>.</p>
  <p style="margin-top:0.4rem;">This page was generated by Claude · 2026-06-11</p>
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
  1: "While filling in company attributes, we discovered a hidden BOM character prepended to the field name in the API response. This caused every company ID lookup to return None. After stripping the BOM with a one-line replace, we ran the batch sync successfully and updated the startup status for 112 companies in Airtable.",
  2: "The dashboard color scheme upgrade was completed and merged. Codex updated the entire color system from a single-color green to the IT Product Warehouse style. This includes a deep navy header, teal as the primary brand color, a nine-color categorical palette for the charts, and semantic accent colors for the KPI numbers. We approved the merge after checking three key screenshots.",
  3: "We created six new slides for the June 15th presentation. They cover the build journey, system overview, the AI scoring system, discrimination analysis, the simulation test walkthrough, and consultant value. We also added a two-level progress indicator to every content slide. The top row shows the six main sections, and the second row shows the sub-pages within the current section.",
  4: "We did a deep dive into the discrimination quality of the four-dimension scoring system. Standard deviation measures how spread out the scores are. Innovation has the best discrimination with a standard deviation of 1.14, while Support is the most concentrated at 0.57. The root cause is insufficient field data. When information is incomplete, the model defaults to a safe score of four, which causes the scores to cluster and lose their ranking power."
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
