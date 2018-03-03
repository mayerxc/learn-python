balance = 2250
interestRate = .045
term = 120
counter = 1

while( counter <= term ):
    balance = balance * (1 + (interestRate / 12))
    interestEarned = balance * (interestRate / 12)
    print("Month number: {:d} \t Interest Earned: ${:.2f} \t Balance is: ${:.2f}".format(counter, interestEarned, balance) )
    counter += 1
