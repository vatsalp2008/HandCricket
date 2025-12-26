import random

class PlayingHandCricket:
    def play_game(self):
        sum1 = 0
        sum2 = 0
        u1 = 0
        u2 = 0
        c1 = 0
        c2 = 0
        
        # Toss
        print("Enter 'ODD' or 'EVEN' for the toss")
        toss = input().strip()
        
        print("Enter your no.")
        t1 = int(input())
        t2 = random.randint(0, 10)
        print(f"Computer's no. {t2}")
        
        t3 = t1 + t2
        
        # Check who won the toss
        user_won_toss = False
        if toss.upper() == "EVEN":
            if t3 % 2 == 0:
                user_won_toss = True
        elif toss.upper() == "ODD":
            if t3 % 2 != 0:
                user_won_toss = True
        else:
            print("Check your spelling. Wrong input")
            return
        
        if user_won_toss:
            print("You won the toss")
            print()
            print("Select whether you want to 'BOWL' or 'BAT' and enter the word")
            select = input().strip()
            
            if select.upper() == "BAT":
                # User bats first
                print("You will now bat")
                while True:
                    print("Enter your no.")
                    u1 = int(input())
                    
                    if u1 > 10 or u1 <= 0:
                        print("Invalid input. Enter a number between 1 and 10")
                        continue
                    
                    c1 = random.randint(0, 10)
                    print(f"Computer's no. {c1}")
                    
                    if u1 == c1:
                        print("You are out")
                        print(f"The target you've set is {sum1}")
                        break
                    
                    sum1 += u1
                
                # User bowls second
                print("You will now bowl")
                while True:
                    print("Enter your no.")
                    u2 = int(input())
                    
                    c2 = random.randint(0, 10)
                    print(f"Computer's no. {c2}")
                    
                    if u2 == c2:
                        print("Computer is out")
                        print(f"You won by {sum1 - sum2} runs")
                        break
                    
                    sum2 += c2
                    
                    if sum2 > sum1:
                        print("Computer won the match")
                        break
            
            elif select.upper() == "BOWL":
                # User bowls first
                print("You will now bowl")
                while True:
                    print("Enter your no.")
                    u1 = int(input())
                    
                    c1 = random.randint(0, 10)
                    print(f"Computer's no. {c1}")
                    
                    if u1 == c1:
                        print("Computer is out")
                        print(f"The target to be achieved is {sum1 + 1}")
                        break
                    
                    sum1 += c1
                
                # User bats second
                print("You will now bat")
                while True:
                    print("Enter your no.")
                    u2 = int(input())
                    
                    if u2 > 10 or u2 <= 0:
                        print("Invalid input. Enter a number between 1 and 10")
                        continue
                    
                    c2 = random.randint(0, 10)
                    print(f"Computer's no. {c2}")
                    
                    if u2 == c2:
                        print("You are out")
                        print(f"You lost by {sum1 - sum2} runs")
                        break
                    
                    sum2 += u2
                    
                    if sum2 > sum1:
                        print("You won the match")
                        break
            
            else:
                print("Check your spelling or enter the correct input")
        
        else:
            # Computer won the toss
            print("Computer won the toss")
            x1 = random.randint(0, 10)
            
            if x1 < 5:
                # Computer chooses to bowl first
                print("You will bat first")
                while True:
                    print("Enter your no.")
                    u1 = int(input())
                    
                    if u1 > 10 or u1 <= 0:
                        print("Invalid input. Enter a number between 1 and 10")
                        continue
                    
                    c1 = random.randint(0, 10)
                    print(f"Computer's no. {c1}")
                    
                    if u1 == c1:
                        print("You are out")
                        print(f"The target you've set is {sum1}")
                        break
                    
                    sum1 += u1
                
                # You bowl second
                print("You will now bowl")
                while True:
                    print("Enter your no.")
                    u2 = int(input())
                    
                    c2 = random.randint(0, 10)
                    print(f"Computer's no. {c2}")
                    
                    if u2 == c2:
                        print("Computer is out")
                        print(f"You won by {sum1 - sum2} runs")
                        break
                    
                    sum2 += c2
                    
                    if sum2 > sum1:
                        print("Computer won the match")
                        break
            
            else:
                # Computer chooses to bat first
                print("You will bowl first")
                while True:
                    print("Enter your no.")
                    u1 = int(input())
                    
                    c1 = random.randint(0, 10)
                    print(f"Computer's no. {c1}")
                    
                    if u1 == c1:
                        print("Computer is out")
                        print(f"The target to be achieved is {sum1 + 1}")
                        break
                    
                    sum1 += c1
                
                # You bat second
                print("You will now bat")
                while True:
                    print("Enter your no.")
                    u2 = int(input())
                    
                    if u2 > 10 or u2 <= 0:
                        print("Invalid input. Enter a number between 1 and 10")
                        continue
                    
                    c2 = random.randint(0, 10)
                    print(f"Computer's no. {c2}")
                    
                    if u2 == c2:
                        print("You are out")
                        print(f"You lost by {sum1 - sum2} runs")
                        break
                    
                    sum2 += u2
                    
                    if sum2 > sum1:
                        print("You won the match")
                        break


def main():
    print("Enter your name")
    name = input()
    print(f"Hello {name}")
    print("=======================")
    print("| WELCOME TO THE GAME |")
    print("=======================")
    print()
    print("WELCOME TO THE CRICKET-MANIA")
    print(".")
    print("Instructions:")
    print(".")
    print("Enter The Numbers Carefully Without Making Any Mistake.")
    print(".")
    print("If The Number Entered By The Computer Is Same As The Number Entered By You,")
    print(".")
    print("You Will Be Declared As Out.")
    print(".")
    print("Your Final Score Will Be The Sum Of The Numbers You Entered Before Getting Out.")
    print(".")
    print("After Getting Out, You Will Have To Bowl.")
    print(".")
    print("Try To Enter A Number Similar To The Number Entered By The Computer.")
    print(".")
    print("If The Sum Of Numbers Entered By The Computer Becomes More Than Your Score, It Will Win.")
    print(".")
    print("But If You Enter A Number Same As The Number Entered By The Computer, You Can Win!")
    print("***********************************************")
    print()
    
    game = PlayingHandCricket()
    game.play_game()


if __name__ == "__main__":
    main()