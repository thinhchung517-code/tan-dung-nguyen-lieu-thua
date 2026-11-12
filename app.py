import streamlit as st

st.set_page_config(
    page_title="LeftoverChef - Nấu ngon từ nguyên liệu sẵn có",
    page_icon="🥘",
    layout="wide"
)

# ============ CSS ============
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Be Vietnam Pro', sans-serif;
    color: #17251e !important;
}
.stApp {
    background:
        radial-gradient(circle at 5% 0%, rgba(224,245,226,.85), transparent 30%),
        radial-gradient(circle at 95% 5%, rgba(255,235,205,.7), transparent 28%),
        radial-gradient(circle at 50% 100%, rgba(230,245,255,.4), transparent 40%),
        #fbfaf6 !important;
}
.block-container { max-width: 1280px; padding-top: 1.6rem; padding-bottom: 3rem; }

.stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span, .stMarkdown label,
[data-testid="stText"], [data-testid="stCaption"], .stCaption, .stAlert, [data-testid="stAlert"] {
    color: #26352d !important;
}
h1,h2,h3,h4,h5,h6,.stMarkdown h1,.stMarkdown h2,.stMarkdown h3,
.stMarkdown h4,.stMarkdown h5,.stMarkdown h6 {
    color: #183b2b !important; font-weight: 800;
}
label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
    color: #24382d !important; font-weight: 600 !important;
}

