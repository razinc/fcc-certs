from itertools import zip_longest

class Category:

    # constructor
    def __init__(self, cat):
        self.cat = cat
        self.ledger = []
    
    def deposit(self, amount, description = ""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": self.amount, "description": self.description})

    def check_funds(self, amount):
        # amount must be negative
        if amount < 0:
            self.amount = amount
        else:
            self.amount = -amount

        self.total = 0

        for i in self.ledger:
            self.total += + i["amount"]
        self.total += self.amount

        if self.total >= 0:
            return True
        else:
            return False

    def withdraw(self, amount, description = ""):
        self.amount = -amount
        self.description = description

        if self.check_funds(self.amount) is True:
            self.ledger.append({"amount": self.amount, "description": self.description})
            return True
        else:
            return False

    def get_balance(self):
        self.total = 0
        
        for i in self.ledger:
            self.total += + i["amount"]
        return self.total
    
    def transfer(self, amount, to_cat):
        self.amount = amount
        self.to_cat = to_cat
        
        if self.check_funds(self.amount) is True:
            # update from's ledger
            self.ledger.append({"amount": self.amount, "description": "Transfer to " + self.to_cat.cat})
        
            # update to's ledger
            self.to_cat.ledger.append({"amount": abs(self.amount), "description": "Transfer from " + self.cat})
            
            return True
        else:
            return False

    def __str__(self):
        output = ""
        star_length = int((30 - len(self.cat)) / 2)
        star = "*"*star_length
        header = f"{star}{self.cat}{star}"
        output += header
        for i in self.ledger:
            description = i["description"][:23]
            amount = str(format(i["amount"], ".2f"))
            spaces = " "*(30 - len(description) - len(amount))
            output += f"\n{description}{spaces}{amount}"
        total = self.get_balance()
        output += f"\nTotal: {total}"

        return output
            
def create_spend_chart(categories):
    data = []
    names = ""
    total_total = 0
    chart = "Percentage spent by category\n"

    for cat in categories:
        # get name
        name = cat.cat
        names += f"{name} "
        
        # get total spent and sum of all total
        total = 0
        for i in cat.ledger:
            amount = i["amount"]
            if amount < 0:
                total += abs(amount)
        total_total += total

        # update data
        data.append({"name": name, "total": total})

    # update data with percentage
    for n, d in enumerate(data):
        percentage = d["total"] / total_total * 100
        d["percentage"] = percentage

    # update chart
    for p in range(100, -10, -10):
        line = f"{str(p).rjust(3)}|"

        for d in data:
            if d["percentage"] > p:
                line += " o "
            else:
                line += "   "

        line += " \n"
        chart += line

    horizontal_line = "-"*(pow(2,3) + 2)
    horizontal_line = f"    {horizontal_line}"
    chart += horizontal_line

    for name in zip_longest(*names.split(),fillvalue = " "):
        chart += "\n     " + "  ".join(name) + "  "
    
    return chart
    