import streamlit as st
import json
import re

# --- Bắt lỗi import an toàn ---
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

st.set_page_config(page_title="LeftoverChef AI", page_icon="🥘", layout="wide")

# ============ CSS ============
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;800&display=swap');
html, body, [class*="css"], .stApp {
    font-family: 'Be Vietnam Pro', sans-serif !important;
    background-color: #fbfaf6 !important;
    color: #17251e !important;
}
.block-container { max-width: 1200px; padding-top: 1.6rem; }
p, span, div, li, label, h1, h2, h3, h4, h5, h6, [data-testid="stText"], [data-testid="stCaption"], .stMarkdown {
    color: #17251e !important;
}
input, textarea, [data-baseweb="input"] input, [data-baseweb="textarea"] textarea {
    background-color: #ffffff !important;
    color: #17251e !important;
    -webkit-text-fill-color: #17251e !important;
}
input::placeholder, textarea::placeholder { color: #718078 !important; -webkit-text-fill-color: #718078 !important; }

.hero { background: linear-gradient(135deg, #d5f0db 0%, #f8fff8 45%, #fff2df 100%); border: 1px solid #cfe4d4; border-radius: 28px; padding: 40px; margin-bottom: 28px; box-shadow: 0 20px 50px -20px rgba(33,87,57,.15); }
.eyebrow { color:#17613f !important; font-weight:800; font-size:12px; background:#c9e8d2; padding:8px 14px; border-radius:30px; display:inline-block; }
.hero h1 { font-size: 48px; margin:16px 0 12px; letter-spacing:-1.5px; color: #183b2b !important; }
.hero p { color:#40564a !important; font-size:16px; max-width:680px; }

.panel { background:#fff; border:1px solid #e0e9e1; border-radius:20px; padding:22px; margin-bottom:18px; box-shadow: 0 8px 24px -12px rgba(27,65,43,.12); }
.recipe { background:#fff; border: 1.5px solid #e2e9e2; border-radius:20px; padding:20px; box-shadow: 0 8px 24px -12px rgba(28,65,43,.12); transition: all .2s; min-height: 320px; display: flex; flex-direction: column; }
.recipe:hover { transform: translateY(-5px); box-shadow: 0 15px 30px -10px rgba(28,65,43,.2); border-color:#a9d2b5; }
.recipe.perfect { border-color:#86efac; background: linear-gradient(180deg, #f0fdf4, #fff 60%); }
.recipe-emoji { font-size:40px; background:#f0f7f1; width:70px; height:70px; display:flex; align-items:center; justify-content:center; border-radius:20px; margin-bottom:12px; }
.match-badge { background:#e1f2e7; color:#155c3b !important; padding:5px 10px; border-radius:20px; font-size:11px; font-weight:800; }
.perfect-badge { background: linear-gradient(90deg,#fde68a,#fbbf24); color:#78350f !important; }
.match-bar { height:6px; background:#eef4ee; border-radius:3px; margin:10px 0; }
.match-bar-fill { height:100%; background: linear-gradient(90deg,#3fa66b,#1f7a4d); border-radius:3px; }
.recipe h4 { margin:12px 0 8px; font-size:18px; color: #183b2b !important; }
.muted { color:#4b5d52 !important; font-size:13px; line-height:1.5; }
.tag { background:#f5f8f5; color:#4b5d52 !important; padding:3px 8px; border-radius:8px; font-size:10px; font-weight:700; margin-right:4px; }

div.stButton > button { border-radius:12px !important; font-weight:700 !important; border:1px solid #b9d3c2; color:#17452f !important; background: #fff !important; }
div.stButton > button[kind="primary"] { background: linear-gradient(135deg, #237a57, #1a5f43) !important; color:#fff !important; border:none; }
div.stButton > button[kind="primary"] * { color: #fff !important; -webkit-text-fill-color: #fff !important; }
.custom-info { background:#f8faf8; border:1px dashed #b9d3c2; border-radius:10px; padding:16px; color:#4b5d52; text-align:center; font-size:14px; }
</style>""", unsafe_allow_html=True)

# ============ SIDEBAR (AI CONFIG) ============
with st.sidebar:
    st.markdown("### ⚙️ Cấu hình AI")
    if not OPENAI_AVAILABLE:
        st.error("⚠️ Chưa cài thư viện `openai`. Vui lòng thêm `openai` vào file `requirements.txt` (nếu dùng Cloud) hoặc chạy `pip install openai` (nếu dùng máy cá nhân).")
    
    use_ai = st.toggle("✨ Sử dụng AI (ChatGPT) để sáng tạo", value=False, disabled=not OPENAI_AVAILABLE)
    api_key = st.text_input("OpenAI API Key", type="password", help="Lấy key tại platform.openai.com")
    st.markdown("---")
    st.markdown("💡 **Mẹo:** Nếu không có API Key, hãy tắt AI để dùng danh sách công thức mẫu có sẵn.")

# ============ HERO & DATA MẪU ============
st.markdown("""<div class="hero">
<div class="eyebrow">✦ TRỢ LÝ NHÀ BẾP</div>
<h1>Trong tủ lạnh có gì?<br><span style="color:#237a57">Nấu món đó!</span></h1>
<p>Nhập nguyên liệu bạn đang có. Chúng tôi sẽ gợi ý món ăn, chỉ ra nguyên liệu còn thiếu và tính tiền mua thêm.</p>
</div>""", unsafe_allow_html=True)

STATIC_RECIPES = [
    {"name":"Trứng chiên cà chua","emoji":"🍳","time":12,"cost":8000,"cheap":True,"desc":"Món đơn giản, dễ ăn.","need":["Trứng","Cà chua","Hành lá"],"steps":"Đánh trứng. Xào cà chua cho mềm, đổ trứng vào chiên chín và thêm hành lá."},
    {"name":"Mì xào rau củ","emoji":"🍜","time":15,"cost":12000,"cheap":True,"desc":"Bữa ăn nhanh với mì và rau củ.","need":["Mì","Rau cải","Trứng","Hành lá"],"steps":"Trụng mì, xào rau, cho mì và gia vị vào đảo đều; thêm trứng nếu thích."},
    {"name":"Đậu phụ sốt cà chua","emoji":"🍅","time":18,"cost":10000,"cheap":True,"desc":"Món thanh đạm, chi phí thấp.","need":["Đậu phụ","Cà chua","Hành lá"],"steps":"Chiên sơ đậu phụ, nấu sốt cà chua rồi cho đậu vào rim thấm vị."},
    {"name":"Cơm chiên trứng","emoji":"🍚","time":10,"cost":7000,"cheap":True,"desc":"Tận dụng cơm nguội và trứng.","need":["Gạo","Trứng","Hành lá"],"steps":"Dùng cơm đã nấu chín để nguội, rang tơi với trứng và hành lá."},
    {"name":"Trứng luộc","emoji":"🥚","time":8,"cost":4000,"cheap":True,"desc":"Nhanh gọn, giàu protein.","need":["Trứng","Muối"],"steps":"Rửa trứng, luộc khoảng 7–10 phút."},
    {"name":"Thịt heo rang","emoji":"🥓","time":20,"cost":18000,"cheap":False,"desc":"Thịt rang đậm đà.","need":["Thịt heo","Hành lá","Nước mắm"],"steps":"Thái thịt, rang cho săn, nêm nước mắm rim đến khi thấm."}
]
PRICES = {"Trứng":3500, "Cà chua":5000, "Thịt heo":12000, "Rau cải":6000, "Đậu phụ":5000, "Mì":4000, "Gạo":5000, "Hành lá":2000, "Muối":500, "Tỏi":1000, "Dầu ăn":1000, "Nước mắm":1000, "Cà rốt":4000, "Bánh mì":5000, "Dưa leo":3000, "Khoai tây":6000, "Cá":15000}

# ============ HELPERS ============
def fmt(n): return f"{n:,}".replace(",", ".")
def get_diff(t): return "⭐ Dễ" if t <= 12 else ("⭐⭐ Vừa" if t <= 20 else "⭐⭐⭐ Khéo")
def get_tags(r):
    tags = []
    if r.get("cheap"): tags.append("💰 Tiết kiệm")
    if r.get("time", 99) <= 15: tags.append("⚡ Nhanh")
    if not any(m in r.get("need", []) for m in ["Thịt heo","Thịt gà","Cá","Bò"]): tags.append("🌱 Chay")
    return tags
def has_ing(item, ings): return any(item.casefold() in x.casefold() or x.casefold() in item.casefold() for x in ings)
def get_missing(r, ings): return [x for x in r["need"] if not has_ing(x, ings)]
def add_ings(val):
    for p in val.split(","):
        p = p.strip()
        if p and p.casefold() not in [x.casefold() for x in st.session_state.ingredients]:
            st.session_state.ingredients.append(p)

# ============ AI GENERATION FUNCTION ============
def generate_ai_recipes(ingredients, api_key):
    if not OPENAI_AVAILABLE:
        st.error("Thư viện openai chưa được cài đặt.")
        return []
    client = OpenAI(api_key=api_key)
    prompt = f"""Bạn là một đầu bếp chuyên nghiệp. Người dùng hiện có các nguyên liệu: {', '.join(ingredients)}.
Hãy gợi ý 3 món ăn ngon, dễ nấu từ những nguyên liệu này (có thể mua thêm tối đa 2 nguyên liệu phụ).
YÊU CẦU BẮT BUỘC: Chỉ trả về một mảng JSON hợp lệ (không có text giải thích, không có markdown ```json).
Cấu trúc mỗi object:
{{
  "name": "Tên món ăn",
  "emoji": "1 emoji đại diện",
  "time": 15,
  "cost": 10000,
  "cheap": true,
  "desc": "Mô tả ngắn",
  "need": ["Nguyên liệu 1", "Nguyên liệu 2"],
  "steps": "Bước 1. Bước 2. Bước 3."
}}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        content = response.choices[0].message.content.strip()
        content = re.sub(r'^```json', '', content)
        content = re.sub(r'^```', '', content)
        content = re.sub(r'```$', '', content).strip()
        return json.loads(content)
    except Exception as e:
        st.error(f"Lỗi AI: {e}")
        return []

# ============ STATE ============
if "ingredients" not in st.session_state: st.session_state.ingredients = []
if "selected_recipe" not in st.session_state: st.session_state.selected_recipe = None
if "ai_results" not in st.session_state: st.session_state.ai_results = []

# ============ LAYOUT ============
left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown('<div class="panel"><h3>🥕 Nguyên liệu của bạn</h3><p class="muted">Nhập nhiều nguyên liệu cách nhau bằng dấu phẩy.</p></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([3, 1])
    with c1: typed = st.text_input("Nhập", placeholder="Ví dụ: trứng, cà chua, hành lá...", label_visibility="collapsed")
    with c2:
        if st.button("＋ Thêm", type="primary", use_container_width=True):
            if typed.strip(): add_ings(typed); st.rerun()

    st.caption("⚡ Chọn nhanh:")
    qc = st.columns(4)
    for idx, item in enumerate(["Trứng", "Cà chua", "Thịt heo", "Rau cải", "Đậu phụ", "Mì", "Gạo", "Hành lá"]):
        with qc[idx % 4]:
            if st.button(item, key=f"q_{item}", use_container_width=True): add_ings(item); st.rerun()

    cnt = len(st.session_state.ingredients)
    ch, cc = st.columns([3, 1])
    with ch: st.markdown(f"**📦 Đang có ({cnt})**")
    with cc:
        if cnt > 0 and st.button("🗑️ Xóa hết", use_container_width=True): st.session_state.ingredients = []; st.rerun()

    if st.session_state.ingredients:
        for item in list(st.session_state.ingredients):
            ic1, ic2 = st.columns([5, 1])
            ic1.markdown(f'<div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:8px;color:#166534 !important;font-weight:600;font-size:14px">🟢 {item}</div>', unsafe_allow_html=True)
            if ic2.button("✕", key=f"rm_{item}"): st.session_state.ingredients.remove(item); st.rerun()
    else: 
        st.markdown('<div class="custom-info">Chưa có nguyên liệu nào.</div>', unsafe_allow_html=True)
    
    if use_ai:
        if st.button("✨ AI Sáng tạo món ăn ngay!", type="primary", use_container_width=True):
            if not api_key:
                st.warning("Vui lòng nhập API Key ở thanh bên trái.")
            elif not st.session_state.ingredients:
                st.warning("Hãy thêm nguyên liệu trước.")
            else:
                with st.spinner("Đầu bếp AI đang suy nghĩ..."):
                    st.session_state.ai_results = generate_ai_recipes(st.session_state.ingredients, api_key)
                    st.session_state.selected_recipe = None 

with right:
    st.markdown("""<div class="panel">
<h3>💡 LeftoverChef hoạt động thế nào?</h3>
<p class="muted">Bật AI ở thanh bên trái để tự động sinh ra công thức mới lạ từ nguyên liệu của bạn.</p>
<div style="background:linear-gradient(135deg,#f4f8f3,#eaf4ec);border-radius:13px;padding:16px;margin:12px 0">
<div style="font-size:28px">🤖</div><b style="color: #17251e !important;">Trí tuệ nhân tạo (AI)</b>
<p class="muted" style="margin:6px 0 0">Gợi ý món ăn bất ngờ, kết hợp nguyên liệu độc đáo mà bạn chưa từng nghĩ tới.</p></div>
</div>""", unsafe_allow_html=True)

# ============ LỌC KẾT QUẢ ============
if use_ai and st.session_state.ai_results:
    display_recipes = st.session_state.ai_results
else:
    display_recipes = STATIC_RECIPES
    if st.session_state.ingredients:
        display_recipes = [r for r in STATIC_RECIPES if len(get_missing(r, st.session_state.ingredients)) < len(r["need"])]
    display_recipes.sort(key=lambda x: len(get_missing(x, st.session_state.ingredients)))

st.markdown("## 🍳 Món ăn gợi ý")
if use_ai:
    st.markdown("<p style='color:#68796d !important;margin-top:-8px'>Công thức được tạo bởi AI dựa trên nguyên liệu của bạn.</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:#68796d !important;margin-top:-8px'>Sử dụng công thức mẫu có sẵn.</p>", unsafe_allow_html=True)

# ============ RENDER GRID & INLINE DETAILS ============
if display_recipes:
    for i in range(0, len(display_recipes), 3):
        row_data = display_recipes[i:i+3]
        cols = st.columns(3)
        
        for j, r in enumerate(row_data):
            miss = get_missing(r, st.session_state.ingredients)
            matched = len(r["need"]) - len(miss)
            pct = round(matched / len(r["need"]) * 100) if st.session_state.ingredients else 0
            is_perfect = pct == 100 and st.session_state.ingredients

            if not st.session_state.ingredients: b_text, b_class, c_class = "📖 Công thức", "match-badge", "recipe"
            elif is_perfect: b_text, b_class, c_class = "✨ Hoàn hảo!", "match-badge perfect-badge", "recipe perfect"
            else: b_text, b_class, c_class = f"♻️ {pct}% phù hợp", "match-badge", "recipe"

            tags_html = "".join([f'<span class="tag">{t}</span>' for t in get_tags(r)])
            
            with cols[j]:
                st.markdown(f'<div class="{c_class}"><div class="recipe-emoji">{r["emoji"]}</div><span class="{b_class}">{b_text}</span><div class="match-bar"><div class="match-bar-fill" style="width:{pct}%"></div></div><h4>{r["name"]}</h4><div class="muted">⏱️ {r["time"]} phút · 💰 ~{fmt(r["cost"])}đ · {get_diff(r["time"])}</div><p class="muted" style="margin-top:8px;flex:1">{r["desc"]}</p><div style="margin-top:8px">{tags_html}</div></div>', unsafe_allow_html=True)
                if st.button("Xem chi tiết →", key=f"b_{r['name']}", use_container_width=True):
                    st.session_state.selected_recipe = r
                    st.rerun()

        row_recipe_names = [r["name"] for r in row_data]
        sel = st.session_state.selected_recipe
        
        if sel and sel["name"] in row_recipe_names:
            st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)
            miss = get_missing(sel, st.session_state.ingredients)
            total = sum(PRICES.get(x, 5000) for x in miss)
            tags_html = "".join([f'<span class="tag">{t}</span>' for t in get_tags(sel)])
            
            st.markdown(f'<div style="background:linear-gradient(120deg,#eaf7ed,#fff8ec);border:1px solid #dce9dd;border-radius:22px;padding:26px;margin:8px 0 20px"><div style="font-size:52px">{sel["emoji"]}</div><h2 style="margin:8px 0">{sel["name"]}</h2><p style="color:#52675a !important;margin:6px 0">{sel["desc"]}</p><div style="margin-top:10px">{tags_html}</div><div style="margin-top:14px;font-weight:700;color:#237a57 !important;display:flex;gap:20px"><span>⏱️ {sel["time"]} phút</span><span>{get_diff(sel["time"])}</span><span>💰 Mua thêm: {fmt(total)}đ</span></div></div>', unsafe_allow_html=True)

            dl, dr = st.columns([1, 1.25], gap="large")
            with dl:
                st.markdown("### 🧺 Nguyên liệu")
                for item in sel["need"]:
                    if item in miss:
                        st.markdown(f'<div style="display:flex;justify-content:space-between;background:#fff7ed;border:1px solid #fed7aa;border-radius:10px;padding:10px;margin-bottom:8px"><span style="font-weight:600;color:#9a3412 !important;">🛒 {item}</span><span style="color:#c2410c !important;font-size:12px;font-weight:700">~{fmt(PRICES.get(item,5000))}đ</span></div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div style="display:flex;justify-content:space-between;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:10px;margin-bottom:8px"><span style="font-weight:600;color:#166534 !important;">✅ {item}</span><span style="color:#15803d !important;font-size:12px;font-weight:600">Đã có</span></div>', unsafe_allow_html=True)
                st.markdown("---")
                st.metric("Chi phí mua thêm", f"{fmt(total)}đ")

            with dr:
                st.markdown("### 👩‍🍳 Các bước thực hiện")
                for num, step in enumerate([p.strip() for p in sel["steps"].replace(";", ".").split(".") if p.strip()], 1):
                    st.markdown(f'<div style="display:flex;gap:12px;background:#fff;border:1px solid #e5ece5;border-radius:14px;padding:14px;margin-bottom:10px"><div style="min-width:32px;height:32px;border-radius:10px;background:linear-gradient(135deg,#e3f3e7,#d1ebd8);color:#237a57 !important;display:flex;align-items:center;justify-content:center;font-weight:800">{num}</div><div style="color:#34483b !important;padding-top:4px">{step}</div></div>', unsafe_allow_html=True)
            
            st.markdown("---")
else:
    st.markdown('<div class="custom-info">Chưa có món nào. Hãy bật AI và nhấn nút "Sáng tạo" hoặc thêm nguyên liệu.</div>', unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#718078 !important;font-size:12px;padding:25px'>LeftoverChef © 2026 - Powered by AI</div>", unsafe_allow_html=True)