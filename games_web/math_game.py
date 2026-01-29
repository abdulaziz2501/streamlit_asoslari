"""
🧮 Matematik O'yin (Streamlit)
"""

import streamlit as st
import random

def generate_problem(difficulty):
    """Matematik misol yaratish"""
    if difficulty == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        op = random.choice(['+', '-'])
        if op == '+':
            answer = num1 + num2
        else:
            if num1 < num2:
                num1, num2 = num2, num1
            answer = num1 - num2
        problem = f"{num1} {op} {num2}"
    
    elif difficulty == 'medium':
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        op = random.choice(['+', '-', '×'])
        if op == '+':
            answer = num1 + num2
        elif op == '-':
            if num1 < num2:
                num1, num2 = num2, num1
            answer = num1 - num2
        else:
            num1 = random.randint(2, 12)
            num2 = random.randint(2, 12)
            answer = num1 * num2
        problem = f"{num1} {op} {num2}"
    
    else:  # hard
        op = random.choice(['+', '-', '×', '÷'])
        if op == '+':
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 100)
            answer = num1 + num2
        elif op == '-':
            num1 = random.randint(50, 100)
            num2 = random.randint(10, 50)
            answer = num1 - num2
        elif op == '×':
            num1 = random.randint(5, 20)
            num2 = random.randint(5, 20)
            answer = num1 * num2
        else:
            num2 = random.randint(2, 12)
            answer = random.randint(2, 15)
            num1 = num2 * answer
        problem = f"{num1} {op} {num2}"
    
    return problem, answer


def show():
    st.title("🧮 Matematik O'yin")
    
    # Initialize state
    if 'math_difficulty' not in st.session_state:
        st.session_state.math_difficulty = None
    if 'math_problem' not in st.session_state:
        st.session_state.math_problem = None
    if 'math_answer' not in st.session_state:
        st.session_state.math_answer = None
    if 'math_score' not in st.session_state:
        st.session_state.math_score = 0
    if 'math_correct' not in st.session_state:
        st.session_state.math_correct = 0
    if 'math_total' not in st.session_state:
        st.session_state.math_total = 0
    
    # Difficulty selection
    if st.session_state.math_difficulty is None:
        st.markdown("### Qiyinlik darajasini tanlang:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("😊 Oson (1-10)", use_container_width=True):
                st.session_state.math_difficulty = 'easy'
                new_question()
                st.rerun()
        
        with col2:
            if st.button("🤔 O'rtacha (1-50)", use_container_width=True):
                st.session_state.math_difficulty = 'medium'
                new_question()
                st.rerun()
        
        with col3:
            if st.button("😰 Qiyin (1-100)", use_container_width=True):
                st.session_state.math_difficulty = 'hard'
                new_question()
                st.rerun()
    
    else:
        # Show stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🎯 Ball", st.session_state.math_score)
        with col2:
            st.metric("✅ To'g'ri", f"{st.session_state.math_correct}/{st.session_state.math_total}")
        with col3:
            percentage = (st.session_state.math_correct / st.session_state.math_total * 100) if st.session_state.math_total > 0 else 0
            st.metric("📈 Foiz", f"{percentage:.0f}%")
        
        # Show problem
        st.markdown("---")
        st.markdown(f"### Savol:")
        st.markdown(f"# {st.session_state.math_problem} = ?")
        
        # Answer input
        user_answer = st.number_input("Javobingiz:", step=1, key="math_input")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("✅ Tekshirish", use_container_width=True):
                check_answer(int(user_answer))
        
        with col2:
            if st.button("⏭️ Keyingi savol", use_container_width=True):
                new_question()
                st.rerun()
        
        with col3:
            if st.button("🏁 Tugatish", use_container_width=True):
                show_final_results()


def new_question():
    """Yangi savol yaratish"""
    problem, answer = generate_problem(st.session_state.math_difficulty)
    st.session_state.math_problem = problem
    st.session_state.math_answer = answer


def check_answer(user_answer):
    """Javobni tekshirish"""
    st.session_state.math_total += 1
    
    if user_answer == st.session_state.math_answer:
        st.session_state.math_correct += 1
        st.session_state.math_score += 10
        st.success(f"✅ TO'G'RI! {st.session_state.math_problem} = {st.session_state.math_answer}")
        if 'stats' in st.session_state:
            st.session_state.stats['wins'] += 1
    else:
        st.error(f"❌ NOTO'G'RI! To'g'ri javob: {st.session_state.math_answer}")
        if 'stats' in st.session_state:
            st.session_state.stats['losses'] += 1
    
    new_question()


def show_final_results():
    """Yakuniy natijani ko'rsatish"""
    st.markdown("---")
    st.markdown("## 🏁 O'YIN TUGADI!")
    
    total = st.session_state.math_total
    correct = st.session_state.math_correct
    score = st.session_state.math_score
    percentage = (correct / total * 100) if total > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("✅ To'g'ri javoblar", f"{correct}/{total}")
    with col2:
        st.metric("📈 Foiz", f"{percentage:.1f}%")
    with col3:
        st.metric("🎯 Ball", score)
    
    if percentage >= 90:
        st.balloons()
        st.success("🏆 A'lo! Ajoyib natija!")
    elif percentage >= 70:
        st.success("🥈 Yaxshi! Davom eting!")
    elif percentage >= 50:
        st.info("🥉 Yomon emas! Mashq qiling!")
    else:
        st.warning("💪 Mashq qiling, yaxshilanasiz!")
    
    if 'stats' in st.session_state:
        st.session_state.stats['total_games'] += 1
    
    if st.button("🔄 Yana o'ynash"):
        st.session_state.math_difficulty = None
        st.session_state.math_score = 0
        st.session_state.math_correct = 0
        st.session_state.math_total = 0
        st.rerun()
