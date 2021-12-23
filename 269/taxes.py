"""Tax Bracket Calculator

Here is the break-down on how much a US citizen's income was
taxed in 2019

      $0 - $9,700   10%
  $9,701 - $39,475  12%
 $39,476 - $84,200  22%
 $84,201 - $160,725 24%
$160,726 - $204,100 32%
$204,101 - $510,300 35%
$510,301 +          37%

For example someone earning $40,000 would
pay $4,658.50, not $40,000 x 22% = $8,800!

    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50

More detail can be found here:
https://www.nerdwallet.com/blog/taxes/federal-income-tax-brackets/

Sample output from running the code in the if/main clause:

          Summary Report
==================================
 Taxable Income:        40,000.00
     Taxes Owed:         4,658.50
       Tax Rate:           11.65%

         Taxes Breakdown
==================================
    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50
"""
from dataclasses import dataclass, field
from typing import List, NamedTuple

Bracket = NamedTuple("Bracket", [("end", int), ("rate", float)])
Taxed = NamedTuple("Taxed", [("amount", float), ("rate", float), ("tax", float)])
BRACKET = [
    Bracket(9_700, 0.1),
    Bracket(39_475, 0.12),
    Bracket(84_200, 0.22),
    Bracket(160_725, 0.24),
    Bracket(204_100, 0.32),
    Bracket(510_300, 0.35),
    Bracket(510_301, 0.37),
]


class Taxes:
    """Taxes class

    Given a taxable income and optional tax bracket, it will
    calculate how much taxes are owed to Uncle Sam.

    """
    def __init__(self, income, bracket=BRACKET):
        self.income = income
        self.bracket = bracket
        self.tax_amounts = []


    def __str__(self) -> str:
        """Summary Report

        Returns:
            str -- Summary report

            Example:

                      Summary Report          
            ==================================
             Taxable Income:        40,000.00
                 Taxes Owed:         4,658.50
                   Tax Rate:           11.65%
        """
        text =  f"          Summary Report          \n"
        text += f"==================================\n"
        text += f" Taxable Income: {self.income:>16,.2f}\n"
        text += f"     Taxes Owed: {self.total:>16,.2f}\n"
        text += f"       Tax Rate: {self.tax_rate:>15.2f}%"
        return text

    def report(self):
        """Prints taxes breakdown report"""
        print(self)
        print()
        print("         Taxes Breakdown          ")
        print("==================================")
        for t in self.tax_amounts:
            print(f"{t.amount:>12,.2f} x {t.rate:1.2f} = {t.tax:>12,.2f}")
        print("----------------------------------")
        print(f"              Total = {self.total:>12,.2f}")

    @property
    def taxes(self) -> float:
        """Calculates the taxes owed

        As it's calculating the taxes, it is also populating the tax_amounts list
        which stores the Taxed named tuples.

        Returns:
            float -- The amount of taxes owed
        """
        self.tax_amounts = []
        prev_end = 0
        for idx, b in enumerate(self.bracket):
            if self.income > b.end:
                tax = (b.end - prev_end) * b.rate
                self.tax_amounts.append(Taxed(amount=b.end, rate=b.rate, tax=tax))
            elif self.income <= b.end:
                if idx == 0:
                    prev_end = 0
                else:
                    prev_end = self.bracket[idx-1].end
                amount = self.income - prev_end
                tax = amount * b.rate
                self.tax_amounts.append(Taxed(amount=amount, rate=b.rate, tax=tax))
                break
            prev_end = b.end
        taxes_owed = sum([x.tax for x in self.tax_amounts])
        return round(taxes_owed, 2)

    @property
    def total(self) -> float:
        """Calculates total taxes owed

        Returns:
            float -- Total taxes owed
        """
        return round(self.taxes, 2)

    @property
    def tax_rate(self) -> float:
        """Calculates the actual tax rate

        Returns:
            float -- Tax rate
        """
        return round((self.taxes / self.income) * 100, 2)


if __name__ == "__main__":
    salary = 40_000
    t = Taxes(salary)
    t.report()