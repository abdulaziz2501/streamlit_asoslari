"""
🎮 TELEGRAM GAMES WEB VERSION
Streamlit-da ishlaydigan interaktiv o'yinlar platformasi
"""

import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="🎮 Telegram Games",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .game-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stats-box {
        background: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        padding: 12px;
        border: none;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_game' not in st.session_state:
    st.session_state.current_game = None
if 'stats' not in st.session_state:
    st.session_state.stats = {
        'total_games': 0,
        'wins': 0,
        'losses': 0,
        'draws': 0
    }

# Sidebar
with st.sidebar:
    st.markdown("## 🎮 O'YINLAR MENYUSI")

    # Statistics
    st.markdown("### 📊 Statistika")
    stats = st.session_state.stats
    col1, col2 = st.columns(2)
    with col1:
        st.metric("O'yinlar", stats['total_games'])
        st.metric("Yutuqlar", stats['wins'])
    with col2:
        st.metric("Mag'lubiyat", stats['losses'])
        st.metric("Durrang", stats['draws'])

    st.markdown("---")

    # Game selection
    st.markdown("### 🎯 O'yin tanlang")

    if st.button("🪨 Tosh-Qaychi-Qog'oz"):
        st.session_state.current_game = "rps"
        st.rerun()

    if st.button("🧮 Matematik O'yin"):
        st.session_state.current_game = "math"
        st.rerun()

    if st.button("🔢 Son Topish"):
        st.session_state.current_game = "number"
        st.rerun()

    if st.button("⭕ X|O O'yini"):
        st.session_state.current_game = "tictactoe"
        st.rerun()

    if st.button("🧠 Eslab Qol"):
        st.session_state.current_game = "memory"
        st.rerun()

    st.markdown("---")

    if st.button("🏠 Bosh Sahifa"):
        st.session_state.current_game = None
        st.rerun()

    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ by Abdulaziz")
    st.markdown("Telegram: @your_username")

# Main content
if st.session_state.current_game is None:
    # Home page
    st.markdown('<h1 class="main-header">🎮 TELEGRAM GAMES</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; font-size: 1.2em; color: #666; margin-bottom: 40px;'>
        5 ta qiziqarli o'yinni bir joyda o'ynang!
    </div>
    """, unsafe_allow_html=True)

    # Game cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='game-card'>
            <h2>🪨 Tosh-Qaychi-Qog'oz</h2>
            <p>Klassik o'yin! Bot bilan yoki do'stingiz bilan o'ynang. 3 ochkogacha!</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='game-card'>
            <h2>🧮 Matematik O'yin</h2>
            <p>Matematik savollar yeching! 3 xil qiyinlik darajasi mavjud.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='game-card'>
            <h2>🔢 Son Topish</h2>
            <p>Yashirin sonni toping! Yaqin/uzoq ko'rsatmalari beriladi.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='game-card'>
            <h2>⭕ X|O O'yini</h2>
            <p>Tic-Tac-Toe! Bot bilan 3 xil qiyinlikda o'ynang.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='game-card'>
            <h2>🧠 Eslab Qol</h2>
            <p>Xotirangizni sinang! Emojilarni eslang va toping.</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_game == "rps":
    from games_web import rock_paper_scissors

    rock_paper_scissors.show()

elif st.session_state.current_game == "math":
    from games_web import math_game

    math_game.show()

elif st.session_state.current_game == "number":
    from games_web import number_guess

    number_guess.show()

elif st.session_state.current_game == "tictactoe":
    from games_web import tic_tac_toe

    tic_tac_toe.show()

elif st.session_state.current_game == "memory":
    from games_web import memory_game

    memory_game.show()
