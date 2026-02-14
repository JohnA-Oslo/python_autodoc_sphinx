class MoneyMachine:
    """Handles monetary transactions and profit tracking.
    
    Manages coin processing, payment validation, change calculation,
    and cumulative profit tracking for the coffee machine.
    
    Attributes:
        CURRENCY (str): Currency symbol for display ($).
        COIN_VALUES (dict): Mapping of coin names to decimal values.
        profit (float): Total accumulated profit from completed sales.
        money_received (float): Current transaction amount from inserted coins.
    
    Example:
        >>> machine = MoneyMachine()
        >>> machine.make_payment(2.50)
        Please insert coins.
        How many quarters?: 10
        Here is $0.00 in change.
        True
    """

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Print current profit total to console.
        
        Displays accumulated profit with currency symbol.
        """
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Prompt user to insert coins and calculate total value.
        
        Interactively requests quantities for each coin denomination
        (quarters, dimes, nickels, pennies) and calculates the total
        monetary value inserted.
        
        Returns:
            float: Total value of all coins inserted.
        """
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Process payment for a drink order.
    
        Prompts user to insert coins, validates sufficient payment,
        calculates change, and updates profit if successful.
        
        Args:
            cost (float): The price of the drink being purchased.
            
        Returns:
            bool: True if payment was accepted, False if insufficient funds.
            
        Example:
            >>> machine = MoneyMachine()
            >>> machine.make_payment(2.50)
            Please insert coins.
            How many quarters?: 10
            ...
            True
        """

        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
