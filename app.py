import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 설정
st.set_page_config(page_title="헤르조르센", layout="centered")

# 2. 화면별 전용 CSS 스타일 정의 (상호 간섭 방지)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gungsuh&family=Noto+Sans+KR:wght@400;700&display=swap');
    
    /* 기본 앱 배경 */
    .stApp {
        background-color: #1a0000;
        color: #ffffff;
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    /* 인트로 전용 스타일 */
    .intro-title {
        font-family: 'Gungsuh', '궁서', serif;
        color: #ff3333;
        font-size: 70px;
        text-align: center;
        font-weight: bold;
        margin-top: 50px;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #8b0000;
        letter-spacing: 5px;
    }
    .intro-box {
        border: 2px solid #ffd700;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        font-size: 19px;
        line-height: 1.8;
        margin: 40px auto;
        max-width: 600px;
        background-color: #2b0000;
    }
    
    /* 진영 선택 카드 디자인 */
    .faction-container {
        display: flex;
        gap: 20px;
        margin-bottom: 25px;
    }
    .faction-card {
        flex: 1;
        background: #111111;
        border: 2px solid #333333;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        transition: transform 0.2s, border-color 0.2s;
    }
    .card-catmom:hover {
        border-color: #00ffcc;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
        transform: translateY(-3px);
    }
    .card-cathate:hover {
        border-color: #ff4444;
        box-shadow: 0 0 15px rgba(255, 68, 68, 0.3);
        transform: translateY(-3px);
    }
    
    /* Streamlit 기본 버튼 일괄 커스텀 (노란색/검은색 고대비 테마) */
    .stButton>button {
        background-color: #ffd700 !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 20px !important;
        border-radius: 8px !important;
        border: 2px solid #ffffff !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 10px rgba(255, 215, 0, 0.2) !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
    }
    .stButton>button:hover {
        background-color: #ffffff !important;
        box-shadow: 0 0 15px #ffd700 !important;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. 세션 상태 관리 초기화
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
if 'faction' not in st.session_state:
    st.session_state.faction = None

# --- [화면 1: 인트로] ---
if st.session_state.stage == 'intro':
    st.markdown('<div class="intro-title">헤르조르센</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="intro-box">
        당신은 시공간의 균열로 현대의 <b>헤르조르센</b>에 떨어진 <b>효령대군</b>입니다.<br>
        각 스테이지마다 자신의 파를 선택 후 승리하십시오!
    </div>
    """, unsafe_allow_html=True)
    
    # 정중앙에 배치되어 무조건 잘 보이는 시작 버튼
    if st.button("🎮 게임 시작하기", key="btn_start"):
        st.session_state.stage = 'select_faction'
        st.rerun()

# --- [화면 2: 진영 선택] ---
elif st.session_state.stage == 'select_faction':
    st.markdown("<h2 style='text-align: center; color: #ffd700; font-family: 궁서; margin-top:20px;'>진영을 선택하십시오</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="faction-card card-catmom">
            <h3 style="color: #00ffcc; margin-top:0;">🐱 캣맘파</h3>
            <p style="font-size: 60px; margin: 15px 0;">🧑‍💼</p>
            <p style="color: #e0e0e0; font-size:15px;"><b>전쟁 시 등장 캐릭터:</b> 고양이를 들고 있는 사람</p>
            <p style="color: #bbb; font-size:14px; margin-top:10px;"><b>무기:</b> 새총 (돌멩이 발사)<br><b>방어 대상:</b> 상처 입은 새들의 공습</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("🟢 캣맘파 선택", key="btn_select_catmom"):
            st.session_state.faction = 'cat_mom'
            
    with col2:
        st.markdown("""
        <div class="faction-card card-cathate">
            <h3 style="color: #ff4444; margin-top:0;">🐦 캣싫어파</h3>
            <p style="font-size: 60px; margin: 15px 0;">🦅</p>
            <p style="color: #e0e0e0; font-size:15px;"><b>전쟁 시 등장 캐릭터:</b> 부상당한 새</p>
            <p style="color: #bbb; font-size:14px; margin-top:10px;"><b>무기:</b> 물총 (물줄기 발사)<br><b>방어 대상:</b> 고양이를 안은 사람들의 진격</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("🔴 캣싫어파 선택", key="btn_select_cathate"):
            st.session_state.faction = 'cat_hate'

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 선택 여부에 따른 동적 UI 하단 출력
    if st.session_state.faction:
        selected_text = "🐱 캣맘파" if st.session_state.faction == 'cat_mom' else "🐦 캣싫어파"
        st.markdown(f"<h4 style='text-align: center; color: #ffffff;'>선택 완료: <span style='color:#ffd700;'>{selected_text}</span></h4>", unsafe_allow_html=True)
        
        if st.button("⚔️ 선택 완료, 전쟁 시작", key="btn_battle_start"):
            st.session_state.stage = 'battle'
            st.rerun()
    else:
        st.markdown("<p style='text-align: center; color: #ff9999; font-weight: bold;'>위의 두 진영 중 하나를 먼저 클릭해 주세요.</p>", unsafe_allow_html=True)

# --- [화면 3 & 4: 인게임 및 결과창 (HTML5 Canvas)] ---
elif st.session_state.stage == 'battle':
    faction = st.session_state.faction
    theme_color = "#00ffcc" if faction == 'cat_mom' else "#ff4444"
    
    # f-string 문자열 포맷팅 및 중괄호 완전 차단 검증 완료
    game_html = f"""
    <div id="game-wrapper" style="text-align: center; background-color: #0c0c0c; padding: 15px; border-radius: 12px; max-width:530px; margin:0 auto;">
        <canvas id="gameCanvas" width="500" height="600" style="border: 3px solid {theme_color}; background:#151518; border-radius: 8px;"></canvas>
    </div>

    <script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    // 변수 초기화
    let timeLeft = 60; // 60초 압축 밸런스 페이즈 게임
    let myScore = 0;
    let enemyScore = 0;
    let gameState = 'countdown'; 
    let countdownTime = 3;
    let phase = 1;
    let hasUlt = true;         
    let ultActiveTimer = 0;    
    
    let shakeTimer = 0;
    let shakeIntensity = 0;

    let bullets = [];
    let enemies = [];
    let particles = [];        

    const lanes = [62, 187, 312, 437];
    const weapons = lanes.map(x => ({{ x: x, y: 550, lastFired: 0 }}));
    const fireCooldown = 150; 

    // 키보드 리스너 등록 개편
    window.removeEventListener('keydown', window.gameKeyHandler);
    window.gameKeyHandler = function(e) {{
        if (gameState !== 'playing') return;
        const now = Date.now();
        if (e.key === '1' && now - weapons[0].lastFired > fireCooldown) {{ fireBullet(0); weapons[0].lastFired = now; }}
        if (e.key === '2' && now - weapons[1].lastFired > fireCooldown) {{ fireBullet(1); weapons[1].lastFired = now; }}
        if (e.key === '3' && now - weapons[2].lastFired > fireCooldown) {{ fireBullet(2); weapons[2].lastFired = now; }}
        if (e.key === '4' && now - weapons[3].lastFired > fireCooldown) {{ fireBullet(3); weapons[3].lastFired = now; }}
        
        if (e.key === ' ' || e.code === 'Space') {{
            e.preventDefault();
            if (hasUlt) useUltimate();
        }}
    }};
    window.addEventListener('keydown', window.gameKeyHandler);

    function fireBullet(index) {{
        bullets.push({{ x: weapons[index].x, y: weapons[index].y - 25 }});
    }}

    function useUltimate() {{
        hasUlt = false;
        ultActiveTimer = 15; 
        triggerShake(15, 10);
        enemies.forEach(e => {{
            myScore += 5;
            createParticles(e.x, e.y, "{theme_color}");
        }});
        enemies = [];
    }}

    function triggerShake(duration, intensity) {{
        shakeTimer = duration;
        shakeIntensity = intensity;
    }}

    function createParticles(x, y, color) {{
        for (let i = 0; i < 6; i++) {{
            particles.push({{
                x: x, y: y,
                vx: (Math.random() - 0.5) * 6,
                vy: (Math.random() - 0.5) * 6,
                radius: Math.random() * 3 + 2,
                alpha: 1,
                color: color
            }});
        }}
    }}

    // 카운트다운 타이머
    let countdownInterval = setInterval(() => {{
        if (gameState === 'countdown') {{
            countdownTime--;
            if (countdownTime <= 0) {{
                gameState = 'playing';
                clearInterval(countdownInterval);
                startMainTimer();
            }}
        }}
    }}, 1000);

    // 메인 시간 타이머 (안전 중괄호 치환 완료)
    function startMainTimer() {{
        let timer = setInterval(() => {{
            if (gameState === 'playing') {{
                timeLeft--;
                if (timeLeft <= 40 && timeLeft > 15) phase = 2;
                else if (timeLeft <= 15) phase = 3;

                if (timeLeft <= 0) {{
                    gameState = 'ended';
                    clearInterval(timer);
                }}
            }}
        }}, 1000);
    }}

    // 적 스폰 루틴
    let spawnCounter = 0;
    function handleEnemySpawning() {{
        spawnCounter++;
        let spawnInterval = phase === 1 ? 40 : (phase === 2 ? 22 : 11);
        if (spawnCounter >= spawnInterval) {{
            spawnCounter = 0;
            let randomLane = Math.floor(Math.random() * 4);
            let baseSpeed = phase === 1 ? 2.5 : (phase === 2 ? 4.2 : 6.2);
            enemies.push({{
                x: lanes[randomLane],
                y: -20,
                speed: baseSpeed + Math.random() * 1.5,
                pulse: 0
            }});
        }}
    }}

    // 60FPS 렌더링 엔진
    function render() {{
        ctx.save();
        if (shakeTimer > 0) {{
            let dx = (Math.random() - 0.5) * shakeIntensity;
            let dy = (Math.random() - 0.5) * shakeIntensity;
            ctx.translate(dx, dy);
            shakeTimer--;
        }}

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // 현대식 도심 아스팔트 바닥 구현
        ctx.fillStyle = "#16161a";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.strokeStyle = "#242429";
        ctx.lineWidth = 1;
        for(let i=0; i<canvas.width; i+=40) {{
            ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke();
        }}
        for(let j=0; j<canvas.height; j+=40) {{
            ctx.beginPath(); ctx.moveTo(0, j); ctx.lineTo(canvas.width, j); ctx.stroke();
        }}

        // 경계선 네온 빔 연출
        ctx.strokeStyle = "{theme_color}";
        ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(0, 460); ctx.lineTo(500, 460); ctx.stroke();

        if (gameState === 'countdown') {{
            ctx.fillStyle = "#ffd700";
            ctx.font = "bold 80px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText(countdownTime, canvas.width/2, canvas.height/2 + 20);
            ctx.restore();
            requestAnimationFrame(render);
            return;
        }}

        // [최종 결과창 비주얼 연출]
        if (gameState === 'ended') {{
            ctx.fillStyle = "#000000";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.textAlign = "center";
            
            let win = myScore >= enemyScore;
            if (win) {{
                ctx.fillStyle = "#FFD700"; // 금색
                ctx.font = "bold 80px sans-serif";
                ctx.fillText("WIN", canvas.width/2, canvas.height/2 - 20);
            }} else {{
                ctx.fillStyle = "#808080"; // 회색
                ctx.font = "bold 80px sans-serif";
                ctx.fillText("LOSE", canvas.width/2, canvas.height/2 - 20);
            }}
            
            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 20px sans-serif";
            ctx.fillText("최종 전쟁 스코어 리포트", canvas.width/2, canvas.height/2 + 50);
            ctx.font = "16px sans-serif";
            ctx.fillStyle = "#bbbbbb";
            ctx.fillText("우리 팀: " + myScore + " 점 VS 상대 팀: " + enemyScore + " 점", canvas.width/2, canvas.height/2 + 85);
            ctx.restore();
            return;
        }}

        handleEnemySpawning();

        // 실시간 전황 대시보드 UI
        ctx.fillStyle = "rgba(0, 0, 0, 0.75)";
        ctx.fillRect(10, 10, 480, 45);
        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 14px sans-serif";
        ctx.textAlign = "left";
        ctx.fillText("⏱️ 남은 시간: " + timeLeft + "초 (페이즈 " + phase + ")", 25, 38);
        ctx.textAlign = "center";
        ctx.fillText("🏆 우리팀: " + myScore, 250, 38);
        ctx.textAlign = "right";
        ctx.fillText("😈 상대팀: " + enemyScore, 475, 38);

        if(hasUlt) {{
            ctx.fillStyle = "#ffd700";
            ctx.font = "12px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText("[SPACEBAR] 효령대군의 전멸기 사용 가능", canvas.width/2, 80);
        }}

        // 아군 디펜스 무기 렌더링
        weapons.forEach((w, i) => {{
            if ("{faction}" === "cat_mom") {{
                ctx.lineWidth = 4;
                ctx.strokeStyle = "#8b5a2b";
                ctx.beginPath();
                ctx.moveTo(w.x - 14, w.y - 12); ctx.lineTo(w.x, w.y + 10); ctx.lineTo(w.x + 14, w.y - 12);
                ctx.stroke();
            }} else {{
                ctx.fillStyle = "#ff4444";
                ctx.fillRect(w.x - 8, w.y - 18, 16, 26);
                ctx.fillStyle = "#00bfff";
                ctx.fillRect(w.x - 3, w.y - 24, 6, 8);
            }}
            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 12px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText((i+1), w.x, w.y + 24);
        }});

        // 투사체 날아가기 연출
        for (let i = bullets.length - 1; i >= 0; i--) {{
            bullets[i].y -= 9;
            ctx.fillStyle = "{faction}" === "cat_mom" ? "#a8a8a8" : "#00f0ff";
            ctx.beginPath();
            ctx.arc(bullets[i].x, bullets[i].y, "{faction}" === "cat_mom" ? 6 : 4, 0, Math.PI * 2);
            ctx.fill();
            if (bullets[i].y < 0) {{ bullets.splice(i, 1); }}
        }}

        // 상대 캐릭터 돌격 연출
        for (let i = enemies.length - 1; i >= 0; i--) {{
            enemies[i].y += enemies[i].speed;
            enemies[i].pulse += 0.12;

            ctx.save();
            ctx.translate(enemies[i].x, enemies[i].y);
            if ("{faction}" === "cat_mom") {{
                // 캣맘파 수비 대상: 상처 입은 새 (날개 흔들림 애니메이션)
                ctx.fillStyle = "#ff6b6b";
                ctx.fillRect(-12, -12, 24, 24);
                ctx.fillStyle = "#ff0000";
                ctx.fillRect(3, -7, 4, 4);
                let wing = Math.sin(enemies[i].pulse) * 8;
                ctx.fillStyle = "#cc3333";
                ctx.fillRect(-20, -5, 8, wing);
            }} else {{
                // 캣싫어파 수비 대상: 고양이를 안고 돌진하는 사람들
                ctx.fillStyle = "#d8bbff";
                ctx.beginPath(); ctx.arc(0, -9, 7, 0, Math.PI*2); ctx.fill();
                ctx.fillRect(-9, -2, 18, 18);
                ctx.fillStyle = "#ffb703"; // 품속의 노란 아기 고양이 모양
                ctx.fillRect(-5, 2, 10, 9);
            }}
            ctx.restore();

            // 방어 구역 한계선 도달 시 스코어 패널티 및 스크린 셰이크
            if (enemies[i].y >= 460) {{
                enemyScore += 10;
                enemies.splice(i, 1);
                triggerShake(6, 6); 
                continue;
            }}

            // 피격 판정
            for (let j = bullets.length - 1; j >= 0; j--) {{
                let dist = Math.hypot(enemies[i].x - bullets[j].x, enemies[i].y - bullets[j].y);
                if (dist < 20) {{
                    myScore += 5;
                    createParticles(enemies[i].x, enemies[i].y, "{theme_color}");
                    enemies.splice(i, 1);
                    bullets.splice(j, 1);
                    break;
                }}
            }}
        }}

        // 입자 파편 튀기기 효과 연산
        for (let i = particles.length - 1; i >= 0; i--) {{
            particles[i].x += particles[i].vx;
            particles[i].y += particles[i].vy;
            particles[i].alpha -= 0.05;
            if (particles[i].alpha <= 0) {{
                particles.splice(i, 1);
                continue;
            }}
            ctx.save();
            ctx.globalAlpha = particles[i].alpha;
            ctx.fillStyle = particles[i].color;
            ctx.beginPath();
            ctx.arc(particles[i].x, particles[i].y, particles[i].radius, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        }}

        // 피크 페이즈 3 사이렌 비네팅 광원 연출
        if (phase === 3 && Math.floor(Date.now() / 250) % 2 === 0) {{
            let gradient = ctx.createRadialGradient(canvas.width/2, canvas.height/2, 180, canvas.width/2, canvas.height/2, 360);
            gradient.addColorStop(0, 'rgba(255,0,0,0)');
            gradient.addColorStop(1, 'rgba(255,0,0,0.3)');
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }}

        if (ultActiveTimer > 0) {{
            ctx.fillStyle = "rgba(255, 255, 255, " + (ultActiveTimer/15) + ")";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ultActiveTimer--;
        }}

        ctx.restore();
        requestAnimationFrame(render);
    }}

    render();
    </script>
    """
    
    # 임베디드 캔버스 실행
    components.html(game_html, height=640)
    
    # 하단 조작 가이드 안내문 배치
    st.markdown("""
        <div style="text-align:center; color:#aaa; font-size:14px; line-height:1.6; margin-top:5px;">
            ⌨️ <b>전투 조작 가이드</b><br>
            키보드 숫자 키 <b>[1], [2], [3], [4]</b>를 리드미컬하게 눌러 해당 구역으로 발사하세요.<br>
            위급 시 <b>[Spacebar]</b>를 누르면 화면 내 모든 적을 전멸시키는 <b>'효령대군의 가호'</b>가 발동됩니다. (판당 1회 제한)
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # 깔끔하고 즉각적으로 반응하는 다시 시작하기 루틴 버튼
    if st.button("🔄 게임 처음부터 다시하기", key="btn_restart_game"):
        st.session_state.stage = 'intro'
        st.session_state.faction = None
        st.rerun()
