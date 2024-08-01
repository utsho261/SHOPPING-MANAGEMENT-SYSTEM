'''
Enter your username. Ensure it starts with a lowercase letter.
Enter your password, which is your username followed by a period (.).
Example:
    1. username: utsho
       password: utsho.
    2. username: abcd
       password: abcd.
'''

header_color = "\033[95m"
text_color = "\033[94m"
border_color = "\033[92m"
instruction_color = "\033[94m"
option_color = "\033[92m"
reset_color = "\033[0m"
def display_welcome_message():

    welcome_message = f"""
    {border_color}\t\t\t\t╔═══════════════════════════════════════╗{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                WELCOME                {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                   TO                  {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                SHOPPING               {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}               MANAGEMENT              {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                 SYSTEM                {border_color}║{reset_color}
    {border_color}\t\t\t\t╚═══════════════════════════════════════╝{reset_color}
    """

    print(welcome_message)

def option():

    option = f"""
    {border_color}\t\t\t\t╔══════════════════════════════════════════╗{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}               YOUR OPTION                {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                                          {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}  1. START SHOPPING                       {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}  2. EXIT(Press 2 or Any Digit Without 1) {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                                          {border_color}║{reset_color}
    {border_color}\t\t\t\t╚══════════════════════════════════════════╝{reset_color}
    """
    print(option)

def Exit():

    exit = f"""
    {border_color}\t\t\t\t╔═══════════════════════════════════════╗{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                                       {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}             Thank You!                {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}             Come Again                {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                                       {border_color}║{reset_color}
    {border_color}\t\t\t\t╚═══════════════════════════════════════╝{reset_color}
    """
    print(exit)

def online_shopping():
    message = f"""
    {border_color}\t\t\t\t╔════════════════════════════════════════════════════════════════════════╗{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                     Welcome To Online Shopping                         {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{instruction_color}                    Please follow the instruction                       {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{option_color}                              1. Vegetables                             {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{option_color}                              2. Fruits                                 {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{option_color}                              3. Cooking                                {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{option_color}                              4. Spices                                 {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{option_color}                              5. Snacks                                 {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t╚════════════════════════════════════════════════════════════════════════╝{reset_color}
     """
    print(message)

def Bill():
    pass
def display_vegetable_details():

    header_color = "\033[95m"
    item_color = "\033[92m"
    border_color = "\033[93m"
    reset_color = "\033[0m"

    vegetable_details = f"""
    {border_color}\t\t\t\t╔═══════════════════════════════════════════════════════════════╗{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                        Vegetable details                      {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}                                                               {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                1. Morich 1KG => Price: 35TK                   {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                2. Alu 1KG => Price: 50TK                      {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                3. Peyaj 1KG => Price: 60TK                    {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                4. Roshun 1KG => Price: 120TK                  {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                5. Begun 1KG => Price: 70TK                    {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                6. Tomato 1KG => Price: 55TK                   {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                7. Gajor 1KG => Price: 35TK                    {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t╚═══════════════════════════════════════════════════════════════╝{reset_color}
    """
    print(vegetable_details)

def display_fruit_details():
    header_color = "\033[95m"
    item_color = "\033[92m"
    border_color = "\033[93m"
    reset_color = "\033[0m"

    fruit_details = f"""
    {border_color}\t\t\t\t╔═══════════════════════════════════════════════════════════════╗{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                          Fruit details                        {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}                                                               {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                1. Apple 1KG => Price: 35TK                    {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                2. Green Apple 1KG => Price: 50TK              {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                3. Orange 1KG => Price: 59TK                   {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                4. Malta 1KG => Price: 119TK                   {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                5. Banana 1KG => Price: 70TK                   {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                6. Pineapple 1KG => Price: 55TK                {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                7. Dragon Fruit 1KG => Price: 750TK            {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t╚═══════════════════════════════════════════════════════════════╝{reset_color}
    """
    print(fruit_details)

