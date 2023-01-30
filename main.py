import argparse as ap


def main(array):
    # Write to compute the variance and the mean of a given list of numbers
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    sumCounter = 0
    for i in array:
        sumCounter += i
    return sumCounter / len(array)


if __name__ == "__main__":
    argParse = ap.ArgumentParser("Variance and Mean Calculator")
    argParse.add_argument("--array", nargs="+", type=int,
                          help="Input a list of numbers to compute the variance and mean of")
    parsedArgs = argParse.parse_args()
    output = main(parsedArgs.array)
    squareCounter = 0
    for i in parsedArgs.array:
        squareCounter += (output - i)**2
    variance = squareCounter / len(parsedArgs.array)
    print('mean = ' + str(output))
    print('variance = ' + str(variance))
