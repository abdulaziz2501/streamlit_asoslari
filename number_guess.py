"""
🔢 Son Topish O'yini (Streamlit)
"""

import streamlit as st
import random

def show():
    st.title("🔢 Son Topish O'yini")
    
    # Initialize state
    if 'number_range' not in st.session_state:
        st.session_state.number_range = None
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = None
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'guesses' not in st.session_state:
        st.session_state.guesses = []
    
    # Range selection
    if st.session_state.number_range is None:
        st.markdown("### Diapazonni tanlang:")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("1-10", use_container_width=True):
                start_game(1, 10)
            if st.button("1-100", use_container_width=True):
                start_game(1, 100)
        
        with col2:
            if st.button("1-50", use_container_width=True):
                start_game(1, 50)
            if st.button("1-1000", use_container_width=True):
                start_game(1, 1000)
    
    else:
        min_num, max_num = st.session_state.number_range
        
        # Game info
        st.info(f"🎯 Men {min_num} va {max_num} orasidagi sonni tanladim!")
        
        # Stats
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🎯 Urinishlar", st.session_state.attempts)
        with col2:
            if st.session_state.guesses:
                st.metric("📊 Oxirgi taxmin", st.session_state.guesses[-1])
        
        # Input
        guess = st.number_input(
            "Taxminingizni kiriting:",
            min_value=min_num,
            max_value=max_num,
            step=1,
            key="number_input"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Tekshirish", use_container_width=True):
                check_guess(int(guess))
        
        with col2:
            if st.button("🏳️ Taslim bo'lish", use_container_width=True):
                surrender()


def start_game(min_num, max_num):
    """O'yinni boshlash"""
    st.session_state.number_range = (min_num, max_num)
    st.session_state.secret_number = random.randint(min_num, max_num)
    st.session_state.attempts = 0
    st.session_state.guesses = []
    st.rerun()


def check_guess(guess):
    """Taxminni tekshirish"""
    st.session_state.attempts += 1
    st.session_state.guesses.append(guess)
    
    secret = st.session_state.secret_number
    difference = abs(secret - guess)
    
    if guess == secret:
        st.balloons()
        st.success(f"🎉 TABRIKLAYMIZ! SIZ YUTDINGIZ!")
        st.success(f"✅ To'g'ri javob: {secret}")
        st.info(f"🎯 Urinishlar: {st.session_state.attempts}")
        
        if st.session_state.attempts <= 3:
            st.success("🏆 A'lo! Juda tez topdingiz!")
        elif st.session_state.attempts <= 5:
            st.success("🥇 Zo'r! Yaxshi natija!")
        elif st.session_state.attempts <= 10:
            st.info("🥈 Yaxshi! Davom eting!")
        else:
            st.info("🥉 Topasiz! Mashq qiling!")
        
        if 'stats' in st.session_state:
            st.session_state.stats['wins'] += 1
            st.session_state.stats['total_games'] += 1
        
        if st.button("🔄 Yana o'ynash"):
            st.session_state.number_range = None
            st.session_state.secret_number = None
            st.session_state.attempts = 0
            st.session_state.guesses = []
            st.rerun()
    else:
        # Yo'nalish
        if guess < secret:
            direction = "📈 Katta son"
        else:
            direction = "📉 Kichik son"
        
        # Yaqinlik
        if difference <= 5:
            hint = "🔥 Juda yaqin!"
        elif difference <= 10:
            hint = "♨️ Yaqin!"
        elif difference <= 20:
            hint = "🌡️ Issiq!"
        elif difference <= 50:
            hint = "❄️ Sovuq!"
        else:
            hint = "🧊 Juda sovuq!"
        
        st.warning(f"{direction} - {hint}")
        st.rerun()


def surrender():
    """Taslim bo'lish"""
    st.error(f"🏳️ TASLIM BO'LDINGIZ")
    st.info(f"To'g'ri javob: {st.session_state.secret_number}")
    st.info(f"Urinishlar: {st.session_state.attempts}")
    
    if 'stats' in st.session_state:
        st.session_state.stats['losses'] += 1
        st.session_state.stats['total_games'] += 1
    
    if st.button("🔄 Yana o'ynash"):
        st.session_state.number_range = None
        st.session_state.secret_number = None
        st.session_state.attempts = 0
        st.session_state.guesses = []
        st.rerun()
