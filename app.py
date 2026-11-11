import streamlit as st

st.set_page_config(
    page_title="LeftoverChef - Nấu ngon từ nguyên liệu sẵn có",
    page_icon="🥘",
    layout="wide"
)

# -------------------- GIAO DIỆN --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

/* Màu chữ mặc định: đậm và dễ đọc trên nền sáng */
html, body, [class*="css"], .stApp {
    font-family:'Be Vietnam Pro',sans-serif;
    color:#17251e !important;
}
.stApp {background:#fbfaf6;}
.block-container {max-width:1150px;padding-top:2rem;padding-bottom:3rem;}

/* Nội dung văn bản Streamlit */
.stMarkdown, .stMarkdown p, .stMarkdown li,
.stMarkdown span, .stMarkdown label,
[data-testid="stText"], [data-testid="stCaption"],
.stCaption, .stAlert, [data-testid="stAlert"] {
    color:#26352d !important;
}
h1, h2, h3, h4, h5, h6,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
.stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
    color:#183b2b !important;
}
label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
    color:#24382d !important;
    font-weight:600 !important;
}

/* Banner đầu trang */
.hero {
    background:linear-gradient(120deg,#edf7ef,#fff8eb);
    border:1px solid #d8e5dc;border-radius:24px;padding:34px 38px;
    margin-bottom:24px;
}
.eyebrow {color:#17613f !important;font-weight:800;font-size:12px;letter-spacing:1.5px;}
.hero h1 {font-size:clamp(32px,4vw,48px);line-height:1.12;color:#183b2b !important;margin:10px 0;}
.hero p {color:#40564a !important;font-size:15px;line-height:1.7;max-width:680px;}

/* Các khung nội dung và thẻ món ăn */
.panel {
    background:#ffffff;border:1px solid #dce7df;border-radius:18px;
    padding:22px;margin-bottom:18px;
}
.panel h3 {color:#183b2b !important;margin-top:0;}
.recipe {
    background:#ffffff;border:1px solid #dce7df;border-radius:16px;
    padding:17px;height:100%;margin-bottom:12px;
}
.recipe h4 {color:#183b2b !important;}
.recipe-emoji {font-size:42px;}
.match {
    display:inline-block;background:#e1f2e7;color:#155c3b !important;
    padding:5px 9px;border-radius:20px;font-size:11px;font-weight:800;
}
.muted {color:#4b5d52 !important;font-size:13px;line-height:1.55;}

/* Ô nhập liệu và các điều khiển */
input, textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
[data-baseweb="select"] input {
    color:#17251e !important;
    -webkit-text-fill-color:#17251e !important;
    background-color:#ffffff !important;
}
input::placeholder, textarea::placeholder {
    color:#718078 !important;
    -webkit-text-fill-color:#718078 !important;
    opacity:1 !important;
}
[data-baseweb="select"] > div {
    background:#ffffff !important;
    color:#17251e !important;
}
[data-baseweb="select"] span,
[data-baseweb="select"] div {
    color:#17251e !important;
}
.stCheckbox label, .stRadio label,
[data-testid="stCheckbox"] label p {
    color:#24382d !important;
}

/* Nút bấm */
div.stButton>button, div.stDownloadButton>button {
    border-radius:10px;font-weight:700;
    border:1px solid #b9d3c2;
    color:#17452f !important;
    background:#ffffff;
}
div.stButton>button[kind="primary"] {
    background:#237a57 !important;
    border-color:#237a57 !important;
    color:#ffffff !important;
}
div.stButton>button:hover, div.stDownloadButton>button:hover {
    border-color:#237a57 !important;
    color:#155c3b !important;
}

/* Khung thông báo và chỉ số */
div[data-testid="stMetric"] {
    background:#f0f6f1;padding:12px;border-radius:12px;
}
[data-testid="stMetricLabel"], [data-testid="stMetricValue"],
[data-testid="stMetricDelta"] {
    color:#183b2b !important;
}
[data-testid="stAlert"] p, [data-testid="stAlert"] div {
    color:#26352d !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">TRỢ LÝ NHÀ BẾP THÔNG MINH</div>
  <h1>Trong tủ lạnh có gì?<br><span style="color:#237a57">Nấu món đó!</span></h1>
  <p>Nhập những nguyên liệu bạn đang có. LeftoverChef gợi ý món ăn phù hợp,
  chỉ ra nguyên liệu còn thiếu và ước tính chi phí cần mua thêm.</p>
  <div style="font-size:42px">🥘 🥬 🍅</div>
</div>
""", unsafe_allow_html=True)

# -------------------- DỮ LIỆU MẪU --------------------
RECIPES = [
    {"name":"Trứng chiên cà chua","emoji":"🍳","time":12,"cost":8000,"cheap":True,
     "desc":"Món đơn giản, dễ ăn và tận dụng nguyên liệu quen thuộc.",
     "need":["Trứng","Cà chua","Hành lá"],
     "steps":"Đánh trứng. Xào cà chua cho mềm, đổ trứng vào chiên chín và thêm hành lá."},
    {"name":"Mì xào rau củ","emoji":"🍜","time":15,"cost":12000,"cheap":True,
     "desc":"Bữa ăn nhanh với mì và rau củ có sẵn trong bếp.",
     "need":["Mì","Rau cải","Trứng","Hành lá"],
     "steps":"Trụng mì, xào rau, cho mì và gia vị vào đảo đều; thêm trứng nếu thích."},
    {"name":"Đậu phụ sốt cà chua","emoji":"🍅","time":18,"cost":10000,"cheap":True,
     "desc":"Món ăn thanh đạm, nguyên liệu dễ tìm và chi phí thấp.",
     "need":["Đậu phụ","Cà chua","Hành lá"],
     "steps":"Chiên sơ đậu phụ, nấu sốt cà chua rồi cho đậu vào rim thấm vị."},
    {"name":"Thịt heo xào rau cải","emoji":"🥬","time":20,"cost":18000,"cheap":False,
     "desc":"Món mặn đủ chất, phù hợp cho bữa cơm gia đình.",
     "need":["Thịt heo","Rau cải","Hành lá"],
     "steps":"Thái thịt mỏng, xào săn rồi cho rau cải vào đảo nhanh trên lửa lớn."},
    {"name":"Cơm chiên trứng","emoji":"🍚","time":10,"cost":7000,"cheap":True,
     "desc":"Tận dụng cơm nguội và trứng để có bữa ăn tiết kiệm.",
     "need":["Gạo","Trứng","Hành lá"],
     "steps":"Dùng cơm đã nấu chín để nguội, rang tơi với trứng và hành lá."},
    {"name":"Canh cà chua đậu phụ","emoji":"🥣","time":16,"cost":9000,"cheap":True,
     "desc":"Món canh nhẹ nhàng, thích hợp dùng cùng cơm nóng.",
     "need":["Cà chua","Đậu phụ","Hành lá"],
     "steps":"Nấu cà chua với nước, cho đậu phụ vào đun nhẹ và nêm vừa ăn."}
]

PRICES = {
    "Trứng":3500, "Cà chua":5000, "Thịt heo":12000, "Rau cải":6000,
    "Đậu phụ":5000, "Mì":4000, "Gạo":5000, "Hành lá":2000
}

if "ingredients" not in st.session_state:
    st.session_state.ingredients = []
if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = None

def add_ingredient(value):
    value = value.strip()
    if value and value.casefold() not in [x.casefold() for x in st.session_state.ingredients]:
        st.session_state.ingredients.append(value)

def has_ingredient(item, ingredients):
    return any(item.casefold() in x.casefold() or x.casefold() in item.casefold()
               for x in ingredients)

def get_missing(recipe):
    return [x for x in recipe["need"] if not has_ingredient(x, st.session_state.ingredients)]

# -------------------- NHẬP NGUYÊN LIỆU --------------------
left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown('<div class="panel"><h3>🥕 Nguyên liệu của bạn</h3><p class="muted">Thêm nguyên liệu đang có trong tủ lạnh hoặc chọn nhanh bên dưới.</p></div>', unsafe_allow_html=True)
    typed = st.text_input("Nhập nguyên liệu", placeholder="Ví dụ: trứng, cà chua, thịt...")
    if st.button("＋ Thêm nguyên liệu", use_container_width=True):
        if typed.strip():
            add_ingredient(typed)
            st.rerun()

    st.caption("Chọn nhanh:")
    quick_items = ["Trứng","Cà chua","Thịt heo","Rau cải","Đậu phụ","Mì","Gạo","Hành lá"]
    quick_cols = st.columns(4)
    for idx, item in enumerate(quick_items):
        with quick_cols[idx % 4]:
            if st.button(item, key=f"quick_{item}", use_container_width=True):
                add_ingredient(item)
                st.rerun()

    st.markdown(f"**Đang có ({len(st.session_state.ingredients)})**")
    if st.session_state.ingredients:
        for item in list(st.session_state.ingredients):
            c1, c2 = st.columns([5,1])
            c1.markdown(f"🟢 {item}")
            if c2.button("✕", key=f"remove_{item}"):
                st.session_state.ingredients.remove(item)
                st.rerun()
    else:
        st.info("Chưa có nguyên liệu nào. Hãy thêm ít nhất một nguyên liệu.")

    fast_only = st.checkbox("Ưu tiên món dưới 20 phút")
    cheap_only = st.checkbox("Ưu tiên món tiết kiệm")
    find_clicked = st.button("✨ Gợi ý món ăn cho tôi", type="primary", use_container_width=True)

with right:
    st.markdown("""
    <div class="panel">
      <h3>💡 LeftoverChef hoạt động như thế nào?</h3>
      <p class="muted">Ứng dụng đối chiếu nguyên liệu bạn nhập với công thức mẫu để tìm món phù hợp.</p>
      <div style="background:#f4f8f3;border-radius:13px;padding:15px;margin:12px 0">
        <div style="font-size:28px">♻️</div><b>Ưu tiên tận dụng đồ sẵn có</b>
        <p class="muted">Gợi ý món có nhiều nguyên liệu trùng khớp nhất, hạn chế mua thêm không cần thiết.</p>
      </div>
      <div style="display:flex;gap:10px">
        <div style="background:#fff8eb;border-radius:12px;padding:13px;flex:1">
          <div style="font-size:24px">⏱️</div><b>Tiết kiệm thời gian</b>
          <p class="muted">Lọc món nhanh, dễ nấu.</p>
        </div>
        <div style="background:#edf5fb;border-radius:12px;padding:13px;flex:1">
          <div style="font-size:24px">💰</div><b>Kiểm soát chi phí</b>
          <p class="muted">Biết cần mua thêm gì.</p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.warning("Bản demo sử dụng công thức và giá nguyên liệu minh họa; chưa kết nối AI hoặc cửa hàng thực tế.")

# -------------------- GỢI Ý MÓN --------------------
if "results" not in st.session_state:
    st.session_state.results = RECIPES[:3]

if find_clicked:
    if not st.session_state.ingredients:
        st.warning("Hãy nhập ít nhất một nguyên liệu trước nhé.")
    else:
        results = []
        for recipe in RECIPES:
            matched = len(recipe["need"]) - len(get_missing(recipe))
            if matched:
                if fast_only and recipe["time"] > 20:
                    continue
                if cheap_only and not recipe["cheap"]:
                    continue
                results.append((matched / len(recipe["need"]), matched, recipe))
        results.sort(key=lambda x: (x[0], x[1]), reverse=True)
        st.session_state.results = [x[2] for x in results]

st.markdown("## 🍳 Món ăn gợi ý")
results = st.session_state.results
st.caption(f"Tìm thấy {len(results)} món ăn phù hợp" if st.session_state.ingredients else "Một số công thức mẫu để bạn trải nghiệm.")
if results:
    cols = st.columns(3)
    for idx, recipe in enumerate(results):
        matched = len(recipe["need"]) - len(get_missing(recipe))
        percent = round(matched / len(recipe["need"]) * 100) if st.session_state.ingredients else 0
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="recipe">
              <div class="recipe-emoji">{recipe['emoji']}</div>
              <span class="match">{percent}% nguyên liệu phù hợp</span>
              <h4 style="margin:12px 0 6px">{recipe['name']}</h4>
              <div class="muted">⏱️ {recipe['time']} phút &nbsp; · &nbsp; 🛒 ~{recipe['cost']:,}đ mua thêm</div>
              <p class="muted">{recipe['desc']}</p>
            </div>
            """.replace(",", "."), unsafe_allow_html=True)
            if st.button("Xem nguyên liệu & cách nấu", key=f"recipe_{recipe['name']}", use_container_width=True):
                st.session_state.selected_recipe = recipe
                st.rerun()
else:
    st.info("Chưa tìm thấy món phù hợp. Hãy thêm nguyên liệu khác hoặc bỏ bớt bộ lọc.")

# -------------------- DANH SÁCH MUA SẮM --------------------
st.markdown("## 🛒 Danh sách cần mua")
selected = st.session_state.selected_recipe
if selected:
    missing = get_missing(selected)
    total = sum(PRICES.get(x, 5000) for x in missing)
    st.markdown(f"### {selected['emoji']} {selected['name']}")
    st.write("**Cách làm:**", selected["steps"])
    if missing:
        st.write("**Nguyên liệu còn thiếu:**")
        for item in missing:
            st.write(f"- {item}: khoảng {PRICES.get(item,5000):,}đ".replace(",", "."))
    else:
        st.success("Bạn đã có đủ nguyên liệu cho món này!")
    st.metric("Chi phí mua thêm ước tính", f"{total:,}đ".replace(",", "."))
    shopping_text = "\\n".join([f"- {x}" for x in missing]) if missing else "Đã có đủ nguyên liệu."
    st.download_button("⬇️ Tải danh sách mua sắm (.txt)",
                       data=f"Danh sách mua cho món {selected['name']}\\n{shopping_text}",
                       file_name="danh_sach_mua_sam.txt", mime="text/plain")
else:
    st.info("Chọn “Xem nguyên liệu & cách nấu” ở một món ăn để tạo danh sách mua sắm.")

# -------------------- GIỚI THIỆU QUY TRÌNH --------------------
st.markdown("## Cách sử dụng")
c1, c2, c3 = st.columns(3)
c1.markdown('<div class="panel"><h3>1️⃣ Nhập nguyên liệu</h3><p class="muted">Liệt kê thực phẩm bạn đang có trong tủ lạnh.</p></div>', unsafe_allow_html=True)
c2.markdown('<div class="panel"><h3>2️⃣ Chọn món phù hợp</h3><p class="muted">Xem độ phù hợp, thời gian nấu và nguyên liệu còn thiếu.</p></div>', unsafe_allow_html=True)
c3.markdown('<div class="panel"><h3>3️⃣ Mua đúng thứ cần</h3><p class="muted">Tạo danh sách mua sắm và dự trù số tiền cần thiết.</p></div>', unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#718078;font-size:12px;padding:25px'>LeftoverChef © 2026 · Biến nguyên liệu còn lại thành bữa ăn mới.</div>", unsafe_allow_html=True)
