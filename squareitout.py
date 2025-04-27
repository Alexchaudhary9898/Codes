start = int(input("enter start of range: "))
end = int(input("enter end of range: "))
squares = [i ** 2 for i in range(start, end + 1)]
print("\nSquares of numbers from", start, "to", end, ":\n". squares)
even_squares = [num for num in squares if num % 2 == 0]
odd_squares = [num for num in squares if num % 2 !- 0]
print("\nEven square values", even_squares)
print("odd squares values:", odd_squares)