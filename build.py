import json
import os
import re

if not os.path.exists('lessons.json'):
    print("找不到 lessons.json，跳過產出。")
    exit(0)

with open('lessons.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

print(f"📦 讀取到 {len(lessons)} 篇教材，開始生成 HTML...")

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Daily English - {{DATE}}</title>
  <style>
    :root {
      --bg: #0f172a; --card-bg: #1e293b; --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.15); --text: #f8fafc;
      --text-muted: #94a3b8; --border: #334155; --highlight: #f59e0b;
      --code-bg: #0b1120; --toeic: #ec4899; --chunk-border: #0ea5e9;
      --chunk-bg: rgba(14, 165, 233, 0.08);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background-color: var(--bg); color: var(--text); line-height: 1.6; padding: 2rem 1rem; display: flex; justify-content: center; }
    .container { max-width: 800px; width: 100%; }
    header { border-bottom: 1px solid var(--border); padding-bottom: 1.5rem; margin-bottom: 1.5rem; }
    .badge { display: inline-block; background: var(--accent-glow); color: var(--accent); padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem; font-weight: 600; margin-bottom: 0.75rem; border: 1px solid rgba(56, 189, 248, 0.3); }
    h1 { font-size: 1.875rem; font-weight: 700; color: var(--text); margin-bottom: 0.5rem; }
    .subtitle { color: var(--text-muted); font-size: 1rem; }
    .audio-control-bar { background: var(--card-bg); border: 1px solid var(--accent); border-radius: 8px; padding: 0.75rem 1.25rem; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem; }
    .speed-label { font-size: 0.9rem; font-weight: 600; color: var(--accent); }
    .speed-slider-group { display: flex; align-items: center; gap: 0.75rem; }
    .speed-slider { accent-color: var(--accent); cursor: pointer; }
    .speed-val { font-family: monospace; font-size: 0.95rem; min-width: 40px; color: var(--highlight); font-weight: 700; }
    .vocab-card { background-color: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; }
    .vocab-header { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 0.75rem; border-bottom: 1px dashed var(--border); padding-bottom: 0.75rem; }
    .word-group { display: flex; align-items: center; gap: 0.75rem; }
    .word { font-size: 1.75rem; font-weight: 700; color: var(--accent); }
    .pos { color: var(--highlight); font-style: italic; font-weight: 600; }
    .ipa { font-family: monospace; color: var(--text-muted); }
    .meaning { font-size: 1.15rem; font-weight: 600; color: var(--text); margin-bottom: 0.75rem; }
    .speak-btn { background: rgba(56, 189, 248, 0.15); border: 1px solid var(--accent); color: var(--accent); border-radius: 6px; padding: 3px 8px; font-size: 0.85rem; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; }
    .speak-btn:hover { background: var(--accent); color: var(--bg); }
    .section-title { font-weight: 700; color: var(--accent); margin-top: 0.75rem; font-size: 0.95rem; }
    .toeic-title { color: var(--toeic); font-weight: 700; margin-top: 0.75rem; font-size: 0.95rem; }
    .chunk-title { color: var(--chunk-border); font-weight: 700; margin-top: 0.75rem; font-size: 0.95rem; }
    .detail-block { background: var(--code-bg); border-radius: 6px; padding: 0.75rem 1rem; margin-top: 0.5rem; font-size: 0.925rem; color: #e2e8f0; border-left: 3px solid var(--accent); }
    .toeic-block { background: var(--code-bg); border-radius: 6px; padding: 0.75rem 1rem; margin-top: 0.5rem; font-size: 0.925rem; color: #e2e8f0; border-left: 3px solid var(--toeic); }
    .chunk-block { background: var(--chunk-bg); border-radius: 6px; padding: 0.75rem 1rem; margin-top: 0.5rem; font-size: 0.95rem; color: #bae6fd; border-left: 3px solid var(--chunk-border); line-height: 1.8; }
    .slash { color: var(--highlight); font-weight: 900; margin: 0 4px; font-size: 1.1rem; }
    .stress { color: #ffffff; font-weight: 700; text-decoration: underline; text-underline-offset: 3px; }
    .breathe { font-size: 0.8rem; color: var(--highlight); margin-right: 6px; }
    ul { list-style: none; }
    li { margin-bottom: 0.4rem; }
    .example-wrap { display: flex; justify-content: space-between; align-items: flex-start; gap: 0.5rem; }
    .example-en { font-weight: 500; color: #cbd5e1; }
    .example-zh { color: var(--text-muted); font-size: 0.875rem; margin-top: 0.25rem; }
    .sprint-summary { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 1px solid var(--accent); border-radius: 12px; padding: 1.5rem; margin-top: 2rem; }
    .sprint-summary h2 { font-size: 1.25rem; color: var(--accent); margin-bottom: 0.75rem; }
    footer { text-align: center; margin-top: 3rem; color: var(--text-muted); font-size: 0.85rem; }
    .back-home { display: inline-block; margin-top: 1rem; color: var(--accent); text-decoration: none; }
  </style>
</head>
<body>
<div class="container">
  <header>
    <span class="badge">Target: TOEIC 700+</span>
    <h1>Daily English Sprint: Day {{DAY_NUM}}</h1>
    <p class="subtitle">{{TOPIC_ZH}} ({{DATE}})</p>
  </header>

  <div class="audio-control-bar">
    <div class="speed-label">🎧 發音語速調節 (Speech Speed)</div>
    <div class="speed-slider-group">
      <input type="range" class="speed-slider" id="speedRate" min="0.6" max="1.3" step="0.1" value="0.9">
      <span class="speed-val" id="speedDisplay">0.9x</span>
    </div>
  </div>

  {{CARDS_HTML}}

  <div class="sprint-summary">
    <h2>🎯 整合複習句型 (Synthesis Pattern)</h2>
    <div class="example-wrap">
      <div class="example-en">"{{SYN_EN}}"</div>
      <button class="speak-btn" onclick="speakText('{{SYN_EN_ESCAPED}}')">🔊</button>
    </div>
    <div class="example-zh" style="margin-top: 0.5rem;">（{{SYN_ZH}}）</div>
    <div class="chunk-title" style="margin-top: 1rem; color: var(--accent);">🗣️ 整合長句跟讀挑戰（嚴格換氣 2 次）</div>
    <div class="chunk-block">{{SYN_CHUNKS}}</div>
  </div>

  <footer>
    <a href="index.html" class="back-home">← 回到主選單</a>
    <p style="margin-top: 1rem;">Daily English Learning Repository &copy; 2026. Designed for Database PM.</p>
  </footer>
</div>

<script>
  const speedSlider = document.getElementById('speedRate');
  const speedDisplay = document.getElementById('speedDisplay');
  speedSlider.addEventListener('input', (e) => { speedDisplay.textContent = e.target.value + 'x'; });
  function speakText(text) {
    if (!('speechSynthesis' in window)) { alert('您的瀏覽器不支援語音合成功能'); return; }
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = parseFloat(speedSlider.value);
    window.speechSynthesis.speak(utterance);
  }
</script>
</body>
</html>
"""

for item in lessons:
    date_clean = item["date"].replace("-", "")
    filename = f"daily_english_{date_clean}.html"
    
    cards_html = ""
    for w in item["words"]:
        safe_example = w["example_en"].replace("'", "\\'")
        card = f"""
  <div class="vocab-card">
    <div class="vocab-header">
      <div class="word-group">
        <span class="word">{w["word"]}</span>
        <button class="speak-btn" onclick="speakText('{w["word"]}')">🔊 朗讀</button>
        <span class="pos">{w["pos"]}</span>
      </div>
      <span class="ipa">{w["ipa"]}</span>
    </div>
    <div class="meaning">{w["meaning"]}</div>
    <div class="section-title">🔊 自然發音拆解</div>
    <div class="detail-block">{w["phonics"]}</div>
    <div class="section-title">🧬 字根字首與來源</div>
    <div class="detail-block">{w["roots"]}</div>
    <div class="toeic-title">🎯 TOEIC 700+ 聽讀核心考點</div>
    <div class="toeic-block">
      <ul>
        <li><strong>🎧 聽力辨析：</strong>{w["toeic_listening"]}</li>
        <li><strong>📖 閱讀搭配詞：</strong>{w["toeic_reading"]}</li>
      </ul>
    </div>
    <div class="section-title">💼 PM 實戰例句與情境</div>
    <div class="detail-block">
      <div class="example-wrap">
        <div class="example-en">"{w["example_en"]}"</div>
        <button class="speak-btn" onclick="speakText('{safe_example}')">🔊</button>
      </div>
      <div class="example-zh">「{w["example_zh"]}」</div>
    </div>
    <div class="chunk-title">🗣️️ 意群跟讀拆解（三段換氣法）</div>
    <div class="chunk-block">{w["chunks"]}</div>
  </div>
"""
        cards_html += card

    safe_syn_en = item["synthesis"]["en"].replace("'", "\\'")
    page_html = TEMPLATE.replace("{{DATE}}", item["date"]) \
                        .replace("{{DAY_NUM}}", str(item["day_num"])) \
                        .replace("{{TOPIC_ZH}}", item["topic_zh"]) \
                        .replace("{{CARDS_HTML}}", cards_html) \
                        .replace("{{SYN_EN}}", item["synthesis"]["en"]) \
                        .replace("{{SYN_EN_ESCAPED}}", safe_syn_en) \
                        .replace("{{SYN_ZH}}", item["synthesis"]["zh"]) \
                        .replace("{{SYN_CHUNKS}}", item["synthesis"]["chunks"])

    with open(filename, 'w', encoding='utf-8') as f_out:
        f_out.write(page_html)
    print(f"  ✓ 已產出 {filename}")

if os.path.exists("index.html"):
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    links_html = ""
    for item in lessons:
        d_clean = item["date"].replace("-", "")
        file_target = f"daily_english_{d_clean}.html"
        link_block = f"""      <a class="list-item" href="{file_target}">
        <div class="item-left">
          <div class="item-date">{item["weekday_zh"]}</div>
          <div class="item-topic">{item["topic_zh"]}</div>
        </div>
        <span class="item-arrow">›</span>
      </a>\n"""
        links_html += link_block

    pattern = r'(<!-- AUTO_WORK_START -->)(.*?)(<!-- AUTO_WORK_END -->)'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, f"\\1\n{links_html}      \\3", content, flags=re.DOTALL)
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("  ✓ index.html 連結已自動更新！")
