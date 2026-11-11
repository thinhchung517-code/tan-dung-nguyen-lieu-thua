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

/* LeftoverChef visual refresh */
.stApp {
    background:
      radial-gradient(circle at 8% 2%, rgba(224,245,226,.72), transparent 28%),
      radial-gradient(circle at 95% 10%, rgba(255,235,205,.55), transparent 25%),
      #fbfaf6 !important;
}
.block-container {max-width:1280px;padding-top:1.6rem;padding-bottom:3rem;}
.hero {
    position:relative; overflow:hidden;
    background:linear-gradient(125deg,#e4f5e8 0%,#f8fff8 48%,#fff2df 100%);
    border:1px solid #d5e8d9;border-radius:28px;padding:clamp(26px,4vw,48px);
    box-shadow:0 14px 36px rgba(33,87,57,.08);
}
.hero:after {
    content:"🥗";position:absolute;right:5%;bottom:-25px;font-size:clamp(90px,13vw,170px);
    opacity:.13;transform:rotate(-12deg);pointer-events:none;
}
.hero .eyebrow {display:inline-block;background:#d3ead9;padding:7px 12px;border-radius:30px;}
.hero h1 {letter-spacing:-1.5px;font-weight:800;}
.hero p {font-size:16px;max-width:650px;}
.panel {
    border:1px solid #e0e9e1;border-radius:20px;padding:23px;
    box-shadow:0 8px 24px rgba(27,65,43,.045);transition:transform .2s,box-shadow .2s;
}
.recipe {
    border:1px solid #e2e9e2;border-radius:20px;padding:20px;
    box-shadow:0 7px 22px rgba(28,65,43,.045);transition:transform .22s,box-shadow .22s,border-color .22s;
    min-height:245px;position:relative;overflow:hidden;
}
.recipe:hover {transform:translateY(-5px);box-shadow:0 15px 30px rgba(28,65,43,.11);border-color:#a9d2b5;}
.recipe-emoji {
    display:flex;align-items:center;justify-content:center;width:68px;height:68px;
    border-radius:20px;background:linear-gradient(145deg,#f0f8ef,#fff4e4);
    font-size:39px;margin-bottom:14px;
}
.match {letter-spacing:.2px;}
div.stButton>button, div.stDownloadButton>button {
    border-radius:12px!important;padding:.62rem 1rem!important;
    transition:all .18s ease!important;font-weight:700!important;
}
div.stButton>button[kind="primary"] {box-shadow:0 6px 14px rgba(35,122,87,.18);}
div.stButton>button:hover {transform:translateY(-1px);}
[data-testid="stMetric"] {border:1px solid #e0e9e1;border-radius:15px;background:#f4f8f4;}
[data-testid="stExpander"] {border-radius:14px!important;border-color:#e0e9e1!important;}
hr {border-color:#e5ebe5!important;}
@media(max-width:700px) {
 .block-container {padding-left:1rem;padding-right:1rem;}
 .hero {border-radius:20px;}
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
     "steps":"Nấu cà chua với nước, cho đậu phụ vào đun nhẹ và nêm vừa ăn."},

    # -------------------- MÓN ĂN BỔ SUNG --------------------
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
st.markdown("<p style='color:#68796d;margin-top:-8px'>Chọn một món để xem nguyên liệu, hướng dẫn nấu và chi phí mua thêm.</p>", unsafe_allow_html=True)
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
              <span class="match">♻️ {percent}% nguyên liệu phù hợp</span>
              <h4 style="margin:12px 0 8px;font-size:18px">{recipe['name']}</h4>
              <div class="muted">⏱️ {recipe['time']} phút &nbsp; · &nbsp; 🛒 ~{recipe['cost']:,}đ mua thêm</div>
              <p class="muted" style="margin-top:10px">{recipe['desc']}</p>
            </div>
            """.replace(",", "."), unsafe_allow_html=True)
            if st.button("Xem nguyên liệu & cách nấu", key=f"recipe_{recipe['name']}", use_container_width=True):
                st.session_state.selected_recipe = recipe
                st.rerun()
else:
    st.info("Chưa tìm thấy món phù hợp. Hãy thêm nguyên liệu khác hoặc bỏ bớt bộ lọc.")

# -------------------- CÔNG THỨC CHI TIẾT & DANH SÁCH MUA SẮM --------------------
st.markdown("## 👨‍🍳 Công thức & nguyên liệu")
selected = st.session_state.selected_recipe
if selected:
    missing = get_missing(selected)
    total = sum(PRICES.get(x, 5000) for x in missing)
    matched_items = [x for x in selected["need"] if x not in missing]

    st.markdown(f"""
    <div style="background:linear-gradient(120deg,#eaf7ed,#fff8ec);border:1px solid #dce9dd;
                border-radius:22px;padding:24px;margin:8px 0 18px">
      <div style="font-size:42px">{selected['emoji']}</div>
      <h2 style="margin:8px 0;color:#183b2b">{selected['name']}</h2>
      <p style="color:#52675a;margin:0">{selected['desc']}</p>
      <div style="margin-top:12px;font-weight:700;color:#237a57">
        ⏱️ {selected['time']} phút &nbsp; · &nbsp; 💰 Dự kiến mua thêm: {total:,}đ
      </div>
    </div>
    """.replace(",", "."), unsafe_allow_html=True)

    detail_left, detail_right = st.columns([1, 1.25], gap="large")
    with detail_left:
        st.markdown("### 🧺 Nguyên liệu")
        st.caption("Đánh dấu những gì bạn đã có trong bếp.")
        for item in selected["need"]:
            if item in missing:
                st.markdown(f"🛒 **{item}** — cần mua thêm (khoảng {PRICES.get(item,5000):,}đ".replace(",", ".") + ")")
            else:
                st.markdown(f"✅ **{item}** — đã có")
        st.markdown("---")
        st.metric("Chi phí mua thêm ước tính", f"{total:,}đ".replace(",", "."))
        shopping_text = "\\n".join([f"- {x}: khoảng {PRICES.get(x,5000):,}đ".replace(",", ".") for x in missing]) if missing else "Đã có đủ nguyên liệu."
        st.download_button("⬇️ Tải danh sách mua sắm (.txt)",
                           data=f"Danh sách mua cho món {selected['name']}\\n{shopping_text}",
                           file_name="danh_sach_mua_sam.txt", mime="text/plain",
                           use_container_width=True)
    with detail_right:
        st.markdown("### 👩‍🍳 Các bước thực hiện")
        # Tách câu hướng dẫn hiện có thành các bước dễ theo dõi; dữ liệu công thức gốc vẫn được giữ.
        raw_steps = selected["steps"].replace(";", ".")
        step_parts = [part.strip() for part in raw_steps.split(".") if part.strip()]
        for number, step in enumerate(step_parts, 1):
            st.markdown(f"""
            <div style="display:flex;gap:12px;align-items:flex-start;background:#fff;
                        border:1px solid #e5ece5;border-radius:14px;padding:13px 15px;margin-bottom:10px">
              <div style="min-width:30px;height:30px;border-radius:10px;background:#e3f3e7;color:#237a57;
                          display:flex;align-items:center;justify-content:center;font-weight:800">{number}</div>
              <div style="color:#34483b;line-height:1.65;padding-top:3px">{step}</div>
            </div>
            """, unsafe_allow_html=True)
        st.info("Mẹo: Chuẩn bị và sơ chế nguyên liệu trước khi bật bếp để nấu nhanh, gọn hơn.")
else:
    st.info("Chọn **“Xem nguyên liệu & cách nấu”** ở một món ăn để xem công thức chi tiết và tạo danh sách mua sắm.")

# -------------------- GIỚI THIỆU QUY TRÌNH --------------------
st.markdown("## Cách sử dụng")
c1, c2, c3 = st.columns(3)
c1.markdown('<div class="panel"><h3>1️⃣ Nhập nguyên liệu</h3><p class="muted">Liệt kê thực phẩm bạn đang có trong tủ lạnh.</p></div>', unsafe_allow_html=True)
c2.markdown('<div class="panel"><h3>2️⃣ Chọn món phù hợp</h3><p class="muted">Xem độ phù hợp, thời gian nấu và nguyên liệu còn thiếu.</p></div>', unsafe_allow_html=True)
c3.markdown('<div class="panel"><h3>3️⃣ Mua đúng thứ cần</h3><p class="muted">Tạo danh sách mua sắm và dự trù số tiền cần thiết.</p></div>', unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#718078;font-size:12px;padding:25px'>LeftoverChef © 2026 · Biến nguyên liệu còn lại thành bữa ăn mới.</div>", unsafe_allow_html=True)
