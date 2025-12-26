import random
import time
import os
import json
from datetime import datetime
from enum import Enum
from typing import Dict, List, Tuple, Optional

class Color:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class GameMode(Enum):
    QUICK = "quick"
    TOURNAMENT = "tournament"
    PRACTICE = "practice"

class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    LEGEND = "legend"

class Player:
    """Represents a player with statistics"""
    def __init__(self, name: str, is_human: bool = True):
        self.name = name
        self.is_human = is_human
        self.stats = {
            'matches_played': 0,
            'matches_won': 0,
            'total_runs': 0,
            'highest_score': 0,
            'total_wickets': 0,
            'best_bowling': 0
        }
        self.current_score = 0
        self.balls_faced = 0
        self.wickets_taken = 0

class HandCricketPro:
    """Enhanced Hand Cricket Game with advanced features"""
    
    def __init__(self):
        self.player = None
        self.computer = Player("Computer", is_human=False)
        self.difficulty = Difficulty.MEDIUM
        self.game_history = []
        self.special_moves = {
            'power_hit': 3,  # Limited power hits per innings
            'defensive_block': 3,  # Limited defensive blocks
            'super_over': False  # Unlocked after certain achievements
        }
        self.achievements = []
        self.commentary_lines = [
            "What a shot! That's going to the boundary!",
            "Excellent bowling! The batsman is under pressure!",
            "The crowd goes wild!",
            "That's a close call!",
            "Brilliant fielding saves runs!",
            "The tension is building up!",
            "What a game we're witnessing today!"
        ]
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Display game banner"""
        banner = f"""
{Color.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  {Color.YELLOW}██╗  ██╗ █████╗ ███╗   ██╗██████╗     {Color.GREEN}██████╗██████╗   {Color.CYAN}║
║  {Color.YELLOW}██║  ██║██╔══██╗████╗  ██║██╔══██╗    {Color.GREEN}██╔════╝██╔══██╗  {Color.CYAN}║
║  {Color.YELLOW}███████║███████║██╔██╗ ██║██║  ██║    {Color.GREEN}██║     ██████╔╝  {Color.CYAN}║
║  {Color.YELLOW}██╔══██║██╔══██║██║╚██╗██║██║  ██║    {Color.GREEN}██║     ██╔══██╗  {Color.CYAN}║
║  {Color.YELLOW}██║  ██║██║  ██║██║ ╚████║██████╔╝    {Color.GREEN}╚██████╗██║  ██║  {Color.CYAN}║
║  {Color.YELLOW}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     {Color.GREEN} ╚═════╝╚═╝  ╚═╝  {Color.CYAN}║
║                                                              ║
║            {Color.WHITE}🏏 CRICKET PRO - ULTIMATE EDITION 🏏{Color.CYAN}            ║
╚══════════════════════════════════════════════════════════════╝{Color.RESET}
        """
        print(banner)
    
    def show_main_menu(self):
        """Display main menu"""
        self.clear_screen()
        self.print_banner()
        print(f"\n{Color.BOLD}MAIN MENU{Color.RESET}")
        print("═" * 40)
        print(f"{Color.GREEN}1.{Color.RESET} Quick Match")
        print(f"{Color.GREEN}2.{Color.RESET} Tournament Mode")
        print(f"{Color.GREEN}3.{Color.RESET} Practice Session")
        print(f"{Color.GREEN}4.{Color.RESET} View Statistics")
        print(f"{Color.GREEN}5.{Color.RESET} Settings")
        print(f"{Color.GREEN}6.{Color.RESET} How to Play")
        print(f"{Color.GREEN}7.{Color.RESET} Exit Game")
        print("═" * 40)
        
    def get_player_name(self):
        """Get player name with validation"""
        while True:
            name = input(f"\n{Color.CYAN}Enter your name (3-15 characters): {Color.RESET}").strip()
            if 3 <= len(name) <= 15:
                return name
            print(f"{Color.RED}Name must be between 3 and 15 characters!{Color.RESET}")
    
    def animated_toss(self):
        """Animated coin toss"""
        print(f"\n{Color.YELLOW}🪙 Tossing the coin...{Color.RESET}")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print()
    
    def conduct_toss(self) -> Tuple[bool, str]:
        """Conduct the toss with animation"""
        print(f"\n{Color.BOLD}TOSS TIME!{Color.RESET}")
        print("Choose: 1. Heads  2. Tails")
        
        while True:
            choice = input("Your choice (1/2): ").strip()
            if choice in ['1', '2']:
                break
            print(f"{Color.RED}Invalid choice! Enter 1 or 2{Color.RESET}")
        
        self.animated_toss()
        
        result = random.choice(['1', '2'])
        result_text = "Heads" if result == '1' else "Tails"
        
        print(f"Result: {Color.YELLOW}{result_text}!{Color.RESET}")
        
        won_toss = choice == result
        
        if won_toss:
            print(f"{Color.GREEN}🎉 You won the toss!{Color.RESET}")
            print("\nChoose: 1. Bat First  2. Bowl First")
            while True:
                decision = input("Your choice (1/2): ").strip()
                if decision in ['1', '2']:
                    return True, 'bat' if decision == '1' else 'bowl'
                print(f"{Color.RED}Invalid choice!{Color.RESET}")
        else:
            print(f"{Color.RED}Computer won the toss!{Color.RESET}")
            decision = 'bat' if random.random() < 0.5 else 'bowl'
            print(f"Computer chooses to {decision} first")
            return False, 'bowl' if decision == 'bat' else 'bat'
    
    def get_computer_number(self, is_batting: bool, player_score: int = 0) -> int:
        """AI for computer based on difficulty"""
        if self.difficulty == Difficulty.EASY:
            return random.randint(0, 6)
        
        elif self.difficulty == Difficulty.MEDIUM:
            if is_batting:
                # Moderate risk-taking
                if player_score > 50:
                    return random.choices([0,1,2,3,4,5,6], weights=[5,10,15,20,20,15,15])[0]
                else:
                    return random.choices([0,1,2,3,4,5,6], weights=[5,10,10,15,25,20,15])[0]
            else:
                # Try to predict patterns
                return random.randint(0, 6)
        
        elif self.difficulty == Difficulty.HARD:
            if is_batting:
                # Smart batting based on score
                if player_score > 100:
                    return random.choices([0,1,2,3,4,5,6], weights=[10,15,20,20,15,10,10])[0]
                else:
                    return random.choices([0,1,2,3,4,5,6], weights=[5,10,10,15,30,20,10])[0]
            else:
                # Better prediction
                common_numbers = [1, 2, 3, 4]
                if random.random() < 0.7:
                    return random.choice(common_numbers)
                return random.randint(0, 6)
        
        else:  # LEGEND
            # Super intelligent AI
            if is_batting:
                if player_score > 150:
                    return random.choices([0,1,2], weights=[30,40,30])[0]
                elif player_score > 100:
                    return random.choices([1,2,3,4], weights=[20,30,30,20])[0]
                else:
                    return random.choices([3,4,5,6], weights=[20,30,30,20])[0]
            else:
                # Advanced pattern recognition (simplified)
                return random.choices([1,2,3,4,5,6], weights=[20,20,20,20,10,10])[0]
    
    def display_scorecard(self, batting_player: Player, bowling_player: Player, target: Optional[int] = None):
        """Display live scorecard"""
        print(f"\n{Color.BOLD}╔{'═'*50}╗{Color.RESET}")
        print(f"{Color.BOLD}║{'SCORECARD':^50}║{Color.RESET}")
        print(f"{Color.BOLD}╠{'═'*50}╣{Color.RESET}")
        
        print(f"{Color.BOLD}║{Color.YELLOW} {batting_player.name:20} {Color.RESET}{Color.BOLD}│{Color.GREEN} Score: {batting_player.current_score:3}/{batting_player.wickets_taken} {Color.RESET}{Color.BOLD}║{Color.RESET}")
        
        if target:
            runs_needed = target - batting_player.current_score
            print(f"{Color.BOLD}║{Color.CYAN} Target: {target:3} {Color.RESET}{Color.BOLD}│{Color.MAGENTA} Need {runs_needed} runs to win {Color.RESET}{Color.BOLD}║{Color.RESET}")
        
        print(f"{Color.BOLD}╚{'═'*50}╝{Color.RESET}")
    
    def play_innings(self, batting_player: Player, bowling_player: Player, target: Optional[int] = None) -> int:
        """Play one innings"""
        batting_player.current_score = 0
        batting_player.balls_faced = 0
        consecutive_dots = 0
        power_hits_left = self.special_moves['power_hit']
        blocks_left = self.special_moves['defensive_block']
        
        print(f"\n{Color.BOLD}{batting_player.name} is batting!{Color.RESET}")
        
        while True:
            self.display_scorecard(batting_player, bowling_player, target)
            
            # Special moves display
            if batting_player.is_human:
                print(f"\n{Color.MAGENTA}Special Moves - Power Hits: {power_hits_left} | Defensive Blocks: {blocks_left}{Color.RESET}")
            
            # Get inputs
            if batting_player.is_human:
                print("\nChoose your number (0-6):")
                if power_hits_left > 0:
                    print(f"{Color.YELLOW}Press 'P' for Power Hit (2x runs if successful){Color.RESET}")
                if blocks_left > 0:
                    print(f"{Color.CYAN}Press 'D' for Defensive Block (avoid out but score 0){Color.RESET}")
                
                user_input = input("Your choice: ").strip().upper()
                
                # Handle special moves
                use_power = False
                use_block = False
                
                if user_input == 'P' and power_hits_left > 0:
                    use_power = True
                    power_hits_left -= 1
                    user_num = random.randint(3, 6)  # Power hits are aggressive
                    print(f"{Color.YELLOW}⚡ POWER HIT ACTIVATED!{Color.RESET}")
                elif user_input == 'D' and blocks_left > 0:
                    use_block = True
                    blocks_left -= 1
                    user_num = -1  # Special value for block
                    print(f"{Color.CYAN}🛡️ DEFENSIVE BLOCK!{Color.RESET}")
                else:
                    try:
                        user_num = int(user_input)
                        if user_num < 0 or user_num > 6:
                            print(f"{Color.RED}Invalid input! Enter 0-6{Color.RESET}")
                            continue
                    except ValueError:
                        print(f"{Color.RED}Invalid input!{Color.RESET}")
                        continue
                
                comp_num = self.get_computer_number(False, batting_player.current_score)
            else:
                user_num = self.get_computer_number(True, batting_player.current_score)
                comp_num = int(input(f"\n{bowling_player.name}, enter your number (0-6): "))
                use_power = False
                use_block = False
            
            # Display the numbers
            time.sleep(0.5)
            print(f"\n{batting_player.name}: {user_num if user_num != -1 else 'BLOCK'} | {bowling_player.name}: {comp_num}")
            
            # Check for out
            if user_num == comp_num and not use_block:
                print(f"\n{Color.RED}🎯 OUT! {batting_player.name} is dismissed!{Color.RESET}")
                print(random.choice(["What a wicket!", "The bowler strikes!", "That's the end of the innings!"]))
                break
            
            # Calculate runs
            if use_block:
                runs = 0
                print(f"{Color.CYAN}Block successful! No runs, but still batting.{Color.RESET}")
            elif use_power:
                runs = user_num * 2
                print(f"{Color.YELLOW}⚡ Power Hit! {runs} runs scored!{Color.RESET}")
            else:
                runs = user_num
            
            batting_player.current_score += runs
            batting_player.balls_faced += 1
            
            # Commentary
            if runs == 0:
                consecutive_dots += 1
                if consecutive_dots >= 3:
                    print(f"{Color.YELLOW}Pressure building! {consecutive_dots} dot balls in a row!{Color.RESET}")
            else:
                consecutive_dots = 0
                if runs == 6:
                    print(f"{Color.GREEN}🎆 SIX! What a shot!{Color.RESET}")
                elif runs >= 4:
                    print(f"{Color.GREEN}FOUR! Excellent shot!{Color.RESET}")
            
            # Check target
            if target and batting_player.current_score > target:
                print(f"\n{Color.GREEN}🏆 {batting_player.name} wins!{Color.RESET}")
                break
        
        return batting_player.current_score
    
    def play_match(self):
        """Play a complete match"""
        self.clear_screen()
        print(f"{Color.BOLD}STARTING MATCH{Color.RESET}")
        print("═" * 50)
        
        # Toss
        won_toss, user_choice = self.conduct_toss()
        
        # Determine innings order
        if user_choice == 'bat':
            first_innings_player = self.player
            second_innings_player = self.computer
        else:
            first_innings_player = self.computer
            second_innings_player = self.player
        
        # First Innings
        print(f"\n{Color.BOLD}FIRST INNINGS{Color.RESET}")
        print("─" * 50)
        first_score = self.play_innings(first_innings_player, second_innings_player)
        
        print(f"\n{Color.BOLD}INNINGS BREAK{Color.RESET}")
        print(f"{first_innings_player.name} scored: {Color.YELLOW}{first_score} runs{Color.RESET}")
        print(f"Target for {second_innings_player.name}: {Color.CYAN}{first_score + 1} runs{Color.RESET}")
        input("\nPress Enter to continue...")
        
        # Second Innings
        self.clear_screen()
        print(f"\n{Color.BOLD}SECOND INNINGS{Color.RESET}")
        print("─" * 50)
        second_score = self.play_innings(second_innings_player, first_innings_player, first_score)
        
        # Match Result
        self.display_match_result(first_innings_player, first_score, second_innings_player, second_score)
        
        # Update statistics
        self.update_stats(first_innings_player, first_score, second_innings_player, second_score)
        
        input("\nPress Enter to return to main menu...")
    
    def display_match_result(self, first_player: Player, first_score: int, second_player: Player, second_score: int):
        """Display match result with graphics"""
        print(f"\n{Color.BOLD}{'═'*60}{Color.RESET}")
        print(f"{Color.BOLD}{'MATCH RESULT':^60}{Color.RESET}")
        print(f"{Color.BOLD}{'═'*60}{Color.RESET}")
        
        print(f"\n{first_player.name}: {first_score} runs")
        print(f"{second_player.name}: {second_score} runs")
        
        if second_score > first_score:
            winner = second_player
            margin = f"by {first_score - second_score + 1} runs"
        else:
            winner = first_player
            margin = f"by {first_score - second_score} runs"
        
        print(f"\n{Color.GREEN}🏆 {winner.name} wins {margin}! 🏆{Color.RESET}")
        print(f"{Color.BOLD}{'═'*60}{Color.RESET}")
        
        # Achievement check
        if winner.is_human and first_score > 100:
            self.unlock_achievement("Century Maker - Score 100+ runs")
        if winner.is_human and first_score - second_score > 50:
            self.unlock_achievement("Dominator - Win by 50+ runs")
    
    def unlock_achievement(self, achievement: str):
        """Unlock and display achievement"""
        if achievement not in self.achievements:
            self.achievements.append(achievement)
            print(f"\n{Color.YELLOW}🎖️ ACHIEVEMENT UNLOCKED: {achievement}{Color.RESET}")
    
    def update_stats(self, first_player: Player, first_score: int, second_player: Player, second_score: int):
        """Update player statistics"""
        # Update matches played
        if first_player.is_human:
            first_player.stats['matches_played'] += 1
            first_player.stats['total_runs'] += first_score
            if first_score > first_player.stats['highest_score']:
                first_player.stats['highest_score'] = first_score
            if second_score <= first_score:
                first_player.stats['matches_won'] += 1
    
    def show_statistics(self):
        """Display player statistics"""
        self.clear_screen()
        print(f"{Color.BOLD}PLAYER STATISTICS{Color.RESET}")
        print("═" * 50)
        
        if self.player:
            stats = self.player.stats
            print(f"\nPlayer: {Color.CYAN}{self.player.name}{Color.RESET}")
            print(f"Matches Played: {stats['matches_played']}")
            print(f"Matches Won: {stats['matches_won']}")
            if stats['matches_played'] > 0:
                win_rate = (stats['matches_won'] / stats['matches_played']) * 100
                print(f"Win Rate: {win_rate:.1f}%")
            print(f"Total Runs: {stats['total_runs']}")
            print(f"Highest Score: {stats['highest_score']}")
            
            print(f"\n{Color.YELLOW}Achievements:{Color.RESET}")
            if self.achievements:
                for achievement in self.achievements:
                    print(f"  🎖️ {achievement}")
            else:
                print("  No achievements yet!")
        else:
            print("No statistics available. Play a match first!")
        
        input("\nPress Enter to continue...")
    
    def show_settings(self):
        """Display and modify game settings"""
        self.clear_screen()
        print(f"{Color.BOLD}GAME SETTINGS{Color.RESET}")
        print("═" * 50)
        
        print(f"\nCurrent Difficulty: {Color.YELLOW}{self.difficulty.value.upper()}{Color.RESET}")
        print("\n1. Easy - Computer makes random choices")
        print("2. Medium - Computer plays strategically")
        print("3. Hard - Computer uses advanced tactics")
        print("4. Legend - Near impossible to beat")
        print("5. Back to Main Menu")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            self.difficulty = Difficulty.EASY
            print(f"{Color.GREEN}Difficulty set to EASY{Color.RESET}")
        elif choice == '2':
            self.difficulty = Difficulty.MEDIUM
            print(f"{Color.GREEN}Difficulty set to MEDIUM{Color.RESET}")
        elif choice == '3':
            self.difficulty = Difficulty.HARD
            print(f"{Color.GREEN}Difficulty set to HARD{Color.RESET}")
        elif choice == '4':
            self.difficulty = Difficulty.LEGEND
            print(f"{Color.GREEN}Difficulty set to LEGEND{Color.RESET}")
        
        if choice in ['1', '2', '3', '4']:
            time.sleep(1)
    
    def show_how_to_play(self):
        """Display game instructions"""
        self.clear_screen()
        print(f"{Color.BOLD}HOW TO PLAY{Color.RESET}")
        print("═" * 50)
        
        instructions = """
        🏏 HAND CRICKET RULES:
        
        1. BASICS:
           • Both players choose numbers from 0 to 6
           • If both choose the same number, the batsman is OUT
           • Otherwise, the batsman scores runs equal to their number
        
        2. SPECIAL MOVES (Limited per innings):
           • Power Hit (P): Double your runs if successful
           • Defensive Block (D): Avoid getting out but score 0
        
        3. WINNING:
           • First player sets a target
           • Second player tries to beat that target
           • Highest scorer wins!
        
        4. TIPS:
           • Mix up your numbers to be unpredictable
           • Use special moves strategically
           • Higher difficulty = smarter computer opponent
        
        5. ACHIEVEMENTS:
           • Score 100+ runs for Century Maker
           • Win by 50+ runs for Dominator
           • More achievements to discover!
        """
        
        print(instructions)
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main game loop"""
        self.clear_screen()
        self.print_banner()
        
        print(f"\n{Color.CYAN}Welcome to Hand Cricket Pro!{Color.RESET}")
        player_name = self.get_player_name()
        self.player = Player(player_name)
        
        while True:
            self.show_main_menu()
            choice = input(f"\n{Color.CYAN}Select option (1-7): {Color.RESET}").strip()
            
            if choice == '1':
                self.play_match()
            elif choice == '2':
                print(f"{Color.YELLOW}Tournament mode coming soon!{Color.RESET}")
                time.sleep(2)
            elif choice == '3':
                print(f"{Color.YELLOW}Practice mode coming soon!{Color.RESET}")
                time.sleep(2)
            elif choice == '4':
                self.show_statistics()
            elif choice == '5':
                self.show_settings()
            elif choice == '6':
                self.show_how_to_play()
            elif choice == '7':
                print(f"\n{Color.GREEN}Thanks for playing Hand Cricket Pro!{Color.RESET}")
                print(f"{Color.YELLOW}See you again soon! 🏏{Color.RESET}")
                break
            else:
                print(f"{Color.RED}Invalid choice! Please try again.{Color.RESET}")
                time.sleep(1)


def main():
    """Entry point of the game"""
    game = HandCricketPro()
    try:
        game.run()
    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}Game interrupted. Thanks for playing!{Color.RESET}")
    except Exception as e:
        print(f"\n{Color.RED}An error occurred: {e}{Color.RESET}")
        print("Please restart the game.")


if __name__ == "__main__":
    main()