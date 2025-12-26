** start of main.py **

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:>7.2f}" 
            lines.append(f"{description:<23}{amount}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines) 


def create_spend_chart(categories):
    total_category= len(categories)
    category_names = []
    length_array = []
    max_category_name_length=0
    

    for category in categories:
        category_names.append(category.name)
        if len(category.name)>max_category_name_length:
            max_category_name_length=len(category.name)
        total_withdrawal=0
        for ledger_item in category.ledger:
            if ledger_item['amount']<0:
                total_withdrawal+=abs(ledger_item['amount'])
        length_array.append(total_withdrawal)

    total=sum(length_array)
    percentage_array=[]
    for i in length_array:
        if total >0:
            percentage_array.append(int(((i / total) * 100) // 10) * 10)
        else:
            percentage_array.append(0)           

    master_array = ["Percentage spent by category"]
    for i in range(100,-1,-10):
        string=''
        string+=f"{i:>3}"
        string+='| '
        for j in percentage_array:
            if j>=i:
                string+='o  '
            else:
                string+='   '    
        master_array.append(string)

    master_array.append(f"{' '*4}{'-'*((total_category*3)+1)}")  


    for i in range(0,max_category_name_length):
        string='     '
        for j in category_names:
            if i < len(j):
                string+=j[i]+'  '
            else:
                string+='   '    
        master_array.append(string)

    return '\n'.join(master_array)            

** end of main.py **

