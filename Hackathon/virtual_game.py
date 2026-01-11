import random

def final(days,cash,shares,price,starting_cash):
    final_value = cash + shares * price
    print("\n🏁 Simulation Over!")
    print_status(days, price, cash, shares)
    print(f"💼 Final Portfolio Value: ${final_value:.2f}")
    profit = final_value - starting_cash
    if profit > 0:
        print(f"🎉 You made a profit of ${profit:.2f}!")
    elif profit < 0:
        print(f"🔻 You lost ${-profit:.2f}.")
    else:
        print("😐 You broke even.")

def print_status(day, price, cash, shares):
    print(f"\n📅 Day {day}")
    print(f"📈 Stock Price: ${price}")
    print(f"💰 Cash: ${cash}")
    print(f"📦 Shares Owned: {shares}")
    print(f"📊 Portfolio Value: ${cash + shares * price}")

def playground_print_status(price, shares):
    print(f"\n📅 Day ∞")
    print(f"📈 Stock Price: ${price}")
    print(f"💰 Cash: ∞")
    print(f"📦 Shares Owned: {shares}")
    print(f"📊 Portfolio Value: ∞")
    

def virtual_trading_game(days=10, starting_cash=1000):
    cash = starting_cash
    shares = 0
    price = round(random.uniform(50, 150), 2)

    print("💹 Welcome To Trade Payground!")
    print(f"🎯 Goal: Grow your portfolio in {days} days.\n")
    
    mode = input("Choose Mode Playground or Finace:  ")
    if mode == "Finace":
        for i in range(days):
            price = round(random.uniform(50, 150), 2)
            print_status(days, price, cash, shares)
            ask = input("Choose a action BUY, SELL, HOLD:")
            if ask == "BUY":
                if cash >= price:
                    cash = cash - price
                    print("✅:) You bought 1 stock for",price)
                    shares = shares+1
                else:
                    print("❌:( You need",str(price)+"$ for this stock Balance:",cash)
            elif ask=="SELL":
                if shares <= 0:
                    print("❌:( You need one ore more shares")
                else:
                    shares=shares-1
                    print("✅:) You sold 1 stock")        
            elif ask == "HOLD":
                print("🤔:| Day held")
            days = days-1
            
            if days == 0:
                final(days,cash,shares,price,starting_cash)
    elif mode == "Playground":
        while True:
            price = round(random.uniform(50, 150), 2)
            playground_print_status(days, price, cash, shares)
            ask = input("Choose a action BUY, SELL, HOLD:")
            if ask == "BUY":
                cash = cash - price
                print("✅ You bought 1 stock for",price)
                shares = shares+1
            elif ask=="SELL":
                if shares <= 0:
                    print("❌ You need one ore more shares")
                else:
                    shares=shares-1
                    print("✅ You sold 1 stock")        
            elif ask == "HOLD":
                print("🤔 Day held")
            days = days+1
            

if __name__ == "__main__":
    virtual_trading_game()