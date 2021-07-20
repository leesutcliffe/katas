import pytest

from banking import Account
from datetime import date

acc = Account()

def test_bank_deposit():
    assert acc.deposit(100) == 100, "Test deposit"

def test_bank_withdraw():
    assert acc.withdraw(20) == 80, "Test deposit"

def test_statement_values(capfd):
    now = date.today()
    today = now.strftime("%d/%m/%Y")
    
    # expected stdout
    # DATE           AMOUNT    BALANCE   
    # 20/07/2021     +100      100.0     
    # 20/07/2021     -20       80.0  
    #
    headings = "{:<15}{:<10}{:<10}".format("DATE", "AMOUNT", "BALANCE")
    line1 = "{:<15}{:<10}{:<10}".format(today, "+100", "100.0")
    line2 = "{:<15}{:<10}{:<10}".format(today, "-20", "80.0")

    acc.printStatement()
    out, err = capfd.readouterr()
    test_sdout = headings + "\n" + line1 + "\n" + line2 + "\n"
    assert out == test_sdout
