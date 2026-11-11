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

html, body, [class*="css"], .stApp {
    font-family:'Be Vietnam Pro',sans-serif;
    color:#17251e !important;
}
.stApp {
    background:
      radial-gradient(1200px 600px at 10% -10%, #e8f5ec 0%, transparent 60%),
      radial-gradient(900px 500px at 100% 0%, #fff3d6 0%, transparent 55%),
      #fbfaf6;
}
.block-container {max-width:1180px;padding-top:2rem;padding-bottom:3rem;}

.stMarkdown, .stMarkdown p, .stMarkdown li,
.stMarkdown span, .stMarkdown label,
[data-testid="stText"], [data-testid="stCaption"],
.stCaption, .stAlert, [data-testid="stAlert"] { color:#26352d !important; }
h1, h2, h3, h4, h5, h6,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
.stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
    color:#183b2b !important; letter-spacing:-0.3px;
}
label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
    color:#24382d !important; font-weight:600 !important;
}

/* HERO */
.hero {
    position:relative;overflow:hidden;
    background:linear-gradient(120deg,#eaf7ee 0%,#fff8eb 60%,#fff2e8 100%);
    border:1px solid #d8e5dc;border-radius:28px;padding:38px 42px;
    margin-bottom:26px; box-shadow:0 20px 40px -20px rgba(35,122,87,.25);
}
.hero::after{
    content:"🥬";position:absolute;right:-10px;top:-10px;
    font-size:160px;opacity:.08;transform:rotate(-15deg);
}
.hero .eyebrow {
    color:#17613f !important;font-weight:800;font-size:12px;letter-spacing:2px;
    display:inline-block;background:#dff1e6;padding:6px 12px;border-radius:20px;
}
.hero h1 {font-size:clamp(30px,4vw,50px);line-height:1.1;color:#183b2b !important;margin:16px 0 12px;}
.hero p {color:#40564a !important;font-size:15.5px;line-height:1.7;max-width:680px;}
.hero .hero-emoji{font-size:34px;letter-spacing:6px;margin-top:8px}

/* PANEL */
.panel {
    background:#ffffff;border:1px solid #e3ece6;border-radius:20px;
    padding:22px;margin-bottom:18px;
    box-shadow:0 8px 24px -16px rgba(24,59,43,.25);
}
.panel h3 {color:#183b2b !important;margin-top:0;font-size:17px;}
.muted {color:#4b5d52 !important;font-size:13px;line-height:1.6;}

/* RECIPE CARD */
.recipe {
    position:relative;
    background:linear-gradient(180deg,#ffffff 0%,#fbfdfb 100%);
    border:1px solid #e3ece6;border-radius:20px;
    padding:20px 18px 16px;height:100%;margin-bottom:10px;
    transition:transform .25s ease, box-shadow .25s ease, border-color .25s ease;
    box-shadow:0 6px 18px -14px rgba(24,59,43,.3);
}
.recipe:hover{
    transform:translateY(-4px);
    box-shadow:0 18px 32px -18px rgba(35,122,87,.45);
    border-color:#b9d3c2;
}
.recipe-emoji {
    font-size:46px;line-height:1;
    display:inline-flex;align-items:center;justify-content:center;
    width:64px;height:64px;border-radius:16px;background:#f0f7f2;
}
.recipe h4 {color:#183b2b !important;font-size:16.5px;margin:12px 0 8px;line-height:1.3;}
.chip-row{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 10px;}
.chip{
    display:inline-flex;align-items:center;gap:4px;
    padding:4px 9px;border-radius:20px;font-size:11px;font-weight:700;
    background:#f3f6f4;color:#3d5145 !important;
}
.chip.time{background:#eef5fb;color:#1b5e8c !important;}
.chip.cost{background:#fff4e0;color:#8a5a00 !important;}
.chip.cheap{background:#e6f6ec;color:#1a6b41 !important;}
.match-bar{height:6px;border-radius:99px;background:#eef2ef;overflow:hidden;margin:6px 0 4px;}
.match-bar > span{
    display:block;height:100%;border-radius:99px;
    background:linear-gradient(90deg,#4fae7c,#237a57);
    transition:width .6s ease;
}
.match-label{font-size:11px;font-weight:800;color:#155c3b !important;}
.ing-row{display:flex;flex-wrap:wrap;gap:5px;margin-top:8px;}
.ing{font-size:10.5px;font-weight:700;padding:3px 8px;border-radius:8px;border:1px solid transparent;}
.ing.have{background:#e6f6ec;color:#1a6b41 !important;border-color:#c9e8d5;}
.ing.miss{background:#fdecec;color:#a33a3a !important;border-color:#f3cccc;}

/* INPUTS & BUTTONS */
input, textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
[data-baseweb="select"] input {
    color:#17251e !important;-webkit-text-fill-color:#17251e !important;background-color:#ffffff !important;
}
input::placeholder, textarea::placeholder {
    color:#718078 !important;-webkit-text-fill-color:#718078 !important;opacity:1 !important;
}
div.stButton>button, div.stDownloadButton>button {
    border-radius:12px;font-weight:700;border:1px solid #b9d3c2;
    color:#17452f !important;background:#ffffff;transition:all .2s ease;
}
div.stButton>button:hover, div.stDownloadButton>button:hover {
    border-color:#237a57 !important;color:#155c3b !important;
    background:#f4faf6 !important;transform:translateY(-1px);
}
div.stButton>button[kind="primary"] {
    background:linear-gradient(135deg,#2f9469,#237a57) !important;
    border-color:transparent !important;color:#ffffff !important;
    box-shadow:0 8px 20px -8px rgba(35,122,87,.6);
}
div[data-testid="stMetric"] {
    background:linear-gradient(135deg,#f0f6f1,#e9f4ec);
    padding:14px 16px;border-radius:14px;border:1px solid #dcebe1;
}
[data-testid="stMetricLabel"]{color:#3d5145 !important;font-size:12px !important;font-weight:700 !important;}
[data-testid="stMetricValue"]{color:#155c3b !important;font-size:26px !important;font-weight:800 !important;}
div[role="dialog"]{border-radius:24px !important;box-shadow:0 40px 80px -30px rgba(0,0,0,.4) !important;}
div[role="dialog"] h2{color:#183b2b !important;}

/* STEPS */
.step-item{
    display:flex;gap:12px;padding:12px 14px;border-radius:12px;
    background:#f7faf8;border:1px solid #e7efe9;margin-bottom:8px;
}
.step-num{
    flex-shrink:0;width:26px;height:26px;border-radius:50%;
    background:#237a57;color:#fff !important;font-weight:800;font-size:13px;
    display:flex;align-items:center;justify-content:center;
}
.step-text{color:#2b3a31 !important;font-size:14px;line-height:1.6;}

/* EMPTY STATE */
.empty-state{
    text-align:center;padding:60px 20px;background:#ffffff;
    border:2px dashed #d8e5dc;border-radius:20px;
}
.empty-state .big{font-size:64px;margin-bottom:12px;}
.empty-state h3{color:#183b2b !important;margin:0 0 8px;}
.empty-state p{color:#718078 !important;font-size:14px;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <span class="eyebrow">✨ TRỢ LÝ NHÀ BẾP THÔNG MINH</span>
  <h1>Trong tủ lạnh có gì?<br><span style="color:#237a57">Nấu món đó!</span></h1>
  <p>Nhập nguyên liệu bạn đang có. LeftoverChef gợi ý món ăn phù hợp, chỉ ra nguyên liệu còn thiếu
  và ước tính chi phí cần mua thêm — nhanh, gọn, tiết kiệm.</p>
  <div class="hero-emoji">🥘 🥬 🍅 🍳</div>
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

# -------------------- STATE --------------------
if "ingredients" not in st.session_state:
    st.session_state.ingredients = []
if "results" not in st.session_state:
    st.session_state.results = RECIPES[:3]

def add_ingredient(value):
    value = value.strip()
    if value and value.casefold() not in [x.casefold() for x in st.session_state.ingredients]:
        st.session_state.ingredients.append(value)

def has_ingredient(item, ingredients):
    return any(item.casefold() in x.casefold() or x.casefold() in item.casefold()
               for x in ingredients)

def get_missing(recipe):
    return [x for x in recipe["need"] if not has_ingredient(x, st.session_state.ingredients)]

def money(n):
    return f"{n:,}".replace(",", ".") + "đ"

# -------------------- MODAL CÁCH NẤU --------------------
@st.dialog("🍳 Cách nấu món ăn", width="large")
def show_recipe_dialog(recipe):
    missing = get_missing(recipe)
    matched = len(recipe["need"]) - len(missing)
    percent = round(matched / len(recipe["need"]) * 100)

    c1, c2 = st.columns([1, 3])
    with c1:
        st.markdown(f"<div style='font-size:72px;text-align:center;background:#f0f7f2;border-radius:18px;padding:10px'>{recipe['emoji']}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"### {recipe['name']}")
        st.markdown(f"<div class='muted'>{recipe['desc']}</div>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='chip-row' style='margin-top:8px'>"
            f"<span class='chip time'>⏱️ {recipe['time']} phút</span>"
            f"<span class='chip cost'>🛒 ~{money(recipe['cost'])}</span>"
            f"{'<span class=\"chip cheap\">💚 Tiết kiệm</span>' if recipe['cheap'] else ''}"
            f"</div>",
            unsafe_allow_html=True
        )

    st.markdown("---")

    if st.session_state.ingredients:
        st.markdown(
            f"<div class='match-label'>Độ phù hợp: {percent}% ({matched}/{len(recipe['need'])} nguyên liệu)</div>"
            f"<div class='match-bar'><span style='width:{percent}%'></span></div>",
            unsafe_allow_html=True
        )
        st.write("")

    st.markdown("#### 🧺 Nguyên liệu")
    ing_html = "<div class='ing-row'>"
    for ing in recipe["need"]:
        if has_ingredient(ing, st.session_state.ingredients):
            ing_html += f"<span class='ing have'>✓ {ing}</span>"
        else:
            ing_html += f"<span class='ing miss'>✗ {ing}</span>"
    ing_html += "</div>"
    st.markdown(ing_html, unsafe_allow_html=True)

    st.write("")
    st.markdown("#### 👨‍🍳 Các bước thực hiện")
    steps = [s.strip() for s in recipe["steps"].replace(";", ".").split(".") if s.strip()]
    for i, step in enumerate(steps, 1):
        st.markdown(
            f"<div class='step-item'><div class='step-num'>{i}</div>"
            f"<div class='step-text'>{step}.</div></div>",
            unsafe_allow_html=True
        )

    st.write("")
    st.markdown("#### 🛒 Nguyên liệu cần mua thêm")
    if missing:
        total = sum(PRICES.get(x, 5000) for x in missing)
        for item in missing:
            st.markdown(f"- **{item}** — khoảng {money(PRICES.get(item, 5000))}")
        st.metric("Tổng chi phí mua thêm", money(total))
    else:
        st.success("🎉 Tuyệt vời! Bạn đã có đủ nguyên liệu cho món này.")

    shopping_text = "\n".join([f"- {x}" for x in missing]) if missing else "Đã có đủ nguyên liệu."
    st.download_button(
        "⬇️ Tải danh sách mua sắm (.txt)",
        data=f"Danh sách mua cho món {recipe['name']}\n{shopping_text}",
        file_name="danh_sach_mua_sam.txt",
        mime="text/plain",
        use_container_width=True,
    )

# -------------------- FORM + FILTER --------------------
left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown('<div class="panel"><h3>🥕 Nguyên liệu của bạn</h3><p class="muted">Thêm nguyên liệu đang có trong tủ lạnh hoặc chọn nhanh bên dưới.</p></div>', unsafe_allow_html=True)
    
    typed = st.text_input("Nhập nguyên liệu", placeholder="Ví dụ: trứng, cà chua, thịt...", label_visibility="collapsed")
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
      <div style="background:#f4f8f3;border-radius:13px;