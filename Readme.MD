# 🪓 Hangman — Python CLI Game

> A terminal-based word guessing game built in Python. Six lives. One word. Can you survive?

---

## 🚀 Quick Start

```bash
git clone https://github.com/MazharulNibir1/Hangman_game.git
cd Hangman_game
python main.py
```

No dependencies. Pure Python standard library.

---

## 🎮 How to Play

- A random word is selected from a 20-word bank
- Guess one letter at a time
- 6 wrong guesses = game over
- Reveal the full word before lives run out to win

---

## ⚙️ Features

- ✅ ASCII hangman that updates live each wrong guess
- ✅ Input validation (single letters only, no repeats)
- ✅ Wrong letter tracker displayed each turn
- ✅ Win/lose detection with word reveal
- ✅ Replay prompt after each game

---

## 🗂️ Project Structure

```
Hangman_game/
├── main.py          # Game loop, display, input handling
├── game_logic.txt   # Game design notes / logic reference
└── README.md
```

---

## 🧠 Game Logic

```
word selected → display blanks → player guesses letter
     ↓
  correct? → fill blank → all filled? → WIN
  wrong?   → lives - 1 → lives = 0?  → LOSE
```

State tracked per turn:
- `word` — secret word
- `guessed` — set of all attempted letters
- `wrong` — list of incorrect guesses
- `lives` — starts at 6, decrements on wrong guess

---

## 🖼️ Preview

```
   -----
   |   |
   O   |
  /|\  |
       |
       |
=========

Word:   _ p p _ e   | Lives: 3
Wrong:  ['x', 'z', 'q']
Guess a letter: 
```

---

## 🛠️ Built With

- Python 3
- `random` module (stdlib)

---

## 📌 What I Learned

- Structuring a CLI game loop with clean separation of concerns
- Using Python sets for O(1) membership checks on guessed letters
- Handling edge cases: repeat guesses, non-alpha input, multi-char input
- Managing game state across turns without external libraries

---

## 🔮 Potential Improvements

- [ ] Difficulty levels (word length / fewer lives)
- [ ] Category-based word banks
- [ ] Score tracker across sessions
- [ ] Hints system

---

## 👤 Author

**Nibir** — [@MazharulNibir1](https://github.com/MazharulNibir1)