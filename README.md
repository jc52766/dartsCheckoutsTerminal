# 🎯 Darts Checkout Practice

A terminal-based program to help you practice darts checkouts. The program presents random checkout scores and validates your dart combinations, ensuring they follow proper darts rules (must finish on a double).

## Features

- **Random Checkout Generation**: Generates valid checkout scores between 2-170 (excludes impossible checkouts like 169, 168, 166, 165, 163, 162, 159)
- **Bullseye Support**: Full support for both outer bull (25) and double bull (50)
- **Input Validation**: Ensures checkouts end with a double and dart combinations are valid
- **Clear Feedback**: Shows whether your attempt is correct or incorrect with helpful error messages
- **Continuous Practice**: Automatically generates new checkouts after successful attempts

## Installation & Usage

1. Ensure you have Python 3 installed
2. Run the program:
   ```bash
   python3 main.py
   ```

## Input Notation

- `s` or no prefix = Single (e.g., `s20` or `20` = Single 20)
- `d` = Double (e.g., `d20` = Double 20)
- `t` = Triple (e.g., `t20` = Triple 20)
- `db` = Double Bull (50 points)
- `ob` = Outer Bull (25 points)

### Examples
- `t20s20d20` = Triple 20 + Single 20 + Double 20 = 120
- `s19t20d20` = Single 19 + Triple 20 + Double 20 = 99
- `t18db` = Triple 18 + Double Bull = 104

## Example Gameplay

```
🎯 Darts Checkout Practice
==============================
Enter your darts using notation like: t20s20d20 or t18db
s = single, d = double, t = triple
db = double bull (50), ob = outer bull (25)
Examples:
  t20s20d20 = Triple 20, Single 20, Double 20
  t18db = Triple 18, Double Bull
Type 'quit' to exit

Checkout: 120
Your darts: t20s20d20
✅ Correct!
Solution: T20 + 20 + D20

Checkout: 99
Your darts: s19t20d20
✅ Correct!
Solution: 19 + T20 + D20

Checkout: 104
Your darts: t18db
✅ Correct!
Solution: T18 + DB

Checkout: 87
Your darts: t20s20d10
❌ Total score 90 doesn't match checkout 87
Try again...
Your darts: t17d18
✅ Correct!
Solution: T17 + D18

Checkout: 50
Your darts: s20s20s10
❌ Checkout must end with a double
Try again...
Your darts: db
✅ Correct!
Solution: DB

Checkout: 145
Your darts: t20t19d16
❌ Invalid input: Triple 19 is not valid
Try again...
Your darts: t20t15d25
✅ Correct!
Solution: T20 + T15 + D25

Checkout: 32
Your darts: quit
Thanks for practicing! 🎯
```

## Rules

1. **Must finish on a double**: All valid checkouts must end with a double (including double bull)
2. **Maximum 3 darts**: You can use up to 3 darts to complete a checkout
3. **Valid dart scores**: Singles and doubles 1-20, triples 1-20, outer bull (25), double bull (50)
4. **No invalid combinations**: Triple bull (t25) is not allowed, doubles/triples above 20 (except bull) are invalid

## Error Handling

The program provides clear feedback for common mistakes:
- Invalid dart scores or combinations
- Checkouts that don't end with a double
- Incorrect total scores
- Too many darts (more than 3)
- Invalid notation

Type `quit` at any time to exit the program.