def display_cooking_details():

    header_color = "\033[95m"
    item_color = "\033[92m"
    border_color = "\033[93m"
    reset_color = "\033[0m"

    cooking_details = f"""
    {border_color}\t\t\t\t╔══════════════════════════════════════════════════════════════╗{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                        Cooking details                       {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}                                                              {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                1. Chal 1KG => Price: 35TK                    {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                2. Dal 1KG => Price: 50TK                     {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                3. Flour 1KG => Price: 59TK                   {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                4. Egg 1KG => Price: 119TK                    {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                5. Salt 1KG => Price: 70TK                    {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                6. Sugar 1KG => Price: 55TK                   {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                7. Vegetable Oil 1L => Price: 200TK           {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t╚══════════════════════════════════════════════════════════════╝{reset_color}
    """
    print(cooking_details)

def display_spices_details():
    header_color = "\033[95m"
    item_color = "\033[92m"
    border_color = "\033[93m"
    reset_color = "\033[0m"

    spices_details = f"""
    {border_color}\t\t\t\t╔═════════════════════════════════════════════════════════════╗{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                          Spices details                     {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}                                                             {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                1. Ada 1KG => Price: 35TK                    {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                2. Daruchini 1KG => Price: 50TK              {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                3. Holud 1KG => Price: 59TK                  {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                4. Lalmorich 1KG => Price: 119TK             {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                5. Golmorich 1KG => Price: 70TK              {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                6. Jira 1KG => Price: 55TK                   {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                7. Shuknamorich 1KG => Price: 35TK           {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t╚═════════════════════════════════════════════════════════════╝{reset_color}
    """
    print(spices_details)

def display_snacks_details():
    header_color = "\033[95m"
    item_color = "\033[92m"
    border_color = "\033[93m"
    reset_color = "\033[0m"

    snacks_details = f"""
    {border_color}\t\t\t\t╔═════════════════════════════════════════════════════════════╗{reset_color}
    {border_color}\t\t\t\t║{reset_color}{header_color}                           Snacks details                    {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}                                                             {border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                1. Chips 1 packet => Price: 35TK             {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                2. Noodles 1 packet => Price: 50TK           {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                3. Biscuits 1 packet => Price: 59TK          {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                4. Cake 1 packet => Price: 119TK             {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                5. Coke 1 liter => Price: 70TK               {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                6. Juice 1 liter => Price: 50TK              {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t║{reset_color}{item_color}                7. Honey nuts 1KG => Price: 1050TK           {reset_color}{border_color}║{reset_color}
    {border_color}\t\t\t\t╚═════════════════════════════════════════════════════════════╝{reset_color}
    """
    print(snacks_details)

def display_details(category_name):
    category_items = {
        "Vegetables": ["Morich", "Alu", "Peyaj", "Roshun", "Begun", "Tomato", "Gajor"],
        "Fruits": ["Apple", "Green Apple", "Orange", "Malta", "Banana", "Pineapple", "Dragon Fruit"],
        "Cooking Essentials": ["Chal", "Dal", "Flour", "Egg", "Salt", "Sugar", "Vegetable Oil"],
        "Spices": ["Ada", "Daruchini", "Holud", "Lalmorich", "Golmorich", "Jira", "Shuknamorich"],
        "Snacks": ["Chips", "Noodles", "Biscuits", "Cake", "Coke", "Juice", "Honey nuts"]
    }

    category_prices = {
        "Vegetables": [35, 50, 60, 120, 70, 55, 35],
        "Fruits": [35, 50, 59, 119, 70, 55, 750],
        "Cooking Essentials": [35, 50, 59, 119, 70, 55, 200],
        "Spices": [35, 50, 59, 119, 70, 55, 35],
        "Snacks": [35, 50, 59, 119, 70, 50, 1050]
    }

    if category_name in category_items:
        items = category_items[category_name]
        prices = category_prices[category_name]
        print(f"\n{'Item':<30} {'Price (per unit)':<20}")
        print('-' * 50)
        for i, item in enumerate(items):
            print(f"{i + 1}. {item:<30} {prices[i]:<20} Tk")
        print('-' * 50)
    else:
        print("\t\t\t\t\t\033[91mInvalid Category.\033[0m")



###########################################################################################################
purchased_items = []
quantities = []
prices = []

def add_to_cart(item_name, quantity, price):
    purchased_items.append(item_name)
    quantities.append(quantity)
    prices.append(price)

