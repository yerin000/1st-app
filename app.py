import streamlit as st
import numpy as np
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# 1. 페이지 설정 및 디자인 CSS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="공통수학1 - 삼각함수 마스터 LAB",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Mobile Friendly & Modern Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #F8FAFC;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #E2E8F0;
        margin-bottom: 20px;
    }
    .concept-box {
        background-color: #EFF6FF;
        border-left: 5px solid #3B82F6;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .hint-box {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 12px;
        border-radius: 4px;
        margin-top: 10px;
    }
    .success-box {
        background-color: #D1FAE5;
        border-left: 5px solid #10B981;
        padding: 12px;
        border-radius: 4px;
        margin-top: 10px;
    }
    .error-box {
        background-color: #FEE2E2;
        border-left: 5px solid #EF4444;
        padding: 12px;
        border-radius: 4px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. 세션 상태 (Session State) 초기화
# -----------------------------------------------------------------------------
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'wrong_answers' not in st.session_state:
    st.session_state.wrong_answers = []
if 'lab_quiz_cleared' not in st.session_state:
    st.session_state.lab_quiz_cleared = False
if 'hint_level' not in st.session_state:
    st.session_state.hint_level = {}

# -----------------------------------------------------------------------------
# 3. 사이드바 메뉴 구성
# -----------------------------------------------------------------------------
st.sidebar.title("📐 삼각함수 마스터")
st.sidebar.caption("2022 개정 교육과정 공통수학1")

menu = st.sidebar.radio(
    "이동할 메뉴를 선택하세요:",
    [
        "1. 삼각함수 시작하기 🎠",
        "2. 개념 학습 📖",
        "3. 그래프 실험실 🔬",
        "4. 인터랙티브 그래프 퀴즈 🎯",
        "5. 문제 풀기 📝",
        "6. 오답 / 복습 노트 📓",
        "7. 삼각함수 도우미 🤖"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("🏆 **나의 학습 현황**")
st.sidebar.write(f"- 풀이 맞춘 문제 수: **{st.session_state.quiz_score} 개**")
st.sidebar.write(f"- 오답 노트 항목: **{len(st.session_state.wrong_answers)} 개**")

# -----------------------------------------------------------------------------
# MENU 1: 삼각함수 시작하기
# -----------------------------------------------------------------------------
if menu == "1. 삼각함수 시작하기 🎠":
    st.markdown("<div class='main-header'>🎠 삼각함수, 도대체 왜 배울까?</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>일상 속의 '반복되는 회전 운동'에서 시작하는 삼각함수 개념</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        <h3>🎡 회전목마의 높이는 시간에 따라 어떻게 변할까?</h3>
        <p>놀이공원에서 회전목마를 타고 일정한 속도로 빙글빙글 돌고 있다고 생각해보세요.<br>
        나의 <b>위치(높이)</b>는 시간에 따라 오르락내리락 일정하게 반복됩니다.<br>
        이런 <b>반복되는 원운동을 수학적으로 매끄럽게 표현해 주는 도구</b>가 바로 <b>삼각함수</b>입니다!</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("⚙️ 회전 상황 조작기")
        time_slider = st.slider("시간 (초 / 각도 조작)", 0, 360, 45, step=5, help="슬라이더를 움직여 회전목마의 위치를 바꿔보세요.")
        speed = st.selectbox("회전 속도 체감", ["보통 (1x)", "빠름 (2x)"])

        rad = np.radians(time_slider)
        y_pos = np.sin(rad)
        x_pos = np.cos(rad)

        st.info(f"⏱ 현재 회전각: **{time_slider}°** | 📏 현재 상대 높이(Y축): **{y_pos:.2f}**")

    with col2:
        fig = go.Figure()
        theta = np.linspace(0, 2*np.pi, 100)
        fig.add_trace(go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines', name='회전 궤도', line=dict(color='lightgray', dash='dash')))
        fig.add_trace(go.Scatter(x=[-1.2, 1.2], y=[0, 0], mode='lines', line=dict(color='gray', width=1), showlegend=False))
        fig.add_trace(go.Scatter(x=[0, 0], y=[-1.2, 1.2], mode='lines', line=dict(color='gray', width=1), showlegend=False))
        fig.add_trace(go.Scatter(x=[0, x_pos], y=[0, y_pos], mode='lines+markers', name='회전 반지름', line=dict(color='blue', width=3)))
        fig.add_trace(go.Scatter(x=[x_pos], y=[y_pos], mode='markers', marker=dict(size=14, color='red'), name='회전목마(점)'))
        fig.add_trace(go.Scatter(x=[x_pos, 1.3], y=[y_pos, y_pos], mode='lines', line=dict(color='red', dash='dot'), name='높이 표시선'))

        fig.update_layout(
            title="🎠 회전목마의 실시간 위치",
            xaxis=dict(range=[-1.5, 1.5], scaleanchor="y", scaleratio=1),
            yaxis=dict(range=[-1.5, 1.5]),
            height=380,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)

    st.success("💡 **핵심 요약**: 일정한 원운동을 시간을 축으로 길게 늘려놓으면 연못의 물결 모양 같은 **사인(Sine) 파동 그래프**가 탄생합니다!")

# -----------------------------------------------------------------------------
# MENU 2: 개념 학습
# -----------------------------------------------------------------------------
elif menu == "2. 개념 학습 📖":
    st.markdown("<div class='main-header'>📖 삼각함수 기초 개념 Master</div>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["STEP 1. 각과 호도법 (Radian)", "STEP 2. 단위원과 삼각함수의 정의"])

    with tab1:
        st.subheader("1️⃣ 60분법(°) vs 호도법(Radian)")
        st.markdown("""
        - **60분법**: 원 한 바퀴를 360등분한 단위 (`1°`, `90°`, `180°` ...)
        - **호도법(라디안)**: **반지름의 길이와 호의 길이가 같아질 때의 각도**를 `1 라디안(rad)`으로 정의합니다.
        - **핵심 관계식**: **$180^\circ = \pi \text{ rad}$**  |  **$360^\circ = 2\pi \text{ rad}$**
        """)

        deg_input = st.select_slider(
            "각도를 조작해보세요:",
            options=[0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360],
            value=60
        )

        rad_val = np.radians(deg_input)
        pi_factor = deg_input / 180.0

        col_a, col_b = st.columns([1, 1])
        with col_a:
            st.markdown(f"""
            <div class='concept-box'>
                <h4>📐 입력된 각도 변환 계산</h4>
                <ul>
                    <li>60분법 각도: <b>{deg_input}°</b></li>
                    <li>호도법(라디안): <b>{pi_factor:.2f} $\pi$ rad</b> (${rad_val:.4f}\text{{ rad}}$)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with col_b:
            fig_rad = go.Figure()
            t = np.linspace(0, 2*np.pi, 100)
            fig_rad.add_trace(go.Scatter(x=np.cos(t), y=np.sin(t), mode='lines', line=dict(color='lightgray')))
            t_sub = np.linspace(0, rad_val, 50)
            fig_rad.add_trace(go.Scatter(x=np.append([0], np.cos(t_sub)), y=np.append([0], np.sin(t_sub)), fill='toself', fillcolor='rgba(59, 130, 246, 0.2)', line=dict(color='blue'), name='각 영역'))
            fig_rad.update_layout(xaxis=dict(range=[-1.2, 1.2]), yaxis=dict(range=[-1.2, 1.2], scaleanchor="x", scaleratio=1), height=300, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_rad, use_container_width=True)

    with tab2:
        st.subheader("2️⃣ 단위원(Unit Circle) 위에서 삼각함수의 정의")
        st.markdown("""
        반지름이 1인 원(단위원) 위에서 동경(각도)이 나타내는 점 $P(x, y)$가 있을 때:
        - **$\cos \theta = x$ 좌표** (가로 위치)
        - **$\sin \theta = y$ 좌표** (세로 높이)
        - **$\tan \theta = \\frac{y}{x}$** (직선의 기울기)
        """)

        angle = st.slider("단위원 위의 점 P 움직이기 (각도 θ):", 0, 360, 45, step=5)
        rad_a = np.radians(angle)
        x_pt = np.cos(rad_a)
        y_pt = np.sin(rad_a)

        c1, c2 = st.columns([1, 1])
        with c1:
            fig_unit = go.Figure()
            t = np.linspace(0, 2*np.pi, 100)
            fig_unit.add_trace(go.Scatter(x=np.cos(t), y=np.sin(t), mode='lines', line=dict(color='gray', dash='dot')))
            fig_unit.add_trace(go.Scatter(x=[-1.3, 1.3], y=[0, 0], mode='lines', line=dict(color='black', width=1)))
            fig_unit.add_trace(go.Scatter(x=[0, 0], y=[-1.3, 1.3], mode='lines', line=dict(color='black', width=1)))
            fig_unit.add_trace(go.Scatter(x=[0, x_pt], y=[0, 0], mode='lines', line=dict(color='blue', width=4), name='cos θ (x좌표)'))
            fig_unit.add_trace(go.Scatter(x=[x_pt, x_pt], y=[0, y_pt], mode='lines', line=dict(color='red', width=4), name='sin θ (y좌표)'))
            fig_unit.add_trace(go.Scatter(x=[0, x_pt], y=[0, y_pt], mode='lines+markers', line=dict(color='black', width=2), marker=dict(size=8, color='green'), name='동경 P'))

            fig_unit.update_layout(xaxis=dict(range=[-1.4, 1.4]), yaxis=dict(range=[-1.4, 1.4], scaleanchor="x", scaleratio=1), height=380, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_unit, use_container_width=True)

        with c2:
            st.markdown(f"""
            <div class='card'>
                <h4>📍 각도 $\theta = {angle}^\circ$ 일 때 삼각함수 값</h4>
                <p>🔹 <b>$\cos({angle}^\circ)$</b> (x좌표) = <span style='color:blue; font-weight:bold;'>{x_pt:.4f}</span></p>
                <p>🔹 <b>$\sin({angle}^\circ)$</b> (y좌표) = <span style='color:red; font-weight:bold;'>{y_pt:.4f}</span></p>
                <p>🔹 <b>$\tan({angle}^\circ)$</b> (기울기) = <span style='color:green; font-weight:bold;'>{np.tan(rad_a):.4f}</span> (단, 90°, 270°는 정의되지 않음)</p>
            </div>
            """, unsafe_allow_html=True)

            st.warning("💡 **꼭 기억하세요!** 단위원 위를 돌 때 **x좌표는 코사인(cos)**, **y좌표는 사인(sin)**입니다!")

# -----------------------------------------------------------------------------
# MENU 3: 그래프 실험실
# -----------------------------------------------------------------------------
elif menu == "3. 그래프 실험실 🔬":
    st.markdown("<div class='main-header'>🔬 삼각함수 그래프 실험실</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>$y = A \\sin(Bx + C) + D$ 변수 계수를 직접 움직이며 그래프의 변화를 관찰하세요.</div>", unsafe_allow_html=True)

    func_type = st.radio("기본 삼각함수 선택:", ["Sine (sin)", "Cosine (cos)", "Tangent (tan)"], horizontal=True)

    col_ctrl, col_graph = st.columns([1, 2])

    with col_ctrl:
        st.subheader("⚙️ 계수 조작 파라미터")
        A = st.slider("진폭 (A)", -3.0, 3.0, 1.0, step=0.5, help="그래프의 위아래 확장/반전 (진폭)")
        B = st.slider("주기 관련 계수 (B)", 0.5, 4.0, 1.0, step=0.5, help="그래프의 좌우 압축/팽창 (주기)")
        C_deg = st.slider("위상 이동 계수 (C)", -180, 180, 0, step=30, help="x축 방향 평행이동")
        D = st.slider("상하 이동 (D)", -3.0, 3.0, 0.0, step=0.5, help="y축 방향 평행이동")

        C = np.radians(C_deg)

    x = np.linspace(-2*np.pi, 2*np.pi, 500)
    
    if "sin" in func_type:
        y = A * np.sin(B * x + C) + D
        func_symbol = r"\sin"
    elif "cos" in func_type:
        y = A * np.cos(B * x + C) + D
        func_symbol = r"\cos"
    else:
        y = A * np.tan(B * x + C) + D
        y[np.abs(y) > 10] = np.nan
        func_symbol = r"\tan"

    with col_graph:
        fig_lab = go.Figure()

        if "sin" in func_type:
            fig_lab.add_trace(go.Scatter(x=x, y=np.sin(x), mode='lines', name='기본 y = sin(x)', line=dict(color='lightgray', dash='dash')))
        elif "cos" in func_type:
            fig_lab.add_trace(go.Scatter(x=x, y=np.cos(x), mode='lines', name='기본 y = cos(x)', line=dict(color='lightgray', dash='dash')))

        fig_lab.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'y = {A}{func_symbol}({B}x + {C_deg}°) + {D}', line=dict(color='#2563EB', width=3)))

        fig_lab.update_layout(
            title=f"수식: y = {A} {func_type[:3]}({B}x + {C_deg}°) + {D}",
            xaxis=dict(
                tickmode='array',
                tickvals=[-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
                ticktext=['-2π', '-π', '0', 'π', '2π']
            ),
            yaxis=dict(range=[-5, 5]),
            height=400,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_lab, use_container_width=True)

    st.markdown("### 💡 AI 그래프 실시간 분석 리포트")
    
    analysis_text = []
    if abs(A) != 1.0:
        analysis_text.append(f"• **진폭(A={A})**: 그래프의 최댓값과 최솟값의 폭이 **{abs(A)}배** 변했습니다.")
    
    period = (2 * np.pi / abs(B)) if "tan" not in func_type else (np.pi / abs(B))
    period_str = f"{period/np.pi:.2f}π"
    analysis_text.append(f"• **주기(B={B})**: 한 번 파동이 반복되는 **주기가 [{period_str}]**로 변했습니다.")
    
    if C_deg != 0:
        shift_x = -C_deg / B
        analysis_text.append(f"• **위상 이동(C={C_deg}°)**: 그래프가 x축 방향으로 **{shift_x:.1f}° 만큼 평행이동**했습니다.")
    if D != 0:
        analysis_text.append(f"• **상하 이동(D={D})**: 중심선이 y = {D} 로 **위아래로 {D}만큼 이동**했습니다.")

    if "tan" not in func_type:
        max_val = abs(A) + D
        min_val = -abs(A) + D
        analysis_text.append(f"• 📈 **현재 함수의 최댓값**: **{max_val:.2f}** | 📉 **최솟값**: **{min_val:.2f}**")

    st.info("\n".join(analysis_text))

    st.markdown("---")
    st.subheader("🔄 단위원운동 ➔ 사인 그래프 연동 애니메이션")

    anim_angle = st.slider("회전 재생 조작기 (각도):", 0, 720, 120, step=10)
    anim_rad = np.radians(anim_angle)

    col_u, col_g = st.columns([1, 2])
    with col_u:
        fig_u = go.Figure()
        t = np.linspace(0, 2*np.pi, 100)
        fig_u.add_trace(go.Scatter(x=np.cos(t), y=np.sin(t), mode='lines', line=dict(color='gray', dash='dot')))
        fig_u.add_trace(go.Scatter(x=[0, np.cos(anim_rad)], y=[0, np.sin(anim_rad)], mode='lines+markers', line=dict(color='red', width=3)))
        fig_u.update_layout(title="단위원 (원운동)", xaxis=dict(range=[-1.3, 1.3]), yaxis=dict(range=[-1.5, 1.5], scaleanchor="x", scaleratio=1), height=300)
        st.plotly_chart(fig_u, use_container_width=True)

    with col_g:
        fig_g = go.Figure()
        x_range = np.linspace(0, 4*np.pi, 300)
        fig_g.add_trace(go.Scatter(x=x_range, y=np.sin(x_range), mode='lines', line=dict(color='lightgray')))
        fig_g.add_trace(go.Scatter(x=[anim_rad], y=[np.sin(anim_rad)], mode='markers', marker=dict(size=12, color='red'), name='현재 높이'))
        fig_g.update_layout(
            title="y = sin(x) 그래프 (높이의 궤적)",
            xaxis=dict(tickmode='array', tickvals=[0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi], ticktext=['0', 'π', '2π', '3π', '4π']),
            yaxis=dict(range=[-1.5, 1.5]),
            height=300
        )
        st.plotly_chart(fig_g, use_container_width=True)

# -----------------------------------------------------------------------------
# MENU 4: 인터랙티브 그래프 퀴즈
# -----------------------------------------------------------------------------
elif menu == "4. 인터랙티브 그래프 퀴즈 🎯":
    st.markdown("<div class='main-header'>🎯 인터랙티브 그래프 맞추기 퀴즈</div>", unsafe_allow_html=True)
    st.markdown("제시된 **목표 조건**에 맞게 슬라이더를 조작하여 정확한 삼각함수 그래프를 완성해 보세요!")

    st.markdown("""
    <div class='concept-box'>
        <h4>🎯 오늘의 미션 퀘스트</h4>
        <p>다음 조건을 만족하는 <b>y = A sin(Bx) + D</b> 그래프를 만드세요.</p>
        <ul>
            <li><b>최댓값: 3</b>, <b>최솟값: -1</b></li>
            <li><b>주기: π (180°)</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    user_A = st.slider("조작 A (진폭)", 0.5, 4.0, 1.0, step=0.5, key="q_A")
    user_B = st.slider("조작 B (주기 계수)", 0.5, 4.0, 1.0, step=0.5, key="q_B")
    user_D = st.slider("조작 D (상하 이동)", -2.0, 3.0, 0.0, step=0.5, key="q_D")

    target_A, target_B, target_D = 2.0, 2.0, 1.0

    if st.button("🚀 정답 확인하기"):
        if user_A == target_A and user_B == target_B and user_D == target_D:
            st.markdown("<div class='success-box'>🎉 <b>정답입니다! 완벽해요!</b><br>진폭 A=2, 주기계수 B=2(주기 π), Y축 이동 D=1을 정확하게 맞추셨습니다!</div>", unsafe_allow_html=True)
            st.session_state.lab_quiz_cleared = True
        else:
            st.markdown("<div class='error-box'>❌ <b>아직 목표와 조금 다릅니다. 아래 힌트를 확인해 보세요!</b></div>", unsafe_allow_html=True)
            
            feedback = []
            if user_A + user_D != 3 or -user_A + user_D != -1:
                feedback.append("• 💡 **높이 힌트**: 최댓값이 3, 최솟값이 -1이 되려면 (진폭 A)와 (상하 이동 D)의 합과 차를 생각해보세요.")
            if user_B != target_B:
                feedback.append("• 💡 **주기 힌트**: 주기가 π가 되려면 공식 $2\pi / B = \pi$ 에서 B의 값은 얼마일까요?")
            
            for fb in feedback:
                st.write(fb)

    x_q = np.linspace(0, 2*np.pi, 300)
    y_user = user_A * np.sin(user_B * x_q) + user_D
    y_target = target_A * np.sin(target_B * x_q) + target_D

    fig_q = go.Figure()
    fig_q.add_trace(go.Scatter(x=x_q, y=y_target, mode='lines', name='목표 정답 그래프', line=dict(color='green', dash='dot', width=2)))
    fig_q.add_trace(go.Scatter(x=x_q, y=y_user, mode='lines', name='내가 만든 그래프', line=dict(color='blue', width=3)))
    fig_q.update_layout(yaxis=dict(range=[-4, 5]), height=350)
    st.plotly_chart(fig_q, use_container_width=True)

# -----------------------------------------------------------------------------
# MENU 5: 문제 풀기 및 단계별 힌트
# -----------------------------------------------------------------------------
elif menu == "5. 문제 풀기 📝":
    st.markdown("<div class='main-header'>📝 삼각함수 단계별 평가 및 문제 풀기</div>", unsafe_allow_html=True)

    problems = [
        {
            "id": 1,
            "type": "유형 A. 기본 개념",
            "question": "각도 120°를 호도법(라디안)으로 올바르게 나타낸 것은?",
            "options": ["π/3 rad", "2π/3 rad", "3π/4 rad", "5π/6 rad"],
            "answer": "2π/3 rad",
            "hint1": "180°가 π 라디안이라는 사실을 떠올려보세요.",
            "hint2": "120° = 180° × (120/180) 입니다.",
            "hint3": "120/180을 약분하면 2/3가 됩니다.",
            "explanation": "180° = π rad 이므로, 120° = 120 × (π / 180) = 2π/3 rad 입니다."
        },
        {
            "id": 2,
            "type": "유형 B. 그래프 읽기",
            "question": "함수 y = 3 sin(2x) + 1 의 최댓값과 주기는 각각 얼마일까요?",
            "options": [
                "최댓값: 4, 주기: π",
                "최댓값: 3, 주기: 2π",
                "최댓값: 4, 주기: 2π",
                "최댓값: 3, 주기: π"
            ],
            "answer": "최댓값: 4, 주기: π",
            "hint1": "최댓값은 (진폭 A) + (상하 이동 D) 로 구합니다.",
            "hint2": "주기는 기본주기 2π를 x의 계수인 B(=2)로 나누어야 합니다.",
            "hint3": "최댓값 = 3 + 1 = 4 / 주기 = 2π / 2 = π 입니다.",
            "explanation": "진폭 A=3, D=1 이므로 최댓값은 3+1 = 4 입니다. x의 계수 B=2 이므로 주기는 2π / 2 = π 가 됩니다."
        }
    ]

    for p in problems:
        st.markdown(f"#### [{p['type']}] Q{p['id']}. {p['question']}")
        user_choice = st.radio(f"정답을 선택하세요 (Q{p['id']}):", p['options'], key=f"q_radio_{p['id']}")

        col_h1, col_h2 = st.columns([1, 1])

        with col_h1:
            h_key = f"hint_{p['id']}"
            if h_key not in st.session_state.hint_level:
                st.session_state.hint_level[h_key] = 0

            if st.button(f"💡 힌트 보기 (현재 {st.session_state.hint_level[h_key]}/3 단계)", key=f"h_btn_{p['id']}"):
                if st.session_state.hint_level[h_key] < 3:
                    st.session_state.hint_level[h_key] += 1

            lvl = st.session_state.hint_level[h_key]
            if lvl >= 1:
                st.markdown(f"<div class='hint-box'><b>힌트 1단계:</b> {p['hint1']}</div>", unsafe_allow_html=True)
            if lvl >= 2:
                st.markdown(f"<div class='hint-box'><b>힌트 2단계:</b> {p['hint2']}</div>", unsafe_allow_html=True)
            if lvl >= 3:
                st.markdown(f"<div class='hint-box'><b>힌트 3단계:</b> {p['hint3']}</div>", unsafe_allow_html=True)

        with col_h2:
            if st.button(f"✅ 정답 제출 (Q{p['id']})", key=f"sub_btn_{p['id']}"):
                if user_choice == p['answer']:
                    st.success("🎉 정답입니다!")
                    st.session_state.quiz_score += 1
                else:
                    st.error("❌ 오답입니다.")
                    wrong_entry = {
                        "question": p['question'],
                        "user_ans": user_choice,
                        "correct_ans": p['answer'],
                        "explanation": p['explanation']
                    }
                    if wrong_entry not in st.session_state.wrong_answers:
                        st.session_state.wrong_answers.append(wrong_entry)

                    st.markdown(f"""
                    <div class='error-box'>
                        <b>왜 틀렸을까? (오답 해설)</b><br>
                        {p['explanation']}
                    </div>
                    """, unsafe_allow_html=True)
        st.markdown("---")

# -----------------------------------------------------------------------------
# MENU 6: 오답 / 복습 노트
# -----------------------------------------------------------------------------
elif menu == "6. 오답 / 복습 노트 📓":
    st.markdown("<div class='main-header'>📓 나의 오답 & 복습 노트</div>", unsafe_allow_html=True)

    if not st.session_state.wrong_answers:
        st.info("🎉 틀린 문제가 없습니다! 아주 훌륭합니다.")
    else:
        st.warning(f"총 {len(st.session_state.wrong_answers)}개의 복습할 문제가 있습니다.")
        for idx, item in enumerate(st.session_state.wrong_answers):
            st.markdown(f"""
            <div class='card'>
                <h4>📌 오답 문제 #{idx+1}</h4>
                <p><b>문제:</b> {item['question']}</p>
                <p>❌ <b>내가 제출한 답:</b> <span style='color:red;'>{item['user_ans']}</span></p>
                <p>✅ <b>정답:</b> <span style='color:green;'>{item['correct_ans']}</span></p>
                <hr>
                <p>💡 <b>상세 바른 풀이 설명:</b><br>{item['explanation']}</p>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MENU 7: 삼각함수 도우미
# -----------------------------------------------------------------------------
elif menu == "7. 삼각함수 도우미 🤖":
    st.markdown("<div class='main-header'>🤖 삼각함수 챗봇 도우미</div>", unsafe_allow_html=True)
    st.caption("공통수학1 삼각함수에 대해 궁금한 점을 무엇이든 질문하세요!")

    faq = st.selectbox(
        "자주 묻는 질문(FAQ)을 선택해 보세요:",
        [
            "질문을 선택하세요...",
            "왜 180도가 파이(π) 라디안인가요?",
            "사인이랑 코사인은 평행이동하면 똑같아지나요?",
            "탄젠트는 왜 주기와 최댓값이 다른가요?"
        ]
    )

    if faq == "왜 180도가 파이(π) 라디안인가요?":
        st.chat_message("assistant").write("원 한 바퀴의 둘레는 $2\pi r$ 입니다. 반지름 $r=1$인 단위원에서 원 전체의 호의 길이는 $2\pi$가 되죠. 원 한 바퀴가 $360^\circ$이므로 $360^\circ = 2\pi \text{ rad}$ 이고, 양변을 2로 나누면 **$180^\circ = \pi \text{ rad}$** 가 됩니다!")
    elif faq == "사인이랑 코사인은 평행이동하면 똑같아지나요?":
        st.chat_message("assistant").write("네, 맞습니다! 사인 그래프를 x축 방향으로 $-\pi/2$ (90°)만큼 평행이동하면 코사인 그래프와 완전히 겹치게 됩니다. 즉, $\cos(x) = \sin(x + \pi/2)$ 의 관계가 성립합니다.")
    elif faq == "탄젠트는 왜 주기와 최댓값이 다른가요?":
        st.chat_message("assistant").write("탄젠트는 $\tan \theta = \\frac{y}{x}$ (기울기)로 정의됩니다. x가 0이 되는 $90^\circ, 270^\circ$ 등에서는 분모가 0이 되어 값이 무한히 커지므로 **최댓값과 최솟값이 없습니다(없음)**. 또한 반 바퀴만 돌아도 기울기 패턴이 똑같이 반복되므로 **주기가 $2\pi$가 아닌 $\pi$**입니다.")

    user_q = st.chat_input("삼각함수에 대해 추가로 궁금한 점을 입력하세요...")
    if user_q:
        st.chat_message("user").write(user_q)
        st.chat_message("assistant").write(f"'{user_q}'에 대한 질문이군요! 삼각함수에서 각도는 회전한 양, 함숫값은 단위원의 좌표(x: cos, y: sin, 기울기: tan)라는 기본 원리를 항상 기억하세요!")
