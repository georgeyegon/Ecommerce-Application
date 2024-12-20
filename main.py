from lib.users import Users
from lib.product import Products
from lib.orders import Orders
from lib.reviews import Reviews
from lib.admin import Admin
import sys

product = Products

def home():
    while True:
        print(" ===> HOME <=== ")
        print("1. Users")
        print("2. Products")
        print("3. Orders")
        print("4. Reviews")
        print("0. Exit")

        choice = input("\nSelect one option: ")
        if choice == "1":
            return user_operations()

        elif choice == "2":
            return product_operations()

        elif choice == "3":
            return order_operations()

        elif choice == "4":
            return review_operations()

        elif choice == "0":
            sys.exit()
        
        else:
            print("Invalid Choice")

def user_operations():
    while True:
        print("\n ===> USER <=== ")
        print("1. Register account")
        print("2. Update user details")
        print("3. Fetch all users")
        print("4. Fetch user by id")
        print("5. Delete user")
        print("6. View all products")
        print("0. HOME")

        choice = input("\nSelect one option: ")

        user = Users()
        if choice == "1":
            name = input("Input name: ")
            email = input("Input email: ")
            phone = input("Input phone: ")

            user_id = user.create_user(name, email, phone)
            print(f"\nUser with id {user_id} created successfully")

        elif choice == "2":
            user_id = input("Enter the id of the user you want to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            age = input("Enter new phone: ")

            userID = user.update_user_by_id(user_id , name, email, age)
            print(f"\nUser with id {userID} updated successfully")

        elif choice == "3":
            all_users = user.fetch_all_users()
            print("\nAll users")
            print(all_users)

        elif choice == "4":
            user_id = input("Enter the id of the user you want to fetch: ")
            single_user = user.get_user(user_id)
            print(single_user)

        elif choice == "5":
            user_id = input("Enter the id of the user you want to delete: ")
            deleted_user_id = user.delete_user_by_id(user_id)
            print(f"\nUser {deleted_user_id} deleted successfully")

        elif choice == "6":
            all_products = product.fetch_all_products()
            print("\nAll products")
            print(all_products)

        elif choice == "0":
            return home()

        else:
            print("Invalid Input")


def product_operations():
    while True:
        print("\n ===> PRODUCTS <=== ")
        print("1. Add product - ADMIN")
        print("2. Update product - ADMIN")
        print("3. Fetch all products")
        print("4. Fetch product by id")
        print("5. Search product by category")
        print("6. Search product by name")
        print("0. HOME")

        choice = input("\nSelect one option: ")

        product = Products()
        if choice == "1":
            while True:
    
                username = "abc"
                password = "xyz"
                admin = Admin(username, password)

                while True:

                    print("\n0. HOME")
                    print("1. Admin Login")

                    choice = input("\nSelect one option: ")
                    if choice == "0":
                        while True:
                            return home()

                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    
                    if admin.login(username, password):
                        print("\nLogin Success!")
                        while True:

                            admin = Admin(username, password)

                            category = input(" \nInput category: ")
                            name = input("Input name: ")
                            price = input("Input price: ")
                            quantity = input("Input quantity: ")
        
                            created_product_id = product.create_product( category, name, price, quantity)
                            print(f"\nProduct {created_product_id} created successfully!")
                            proceed = input("Do you want to add another product? (y/n): ").lower()
                            if proceed != "y":
                                break  
                        break
                    else:
                        print("\nLogin Failed!")

        elif choice == "2":
            while True:
    
                username = "abc"
                password = "xyz"
                admin = Admin(username, password)

                while True:

                    print("\n0. HOME")
                    print("1. Admin Login")

                    choice = input("\nSelect one option: ")
                    if choice == "0":
                        while True:
                            return home()

                    username = input("Enter username: ")
                    password = input("Enter password: ")                    

                    if admin.login(username, password):
                        print("\nLogin Success!")
                        while True:

                            admin = Admin(username, password)

                            product_id = input("Input product id: ")
                            category = input("Update category: ")
                            name = input("Update name: ")
                            price = input("Update price: ")
                            quantity = input("Update quantity: ")

                            updated_product = product.update_product_by_id(product_id, category, name, price, quantity)
                            print(f"\nProduct {updated_product} updated successfully!")
                            proceed = input("Do you want to add another product? (y/n): ").lower()
                            if proceed != "y":
                                break  
                        break
                    else:
                        print("\nLogin Failed!")

        elif choice == "3":
            all_products = product.fetch_all_products()
            print("\nAll products")
            print(all_products)

        elif choice == "4":
            product_id = input("Enter product id: ")
            single_product = product.search_product_by_id(product_id)
            print("\nFetch product by id ")
            print(single_product)

        elif choice == "5":
            product_category = input("Enter product category: ")
            product_category = product.search_product_by_category(product_category)
            print("\nFetch product by category ")
            print(product_category)

        elif choice == "6":
            product_name = input("Enter product name: ")
            product_name = product.search_product_by_name(product_name)
            print("\nFetch product by name ")
            print(product_name)

        elif choice == "0":
            return home()

        else:
            print("Invalid Input")

def order_operations():
    while True:
        print("\n ===> ORDER <=== ")
        print("1. Add to cart")
        print("2. Remove from cart")
        print("3. Order history")
        print("0. HOME")

        choice = input("\nSelect one option: ")

        order = Orders()

        if choice == "1":
            name = input("Enter product name: ")
            price = input("Enter price: ")
            quantity = input("Enter quantity: ")
            created_order_id = order.add_to_cart(name, price, quantity)
            print(f"\nOrder {created_order_id} created")

        elif choice == "2":
            order_id = input("Enter order id: ")
            deleted_order_id = order.delete_by_order_id(order_id)
            print(f"\nOrder {deleted_order_id} deleted")

        elif choice == "3":
            all_orders = order.fetch_all_orders()
            print("\nAll orders")
            print(all_orders)
        
        elif choice == "0":
            return home()

        else:
            print("Invalid Choice")

def review_operations():
    while True:
        print("\n ===> REVIEWS <=== ")
        print("1.Add review")
        print("2.Fetch all reviews by user id")
        print("3.Fetch all reviews by product id")
        print("4.Fetch all reviews")
        print("5.Delete review")
        print("0.HOME")

        choice = input("\nSelect one option: ")

        review = Reviews()

        if choice == "1":
            user_id = input("Input user id: ")
            product_id = input("Input product id: ")
            review_ = input("Input review: ")
            review_id = review.create_review(review_, product_id, user_id)
            print(f"\nReview {review_id} created")

        elif choice == "2":
            user_id = input("Enter user id: ")
            reviews_by_user_id = review.get_reviews_by_user_id(user_id)
            print("\nFetch review by user id ")
            print(reviews_by_user_id)

        elif choice == "3":
            product_id = input("Enter product id: ")
            reviews_by_product_id = review.get_review_by_product_id(product_id)
            print("\nFetch review by product id ")
            print(reviews_by_product_id)

        elif choice == "4":
            all_reviews = review.fetch_all_reviews()
            print("\nAll reviews")
            print(all_reviews)

        elif choice == "5":
            review_id = input("Enter review id: ")
            deleted_review_id = review.delete_review_by_id(review_id)
            print(f"\nReview {deleted_review_id} deleted successfully")   

        elif choice == "0":
            return home()




home()

