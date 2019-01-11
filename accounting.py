
def customer_balances(customer_orders_file):
    """
    lists customers and balances for melon purchases

    args:
    none

    returns:
    customer name along with what they've paid and what we expect them to pay

    """
    melon_cost = 1.00 #set value for cost per melon
    customer_orders_file = open(customer_orders_file) #opens file

    for line in customer_orders_file: #for every line in the file
        line = line.rstrip() #remove the white space in between lines
        words = line.split('|') #split lines by | to create a list

        customer_name = words[1] #customer name is second item in list
        customer_melons = float(words[2]) #melon count is third
        customer_paid = float(words[3]) #paid amount is fourth
       
        customer_expected = customer_melons * melon_cost #calculate payment expected based on melon cost and order count
        if customer_expected != customer_paid: #if expected doesn't equal paid
            print(customer_name, "paid {:.2f}, expected {:.2f}".format( #print out what they've paid and what we expect them to pay
            customer_paid, customer_expected))

    customer_orders_file.close()


customer_orders_file = "customer-orders.txt"
customer_balances(customer_orders_file)
