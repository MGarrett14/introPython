# 1. create a program that takes in an input
# 2. your program needs to do somthing with that data (atleast 3 things)
# 3. your program needs to output a result. 


# demo vpn
# vpn should alert user of malicious sites

# 1. user types in a website

# 2. give user options for where they want to establish a new IP address

# 3.  alerts user of mailicious virus in this country, and ask if they want to swtich countires or stay in that country 

# base unique ip addresses to specific countries
# canada should have its own ip
# paris should have its own ip
# Ghana should have its onw ip 

import random   

class VPN:
    def __init__(self):
        self.current_ip = None
        self.location = None
        self.virus_detected = False

    def choose_location(self):
        print("Choose your VPN location:")
        print("1. United States")
        print("2. United Kingdom")
        print("3. Germany")
        choice = input("Enter the number of your choice: ")
        locations = {
            '1': 'United States',
            '2': 'United Kingdom',
            '3': 'Germany'
        }
        self.location = locations.get(choice)
        self.generate_ip()

    def generate_ip(self):
        if self.location:
            octets = [random.randint(1, 255) for _ in range(4)]
            self.current_ip = ".".join(map(str, octets))
            print(f"Your new IP address: {self.current_ip} ({self.location})")

    def warn_about_virus(self):
        print("Warning: A virus has been detected for this IP address!")
        response = input("Do you want to switch location and generate a new IP? (yes/no): ").lower()
        if response == 'yes':
            self.choose_location()
            self.virus_detected = False
        else:
            print("You continue at your own risk!")

    def block_pop_up_ads(self):
        print("Blocking pop-up ads with potential viruses...")

    def browse_website(self, website):
        if self.virus_detected:
            print("Virus detected! Avoid entering sensitive information.")
            while True:
                response = input("You have a virus! Do you want to exit the website? (yes/no): ").lower()
                if response == 'yes':
                    break
                else:
                    print("You continue at your own risk!")
        else:
            print(f"Browsing {website} securely through VPN...")
            self.block_pop_up_ads()
            # Simulate potential virus detection
            if random.choice([True, False]):
                self.virus_detected = True
                self.warn_about_virus()


def main():
    vpn = VPN()
    website = input("Enter the website you want to visit: ")
    vpn.choose_location()
    vpn.browse_website(website)

if __name__ == "__main__":
    main()




