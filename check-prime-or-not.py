number = int(input("Koi ek number daaliye: "))
is_prime = True  # Pehle maan lete hain ki number prime hai

if number > 1:  # Prime hone ke liye number 1 se bada hona chahiye
    for i in range(2, number):
        if number % i == 0:  # Agar kisi bhi divisor se divisible hai
            is_prime = False  # Toh prime nahi hai
            break  # Loop ko turant stop kar dete hain
    if is_prime:
        print(f"{number} ek prime number hai.")
    else:
        print(f"{number} prime nahi hai.")
else:
    print(f"{number} prime nahi hai.")
