"""
🪨✂️📄 Tosh-Qaychi-Qog'oz (Streamlit)
"""

import streamlit as st
import random

def show():
    st.title("🪨✂️📄 Tosh-Qaychi-Qog'oz")
    
    # Initialize game state
    if 'rps_score' not in st.session_state:
        st.session_state.rps_score = {'player': 0, 'bot': 0}
    if 'rps_mode' not in st.session_state:
        st.session_state.rps_mode = None
    
    # Game info
    st.info("🎯 Birinchi 3 ochko yig'gan g'olib!")
    
    # Mode selection
    if st.session_state.rps_mode is None:
        st.markdown("### O'yin rejimini tanlang:")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🤖 Bot bilan o'ynash", key="rps_bot"):
                st.session_state.rps_mode = "bot"
                st.session_state.rps_score = {'player': 0, 'bot': 0}
                st.rerun()
        with col2:
            st.info("👥 1vs1 rejimi hozircha mavjud emas")
    else:
        # Show score
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.metric("👤 Siz", st.session_state.rps_score['player'])
        with col2:
            st.markdown("<h3 style='text-align: center;'>🆚</h3>", unsafe_allow_html=True)
        with col3:
            st.metric("🤖 Bot", st.session_state.rps_score['bot'])
        
        # Check winner
        if st.session_state.rps_score['player'] >= 3:
            st.success("🎉 SIZ YUTDINGIZ! Tabriklaymiz!")
            if 'stats' in st.session_state:
                st.session_state.stats['wins'] += 1
                st.session_state.stats['total_games'] += 1
            if st.button("🔄 Yana o'ynash"):
                st.session_state.rps_mode = None
                st.session_state.rps_score = {'player': 0, 'bot': 0}
                st.rerun()
            return
        
        elif st.session_state.rps_score['bot'] >= 3:
            st.error("😔 BOT YUTDI! Keyingi safar omad!")
            if 'stats' in st.session_state:
                st.session_state.stats['losses'] += 1
                st.session_state.stats['total_games'] += 1
            if st.button("🔄 Yana o'ynash"):
                st.session_state.rps_mode = None
                st.session_state.rps_score = {'player': 0, 'bot': 0}
                st.rerun()
            return
        
        # Game buttons
        st.markdown("### Tanlovingizni qiling:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🪨 Tosh", key="rock", use_container_width=True):
                play_round("rock")
        
        with col2:
            if st.button("✂️ Qaychi", key="scissors", use_container_width=True):
                play_round("scissors")
        
        with col3:
            if st.button("📄 Qog'oz", key="paper", use_container_width=True):
                play_round("paper")
        
        # Reset button
        if st.button("🔄 Qaytadan boshlash"):
            st.session_state.rps_mode = None
            st.session_state.rps_score = {'player': 0, 'bot': 0}
            st.rerun()


def play_round(player_choice):
    """Bir raund o'ynash"""
    choices = ['rock', 'scissors', 'paper']
    bot_choice = random.choice(choices)
    
    emoji_map = {'rock': '🪨', 'scissors': '✂️', 'paper': '📄'}
    
    # Determine winner
    result = None
    if player_choice == bot_choice:
        result = "draw"
    elif (player_choice == 'rock' and bot_choice == 'scissors') or \
         (player_choice == 'scissors' and bot_choice == 'paper') or \
         (player_choice == 'paper' and bot_choice == 'rock'):
        result = "win"
        st.session_state.rps_score['player'] += 1
    else:
        result = "loss"
        st.session_state.rps_score['bot'] += 1
    
    # Show result
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### 👤 Siz: {emoji_map[player_choice]}")
    with col2:
        st.markdown(f"### 🤖 Bot: {emoji_map[bot_choice]}")
    
    if result == "win":
        st.success("🎉 Siz yutdingiz bu raundda!")
    elif result == "loss":
        st.error("😔 Bot yutdi bu raundda!")
    else:
        st.info("🤝 Durrang!")
    
    st.rerun()
