import random
import re

def generate_checkout():
    """Generate a random valid checkout score between 2 and 170."""
    # Invalid checkouts that cannot be finished with a double
    invalid_checkouts = {169, 168, 166, 165, 163, 162, 159}
    
    while True:
        checkout = random.randint(2, 170)
        if checkout not in invalid_checkouts:
            return checkout

def parse_input(user_input):
    """Parse user input like 't20s20d20' or 't18db' into a list of dart scores."""
    user_input = user_input.lower().strip()
    
    darts = []
    i = 0
    
    while i < len(user_input):
        # Check for bullseye patterns first
        if i + 1 < len(user_input) and user_input[i:i+2] == 'db':
            # Double bull = 50
            darts.append((50, True))
            i += 2
        elif i + 1 < len(user_input) and user_input[i:i+2] == 'ob':
            # Outer bull = 25
            darts.append((25, False))
            i += 2
        else:
            # Regular dart pattern: optional multiplier (s/d/t) followed by number
            multiplier = ''
            if user_input[i] in 'sdt':
                multiplier = user_input[i]
                i += 1
            
            # Extract number
            number_str = ''
            while i < len(user_input) and user_input[i].isdigit():
                number_str += user_input[i]
                i += 1
            
            if not number_str:
                raise ValueError("Invalid dart notation")
            
            score = int(number_str)
            
            # Validate dart score (1-20 or 25 for bull)
            if score < 1 or (score > 20 and score != 25):
                raise ValueError(f"Invalid dart score: {score}")
            
            # Apply multiplier
            if multiplier == 's' or multiplier == '':
                dart_score = score
                is_double = False
            elif multiplier == 'd':
                dart_score = score * 2
                is_double = True
            elif multiplier == 't':
                dart_score = score * 3
                is_double = False
            
            # Validate maximum possible scores
            if multiplier == 't' and score == 25:
                raise ValueError("Triple bull (t25) is not valid")
            if multiplier == 'd' and score > 20 and score != 25:
                raise ValueError(f"Double {score} is not valid")
            if multiplier == 't' and score > 20:
                raise ValueError(f"Triple {score} is not valid")
            
            darts.append((dart_score, is_double))
    
    return darts

def validate_checkout(checkout_score, darts):
    """Validate if the darts thrown complete the checkout correctly."""
    if not darts:
        return False, "No darts thrown"
    
    # Check if we have at most 3 darts
    if len(darts) > 3:
        return False, "Too many darts (maximum 3)"
    
    # Calculate total score
    total_score = sum(dart[0] for dart in darts)
    
    # Check if total matches checkout
    if total_score != checkout_score:
        return False, f"Total score {total_score} doesn't match checkout {checkout_score}"
    
    # Check if last dart is a double
    last_dart_is_double = darts[-1][1]
    if not last_dart_is_double:
        return False, "Checkout must end with a double"
    
    return True, "Correct!"

def format_darts_display(darts):
    """Format darts for display."""
    dart_strings = []
    for score, is_double in darts:
        if score == 50 and is_double:
            dart_strings.append("DB")
        elif score == 25 and not is_double:
            dart_strings.append("OB")
        elif is_double:
            dart_strings.append(f"D{score//2}")
        elif score % 3 == 0 and score <= 60 and score > 20:
            # Could be a triple
            base = score // 3
            if base <= 20:
                dart_strings.append(f"T{base}")
            else:
                dart_strings.append(f"{score}")
        else:
            dart_strings.append(f"{score}")
    
    return " + ".join(dart_strings)

def main():
    """Main game loop."""
    print("🎯 Darts Checkout Practice")
    print("=" * 30)
    print("Enter your darts using notation like: t20s20d20 or t18db")
    print("s = single, d = double, t = triple")
    print("db = double bull (50), ob = outer bull (25)")
    print("Examples:")
    print("  t20s20d20 = Triple 20, Single 20, Double 20")
    print("  t18db = Triple 18, Double Bull")
    print("Type 'quit' to exit")
    print()
    
    while True:
        checkout = generate_checkout()
        print(f"Checkout: {checkout}")
        
        while True:
            try:
                user_input = input("Your darts: ").strip()
                
                if user_input.lower() == 'quit':
                    print("Thanks for practicing! 🎯")
                    return
                
                if not user_input:
                    print("Please enter your darts or 'quit' to exit")
                    continue
                
                darts = parse_input(user_input)
                is_valid, message = validate_checkout(checkout, darts)
                
                if is_valid:
                    print(f"✅ {message}")
                    print(f"Solution: {format_darts_display(darts)}")
                    print()
                    break
                else:
                    print(f"❌ {message}")
                    print("Try again...")
                    
            except ValueError as e:
                print(f"❌ Invalid input: {e}")
                print("Try again...")
            except KeyboardInterrupt:
                print("\nThanks for practicing! 🎯")
                return

if __name__ == "__main__":
    main()
