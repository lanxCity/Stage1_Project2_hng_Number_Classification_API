def classify_func(num):
    """
    Classify a number based on its properties.
    @param int num: int
    """
    original_num = num

    def is_even():
        return num % 2 == 0

    def is_prime():
        """Efficient prime check (skips even numbers & unnecessary divisions)."""
        if num < 2:
            return False
        if num in (2, 3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def is_armstrong():
        """
        An Armstrong number (also known as a narcissistic number) is a number
        that is equal to the sum of its own digits, each raised to the power of
        the number of digits.

        - Count the digits of the number.
        - This tells you the power to which each digit should be raised.
        - For each digit, raise it to the power of the number of digits, then sum these values.
        - Check if the sum is equal to the original number.
        """
        if num < 0:  # Perfect numbers must be positive
            return False

        str_num = str(num)
        power = len(str_num)
        return sum(int(i) ** power for i in str_num) == num

    def is_perfect():
        """
                A perfect number is a number that is equal to the sum of its proper divisors (excluding itself).
        👉      Example: 6 (1 + 2 + 3 = 6) and 28 (1 + 2 + 4 + 7 + 14 = 28).

                since we are using sq-root, we should add both "i" and "num // i" to total for every loop.
                But to avoid the last factor or square-root to be added twice, we use "if i != num // i"
                - Using 36 as example,

                i	x // i	Condition (i != x // i)	Added Values
                -------------------------------------------------
                2 	18	    ✅ Yes	                  2 + 18
                3	12	    ✅ Yes	                  3 + 12
                4	9	    ✅ Yes	                  4 + 9
                6	6	    ❌ No	                  Only 6 (not added twice)

        """
        if num <= 1:  # Perfect numbers must be positive
            return False

        total = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        return num == total

    def digit_sum():
        """
        sum of each digit inside the number
        """
        return sum(int(i) for i in str(abs(num)))

    properties = ["even" if is_even() else "odd"]

    if is_armstrong():
        properties.insert(0, "armstrong")

    return {
        "number": int(original_num),
        "is_prime": is_prime(),
        "is_perfect": is_perfect(),
        "properties": properties,
        "digit_sum": digit_sum(),
    }
