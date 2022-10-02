# Day 5 - Luhn formula

The Luhn formula is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, National Provider Identifier numbers in the United States, Canadian Social Insurance Numbers, Israeli ID Numbers, South African ID Numbers, Greek Social Security Numbers (ΑΜΚΑ), and Greek Tax Identification Numbers (ΑΦΜ).

```python
def validCard(card):
    card = [int(x) for x in str(card)]
    card = card[::-1]
    for i in range(1, len(card), 2):
        card[i] *= 2
        if card[i] > 9:
            card[i] -= 9
    return sum(card) % 10 == 0
```

The first step for this formula in Python is to validate all the characters of the card number, if they are not numbers, the function will return false.
Then the card number is reversed, and the digits in the odd positions are multiplied by 2, if the result is greater than 9, 9 is subtracted from the result.
Finally, the sum of all the digits is calculated, and if the result is divisible by 10, the card number is valid.

This is the same process for a different number in the module.

The complete code is in there: [Luhn formula](./validation.py)