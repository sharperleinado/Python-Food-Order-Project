food_type = ["food box", "soup box"]

food_box = ["ewa aganyin", "pounded yam and egusi",
            "pounded yam and eforiro", "semo and egusi",
            "semo and eforiro", "eba and egusi",
            "eba and eforiro", "ofada rice",
            "jollof rice", "rice, beans and stew",
            "fried rice and chicken", "pepper soup"]

food_price = [250, 300, 300, 300, 300, 200, 200, 400, 400, 350,
              500, 500]

soup_box = ["egusi", "eforiro",
            "ila asepo", "ewedu",
            "ogbona", "banga Soup",
            "ofada stew", "adi fried stew"]

soup_price = [[2000, 4000, 7000], [1500, 3500, 6500],
              [1000, 2000, 4000], [1000, 2000, 4000],
              [2000, 4000, 7000], [1500, 3000, 4500],
              [3000, 4000, 5000], [1000, 2000, 3000]]


def username(user):
    return "Hi " + user.capitalize() + ", " + "Welcome to ADi meals mobile\nChoose box!\n"

print(username(input("Enter a name: ")))

for item in food_type:
    print(item.capitalize())


def select_foodtype(foodtype):
    subtype = ""
    price_in_packs = ""
    total_price = ""
    mini_box = ""
    medium_box = ""
    mega_box = ""

    if foodtype == "food box":
        for item in food_box:
            print(item.capitalize())
        subtype = input("\nEnter food you want: ")
        if subtype == "ewa aganyin":
            print("Unitary_price: " + str(food_price[0]))
            price_in_packs = int(input(f"\nDo you wish to buy {food_box[0]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[0])
                print(f"{price_in_packs} pack of {food_box[0]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "pounded yam and egusi":
            print("Unitary_price: " + str(food_price[1]))
            price_in_packs = int(
                input(f"\nDo you wish to buy {food_box[1]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[1])
                print(f"{price_in_packs} pack of {food_box[1]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "pounded yam and eforiro":
            print("Unitary_price: " + str(food_price[2]))
            price_in_packs = int(input(f"\nDo you wish to buy {food_box[2]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[2])
                print(f"{price_in_packs} pack of {food_box[2]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "semo and egusi":
            print("Unitary_price: " + str(food_price[3]))
            price_in_packs = int(input(f"\nDo you wish to buy {food_box[3]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[3])
                print(f"{price_in_packs} pack of {food_box[3]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "semo and eforiro":
            print("Unitary_price: " + str(food_price[4]))
            price_in_packs = int(input(f"\nDo you wish to buy {food_box[4]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[4])
                print(f"{price_in_packs} pack of {food_box[4]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "eba and egusi":
            print("Unitary_price: " + str(food_price[5]))
            price_in_packs = int(input(f"\nDo you wish to buy {food_box[5]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[5])
                print(f"{price_in_packs} pack of {food_box[5]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "eba and eforiro":
            print("Unitary_price: " + str(food_price[6]))
            price_in_packs = int(input(f"\nDo you wish to buy {food_box[6]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[6])
                print(f"{price_in_packs} pack of {food_box[6]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "ofada rice":
            print("Unitary_price: " + str(food_price[7]))
            price_in_packs = int(input(f"\nDo you wish to buy {food_box[7]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[7])
                print(f"{price_in_packs} pack of {food_box[7]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "jollof rice":
            print("Unitary_price: " + str(food_price[8]))
            price_in_packs = int(input(f"\nDo you wish to buy {food_box[8]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[8])
                print(f"{price_in_packs} pack of {food_box[8]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "rice and beans and stew":
            print("Unitary_price: " + str(food_price[9]))
            price_in_packs = int(input(f"\nDo you wish to buy {food_box[9]} in pack?\n\nPack of: Enter number between 20 and 500: "))
            if price_in_packs >= 20 and price_in_packs <= 500:
                total_price = price_in_packs * int(food_price[9])
                print(f"{price_in_packs} pack of {food_box[9]} cost ₦{total_price}")
            elif price_in_packs < 20:
                print(f"Number of packs input too small!")
            else:
                print(f"Number of packs input too large!")

        elif subtype == "fried rice":
                print("Unitary_price: " + str(food_price[10]))
                price_in_packs = int(input(f"\nDo you wish to buy {food_box[10]} in pack?\n\nPack of: Enter number between 20 and 500: "))
                if price_in_packs >= 20 and price_in_packs <= 500:
                    total_price = price_in_packs * int(food_price[10])
                    print(f"{price_in_packs} pack of {food_box[10]} cost ₦{total_price}")
                elif price_in_packs < 20:
                    print(f"Number of packs input too small!")
                else:
                    print(f"Number of packs input too large!")

        elif subtype == "pepper soup":
                print("Unitary_price: " + str(food_price[11]))
                price_in_packs = int(input(f"\nDo you wish to buy {food_box[11]} in pack?\n\nPack of: Enter number between 20 and 500: "))
                if price_in_packs >= 20 and price_in_packs <= 500:
                    total_price = price_in_packs * int(food_price[11])
                    print(f"{price_in_packs} pack of {food_box[11]} cost ₦{total_price}")
                elif price_in_packs < 20:
                    print(f"Number of packs input too small!")
                else:
                    print(f"Number of packs input too large!")

    else:
        if foodtype == "soup box":
            for item in soup_box:
                print(item.capitalize())
            subtype = input("\nEnter soup you want: ")
            if subtype == "egusi":
                print(f"Mini box: ₦{soup_price[0][0]}")
                print(f"Medium box: ₦{soup_price[0][1]}")
                print(f"Mega box: ₦{soup_price[0][2]}")

            elif subtype == "eforiro":
                print(f"Mini box: ₦{soup_price[1][0]}")
                print(f"Medium box: ₦{soup_price[1][1]}")
                print(f"Mega box: ₦{soup_price[1][2]}")

            elif subtype == "ila asepo":
                print(f"Mini box: ₦{soup_price[2][0]}")
                print(f"Medium box: ₦{soup_price[2][1]}")
                print(f"Mega box: ₦{soup_price[2][2]}")

            elif subtype == "ewedu":
                print(f"Mini box: ₦{soup_price[3][0]}")
                print(f"Medium box: ₦{soup_price[3][1]}")
                print(f"Mega box: ₦{soup_price[3][2]}")

            elif subtype == "ogbona":
                print(f"Mini box: ₦{soup_price[4][0]}")
                print(f"Medium box: ₦{soup_price[4][1]}")
                print(f"Mega box: ₦{soup_price[4][2]}")

            elif subtype == "banga soup":
                print(f"Mini box: ₦{soup_price[5][0]}")
                print(f"Medium box: ₦{soup_price[5][1]}")
                print(f"Mega box: ₦{soup_price[5][2]}")

            elif subtype == "ofada stew":
                print(f"Mini box: ₦{soup_price[6][0]}")
                print(f"Medium box: ₦{soup_price[6][1]}")
                print(f"Mega box: ₦{soup_price[6][2]}")

            elif subtype == "adi fried stew":
                print(f"Mini box: ₦{soup_price[7][0]}")
                print(f"Medium box: ₦{soup_price[7][1]}")
                print(f"Mega box: ₦{soup_price[7][2]}")

select_foodtype(input("\nEnter Food box or Soup box: "))