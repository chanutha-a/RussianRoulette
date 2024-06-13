import socket
import random
import os
import json


banned_ips_file = "banned_ips.json"
game_file = "RussianRoulette.py"


def get_ip_address():
    try:
        # Create a socket connection to a remote server (can be any valid address)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))  # Connect to Google's public DNS server
        ip_address = sock.getsockname()[0]  # Get the local IP address of the socket
        sock.close()
        return ip_address
    except socket.error as e:
        print(f"Socket error: {e}")
        return None


def load_banned_ips():
    if os.path.exists(banned_ips_file):
        with open(banned_ips_file, "r") as file:
            banned_ips = json.load(file)
            return banned_ips
    else:
        return {}


def save_banned_ips(banned_ips):
    with open(banned_ips_file, "w") as file:
        json.dump(banned_ips, file, indent=4)


def russian_roulette(ip_address):
    revolver = ["empty", "empty", "empty", "empty", "empty", "loaded"]
    earnings = 0

    print("Welcome to Russian Roulette!")
    input("Press Enter to pull the trigger... (Enter to continue, 99.9% of gamblers stop before their big win!!!)")

    while True:
        random_outcome = random.randint(0, 5)

        if revolver[random_outcome] == "loaded":
            print("BANG! Bro's bread is up but his pulse is down 💀")
            # Ban the IP address and delete the game
            ban_ip_address(ip_address)
            delete_game()
            break
        else:
            print("Click! IF YOU GOT BALLS!! YOU WONT!!!.")
            earnings += 1000
            print(f"Earnings: ${earnings}")
            choice = input("Press Enter to pull the trigger again, or type 'q' to stop (99.9% of gamblers stop before their big win!!!): ").strip().lower()
            if choice == 'q':
                print("Bro stop being a pussy")
                break


def ban_ip_address(ip_address):
    banned_ips = load_banned_ips()
    banned_ips[ip_address] = True
    save_banned_ips(banned_ips)
    print(f" GGs kid the IP address {ip_address} is banned.")


def delete_game():
    print("Deleting the game... Installing crypto miner.....")
    try:
        os.remove(game_file)  # Delete the game file

        # Check if the file still exists
        if not os.path.exists(game_file):
            print(f"Game file '{game_file}' has been deleted.")
        else:
            print(f"Failed to delete '{game_file}'.")
    except OSError as e:
        print(f"Error deleting '{game_file}': {e}")



if __name__ == "__main__":
    ip_address = get_ip_address()
    if ip_address:
        print(f"Detected IP address: {ip_address}")
    else:
        print("Failed to detect IP address.")


    banned_ips = load_banned_ips()
    if ip_address in banned_ips:
        print("GGs kid you are banned from playing this game on this IP address ;) Get a real life")
    else:
        russian_roulette(ip_address)