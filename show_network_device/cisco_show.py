from netmiko import ConnectHandler


device = {
    "address":"192.168.2.2",
    "device_type":"cisco_ios",
    "port": 22,
    "username":"ciaran",
    "password":"crystal",
    "secret":"crystal"
}

commands = [
    "show run",
    "show ip interface brief",
    "show vlan brief",
    "show arp",
    "show mac address-table",
    "show ntp status"
]

with ConnectHandler(ip = device["address"],
                    port = device["port"],
                    username = device["username"],
                    password = device["password"],
                    secret = device["secret"],
                    device_type = device["device_type"]) as ch:
    ch.enable()
    for command in commands:
        try:
            output = ch.send_command(command)
        except Exception as e:
            raise e
        else:
            with open(f"{command}.txt", "w") as f:
                f.write(output)
        print(output)

