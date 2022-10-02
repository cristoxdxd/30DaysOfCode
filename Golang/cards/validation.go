package main

import (
	"fmt"
	"strconv"
)

func main() {
	var cardNumber string
	fmt.Print("Enter a card number: ")
	fmt.Scanln(&cardNumber)
	fmt.Println("Valid: ", validate(cardNumber))
}

func validate(cardNumber string) bool {
	var sum int
	for i := 0; i < len(cardNumber); i++ {
		digit, _ := strconv.Atoi(string(cardNumber[i]))
		if i%2 == 0 {
			digit *= 2
			if digit > 9 {
				digit -= 9
			}
		}
		sum += digit
	}
	return sum % 10 == 0
}
