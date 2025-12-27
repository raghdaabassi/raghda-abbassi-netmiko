
print("Hello, Git!")
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": 22,
}

def main():
    connexion = ConnectHandler(**device)

    # 1) show clock
    print("=== DATE DU ROUTEUR ===")
    print(connexion.send_command("show clock"))

    # 2) Save interfaces
    print("\n=== SAUVEGARDE DES INTERFACES ===")
    interfaces = connexion.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)
    print("Interfaces enregistrées dans interfaces.txt")
if __name__ == "__main__":
    main()
