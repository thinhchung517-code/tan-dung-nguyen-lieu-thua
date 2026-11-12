import streamlit as st

st.set_page_config(page_title="LeftoverChef", page_icon="🥘", layout="wide")

# ============ CSS (Đã fix triệt để lỗi Dark Mode) ============
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;800&display=swap');

/* Cưỡng chế nền sáng cho toàn bộ app */
html, body, [class*="css"], .stApp {
    font-family: 'Be Vietnam Pro', sans-serif !important;
    background-color: #fbfaf6 !important;
    color: #17251e !important;
}
.block-container { max-width: 1200px; padding-top: 1.6rem; }

/* Cưỡng chế màu chữ tối cho tất cả các thẻ text */
p, span, div, li, label, h1, h2, h3, h4, h5, h6, [data-testid="stText"], [data-testid="stCaption"], .stMarkdown {
    color: #17251e !important;
}

/* FIX Ô NHẬP LIỆU BỊ ĐEN */
input, textarea, [data-baseweb="input"] input, [data-baseweb="textarea"] textarea {
    background-color: #ffffff !important;
    color: #17251e !important;
    -webkit-text-fill-color: #17251e !important;
}
input::placeholder, textarea::placeholder { 
    color: #718078 !important; 
    -webkit-text-fill-color: #718078 !important; 
}

