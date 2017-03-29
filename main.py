"""
Google Code Jam 2016: Qualification Round, Problem A: Bleatrix
https://code.google.com/codejam/contest/6254486/dashboard#s=p0&a=1

---Problem---

    Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N. 
Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits 
in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so 
far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.

    Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, suppose that 
Bleatrix picks N = 1692. She would count as follows:

    * N = 1692. Now she has seen the digits 1, 2, 6, and 9.
    * 2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
    * 3N = 5076. Now she has seen all ten digits, and falls asleep.

    What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA 
instead.

---Input---

    The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line 
with a single integer N, the number Bleatrix has chosen.

---Output---

    For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y 
is the last number that Bleatrix will name before falling asleep, according to the rules described in the statement.

---Limits---

1 ≤ T ≤ 100.

---Small dataset---

0 ≤ N ≤ 200.

---Large dataset---

0 ≤ N ≤ 106.

"""

__author__ = "H.D. 'Chip' McCullough IV"

# Define file I/O locations
DATASET_SMALL = './inputs/A-small-practice.in'
DATASET_LARGE = './inputs/A-large-practice.in'
OUT_SMALL = './outputs/A-small-practice.out'
OUT_LARGE = './outputs/A-large-practice.out'

# Define base case
case = 1


def make_tired(number: int, iteration: int, found: list) -> int:
    """
    Parse param:number and add unique digits [0-9] 
    :param number: Bleatrix's current number
    :type number: int
    :param iteration: Bleatrix's current iteration
    :type number: int
    :return: Bleatrix's final iteration falling asleep
    """
    if not isinstance(number, int):
        raise TypeError

    if len(found) == 10:
        return (iteration - 1)
    elif number == 0:
        return -1
    else:
        parse = str(number)
        for digit in parse:
            if digit not in found:
                found.append(digit)
        return make_tired((iteration + 1) * N, (iteration + 1), found)


if __name__ == "__main__":
    f_in = open(DATASET_LARGE, 'r')                                        # Open input dataset
    f_out = open(OUT_LARGE, 'w')                                           # Open output dataset
    T = int(f_in.readline())                                               # Get number of tests

    while (case <= T):
        N = int(f_in.readline())                                           # Get next number
        final = make_tired(N, 1, [])                                       # Begin counting
        if (final == -1):                                                  # All 10 digits were not found
            f_out.write("Case #{0}: INSOMNIA\n".format(case))
        else:                                                              # All 10 digits were found
            f_out.write("Case #{0}: {1}\n".format(case, (final * N)))
        case += 1

    f_in.close()
    f_out.close()