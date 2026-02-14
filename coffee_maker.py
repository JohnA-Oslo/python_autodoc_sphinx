class CoffeeMaker:
    """Manages coffee machine resources and drink preparation.
    
    Tracks available ingredients (water, milk, coffee) and handles
    resource validation and deduction when preparing drinks.
    
    Attributes:
        resources (dict): Available ingredients with quantities.
            Keys: 'water' (ml), 'milk' (ml), 'coffee' (g).
    
    Example:
        >>> maker = CoffeeMaker()
        >>> maker.report()
        Water: 300ml
        Milk: 200ml
        Coffee: 100g
    """
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Print current resource levels to console.
        
        Displays remaining quantities of water (ml), milk (ml),
        and coffee (g) in a formatted report.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Check if sufficient resources exist to make a drink.
        
        Compares drink ingredient requirements against current
        resource levels. Prints error message if any ingredient
        is insufficient.
        
        Args:
            drink (MenuItem): The drink to validate resources for.
        
        Returns:
            bool: True if all ingredients are sufficient, False otherwise.
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Prepare a drink by deducting ingredients from resources.
        
        Subtracts required ingredients from available resources
        and confirms drink preparation to user.
        
        Args:
            order (MenuItem): The drink to prepare.
        
        Note:
            This method assumes resources have been validated
            via is_resource_sufficient() before calling.
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