/* Hero Section */
.hero { background: linear-gradient(135deg, #d5f0db 0%, #f8fff8 45%, #fff2df 100%); border: 1px solid #cfe4d4; border-radius: 28px; padding: 40px; margin-bottom: 28px; box-shadow: 0 20px 50px -20px rgba(33,87,57,.15); }
.eyebrow { color:#17613f !important; font-weight:800; font-size:12px; background:#c9e8d2; padding:8px 14px; border-radius:30px; display:inline-block; }
.hero h1 { font-size: 48px; margin:16px 0 12px; letter-spacing:-1.5px; color: #183b2b !important; }
.hero p { color:#40564a !important; font-size:16px; max-width:680px; }

/* Khung Panel */
.panel { background:#fff; border:1px solid #e0e9e1; border-radius:20px; padding:22px; margin-bottom:18px; box-shadow: 0 8px 24px -12px rgba(27,65,43,.12); }
.panel h3 { margin-top:0; color: #183b2b !important; }

/* Thẻ món ăn */
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

/* Nút bấm */
div.stButton > button { border-radius:12px !important; font-weight:700 !important; border:1px solid #b9d3c2; color:#17452f !important; background: #fff !important; }
div.stButton > button:hover { border-color: #237a57 !important; }
div.stButton > button[kind="primary"] { background: linear-gradient(135deg, #237a57, #1a5f43) !important; color:#fff !important; border:none; }
div.stButton > button[kind="primary"] * { color: #fff !important; -webkit-text-fill-color: #fff !important; }

/* Các box custom */
.custom-info { background:#f8faf8; border:1px dashed #b9d3c2; border-radius:10px; padding:16px; color:#4b5d52; text-align:center; font-size:14px; }
.custom-warning { background:#fff8eb; border:1px solid #fed7aa; border-radius:10px; padding:12px; color:#9a3412 !important; font-size:14px; }
</style>""", unsafe_allow_html=True)

st.markdown("""<div class="hero">
<div class="eyebrow">✦ TRỢ LÝ NHÀ BẾP</div>
<h1>Trong tủ lạnh có gì?<br><span style="color:#237a57">Nấu món đó!</span></h1>
<p>Nhập nguyên liệu bạn đang có. LeftoverChef sẽ gợi ý món ăn, chỉ ra nguyên liệu còn thiếu và tính tiền mua thêm.</p>
</div>""", unsafe_allow_html=True)

RECIPES = [
    {"name":"Trứng chiên cà chua","emoji":"🍳","time":12,"cost":8000,"cheap":True,"desc":"Món đơn giản, dễ ăn.","need":["Trứng","Cà chua","Hành lá"],"steps":"Đánh trứng. Xào cà chua cho mềm, đổ trứng vào chiên chín và thêm hành lá."},
    {"name":"Mì xào rau củ","emoji":"🍜","time":15,"cost":12000,"cheap":True,"desc":"Bữa ăn nhanh với mì và rau củ.","need":["Mì","Rau cải","Trứng","Hành lá"],"steps":"Trụng mì, xào rau, cho mì và gia vị vào đảo đều; thêm trứng nếu thích."},
    {"name":"Đậu phụ sốt cà chua","emoji":"🍅","time":18,"cost":10000,"cheap":True,"desc":"Món thanh đạm, chi phí thấp.","need":["Đậu phụ","Cà chua","Hành lá"],"steps":"Chiên sơ đậu phụ, nấu sốt cà chua rồi cho đậu vào rim thấm vị."},
    {"name":"Thịt heo xào rau cải","emoji":"🥬","time":20,"cost":18000,"cheap":False,"desc":"Món mặn đủ chất cho gia đình.","need":["Thịt heo","Rau cải","Hành lá"],"steps":"Thái thịt mỏng, xào săn rồi cho rau cải vào đảo nhanh."},
    {"name":"Cơm chiên trứng","emoji":"🍚","time":10,"cost":7000,"cheap":True,"desc":"Tận dụng cơm nguội và trứng.","need":["Gạo","Trứng","Hành lá"],"steps":"Dùng cơm đã nấu chín để nguội, rang tơi với trứng và hành lá."},
    {"name":"Canh cà chua đậu phụ","emoji":"🥣","time":16,"cost":9000,"cheap":True,"desc":"Món canh nhẹ nhàng.","need":["Cà chua","Đậu phụ","Hành lá"],"steps":"Nấu cà chua với nước, cho đậu phụ vào đun nhẹ và nêm vừa ăn."},
    {"name":"Trứng luộc","emoji":"🥚","time":8,"cost":4000,"cheap":True,"desc":"Nhanh gọn, giàu protein.","need":["Trứng","Muối"],"steps":"Rửa trứng, luộc khoảng 7–10 phút."},
    {"name":"Trứng sốt cà chua","emoji":"🍅","time":15,"cost":9000,"cheap":True,"desc":"Trứng mềm kết hợp sốt chua ngọt.","need":["Trứng","Cà chua","Hành lá"],"steps":"Chiên sơ trứng, xào cà chua rồi cho trứng vào rim vài phút."},
    {"name":"Rau cải xào tỏi","emoji":"🥬","time":10,"cost":7000,"cheap":True,"desc":"Rau xanh thanh nhẹ.","need":["Rau cải","Tỏi","Dầu ăn"],"steps":"Phi thơm tỏi, cho rau cải vào xào trên lửa lớn."},
    {"name":"Đậu phụ chiên giòn","emoji":"🧈","time":12,"cost":8000,"cheap":True,"desc":"Vàng giòn bên ngoài, mềm bên trong.","need":["Đậu phụ","Dầu ăn","Nước mắm"],"steps":"Cắt đậu, thấm khô rồi chiên vàng đều."},
    {"name":"Mì trứng","emoji":"🍜","time":10,"cost":7000,"cheap":True,"desc":"Bữa ăn nhanh dễ tìm.","need":["Mì","Trứng","Hành lá"],"steps":"Nấu mì, cho trứng vào nấu chín và thêm hành lá."},
    {"name":"Thịt heo rang","emoji":"🥓","time":20,"cost":18000,"cheap":False,"desc":"Thịt rang đậm đà.","need":["Thịt heo","Hành lá","Nước mắm"],"steps":"Thái thịt, rang cho săn, nêm nước mắm rim đến khi thấm."},
    {"name":"Bánh mì trứng","emoji":"🥖","time":10,"cost":10000,"cheap":True,"desc":"Bữa sáng tiện lợi.","need":["Bánh mì","Trứng","Dưa leo"],"steps":"Chiên trứng, kẹp vào bánh mì cùng dưa leo."},
    {"name":"Khoai tây chiên","emoji":"🍟","time":20,"cost":12000,"cheap":True,"desc":"Món ăn vặt giòn thơm.","need":["Khoai tây","Dầu ăn","Muối"],"steps":"Gọt vỏ, cắt que, ngâm nước rồi chiên vàng."},
    {"name":"Canh khoai tây cà rốt","emoji":"🥕","time":25,"cost":14000,"cheap":True,"desc":"Canh rau củ ngọt tự nhiên.","need":["Khoai tây","Cà rốt","Hành lá"],"steps":"Cắt nhỏ khoai tây, cà rốt, nấu đến khi mềm rồi nêm gia vị."},
    {"name":"Cá sốt cà chua","emoji":"🐟","time":25,"cost":22000,"cheap":False,"desc":"Cá thấm sốt đậm đà.","need":["Cá","Cà chua","Hành lá"],"steps":"Chiên sơ cá, nấu sốt cà chua rồi rim cá nhỏ lửa."}
]

PRICES = {"Trứng":3500, "Cà chua":5000, "Thịt heo":12000, "Rau cải":6000, "Đậu phụ":5000, "Mì":4000, "Gạo":5000, "Hành lá":2000, "Muối":500, "Tỏi":1000, "Dầu ăn":1000, "Nước mắm":1000, "Cà rốt":4000, "Bánh mì":5000, "Dưa leo":3000, "Khoai tây":6000, "Cá":15000}

def fmt(n): return f"{n:,}".replace(",", ".")
def get_diff(t): return "⭐ Dễ" if t <= 12 else ("⭐⭐ Vừa" if t <= 20 else "⭐⭐⭐ Khéo")
def get_tags(r):
    tags = []
    if r["cheap"]: tags.append("💰 Tiết kiệm")
    if r["time"] <= 15: tags.append("⚡ Nhanh")
    if not any(m in r["need"] for m in ["Thịt heo","Thịt gà","Cá"]): tags.append("🌱 Chay")
    return tags

def has_ing(item, ings):
    return any(item.casefold() in x.casefold() or x.casefold() in item.casefold() for x in ings)
def get_missing(r):
    return [x for x in r["need"] if not has_ing(x, st.session_state.ingredients)]
def add_ings(val):
    for p in val.split(","):
        p = p.strip()
        if p and p.casefold() not in [x.casefold() for x in st.session_state.ingredients]:
            st.session_state.ingredients.append(p)

if "ingredients" not in st.session_state: st.session_state.ingredients = []
if "selected_recipe" not in st.session_state: st.session_state.selected_recipe = None

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
        # Thay st.info bằng custom div
        st.markdown('<div class="custom-info">Chưa có nguyên liệu nào.</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**🎛️ Bộ lọc & sắp xếp**")
    fc1, fc2 = st.columns(2)
    with fc1: fast_only = st.checkbox("⚡ Món dưới 20 phút")
    with fc2: cheap_only = st.checkbox("💰 Món tiết kiệm")
    sort_by = st.radio("Sắp xếp theo", ["Phù hợp nhất", "Nhanh nhất", "Rẻ nhất"], horizontal=True)

with right:
    st.markdown("""<div class="panel">
<h3>💡 LeftoverChef là gì?</h3>
<p class="muted">Ứng dụng đối chiếu nguyên liệu bạn có với công thức mẫu.</p>
<div style="background:linear-gradient(135deg,#f4f8f3,#eaf4ec);border-radius:13px;padding:16px;margin:12px 0">
<div style="font-size:28px">♻️</div><b style="color: #17251e !important;">Ưu tiên tận dụng đồ sẵn có</b>
<p class="muted" style="margin:6px 0 0">Hạn chế mua thêm không cần thiết.</p></div>
<div style="display:flex;gap:10px">
<div style="background:#fff8eb;border-radius:12px;padding:14px;flex:1"><div style="font-size:24px">⏱️</div><b style="color: #17251e !important;">Tiết kiệm thời gian</b></div>
<div style="background:#edf5fb;border-radius:12px;padding:14px;flex:1"><div style="font-size:24px">💰</div><b style="color: #17251e !important;">Kiểm soát chi phí</b></div>
</div></div>""", unsafe_allow_html=True)


res = []
for r in RECIPES:
    m = len(r["need"]) - len(get_missing(r))
    if st.session_state.ingredients and m == 0: continue
    if fast_only and r["time"] > 20: continue
    if cheap_only and not r["cheap"]: continue
    res.append({"r": r, "m": m, "ratio": m / len(r["need"]) if st.session_state.ingredients else 0})

if sort_by == "Phù hợp nhất": res.sort(key=lambda x: (x["ratio"], x["m"]), reverse=True)
elif sort_by == "Nhanh nhất": res.sort(key=lambda x: x["r"]["time"])
elif sort_by == "Rẻ nhất": res.sort(key=lambda x: x["r"]["cost"])
if not st.session_state.ingredients: res = res[:6]

st.markdown("## 🍳 Món ăn gợi ý")
if st.session_state.ingredients:
    st.markdown(f"<p style='color:#68796d !important;margin-top:-8px'>Tìm thấy <b>{len(res)}</b> món phù hợp với <b>{len(st.session_state.ingredients)}</b> nguyên liệu bạn có.</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:#68796d !important;margin-top:-8px'>Công thức mẫu. Hãy thêm nguyên liệu để có kết quả chính xác.</p>", unsafe_allow_html=True)

# === RENDER GRID & INLINE RECIPE DETAILS ===
if res:
    # Duyệt theo từng hàng (mỗi hàng 3 món)
    for i in range(0, len(res), 3):
        row_data = res[i:i+3]
        cols = st.columns(3)
        
        # Render 3 thẻ món ăn
        for j, item in enumerate(row_data):
            r = item["r"]
            pct = round(item["ratio"] * 100)
            is_perfect = pct == 100 and st.session_state.ingredients

            if not st.session_state.ingredients: b_text, b_class, c_class = "📖 Công thức mẫu", "match-badge", "recipe"
            elif is_perfect: b_text, b_class, c_class = "✨ Hoàn hảo!", "match-badge perfect-badge", "recipe perfect"
            else: b_text, b_class, c_class = f"♻️ {pct}% phù hợp", "match-badge", "recipe"

            tags_html = "".join([f'<span class="tag">{t}</span>' for t in get_tags(r)])
            
            with cols[j]:
                st.markdown(f'<div class="{c_class}"><div class="recipe-emoji">{r["emoji"]}</div><span class="{b_class}">{b_text}</span><div class="match-bar"><div class="match-bar-fill" style="width:{pct}%"></div></div><h4>{r["name"]}</h4><div class="muted">⏱️ {r["time"]} phút · 💰 ~{fmt(r["cost"])}đ · {get_diff(r["time"])}</div><p class="muted" style="margin-top:8px;flex:1">{r["desc"]}</p><div style="margin-top:8px">{tags_html}</div></div>', unsafe_allow_html=True)
                if st.button("Xem chi tiết →", key=f"b_{r['name']}", use_container_width=True):
                    st.session_state.selected_recipe = r
                    st.rerun()

        # Kiểm tra xem món ăn đang chọn có nằm trong hàng này không
        # Nếu có, render công thức NGAY BÊN DƯỚI HÀNG ĐÓ
        row_recipe_names = [item["r"]["name"] for item in row_data]
        sel = st.session_state.selected_recipe
        
        if sel and sel["name"] in row_recipe_names:
            st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True) # spacer
            miss = get_missing(sel)
            total = sum(PRICES.get(x, 5000) for x in miss)
            tags_html = "".join([f'<span class="tag">{t}</span>' for t in get_tags(sel)])
            
            # Render Header món ăn chi tiết
            st.markdown(f'<div style="background:linear-gradient(120deg,#eaf7ed,#fff8ec);border:1px solid #dce9dd;border-radius:22px;padding:26px;margin:8px 0 20px"><div style="font-size:52px">{sel["emoji"]}</div><h2 style="margin:8px 0">{sel["name"]}</h2><p style="color:#52675a !important;margin:6px 0">{sel["desc"]}</p><div style="margin-top:10px">{tags_html}</div><div style="margin-top:14px;font-weight:700;color:#237a57 !important;display:flex;gap:20px"><span>⏱️ {sel["time"]} phút</span><span>{get_diff(sel["time"])}</span><span>💰 Mua thêm: {fmt(total)}đ</span></div></div>', unsafe_allow_html=True)

            # Render 2 cột chi tiết
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
                
                shopping_text = "\n".join([f"- {x}: khoảng {fmt(PRICES.get(x,5000))}đ" for x in miss]) if miss else "Đã có đủ nguyên liệu."
                download_content = f"Danh sách mua cho món {sel['name']}\n\n{shopping_text}\n\nTổng cộng: {fmt(total)}đ"
                st.download_button("⬇️ Tải danh sách (.txt)", data=download_content, file_name="danh_sach_mua_sam.txt", mime="text/plain", use_container_width=True)

            with dr:
                st.markdown("### 👩‍🍳 Các bước thực hiện")
                for num, step in enumerate([p.strip() for p in sel["steps"].replace(";", ".").split(".") if p.strip()], 1):
                    st.markdown(f'<div style="display:flex;gap:12px;background:#fff;border:1px solid #e5ece5;border-radius:14px;padding:14px;margin-bottom:10px"><div style="min-width:32px;height:32px;border-radius:10px;background:linear-gradient(135deg,#e3f3e7,#d1ebd8);color:#237a57 !important;display:flex;align-items:center;justify-content:center;font-weight:800">{num}</div><div style="color:#34483b !important;padding-top:4px">{step}</div></div>', unsafe_allow_html=True)
                st.markdown('<div class="custom-info" style="text-align:left; margin-top: 15px;">💡 <b>Mẹo:</b> Sơ chế nguyên liệu trước khi bật bếp để nấu nhanh hơn.</div>', unsafe_allow_html=True)
            
            st.markdown("---") # Vạch phân cách sau khi hết chi tiết
else:
    st.markdown('<div class="custom-info">Chưa tìm thấy món phù hợp. Hãy thêm nguyên liệu khác.</div>', unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:#718078 !important;font-size:12px;padding:25px'>LeftoverChef © 2026</div>", unsafe_allow_html=True)
