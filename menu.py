class MenuItem:
    """Represents a single menu item with ingredients and pricing.
    
    Defines a beverage option with its name, required ingredients,
    and cost.
    
    Attributes:
        name (str): Display name of the menu item.
        cost (float): Price of the item in dollars.
        ingredients (dict): Required ingredients with quantities.
            Keys: 'water' (ml), 'milk' (ml), 'coffee' (g).
    
    Example:
        >>> latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
        >>> print(f"{latte.name} costs ${latte.cost}")
        latte costs $2.5
    """
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Manages available menu items and drink lookup.
    
    Maintains a collection of available beverages and provides
    functionality to list options and find specific drinks.
    
    Attributes:
        menu (list): Collection of MenuItem objects available for order.
    
    Example:
        >>> menu = Menu()
        >>> print(menu.get_items())
        latte/espresso/cappuccino/
    """
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Generate formatted string of all available menu items.
        
        Returns:
            str: Slash-separated list of menu item names (e.g., "latte/espresso/").
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Search menu for a drink by name.
        
        Performs case-sensitive search for a menu item matching
        the provided name. Prints error message if not found.
        
        Args:
            order_name (str): Name of the drink to find.
        
        Returns:
            MenuItem: The matching menu item if found, None otherwise.
        
        Example:
            >>> menu = Menu()
            >>> drink = menu.find_drink("latte")
            >>> print(drink.name)
            latte
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