def print_bill():
    total = 0
    print(f"\n{' ' * 20}Bill Details")
    print(f"{'DESCRIPTION':<30} {'PER UNIT':<15} {'QUANTITY':<10} {'PRICE':<10}")
    print('-' * 65)

    for item, quantity, price in zip(purchased_items, quantities, prices):
        unit_price = price / quantity
        print(f"{item:<30} {unit_price:<15} {quantity:<10} {price:<10}")
        total += price

    print('-' * 65)
    print(f"{'Total':<30} {'':<15} {'':<10} {total:<5}Tk")
    print('\n')

def main():
    display_welcome_message()

    while True:
        user_name = input("\t\t\t\t\t\tEnter User Name: ").lower()
        password1 = user_name + '.'
        password = input("\t\t\t\t\t\tEnter Password: ")

        if password == password1 and 'a' <= user_name[0] <= 'z':
            while True:
                online_shopping()
                try:
                    c = int(input("\t\t\t\t\tCHOOSE YOUR OPTION (1-5): "))
                except ValueError:
                    print("\t\t\t\t\t\033[91mInvalid Input.\033[0m \n\t\t\t\t\t\033[92mTry again.\033[0m")
                    continue

                if c in [1, 2, 3, 4, 5]:
                    categories = {
                        1: (display_vegetable_details, ["Morich", "Alu", "Peyaj", "Roshun", "Begun", "Tomato", "Gajor"], [35, 50, 60, 120, 70, 55, 35]),
                        2: (display_fruit_details, ["Apple", "Green Apple", "Orange", "Malta", "Banana", "Pineapple", "Dragon Fruit"], [35, 50, 59, 119, 70, 55, 750]),
                        3: (display_cooking_details, ["Chal", "Dal", "Flour", "Egg", "Salt", "Sugar", "Vegetable Oil"], [35, 50, 59, 119, 70, 55, 200]),
                        4: (display_spices_details, ["Ada", "Daruchini", "Holud", "Lalmorich", "Golmorich", "Jira", "Shuknamorich"], [35, 50, 59, 119, 70, 55, 35]),
                        5: (display_snacks_details, ["Chips", "Noodles", "Biscuits", "Cake", "Coke", "Juice", "Honey nuts"], [35, 50, 59, 119, 70, 50, 1050])
                    }

                    display_details, item_names, item_prices = categories[c]

                    while True:
                        display_details()
                        try:
                            choice_item = int(input("\t\t\t\t\tEnter Your Choice: "))
                        except ValueError:
                            print("\t\t\t\t\t\033[91mInvalid Input.\033[0m \n\t\t\t\t\t\033[92mTry again.\033[0m")
                            continue

                        if 1 <= choice_item <= len(item_names):
                            try:
                                quantity = int(input("\t\t\t\t\tEnter Quantity: "))
                                selected_item = item_names[choice_item - 1]
                                price = quantity * item_prices[choice_item - 1]
                                add_to_cart(selected_item, quantity, price)
                                print(f"\n\t\t\t\t\tYou have chosen {selected_item}.\n\t\t\t\t\tQuantity: {quantity}.\n\t\t\t\t\tPrice: {price} TK\n")
                                cont = input("\t\t\t\t\tDo you want to buy other items in the same category? (yes/no) or (y/n): ")
                                if cont.lower() == "yes" or cont.lower() == "y":
                                    continue
                                else:
                                    cont = input("\t\t\t\t\tDo you want to buy from other categories? (yes/no) or (y/n): ")
                                    if cont.lower() == "yes" or cont.lower() == "y":
                                        break
                                    else:
                                        print("\t\t\t\t\t\033[90mExiting.....\033[0m")
                                        print_bill()
                                        Exit()
                                        exit()
                            except ValueError:
                                print("\t\t\t\t\t\033[91mInvalid Quantity.\033[0m \n\t\t\t\t\t\033[92mTry again.\033[0m")
                        else:
                            print("\t\t\t\t\t\033[91mInvalid Choice.\033[0m \n\t\t\t\t\t\033[92mTry again.\033[0m")
                else:
                    print("\t\t\t\t\t\033[91mInvalid Choice.\033[0m \n\t\t\t\t\t\033[92mTry again.\033[0m")
        else:
            print("\t\t\t\t\t\033[91mWrong Password.\033[0m" if 'a' <= user_name[0] <= 'z' else "\t\t\t\t\t\033[91mWrong User Name.\033[0m")
            print("\t\t\t\t\t\033[92mTry again.\033[0m")
            print("")

if __name__ == "__main__":
    main()
