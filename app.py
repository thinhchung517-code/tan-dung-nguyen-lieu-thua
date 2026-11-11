<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Leftover Chef–Nấu ngon từ nguyên liệu sẵn có</title>
<style>
:root{--green:#237a57;--green2:#e9f5ee;--ink:#20332b;--muted:#6d7d74;--cream:#fbfaf6;--orange:#f3a64a;--line:#e5ebe6;--white:#fff}
*{box-sizing:border-box}body{margin:0;font-family:Inter,Arial,sans-serif;background:var(--cream);color:var(--ink)}
header{background:rgba(255,255,255,.94);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:5}
.nav{max-width:1120px;margin:auto;padding:16px 22px;display:flex;align-items:center;justify-content:space-between}
.brand{font-size:22px;font-weight:850;color:var(--green);letter-spacing:-.7px}.brand span{color:var(--orange)}
.nav small{color:var(--muted);font-weight:600}
main{max-width:1120px;margin:34px auto;padding:0 22px}
.hero{display:grid;grid-template-columns:1.15fr .85fr;gap:28px;align-items:center;background:linear-gradient(120deg,#edf7ef,#fff8eb);border-radius:26px;padding:36px;overflow:hidden}
.eyebrow{color:var(--green);font-weight:800;font-size:12px;letter-spacing:1.5px;text-transform:uppercase}
h1{font-size:clamp(34px,5vw,54px);line-height:1.05;letter-spacing:-2px;margin:12px 0}
.hero p{color:#61736a;line-height:1.7;max-width:520px}
.hero-art{font-size:110px;text-align:center;filter:drop-shadow(0 12px 12px #9bb7a455)}
.btn{border:0;border-radius:12px;padding:12px 18px;background:var(--green);color:white;font-weight:750;cursor:pointer;transition:.2s}
.btn:hover{background:#185d40;transform:translateY(-1px)}.btn.secondary{background:white;color:var(--green);border:1px solid #cfe1d5}
.layout{display:grid;grid-template-columns: .95fr 1.05fr;gap:22px;margin-top:24px}
.panel{background:var(--white);border:1px solid var(--line);border-radius:20px;padding:24px;box-shadow:0 8px 24px #20332b08}
h2{font-size:21px;margin:0 0 8px}.sub{color:var(--muted);font-size:14px;line-height:1.55;margin:0 0 18px}
.inputrow{display:flex;gap:8px}.inputrow input,.search{width:100%;padding:13px 14px;border:1px solid #dce5de;border-radius:11px;font-size:14px;outline:none}
input:focus{border-color:var(--green);box-shadow:0 0 0 3px #237a5714}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:17px 0}
.chip{border:1px solid #d9e7dd;background:#f5faf6;color:#35634d;border-radius:999px;padding:8px 12px;font-size:13px;cursor:pointer}
.chip.active{background:var(--green);color:white;border-color:var(--green)}
.ingredient-list{display:flex;flex-wrap:wrap;gap:8px;min-height:34px;margin:14px 0 20px}
.tag{background:#f0f5f1;border-radius:9px;padding:8px 10px;font-size:13px;display:flex;gap:8px;align-items:center}
.tag button{border:0;background:none;color:#789087;cursor:pointer;font-size:16px;padding:0}
.options{display:flex;gap:12px;flex-wrap:wrap;color:var(--muted);font-size:13px;margin:14px 0}
.options label{display:flex;gap:6px;align-items:center}
.sectionhead{display:flex;justify-content:space-between;align-items:center;gap:10px;margin:28px 0 14px}
.sectionhead h2{margin:0}.count{font-size:12px;background:var(--green2);color:var(--green);padding:6px 10px;border-radius:99px;font-weight:750}
.recipes{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.recipe{border:1px solid var(--line);border-radius:17px;overflow:hidden;background:white;transition:.2s}
.recipe:hover{transform:translateY(-3px);box-shadow:0 10px 24px #20332b12}
.foodpic{height:130px;display:grid;place-items:center;font-size:64px;background:linear-gradient(135deg,#f4f6e9,#fcebd8)}
.recipebody{padding:15px}.recipebody h3{margin:0 0 7px;font-size:16px}.meta{display:flex;gap:10px;color:var(--muted);font-size:12px;margin:8px 0}
.match{font-size:11px;color:var(--green);font-weight:800;background:var(--green2);padding:5px 8px;border-radius:99px;display:inline-block}
.recipebody p{font-size:13px;line-height:1.5;color:var(--muted);min-height:38px}
.recipebody button{width:100%;padding:9px;border-radius:9px;border:1px solid #d5e5da;background:white;color:var(--green);font-weight:750;cursor:pointer}
.recipebody button:hover{background:var(--green2)}
.shopping{margin-top:22px}
.shoppingtop{display:flex;justify-content:space-between;align-items:center}
.shopitems{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin:15px 0}
.shopitem{display:flex;justify-content:space-between;gap:8px;background:#f7faf7;padding:10px 12px;border-radius:10px;font-size:13px}
.shopitem span:last-child{color:var(--muted)}
.estimate{display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:14px;font-weight:800}
.how{margin-top:22px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.step{padding:17px;background:white;border:1px solid var(--line);border-radius:15px}
.step b{display:block;margin:8px 0 5px}.step p{margin:0;color:var(--muted);font-size:13px;line-height:1.5}
footer{text-align:center;color:var(--muted);font-size:12px;padding:35px 20px}
.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#20332b;color:white;padding:12px 18px;border-radius:12px;opacity:0;pointer-events:none;transition:.25s;z-index:10}.toast.show{opacity:1}
@media(max-width:760px){.hero{grid-template-columns:1fr;padding:26px}.hero-art{font-size:76px}.layout{grid-template-columns:1fr}.recipes{grid-template-columns:1fr 1fr}.how{grid-template-columns:1fr}.nav small{display:none}}
@media(max-width:440px){.recipes{grid-template-columns:1fr}.panel{padding:18px}.inputrow{flex-direction:column}}
</style>
</head>
<body>
<header><div class="nav"><div class="brand">Leftover<span>Chef</span> 🍃</div><small>Ăn ngon hơn · Tiết kiệm hơn · Ít lãng phí hơn</small></div></header>
<main>
<section class="hero">
 <div><div class="eyebrow">Trợ lý nhà bếp thông minh</div><h1>Trong tủ lạnh có gì?<br><span style="color:var(--green)">Nấu món đó!</span></h1>
 <p>Nhập những nguyên liệu bạn đang có. LeftoverChef gợi ý món ăn phù hợp, chỉ ra nguyên liệu còn thiếu và ước tính chi phí cần mua thêm.</p>
 <button class="btn" onclick="document.getElementById('ingredientInput').focus()">Khám phá món ăn ↓</button></div>
 <div class="hero-art" aria-label="Nồi thức ăn">🥘🥬</div>
</section>
<div class="layout">
 <section class="panel">
  <h2>🥕 Nguyên liệu của bạn</h2><p class="sub">Thêm nguyên liệu đang có trong tủ lạnh hoặc chọn nhanh bên dưới.</p>
  <div class="inputrow"><input id="ingredientInput" placeholder="Ví dụ: trứng, cà chua, thịt..." onkeydown="if(event.key==='Enter')addIngredient()"><button class="btn" onclick="addIngredient()">Thêm</button></div>
  <div class="chips" id="quickChips">
   <button class="chip" onclick="quickAdd('Trứng')">🥚 Trứng</button><button class="chip" onclick="quickAdd('Cà chua')">🍅 Cà chua</button><button class="chip" onclick="quickAdd('Thịt heo')">🥩 Thịt heo</button><button class="chip" onclick="quickAdd('Rau cải')">🥬 Rau cải</button><button class="chip" onclick="quickAdd('Đậu phụ')">🧈 Đậu phụ</button><button class="chip" onclick="quickAdd('Mì')">🍜 Mì</button><button class="chip" onclick="quickAdd('Gạo')">🍚 Gạo</button><button class="chip" onclick="quickAdd('Hành lá')">🌿 Hành lá</button>
  </div>
  <div style="font-size:13px;font-weight:750">Đang có (<span id="ingredientCount">0</span>)</div>
  <div class="ingredient-list" id="ingredientList"><span style="color:#9aa79f;font-size:13px">Chưa có nguyên liệu nào.</span></div>
  <div class="options"><label><input type="checkbox" id="fastOnly"> Ưu tiên món dưới 20 phút</label><label><input type="checkbox" id="cheapOnly"> Ưu tiên tiết kiệm</label></div>
  <button class="btn" style="width:100%" onclick="suggestRecipes()">✨ Gợi ý món ăn cho tôi</button>
 </section>
 <section class="panel">
  <h2>💡 Cách LeftoverChef hoạt động</h2><p class="sub">Ứng dụng đối chiếu nguyên liệu bạn nhập với công thức mẫu để tìm món phù hợp.</p>
  <div style="background:#f4f8f3;border-radius:15px;padding:17px;margin:15px 0">
   <div style="font-size:30px">♻️</div><b>Ưu tiên tận dụng đồ sẵn có</b><p class="sub" style="margin:6px 0 0">Gợi ý món có nhiều nguyên liệu trùng khớp nhất, hạn chế mua thêm không cần thiết.</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
   <div style="background:#fff8eb;border-radius:13px;padding:14px"><div style="font-size:25px">⏱️</div><b style="font-size:14px">Tiết kiệm thời gian</b><p class="sub" style="margin:5px 0 0">Lọc món nhanh, dễ nấu.</p></div>
   <div style="background:#edf5fb;border-radius:13px;padding:14px"><div style="font-size:25px">💰</div><b style="font-size:14px">Kiểm soát chi phí</b><p class="sub" style="margin:5px 0 0">Biết cần mua thêm gì.</p></div>
  </div>
  <p style="font-size:12px;color:var(--muted);line-height:1.5;margin:15px 0 0">* Bản demo sử dụng dữ liệu công thức minh họa, chưa kết nối AI hoặc cửa hàng thực tế.</p>
 </section>
</div>
<div class="sectionhead"><h2>🍳 Món ăn gợi ý</h2><span class="count" id="resultCount">3 công thức mẫu</span></div>
<div class="recipes" id="recipeResults"></div>
<section class="panel shopping">
 <div class="shoppingtop"><div><h2>🛒 Danh sách cần mua</h2><p class="sub" style="margin:5px 0 0">Nguyên liệu còn thiếu cho món bạn chọn.</p></div><button class="btn secondary" onclick="copyShopping()">Sao chép</button></div>
 <div id="shoppingContent" class="sub" style="margin-top:18px">Chọn “Xem nguyên liệu” ở một món ăn để tạo danh sách mua sắm.</div>
</section>
<section class="how">
 <div class="step"><div style="font-size:25px">1️⃣</div><b>Nhập nguyên liệu</b><p>Liệt kê thực phẩm bạn đang có trong tủ lạnh.</p></div>
 <div class="step"><div style="font-size:25px">2️⃣</div><b>Chọn món phù hợp</b><p>Xem độ phù hợp, thời gian nấu và nguyên liệu còn thiếu.</p></div>
 <div class="step"><div style="font-size:25px">3️⃣</div><b>Mua đúng thứ cần</b><p>Tạo danh sách mua sắm và dự trù số tiền cần thiết.</p></div>
</section>
</main>
<footer>LeftoverChef © 2026 · Biến nguyên liệu còn lại thành bữa ăn mới.</footer>
<div class="toast" id="toast"></div>
<script>
const recipes=[
 {id:1,name:'Trứng chiên cà chua',emoji:'🍳',time:12,cost:8000,cheap:true,desc:'Món đơn giản, dễ ăn và tận dụng nguyên liệu quen thuộc.',need:['Trứng','Cà chua','Hành lá'],steps:'Đánh trứng, xào cà chua, đổ trứng vào chiên chín và thêm hành lá.'},
 {id:2,name:'Mì xào rau củ',emoji:'🍜',time:15,cost:12000,cheap:true,desc:'Bữa ăn nhanh với mì và rau củ có sẵn trong bếp.',need:['Mì','Rau cải','Trứng','Hành lá'],steps:'Trụng mì, xào rau, cho mì và gia vị vào đảo đều; thêm trứng nếu thích.'},
 {id:3,name:'Đậu phụ sốt cà chua',emoji:'🍅',time:18,cost:10000,cheap:true,desc:'Món ăn thanh đạm, nguyên liệu dễ tìm và chi phí thấp.',need:['Đậu phụ','Cà chua','Hành lá'],steps:'Chiên sơ đậu phụ, nấu sốt cà chua rồi cho đậu vào rim thấm vị.'},
 {id:4,name:'Thịt heo xào rau cải',emoji:'🥬',time:20,cost:18000,cheap:false,desc:'Món mặn đủ chất, phù hợp cho bữa cơm gia đình.',need:['Thịt heo','Rau cải','Hành lá'],steps:'Thái thịt mỏng, xào săn rồi cho rau cải vào đảo nhanh trên lửa lớn.'},
 {id:5,name:'Cơm chiên trứng',emoji:'🍚',time:10,cost:7000,cheap:true,desc:'Tận dụng cơm nguội và trứng để có bữa ăn tiết kiệm.',need:['Gạo','Trứng','Hành lá'],steps:'Dùng cơm đã nấu chín để nguội, rang tơi với trứng và hành lá.'},
 {id:6,name:'Canh cà chua đậu phụ',emoji:'🥣',time:16,cost:9000,cheap:true,desc:'Món canh nhẹ nhàng, thích hợp dùng cùng cơm nóng.',need:['Cà chua','Đậu phụ','Hành lá'],steps:'Nấu cà chua với nước, cho đậu phụ vào đun nhẹ và nêm vừa ăn.'}
];
let ingredients=[],selectedRecipe=null;
const norm=s=>s.trim().toLocaleLowerCase('vi');
function toast(msg){let t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1900)}
function addIngredient(){let input=document.getElementById('ingredientInput'),v=input.value.trim();if(!v)return;if(ingredients.some(x=>norm(x)===norm(v))){toast('Nguyên liệu này đã có rồi');return}ingredients.push(v);input.value='';renderIngredients()}
function quickAdd(v){if(!ingredients.some(x=>norm(x)===norm(v))){ingredients.push(v);renderIngredients()}else toast('Nguyên liệu này đã có rồi')}
function removeIngredient(v){ingredients=ingredients.filter(x=>x!==v);renderIngredients()}
function renderIngredients(){document.getElementById('ingredientCount').textContent=ingredients.length;let el=document.getElementById('ingredientList');el.innerHTML=ingredients.length?ingredients.map(v=>`<span class="tag">${escapeHTML(v)} <button aria-label="Xóa ${escapeHTML(v)}" onclick="removeIngredient('${v.replace(/'/g,"\\'")}')">×</button></span>`).join(''):'<span style="color:#9aa79f;font-size:13px">Chưa có nguyên liệu nào.</span>'}
function escapeHTML(s){return s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function matchScore(r){return r.need.filter(n=>ingredients.some(i=>norm(i).includes(norm(n))||norm(n).includes(norm(i)))).length}
function suggestRecipes(){if(!ingredients.length){toast('Hãy nhập ít nhất một nguyên liệu');return}let list=recipes.map(r=>({...r,score:matchScore(r)})).filter(r=>r.score>0);if(document.getElementById('fastOnly').checked)list=list.filter(r=>r.time<=20);if(document.getElementById('cheapOnly').checked)list=list.filter(r=>r.cheap);list.sort((a,b)=>(b.score/b.need.length)-(a.score/a.need.length)||a.cost-b.cost);renderRecipes(list);toast('Đã tìm thấy '+list.length+' món phù hợp')}
function renderRecipes(list=recipes.slice(0,3)){let el=document.getElementById('recipeResults');document.getElementById('resultCount').textContent=list.length+' món ăn';el.innerHTML=list.length?list.map(r=>{let score=ingredients.length?matchScore(r):0;let pct=ingredients.length?Math.round(score/r.need.length*100):0;return `<article class="recipe"><div class="foodpic">${r.emoji}</div><div class="recipebody"><span class="match">${ingredients.length?pct+'% nguyên liệu phù hợp':'Gợi ý nổi bật'}</span><h3>${r.name}</h3><div class="meta"><span>⏱ ${r.time} phút</span><span>🛒 ~${r.cost.toLocaleString('vi-VN')}đ mua thêm</span></div><p>${r.desc}</p><button onclick="showShopping(${r.id})">Xem nguyên liệu & cách nấu</button></div></article>`}).join(''):'<div class="panel" style="grid-column:1/-1;color:var(--muted)">Chưa tìm thấy món phù hợp. Hãy thêm nguyên liệu khác hoặc bỏ bớt bộ lọc.</div>'}
function showShopping(id){let r=recipes.find(x=>x.id===id);selectedRecipe=r;let missing=r.need.filter(n=>!ingredients.some(i=>norm(i).includes(norm(n))||norm(n).includes(norm(i))));let prices={'Trứng':3500,'Cà chua':5000,'Thịt heo':12000,'Rau cải':6000,'Đậu phụ':5000,'Mì':4000,'Gạo':5000,'Hành lá':2000};let total=missing.reduce((s,n)=>s+(prices[n]||5000),0);document.getElementById('shoppingContent').innerHTML=`<b style="color:var(--ink)">${r.name}</b><p style="margin:7px 0;color:var(--muted)">Cách làm: ${r.steps}</p>${missing.length?`<div class="shopitems">${missing.map(n=>`<div class="shopitem"><span>＋ ${n}</span><span>${(prices[n]||5000).toLocaleString('vi-VN')}đ</span></div>`).join('')}</div>`:'<p style="color:var(--green)">🎉 Bạn đã có đủ nguyên liệu cho món này!</p>'}<div class="estimate"><span>Chi phí mua thêm ước tính</span><span>${total.toLocaleString('vi-VN')}đ</span></div>`;document.querySelector('.shopping').scrollIntoView({behavior:'smooth',block:'center'})}
function copyShopping(){if(!selectedRecipe){toast('Bạn hãy chọn một món ăn trước');return}let missing=selectedRecipe.need.filter(n=>!ingredients.some(i=>norm(i).includes(norm(n))||norm(n).includes(norm(i))));let text=`Danh sách mua cho món ${selectedRecipe.name}:\n`+(missing.length?missing.map(n=>'- '+n).join('\n'):'Đã có đủ nguyên liệu');if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(()=>toast('Đã sao chép danh sách mua sắm')).catch(()=>toast('Không thể sao chép trên trình duyệt này'))}else toast('Trình duyệt không hỗ trợ sao chép')}
renderRecipes();
</script>
</body>
</html>
