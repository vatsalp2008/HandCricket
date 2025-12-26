# HandCricket 🏏

A Python-based Hand Cricket game featuring two versions: a classic implementation and an advanced edition with AI difficulty levels, special moves, achievements, and comprehensive statistics tracking.

## 📖 About

Hand Cricket is a popular number-guessing cricket game where players compete by choosing numbers (0-6). When both players select the same number, the batsman is out. Otherwise, the batsman scores runs equal to their chosen number.

## 🎮 Game Versions

### Basic Version (`hand_cricket.py`)
Simple, straightforward Hand Cricket with:
- Traditional toss mechanics (ODD/EVEN)
- Numbers 0-10 for gameplay
- Basic bat/bowl decision
- Score tracking and match results

### Advanced Version (`advance.py`)
Feature-rich edition including:
- 🎨 Colorful ASCII art interface
- 🤖 4 AI difficulty levels (Easy/Medium/Hard/Legend)
- ⚡ Special moves (Power Hits & Defensive Blocks)
- 📊 Comprehensive statistics and achievements
- 🎯 Smart adaptive AI
- 📈 Live scorecard with animations

## 🚀 Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/HandCricket.git
cd HandCricket

# Run basic version
python hand_cricket.py

# Run advanced version
python advance.py
```

**Requirements:** Python 3.6+

## 🎯 How to Play

1. **Toss**: Win the toss to choose batting or bowling
2. **Batting**: Choose numbers (0-6), avoid matching the bowler's number
3. **Bowling**: Match the batsman's number to get them out
4. **Winning**: Score more runs than your opponent

### Special Moves (Advanced Version Only)
- **Power Hit (P)**: Double your runs (3 per innings)
- **Defensive Block (D)**: Avoid getting out (3 per innings)

## 🏆 Features Comparison

| Feature | Basic | Advanced |
|---------|-------|----------|
| Core Gameplay | ✅ | ✅ |
| Colorful UI | ❌ | ✅ |
| Multiple Difficulties | ❌ | ✅ |
| Special Moves | ❌ | ✅ |
| Statistics Tracking | ❌ | ✅ |
| Achievements | ❌ | ✅ |
| Smart AI | ❌ | ✅ |
| Animated Interface | ❌ | ✅ |

## 📊 Statistics & Achievements

Track your performance with:
- Matches played/won
- Win rate percentage
- Total runs and highest score
- Unlockable achievements

**Achievements include:**
- 🎯 Century Maker (100+ runs)
- 💪 Dominator (Win by 50+ runs)
- And more!

## 🛠️ Technical Stack

- **Language**: Python 3.x
- **Modules**: random, time, os, json, datetime, enum, typing
- **Features**: ANSI color codes, OOP design, type hints

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📝 Future Roadmap

- [ ] Tournament mode
- [ ] Multiplayer support
- [ ] Persistent game saves
- [ ] Leaderboard system
- [ ] GUI version
- [ ] Mobile app

## 👤 Author

**Vatsal Patel**
- GitHub: [@vatsalpatel](https://github.com/yourusername)
- Northeastern University - MS in Computer Science

## 📄 License

Open source under the MIT License.

---

**Ready to play? Choose your version and start batting! 🏏**