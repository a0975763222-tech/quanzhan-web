<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>銓展通訊 Quanzhan Telecom | 全系列報價旗艦店</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { background-color: #020617; color: #f8fafc; }
        .brushed-metal {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            background-image: repeating-linear-gradient(0deg, rgba(255,255,255,0.01) 0px, rgba(255,255,255,0.01) 1px, transparent 1px, transparent 2px);
            border-bottom: 1px solid #334155;
        }
        /* 品牌專屬色邊框 */
        .brand-apple { border-top: 4px solid #f5f5f7; }
        .brand-samsung { border-top: 4px solid #034ea2; }
        .brand-oppo { border-top: 4px solid #00ad11; }
        .brand-redmi { border-top: 4px solid #ff4d4d; }
        .brand-vivo { border-top: 4px solid #005aff; }
        .brand-default { border-top: 4px solid #64748b; }

        .glass-card {
            background: rgba(30, 41, 59, 0.4);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 1.5rem;
            transition: all 0.3s ease;
        }
        .glass-card:hover { transform: translateY(-5px); border-color: rgba(255, 255, 255, 0.2); }
    </style>
</head>
<body>

    <header class="brushed-metal pt-12 pb-16 px-6 text-center">
        <h1 class="text-4xl md:text-5xl font-black mb-4 tracking-tighter text-white">銓展通訊</h1>
        <div class="max-w-xs mx-auto text-left space-y-2 text-sm text-slate-400">
            <div class="flex items-center gap-3"><i class="fa-solid fa-location-dot w-4 text-blue-400"></i> 桃園市龜山區中興路402號</div>
            <div class="flex items-center gap-3"><i class="fa-solid fa-phone w-4 text-blue-400"></i> 03-3590858</div>
            <div class="flex items-center gap-3"><i class="fa-solid fa-id-card w-4 text-blue-400"></i> 統編 80089553</div>
        </div>
    </header>

    <main class="max-w-6xl mx-auto -mt-8 px-6 pb-20">
        <div class="bg-slate-900 border-2 border-slate-700 rounded-2xl flex items-center px-6 py-4 mb-12 shadow-2xl">
            <i class="fa-solid fa-magnifying-glass text-slate-500 mr-4"></i>
            <input type="text" id="searchInput" placeholder="搜尋：iPhone, iPad, AirPods, Watch..." class="bg-transparent w-full focus:outline-none text-white lg:text-lg">
        </div>

        <h2 class="text-2xl font-bold mb-8 flex items-center gap-3">
            <span class="w-1.5 h-8 bg-blue-500 rounded-full shadow-[0_0_10px_#3b82f6]"></span> 當日即時報價
        </h2>

        <div id="priceContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            </div>
    </main>

    <section class="bg-slate-900/50 py-16 px-6 border-t border-slate-800">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-2xl font-bold mb-8 text-center md:text-left">專業通訊服務</h2>
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="glass-card p-6 text-center group cursor-pointer hover:bg-slate-800">
                    <i class="fa-solid fa-sim-card text-3xl mb-3 text-blue-400 group-hover:scale-110 transition-transform"></i>
                    <div class="font-bold">門號特惠</div>
                </div>
                <div class="glass-card p-6 text-center group cursor-pointer hover:bg-slate-800">
                    <i class="fa-solid fa-credit-card text-3xl mb-3 text-emerald-400 group-hover:scale-110 transition-transform"></i>
                    <div class="font-bold">無卡分期</div>
                </div>
                <div class="glass-card p-6 text-center group cursor-pointer hover:bg-slate-800">
                    <i class="fa-solid fa-headphones text-3xl mb-3 text-purple-400 group-hover:scale-110 transition-transform"></i>
                    <div class="font-bold">精選配件</div>
                </div>
                <div class="glass-card p-6 text-center group cursor-pointer hover:bg-slate-800">
                    <i class="fa-solid fa-rotate text-3xl mb-3 text-amber-400 group-hover:scale-110 transition-transform"></i>
                    <div class="font-bold">手機回收</div>
                </div>
            </div>
        </div>
    </section>

    <script>
        // 品牌與配件視覺配置
        const config = {
            'Apple': { icon: 'fa-apple', color: 'brand-apple' },
            'Samsung': { icon: 'fa-mobile-screen', color: 'brand-samsung' },
            'OPPO': { icon: 'fa-mobile-vibration', color: 'brand-oppo' },
            'Redmi': { icon: 'fa-robot', color: 'brand-redmi' },
            'vivo': { icon: 'fa-v', color: 'brand-vivo' },
            'iPad': { icon: 'fa-tablet-screen-button', color: 'brand-apple' },
            'AirPods': { icon: 'fa-headphones', color: 'brand-apple' },
            'Watch': { icon: 'fa-clock', color: 'brand-apple' }
        };

        async function load() {
            try {
                const res = await fetch('prices.json');
                const data = await res.json();
                const container = document.getElementById('priceContainer');
                
                container.innerHTML = data.map(item => {
                    // 根據品名或品牌判斷圖示
                    let style = config[item.brand] || { icon: 'fa-mobile', color: 'brand-default' };
                    if (item.model.includes('iPad')) style = config['iPad'];
                    if (item.model.includes('AirPods')) style = config['AirPods'];
                    if (item.model.includes('Watch')) style = config['Watch'];

                    return `
                        <div class="glass-card p-8 ${style.color}">
                            <div class="flex justify-between items-center mb-6">
                                <span class="text-xs font-black tracking-widest text-slate-400 uppercase">${item.brand}</span>
                                <i class="fa-solid ${style.icon} text-2xl opacity-40"></i>
                            </div>
                            <h3 class="text-2xl font-bold text-white mb-2">${item.model}</h3>
                            <p class="text-slate-500 text-sm mb-8">${item.specs}</p>
                            <div class="flex items-baseline gap-2 mb-8">
                                <span class="text-3xl font-black text-white italic">NT$ ${parseInt(item.price).toLocaleString()}</span>
                                <span class="text-slate-600 text-xs line-through decoration-slate-800">原價 ${parseInt(item.msrp).toLocaleString()}</span>
                            </div>
                            <button onclick="window.open('https://line.me/R/ti/p/@your_id')" class="w-full bg-white text-black font-black py-4 rounded-2xl hover:bg-blue-50 transition-all shadow-lg active:scale-95">
                                LINE 諮詢價格
                            </button>
                        </div>
                    `;
                }).join('');
            } catch (e) { console.error(e); }
        }
        load();
    </script>
</body>
</html>
