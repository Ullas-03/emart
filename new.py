import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import requests

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Dress Store")
root.geometry("700x500")

cart = []
new_customer = False

customer_username = ""
customer_email = ""
customer_phone = ""

def load_img(path_or_url):
    try:
        if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
            response = requests.get(path_or_url)
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(path_or_url)

        img = img.resize((180, 200))
        return ImageTk.PhotoImage(img)

    except Exception as e:
        print(f"Error loading image {path_or_url}: {e}")
        return None
def clear():
    for widget in root.winfo_children():
        widget.destroy()


def login_page():
    clear()

    tk.Label(root,text="Dress Store",font=("Arial", 22, "bold")).pack(pady=10)

    tk.Label(root,text="Login",font=("Arial", 18)).pack(pady=10)

    tk.Label(root, text="Username").pack()

    user = tk.Entry(root,width=30)
    user.pack(pady=5)

    tk.Label(root, text="Password").pack()

    pwd = tk.Entry(root, show="*",width=30)
    pwd.pack(pady=5)

    tk.Label(root,text="Email").pack()

    email = tk.Entry(root,width=30)
    email.pack(pady=5)

    tk.Label(root,text="Phone Number").pack()

    Phone = tk.Entry(root,width=30)
    Phone.pack(pady=5)

    def login():
        global new_customer
        global customer_username
        global customer_email
        global customer_phone

        Username = user.get().strip()
        Password = pwd.get().strip()
        email_Value = email.get().strip()
        Phone_Value = Phone.get().strip() 

        if Username == " " or Password == " " or email_Value == " " or Phone_Value == "":
            messagebox.showerror(
                "Error","Please enter all details."

            )
            return
            if Username != "ullas" or Password != "123":
                messagebox.showerror("ERROR","Invalid Username or Password")
                return
            
            email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

            if not re.match(email_pattern,email_Value):
                messagebox.showerror("ERROR","Please enter a valid email")
                return

            if not Phone_Value.iddigit() or len(Phone_Value) != 10:
                messagebox.showerror("ERROR","Phone number must be 10 digits.")
                return

            customer_username = Username
            customer_email = email_Value
            customer_phone = Phone_Value


            answer = messagebox.askyesno(
                "New Customer Offer",
                "Are you a new customer?\n\n"
                "New customers get 30% OFF!"
            )

            new_customer = answer

            if new_customer:
                messagebox.showinfo(
                    "Special Offer",
                    "🎉 Congratulations!\n\n"
                    "You received 30% OFF as a new customer!"
                )

            main_menu()

        else:
            messagebox.showerror("Error","Invalid Login" )

    tk.Button(root,text="Login",width=15,command=login).pack(pady=15)


def main_menu():
    clear()

    tk.Label(root,text="Dress Collection",font=("Arial", 18, "bold")).pack(pady=20)

    if new_customer:
        tk.Label(root,text="🎉 New Customer Offer: 30% OFF",font=("Arial", 13, "bold")).pack(pady=5)

    frame = tk.Frame(root)
    frame.pack(pady=20)

    tk.Button(frame,text="Men",width=15,command=men).grid(row=0, column=0, padx=10)

    tk.Button(frame,text="Women",width=15,command=women).grid(row=0, column=1, padx=10)

    tk.Button(frame,text="Kids",width=15,command=kids).grid(row=0, column=2, padx=10)

    tk.Button(root,text="View Cart",width=20,command=view_cart).pack(pady=20)

def add_to_cart(item, price):
    cart.append((item, price))

    messagebox.showinfo(
        "Cart",
        f"{item} added to cart"
    )
def show_items(title, items):
    clear()

    tk.Label(root,text=title,font=("Arial", 16, "bold")).pack(pady=10)

    if new_customer:
        tk.Label(root,text="🎉 30% OFF New Customer Offer",font=("Arial", 12, "bold")).pack()

    frame = tk.Frame(root)
    frame.pack()

    row = 0
    col = 0

    global active_images
    active_images = []

    for item in items:

        img = load_img(item["img"])

        card = tk.Frame(frame,bd=2,relief="ridge")

        card.grid( row=row, column=col, padx=10,pady=10)

        if img:
            tk.Label(card,image=img ).pack()

            active_images.append(img)

        else:
            tk.Label(card,text="No Image",width=15,height=8,bg="lightgray").pack()

        tk.Label(card,text=item["name"] ).pack()

        tk.Label(card,text=f"₹{item['price']}").pack()

        tk.Button(card,text="Buy",command=lambda i=item:
                add_to_cart(i["name"], i["price"])).pack(pady=5)

        col += 1

        if col == 3:
            col = 0
            row += 1

    tk.Button(root, text="Back", command=main_menu).pack(pady=10)


# ---------- MEN ----------
def men():

    items = [
        {
            "name": "T-Shirt",
            "price": 800,
            "img": "img11.png"
        },
        {
            "name": "T-Shirt",
            "price": 500,
            "img": "img13.png"
        },
        {
            "name": "Combo",
            "price": 1500,
            "img": "man1.jpg"
        },
        {
            "name": "Combo",
            "price": 1800,
            "img": "man2.jpg"
        },
        {
            "name": "Shirt and Pant",
            "price": 1000,
            "img": "man3.jpg"
        },
        {
            "name": "Shirt",
            "price": 500,
            "img": "mam4.png"
        }
    ]

    show_items(
        "Men Collection",
        items
    )


# ---------- WOMEN ----------
def women():

    items = [
        {
            "name": "Saree",
            "price": 1500,
            "img": "saree.jpg"
        },
        {
            "name": "Saree",
            "price": 2500,
            "img": "saree2.jpg"
        },
        {
            "name": "Saree",
            "price": 1800,
            "img": "saree3.jpg"
        }
    ]

    show_items(
        "Women Collection",
        items
    )


# ---------- KIDS ----------
def kids():

    items = [
        {
            "name": "Frock",
            "price": 1500,
            "img": "kid1.jpg"
        },
        {
            "name": "Frock",
            "price": 700,
            "img": "kid22.jpg"
        },
        {
            "name": "Frock",
            "price": 1000,
            "img": "kid3.jpg"
        }
    ]

    show_items(
        "Kids Collection",
        items
    )

def view_cart():
    clear()

    tk.Label(root,text="Cart",font=("Arial", 18, "bold")).pack(pady=10)

    if len(cart) == 0:
        tk.Label( root, text="Your cart is empty").pack(pady=20)

        tk.Button(root,text="Back",command=main_menu).pack()

        return

    total = 0

    for item, price in cart:

        tk.Label(root,text=f"{item} - ₹{price}").pack()

        total += price

    discount = 0

    if new_customer:
        discount = total * 0.30

    final_total = total - discount

    tk.Label(root,text=f"Subtotal: ₹{total:.2f}",font=("Arial", 12) ).pack(pady=5)

    if new_customer:

        tk.Label(root,text=f"New Customer Discount (30%): -₹{discount:.2f}",font=("Arial", 12, "bold")).pack(pady=5)

    tk.Label(root,text=f"Total: ₹{final_total:.2f}",font=("Arial", 15, "bold") ).pack(pady=10)

    tk.Button( root, text="Back", command=main_menu).pack(pady=5)

login_page()

root.mainloop()