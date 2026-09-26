class Loan:
    #constructor/default sonstructor in the params
    def __init__(currentObject, annualInterestRate = 2, numberOfYears = 1, loanAmount = 1000, borrower = " "):
        # in the params are the defaul values. below asr private instant variables
        currentObject.__annualInterestRate = annualInterestRate
        currentObject.__numberOfYears = numberOfYears
        currentObject.__loanAmount = loanAmount
        currentObject.__borrower = borrower
        
    # SIMPLE GETTERS
    # Directly return an instance variable
    # we already know. just return the value of the instant variables value
    def getAnnualInterestRate(currentObject):
        return currentObject.__annualInterestRate
    def getNumberOfYears(currentObject):
        return currentObject.__numberOfYears
    def getLoanAmount(currentObject):
        return currentObject.__loanAmount
    def getBorrower(currentObject):
        return currentObject.__borrower
    
    #setters
    def setAnnualInterestRate(currentObject, annualInterestRate):
        currentObject.__annualInterestRate = annualInterestRate
    def setNumberOfYears(currentObject, numberOfYears):
        currentObject.__numberOfYears = numberOfYears
    def setLoanAmount(currentObject, loanAmount):
        currentObject.__loanAmount = loanAmount
    def setBorrower(currentObject, borrower):
        currentObject.__borrower = borrower
        
    # GET-STYLE METHODS THAT DO EXTRA WORK
    # They Calculate something, THEN return it
    def getMonthlyPayments(currentObject):
        monthlyInterestRate = currentObject.__annualInterestRate / 1200
        monthlyPayment = currentObject.__loanAmount * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (currentObject.__numberOfYears * 12)))
        return monthlyPayment
        
    def getTotalPayment(currentObject):
        totalPayment = currentObject.getMonthlyPayments() * currentObject.__numberOfYears * 12
        return totalPayment
    
def main():
        annualInterestRate = float(input("Enter the yearly interest rate, for example, 7.25: "))
        
        numberOfYears = int(input("/enter the number of years this shyt will be active: "))
        
        loanAmount = float(input("Enter loan amount: "))
        
        borrower = str(input("Enter borrowers mutha freakin name: "))
        
    # Remember: the params in the constructor receive the arguments in the same exact order
    # that are passed inside when creating the object.
    #
    # ARGUMENTS (main.py)               PARAMETERS (Loan class)
    # annualInterestRate  ----------->  annualInterestRate
    # numberOfYears       ----------->  numberOfYears
    # loanAmount          ----------->  loanAmount
    # borrower            ----------->  borrower
    #
        loan1 = Loan(annualInterestRate, numberOfYears, loanAmount, borrower)
        print("This loan is for ", loan1.getBorrower())
        print(f"The monthly payment is:  {loan1.getMonthlyPayments():.2f}")
        print(f"The total payment for {loan1.getBorrower()}'s ass is {loan1.getTotalPayment(): .2f}")        
        
        
main()