.hero {
    position: relative; overflow: hidden;
    background: linear-gradient(135deg, #d5f0db 0%, #f8fff8 45%, #fff2df 100%);
    border: 1px solid #cfe4d4; border-radius: 28px;
    padding: clamp(28px, 4vw, 52px);
    box-shadow: 0 20px 50px -20px rgba(33,87,57,.15);
    margin-bottom: 28px;
}
.hero:before { content:""; position:absolute; inset:0;
    background: radial-gradient(circle at 80% 20%, rgba(255,255,255,.5), transparent 50%);
    pointer-events:none; }
.hero:after { content:"🍳"; position:absolute; right:4%; bottom:-30px;
    font-size: clamp(100px, 15vw, 200px); opacity:.1;
    transform: rotate(-10deg); pointer-events:none; }
.eyebrow { display:inline-block; color:#17613f !important; font-weight:800;
    font-size:12px; letter-spacing:1.8px; background:#c9e8d2;
    padding:8px 14px; border-radius:30px; position:relative; }
.hero h1 { font-size: clamp(32px,4.2vw,54px); line-height:1.08;
    color:#183b2b !important; margin:16px 0 12px;
    letter-spacing:-1.5px; font-weight:900; position:relative; }
.hero p { color:#40564a !important; font-size:16px; line-height:1.7;
    max-width:680px; position:relative; }

.panel {
    background:#ffffff; border:1px solid #e0e9e1; border-radius:20px;
    padding:22px; margin-bottom:18px;
    box-shadow: 0 8px 24px -12px rgba(27,65,43,.12);
}
.panel h3 { color:#183b2b !important; margin-top:0; font-weight:800; }

.recipe {
    position: relative; background:#ffffff;
    border: 1.5px solid #e2e9e2; border-radius:20px;
    padding:20px; box-shadow: 0 8px 24px -12px rgba(28,65,43,.12);
    transition: all .25s ease; min-height: 340px;
    overflow: hidden; display: flex; flex-direction: column;
}
.recipe:hover { transform: translateY(-6px);
    box-shadow: 0 20px 40px -12px rgba(28,65,43,.22);
    border-color:#a9d2b5; }
.recipe.perfect { border-color:#86efac;
    background: linear-gradient(180deg, #f0fdf4, #ffffff 60%); }
.recipe-emoji { display:flex; align-items:center; justify-content:center;
    width:72px; height:72px; border-radius:20px;
    background: linear-gradient(145deg, #e8f5e8, #fff4e4);
    font-size:40px; margin-bottom:14px; }
.match-badge { display:inline-flex; align-items:center; gap:4px;
    background:#e1f2e7; color:#155c3b !important;
    padding:5px 10px; border-radius:20px; font-size:11px;
    font-weight:800; letter-spacing:.2px; }
.match-badge.perfect-badge {
    background: linear-gradient(90deg,#fde68a,#fbbf24); color:#78350f !important; }
.match-bar { height:6px; background:#eef4ee; border-radius:3px;
    overflow:hidden; margin:10px 0 4px; }
.match-bar-fill { height:100%;
    background: linear-gradient(90deg,#3fa66b,#1f7a4d);
    border-radius:3px; transition: width .3s ease; }
.recipe h4 { color:#183b2b !important; margin:12px 0 8px;
    font-size:18px; font-weight:700; line-height:1.3; }
.muted { color:#4b5d52 !important; font-size:13px; line-height:1.55; }
.tag { display:inline-block; background:#f5f8f5; color:#4b5d52;
    padding:3px 8px; border-radius:8px; font-size:10px;
    font-weight:700; margin-right:4px; margin-top:4px; }

input, textarea, [data-baseweb="input"] input, [data-baseweb="textarea"] textarea,
[data-baseweb="select"] input {
    color:#17251e !important; -webkit-text-fill-color:#17251e !important;
    background-color:#ffffff !important; }
input::placeholder, textarea::placeholder {
    color:#718078 !important; -webkit-text-fill-color:#718078 !important;
    opacity:1 !important; }
[data-baseweb="select"] > div { background:#ffffff !important; color:#17251e !important; }
[data-baseweb="select"] span, [data-baseweb="select"] div { color:#17251e !important; }
.stCheckbox label, .stRadio label, [data-testid="stCheckbox"] label p {
    color:#24382d !important; }

div.stButton > button, div.stDownloadButton > button {
    border-radius:12px !important; padding:.62rem 1rem !important;
    transition: all .18s ease !important; font-weight:700 !important;
    border:1px solid #b9d3c2; color:#17452f !important; background:#ffffff; }
div.stButton > button:hover, div.stDownloadButton > button:hover {
    border-color:#237a57 !important; color:#155c3b !important;
    transform: translateY(-1px); }
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #237a57, #1a5f43) !important;
    border-color:#237a57 !important; color:#ffffff !important;
    box-shadow: 0 6px 14px rgba(35,122,87,.22); }

div[data-testid="stMetric"] {
    background:#f4f8f4; padding:12px; border-radius:14px;
    border:1px solid #e0e9e1; }
[data-testid="stMetricLabel"], [data-testid="stMetricValue"],
[data-testid="stMetricDelta"] { color:#183b2b !important; }
[data-testid="stExpander"] {
    border-radius:14px !important; border-color:#e0e9e1 !important; }
hr { border-color:#e5ebe5 !important; }

@media (max-width: 700px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .hero { border-radius: 20px; }
}
</style>
""", unsafe_allow_html=True)

# ============ HERO ============
st.markdown("""
<div class="hero">
  <div class="eyebrow">✦ TRỢ LÝ NHÀ BẾP THÔNG MINH</div>
  <h1>Trong tủ lạnh có gì?<br><span style="color:#237a57">Nấu món đó!</span></h1>
  <p>Nhập những nguyên liệu bạn đang có. LeftoverChef gợi ý món ăn phù hợp,
  chỉ ra nguyên liệu còn thiếu và ước tính chi phí cần mua thêm — tất cả trong vài giây.</p>
  <div style="font-size:42px;margin-top:8px;position:relative">🥘 🥬 🍅</div>
</div>
""", unsafe_allow_html=True)

# ============ DATA ============
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
     "steps":"Nấu cà chua với nước, cho đậu phụ vào đun nhẹ và nêm vừa ăn."},
    {"name":"Trứng luộc","emoji":"🥚","time":8,"cost":4000,"cheap":True,
     "desc":"Món đơn giản, nhanh gọn và giàu protein.",
     "need":["Trứng","Muối"],
     "steps":"Rửa trứng, cho vào nồi nước ngập trứng và luộc khoảng 7–10 phút tùy độ chín mong muốn."},
    {"name":"Trứng sốt cà chua","emoji":"🍅","time":15,"cost":9000,"cheap":True,
     "desc":"Trứng mềm kết hợp sốt cà chua chua ngọt, rất đưa cơm.",
     "need":["Trứng","Cà chua","Hành lá"],
     "steps":"Chiên sơ trứng, xào cà chua với gia vị rồi cho trứng vào rim vài phút và thêm hành lá."},
    {"name":"Trứng hấp","emoji":"🍮","time":20,"cost":7000,"cheap":True,
     "desc":"Món trứng mềm mịn, dễ ăn và dễ thực hiện.",
     "need":["Trứng","Hành lá","Nước mắm"],
     "steps":"Đánh trứng với nước và gia vị, lọc qua rây rồi hấp nhỏ lửa đến khi trứng đông mềm."},
    {"name":"Rau cải xào tỏi","emoji":"🥬","time":10,"cost":7000,"cheap":True,
     "desc":"Món rau xanh thanh nhẹ, phù hợp với mọi bữa cơm.",
     "need":["Rau cải","Tỏi","Dầu ăn"],
     "steps":"Phi thơm tỏi, cho rau cải vào xào trên lửa lớn, nêm gia vị vừa ăn."},
    {"name":"Rau muống xào tỏi","emoji":"🌿","time":12,"cost":8000,"cheap":True,
     "desc":"Món rau quen thuộc, giòn ngon và tiết kiệm.",
     "need":["Rau muống","Tỏi","Dầu ăn"],
     "steps":"Nhặt và rửa rau muống, phi thơm tỏi rồi cho rau vào xào nhanh trên lửa lớn."},
    {"name":"Đậu phụ chiên giòn","emoji":"🧈","time":12,"cost":8000,"cheap":True,
     "desc":"Đậu phụ vàng giòn bên ngoài, mềm bên trong.",
     "need":["Đậu phụ","Dầu ăn","Nước mắm"],
     "steps":"Cắt đậu thành miếng vừa ăn, thấm khô rồi chiên vàng đều các mặt."},
    {"name":"Đậu phụ sốt hành","emoji":"🍲","time":15,"cost":9000,"cheap":True,
     "desc":"Đậu phụ mềm thấm vị, ăn cùng cơm nóng rất hợp.",
     "need":["Đậu phụ","Hành lá","Nước mắm"],
     "steps":"Chiên sơ đậu phụ, pha nước mắm với chút nước và gia vị, rim đậu rồi rắc hành lá."},
    {"name":"Mì trứng","emoji":"🍜","time":10,"cost":7000,"cheap":True,
     "desc":"Bữa ăn nhanh với những nguyên liệu dễ tìm.",
     "need":["Mì","Trứng","Hành lá"],
     "steps":"Nấu mì theo hướng dẫn, cho trứng vào nấu chín và thêm hành lá."},
    {"name":"Mì xào trứng","emoji":"🍝","time":12,"cost":8000,"cheap":True,
     "desc":"Mì dai xào cùng trứng, thích hợp cho bữa ăn nhanh.",
     "need":["Mì","Trứng","Rau cải"],
     "steps":"Trụng mì vừa mềm, xào rau cải rồi cho mì và trứng vào đảo đều với gia vị."},
    {"name":"Cơm chiên rau củ","emoji":"🍚","time":15,"cost":10000,"cheap":True,
     "desc":"Tận dụng cơm nguội và rau củ còn lại trong tủ lạnh.",
     "need":["Gạo","Trứng","Rau cải","Cà rốt"],
     "steps":"Dùng cơm đã nấu chín, xào rau củ, thêm trứng và cơm rồi rang tơi."},
    {"name":"Canh rau cải","emoji":"🥬","time":15,"cost":8000,"cheap":True,
     "desc":"Món canh thanh mát, dễ nấu cho bữa cơm gia đình.",
     "need":["Rau cải","Hành lá","Thịt heo"],
     "steps":"Đun sôi nước, cho thịt heo đã thái mỏng vào nấu chín, thêm rau cải và nêm gia vị."},
    {"name":"Canh trứng cà chua","emoji":"🥣","time":12,"cost":7000,"cheap":True,
     "desc":"Món canh nóng dễ nấu với vị chua nhẹ.",
     "need":["Trứng","Cà chua","Hành lá"],
     "steps":"Xào cà chua mềm, thêm nước đun sôi, từ từ đổ trứng đã đánh vào rồi khuấy nhẹ."},
    {"name":"Thịt heo rang","emoji":"🥓","time":20,"cost":18000,"cheap":False,
     "desc":"Thịt heo rang đậm đà, ăn cùng cơm nóng.",
     "need":["Thịt heo","Hành lá","Nước mắm"],
     "steps":"Thái thịt vừa ăn, rang cho săn và ra bớt mỡ, nêm nước mắm cùng gia vị rồi rim đến khi thấm."},
    {"name":"Thịt heo xào cà chua","emoji":"🍅","time":18,"cost":18000,"cheap":False,
     "desc":"Thịt mềm kết hợp cà chua tạo vị chua ngọt dễ ăn.",
     "need":["Thịt heo","Cà chua","Hành lá"],
     "steps":"Xào thịt heo cho săn, thêm cà chua và gia vị, đảo đến khi cà chua mềm và thịt chín."},
    {"name":"Thịt heo xào rau củ","emoji":"🥘","time":20,"cost":20000,"cheap":False,
     "desc":"Món xào nhiều màu sắc, kết hợp thịt và rau củ.",
     "need":["Thịt heo","Rau cải","Cà rốt"],
     "steps":"Xào thịt heo gần chín, cho cà rốt và rau cải vào đảo nhanh, nêm vừa ăn."},
    {"name":"Bánh mì trứng","emoji":"🥖","time":10,"cost":10000,"cheap":True,
     "desc":"Bữa sáng tiện lợi, nhanh chóng và no bụng.",
     "need":["Bánh mì","Trứng","Dưa leo"],
     "steps":"Chiên trứng, kẹp vào bánh mì cùng dưa leo và thêm gia vị hoặc nước sốt tùy thích."},
    {"name":"Khoai tây chiên","emoji":"🍟","time":20,"cost":12000,"cheap":True,
     "desc":"Món ăn vặt giòn thơm, dễ làm tại nhà.",
     "need":["Khoai tây","Dầu ăn","Muối"],
     "steps":"Gọt vỏ khoai tây, cắt que, ngâm nước rồi thấm khô và chiên vàng."},
    {"name":"Salad dưa leo cà chua","emoji":"🥗","time":10,"cost":9000,"cheap":True,
     "desc":"Món rau trộn tươi mát, không cần nấu lâu.",
     "need":["Dưa leo","Cà chua","Xà lách"],
     "steps":"Rửa sạch rau củ, cắt miếng vừa ăn rồi trộn với nước sốt nhẹ."},
    {"name":"Canh khoai tây cà rốt","emoji":"🥕","time":25,"cost":14000,"cheap":True,
     "desc":"Món canh rau củ ngọt tự nhiên, dễ ăn.",
     "need":["Khoai tây","Cà rốt","Hành lá"],
     "steps":"Gọt vỏ và cắt nhỏ khoai tây, cà rốt, nấu đến khi mềm rồi nêm gia vị và thêm hành lá."},
    {"name":"Cá sốt cà chua","emoji":"🐟","time":25,"cost":22000,"cheap":False,
     "desc":"Cá thấm sốt cà chua đậm đà, dùng với cơm nóng.",
     "need":["Cá","Cà chua","Hành lá"],
     "steps":"Chiên sơ cá, nấu cà chua thành sốt rồi cho cá vào rim nhỏ lửa đến khi thấm."},
    {"name":"Gà xào sả","emoji":"🍗","time":25,"cost":22000,"cheap":False,
     "desc":"Thịt gà thơm mùi sả, thích hợp cho bữa cơm gia đình.",
     "need":["Thịt gà","Sả","Hành lá"],
     "steps":"Ướp gà với gia vị và sả băm, xào săn rồi thêm chút nước và rim đến khi gà chín."},
    {"name":"Bắp cải xào trứng","emoji":"🥬","time":15,"cost":10000,"cheap":True,
     "desc":"Món xào đơn giản, kết hợp rau xanh và trứng.",
     "need":["Bắp cải","Trứng","Hành lá"],
     "steps":"Thái bắp cải, xào mềm vừa tới rồi cho trứng vào đảo đều, nêm gia vị."},
    {"name":"Cháo trứng","emoji":"🥣","time":25,"cost":9000,"cheap":True,
     "desc":"Món cháo nóng mềm, nhẹ bụng và tiết kiệm.",
     "need":["Gạo","Trứng","Hành lá"],
     "steps":"Nấu gạo với nhiều nước đến khi nở mềm, đập trứng vào khuấy đều và nêm gia vị."},
    {"name":"Cà tím xào tỏi","emoji":"🍆","time":15,"cost":10000,"cheap":True,
     "desc":"Cà tím mềm thơm, chế biến nhanh cho bữa cơm.",
     "need":["Cà tím","Tỏi","Dầu ăn"],
     "steps":"Cắt cà tím thành miếng, phi thơm tỏi rồi xào cà tím đến khi mềm, nêm vừa ăn."}
]

PRICES = {
    "Trứng":3500, "Cà chua":5000, "Thịt heo":12000, "Rau cải":6000,
    "Đậu phụ":5000, "Mì":4000, "Gạo":5000, "Hành lá":2000,
    "Muối":500, "Tỏi":1000, "Dầu ăn":1000, "Nước mắm":1000,
    "Rau muống":6000, "Cà rốt":4000, "Bánh mì":5000, "Dưa leo":3000,
    "Khoai tây":6000, "Xà lách":5000, "Cá":15000, "Thịt gà":15000,
    "Sả":2000, "Bắp cải":5000, "Cà tím":6000
}

# ============ HELPERS ============
def fmt_price(n):
    return f"{n:,}".replace(",", ".")

def get_difficulty(time_min):
    if time_min <= 12:
        return "⭐ Dễ"
    if time_min <= 20:
        return "⭐⭐ Vừa"
    return "⭐⭐⭐ Khéo"

def get_tags(recipe):
    tags = []
    if recipe["cheap"]:
        tags.append("💰 Tiết kiệm")
    if recipe["time"] <= 15:
        tags.append("⚡ Nhanh")
    meats = {"Thịt heo", "Thịt gà", "Cá"}
    if not any(m in recipe["need"] for m in meats):
        tags.append("🌱 Chay")
    return tags

def has_ingredient(item, ingredients):
    return any(item.casefold() in x.casefold() or x.casefold() in item.casefold()
               for x in ingredients)

def get_missing(recipe):
    return [x for x in recipe["need"] if not has_ingredient(x, st.session_state.ingredients)]

def add_ingredients(value):
    for part in value.split(","):
        part = part.strip()
        if part and part.casefold() not in [x.casefold() for x in st.session_state.ingredients]:
            st.session_state.ingredients.append(part)

def compute_results(fast_only, cheap_only, sort_by):
    results = []
    for recipe in RECIPES:
        matched = len(recipe["need"]) - len(get_missing(recipe))
        if st.session_state.ingredients and matched == 0:
            continue
        if fast_only and recipe["time"] > 20:
            continue
        if cheap_only and not recipe["cheap"]:
            continue
        ratio = matched / len(recipe["need"]) if st.session_state.ingredients else 0
        results.append({"recipe": recipe, "matched": matched, "ratio": ratio})

    if sort_by == "Phù hợp nhất":
        results.sort(key=lambda x: (x["ratio"], x["matched"]), reverse=True)
    elif sort_by == "Nhanh nhất":
        results.sort(key=lambda x: x["recipe"]["time"])
    elif sort_by == "Rẻ nhất":
        results.sort(key=lambda x: x["recipe"]["cost"])
    return results

# ============ SESSION STATE ============
if "ingredients" not in st.session_state:
    st.session_state.ingredients = []
if "selected_recipe" not in st.session_state:
    st.session_state.selected_recipe = None

# ============ LAYOUT ============
left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown(
        '<div class="panel"><h3>🥕 Nguyên liệu của bạn</h3>'
        '<p class="muted">Thêm nguyên liệu trong tủ lạnh — có thể nhập nhiều nguyên liệu cách nhau bằng dấu phẩy.</p></div>',
        unsafe_allow_html=True)

    c_input, c_add = st.columns([3, 1])
    with c_input:
        typed = st.text_input("Nhập nguyên liệu",
                              placeholder="Ví dụ: trứng, cà chua, hành lá...",
                              label_visibility="collapsed")
    with c_add:
        if st.button("＋ Thêm", type="primary", use_container_width=True):
            if typed.strip():
                add_ingredients(typed)
                st.rerun()

    st.caption("⚡ Chọn nhanh:")
    quick_items = ["Trứng", "Cà chua", "Thịt heo", "Rau cải",
                   "Đậu phụ", "Mì", "Gạo", "Hành lá"]
    quick_cols = st.columns(4)
    for idx, item in enumerate(quick_items):
        with quick_cols[idx % 4]:
            if st.button(item, key=f"quick_{item}", use_container_width=True):
                add_ingredients(item)
                st.rerun()

    ing_count = len(st.session_state.ingredients)
    c_head, c_clear = st.columns([3, 1])
    with c_head:
        st.markdown(f"**📦 Đang có ({ing_count})**")
    with c_clear:
        if ing_count > 0 and st.button("🗑️ Xóa hết", use_container_width=True):
            st.session_state.ingredients = []
            st.rerun()

    if st.session_state.ingredients:
        for item in list(st.session_state.ingredients):
            c1, c2 = st.columns([5, 1])
            c1.markdown(
                f'<div style="background:#f0fdf4;border:1px solid #bbf7d0;'
                f'border-radius:10px;padding:8px 12px;color:#166534;'
                f'font-weight:600;font-size:14px">🟢 {item}</div>',
                unsafe_allow_html=True)
            if c2.button("✕", key=f"remove_{item}"):
                st.session_state.ingredients.remove(item)
                st.rerun()
    else:
        st.info("Chưa có nguyên liệu nào. Hãy thêm ít nhất một nguyên liệu để bắt đầu.")

    st.markdown("---")
    st.markdown("**🎛️ Bộ lọc & sắp xếp**")
    fc1, fc2 = st.columns(2)
    with fc1:
        fast_only = st.checkbox("⚡ Món dưới 20 phút")
    with fc2:
        cheap_only = st.checkbox("💰 Món tiết kiệm")
    sort_by = st.radio("Sắp xếp theo",
                       ["Phù hợp nhất", "Nhanh nhất", "Rẻ nhất"],
                       horizontal=True)

with right:
    st.markdown("""
    <div class="panel">
      <h3>💡 LeftoverChef hoạt động như thế nào?</h3>
      <p class="muted">Ứng dụng đối chiếu nguyên liệu bạn nhập với công thức mẫu để tìm món phù hợp.</p>
      <div style="background:linear-gradient(135deg,#f4f8f3,#eaf4ec);border-radius:13px;padding:16px;margin:12px 0">
        <div style="font-size:28px">♻️</div><b>Ưu tiên tận dụng đồ sẵn có</b>
        <p class="muted" style="margin:6px 0 0">Gợi ý món có nhiều nguyên liệu trùng khớp nhất, hạn chế mua thêm không cần thiết.</p>
      </div>
      <div style="display:flex;gap:10px">
        <div style="background:#fff8eb;border-radius:12px;padding:14px;flex:1">
          <div style="font-size:24px">⏱️</div><b>Tiết kiệm thời gian</b>
          <p class="muted" style="margin:6px 0 0">Lọc món nhanh, dễ nấu.</p>
        </div>
        <div style="background:#edf5fb;border-radius:12px;padding:14px;flex:1">
          <div style="font-size:24px">💰</div><b>Kiểm soát chi phí</b>
          <p class="muted" style="margin:6px 0 0">Biết cần mua thêm gì.</p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.warning("📝 Bản demo sử dụng công thức và giá nguyên liệu minh họa; chưa kết nối AI hoặc cửa hàng thực tế.")

# ============ KẾT QUẢ ============
results = compute_results(fast_only, cheap_only, sort_by)
if not st.session_state.ingredients:
    results = results[:6]

st.markdown("## 🍳 Món ăn gợi ý")
if st.session_state.ingredients:
    st.markdown(
        f"<p style='color:#68796d;margin-top:-8px'>Tìm thấy <b>{len(results)}</b> món phù hợp "
        f"với <b>{len(st.session_state.ingredients)}</b> nguyên liệu bạn có. Chọn một món để xem chi tiết.</