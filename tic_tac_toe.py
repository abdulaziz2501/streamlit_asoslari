"""
⭕ X|O O'yini (Streamlit)
"""

import streamlit as st
import random

def show():
    st.title("⭕ X|O O'yini")
    
    # Initialize state
    if 'ttt_mode' not in st.session_state:
        st.session_state.ttt_mode = None
    if 'ttt_difficulty' not in st.session_state:
        st.session_state.ttt_difficulty = None
    if 'ttt_board' not in st.session_state:
        st.session_state.ttt_board = [['' for _ in range(3)] for _ in range(3)]
    if 'ttt_current_player' not in st.session_state:
        st.session_state.ttt_current_player = 'X'
    if 'ttt_game_over' not in st.session_state:
        st.session_state.ttt_game_over = False
    
    # Mode selection
    if st.session_state.ttt_mode is None:
        st.markdown("### O'yin rejimini tanlang:")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🤖 Bot bilan o'ynash", use_container_width=True):
                st.session_state.ttt_mode = 'bot'
                st.rerun()
        
        with col2:
            if st.button("👥 1 vs 1", use_container_width=True):
                st.session_state.ttt_mode = '1v1'
                reset_game()
                st.rerun()
    
    # Difficulty selection for bot mode
    elif st.session_state.ttt_mode == 'bot' and st.session_state.ttt_difficulty is None:
        st.markdown("### Qiyinlik darajasini tanlang:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("😊 Oson", use_container_width=True):
                st.session_state.ttt_difficulty = 'easy'
                reset_game()
                st.rerun()
        
        with col2:
            if st.button("🤔 O'rtacha", use_container_width=True):
                st.session_state.ttt_difficulty = 'medium'
                reset_game()
                st.rerun()
        
        with col3:
            if st.button("😰 Qiyin", use_container_width=True):
                st.session_state.ttt_difficulty = 'hard'
                reset_game()
                st.rerun()
    
    # Game board
    else:
        if st.session_state.ttt_mode == 'bot':
            st.info(f"🤖 Bot bilan o'ynash - Qiyinlik: {st.session_state.ttt_difficulty}")
            st.markdown("❌ Siz: X | ⭕ Bot: O")
        else:
            st.info(f"👥 1 vs 1 - Hozir: {'❌ X' if st.session_state.ttt_current_player == 'X' else '⭕ O'}")
        
        # Draw board
        for i in range(3):
            cols = st.columns(3)
            for j in range(3):
                with cols[j]:
                    cell_value = st.session_state.ttt_board[i][j]
                    button_text = cell_value if cell_value else "⬜"
                    
                    if st.button(
                        button_text,
                        key=f"cell_{i}_{j}",
                        use_container_width=True,
                        disabled=st.session_state.ttt_game_over or cell_value != ''
                    ):
                        make_move(i, j)
        
        # Control buttons
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Qaytadan boshlash", use_container_width=True):
                reset_game()
                st.rerun()
        with col2:
            if st.button("🔙 Orqaga", use_container_width=True):
                st.session_state.ttt_mode = None
                st.session_state.ttt_difficulty = None
                reset_game()
                st.rerun()


def reset_game():
    """O'yinni qaytadan boshlash"""
    st.session_state.ttt_board = [['' for _ in range(3)] for _ in range(3)]
    st.session_state.ttt_current_player = 'X'
    st.session_state.ttt_game_over = False


def make_move(row, col):
    """Yurish qilish"""
    # Player move
    st.session_state.ttt_board[row][col] = st.session_state.ttt_current_player
    
    # Check winner
    winner = check_winner()
    if winner:
        handle_game_end(winner)
        return
    
    # Bot move for bot mode
    if st.session_state.ttt_mode == 'bot' and st.session_state.ttt_current_player == 'X':
        bot_row, bot_col = get_bot_move()
        if bot_row is not None:
            st.session_state.ttt_board[bot_row][bot_col] = 'O'
            
            winner = check_winner()
            if winner:
                handle_game_end(winner)
                return
    
    # Switch player for 1v1 mode
    if st.session_state.ttt_mode == '1v1':
        st.session_state.ttt_current_player = 'O' if st.session_state.ttt_current_player == 'X' else 'X'
    
    st.rerun()


def check_winner():
    """G'olibni tekshirish"""
    board = st.session_state.ttt_board
    
    # Gorizontal va vertikal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    
    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    
    # Durrang
    if all(board[i][j] != '' for i in range(3) for j in range(3)):
        return 'draw'
    
    return None


def handle_game_end(winner):
    """O'yin tugashini boshqarish"""
    st.session_state.ttt_game_over = True
    
    if winner == 'X':
        st.balloons()
        st.success("🎉 X YUTDI!")
        if 'stats' in st.session_state and st.session_state.ttt_mode == 'bot':
            st.session_state.stats['wins'] += 1
            st.session_state.stats['total_games'] += 1
    elif winner == 'O':
        if st.session_state.ttt_mode == 'bot':
            st.error("😔 BOT YUTDI!")
            if 'stats' in st.session_state:
                st.session_state.stats['losses'] += 1
                st.session_state.stats['total_games'] += 1
        else:
            st.balloons()
            st.success("🎉 O YUTDI!")
    else:
        st.info("🤝 DURRANG!")
        if 'stats' in st.session_state:
            st.session_state.stats['draws'] += 1
            st.session_state.stats['total_games'] += 1


def get_bot_move():
    """Bot yurishi"""
    board = st.session_state.ttt_board
    difficulty = st.session_state.ttt_difficulty
    
    # Bo'sh kataklar
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    
    if not empty_cells:
        return None, None
    
    # Easy mode
    if difficulty == 'easy' and random.random() < 0.7:
        return random.choice(empty_cells)
    
    # Medium mode
    if difficulty == 'medium' and random.random() < 0.3:
        return random.choice(empty_cells)
    
    # Smart moves
    # 1. Yutish imkoniyati
    for i, j in empty_cells:
        board[i][j] = 'O'
        if check_winner() == 'O':
            board[i][j] = ''
            return i, j
        board[i][j] = ''
    
    # 2. Raqibni to'sish
    for i, j in empty_cells:
        board[i][j] = 'X'
        if check_winner() == 'X':
            board[i][j] = ''
            return i, j
        board[i][j] = ''
    
    # 3. Markaz
    if (1, 1) in empty_cells:
        return 1, 1
    
    # 4. Burchaklar
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [c for c in corners if c in empty_cells]
    if available_corners:
        return random.choice(available_corners)
    
    # 5. Random
    return random.choice(empty_cells)
