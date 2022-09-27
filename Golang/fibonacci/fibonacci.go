package main

import "fmt"

func main() {
	var n int
	a := 0
	b := 1
	c := 0
	fmt.Print("Enter the number of terms: ")
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Print(c," ")
		c = a + b
		a = b
		b = c
	}
}
