total = 0
with open('day1/puzzle1-input.txt') as f:
    input = f.read().splitlines()

    for line in input:
        # extract the numbers from the line
        filtered_line = list(filter(str.isnumeric, line))
        # concatenate first and last digit if length is greater than 1 otherwise concat the first digit
        # to itself twice then convert that string into an integer and add it to our total

        total += int(filtered_line[0] + filtered_line[-1] if len(
            filtered_line) > 1 else filtered_line[0] + filtered_line[0])
print(total)
