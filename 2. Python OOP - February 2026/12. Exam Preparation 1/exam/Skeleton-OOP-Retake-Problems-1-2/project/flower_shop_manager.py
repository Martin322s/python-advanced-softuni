from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant
from project.clients.regular_client import RegularClient
from project.clients.business_client import BusinessClient

class FlowerShopManager:
    def __init__(self):
        self.income = 0.0
        self.plants = []
        self.clients = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        valid_flowers = ['Flower', 'LeafPlant']

        if plant_type not in valid_flowers:
            raise ValueError("Unknown plant type!")

        plant = None
        if plant_type == 'Flower':
            plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
        else:
            plant = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)

        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        valid_clients = ['RegularClient', 'BusinessClient']

        if client_type not in valid_clients:
            raise ValueError("Unknown client type!")

        if [client for client in self.clients if client.phone_number == client_phone_number]:
            raise ValueError("This phone number has been used!")

        client = None
        if client_type == 'RegularClient':
            client = RegularClient(client_name, client_phone_number)
        else:
            client = BusinessClient(client_name, client_phone_number)

        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        if not [client for client in self.clients if client.phone_number == client_phone_number]:
            raise ValueError("Client not found!")

        if not [plant for plant in self.plants if plant.name == plant_name]:
            raise ValueError("Plants not found!")

        available = len([plant for plant in self.plants if plant.name == plant_name])
        if available < plant_quantity:
            return "Not enough plant quantity."

        client = [client for client in self.clients if client.phone_number == client_phone_number][0]
        plant_price = [plant for plant in self.plants if plant.name == plant_name][0].price

        removed_count = 0
        i = 0
        while i < len(self.plants) and removed_count < plant_quantity:
            if self.plants[i].name == plant_name:
                self.plants.pop(i)
                removed_count += 1
                continue
            i += 1

        order_amount = (plant_price * plant_quantity) * (1 - (client.discount / 100))
        self.income += order_amount

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        if not [plant for plant in self.plants if plant.name == plant_name]:
            return "No such plant name."

        plant = [plant for plant in self.plants if plant.name == plant_name][0]
        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        count = len([client for client in self.clients if client.total_orders == 0])
        self.clients = [client for client in self.clients if client.total_orders != 0]
        return f"{count} client/s removed."

    def shop_report(self):
        count_of_all_orders = sum([client.total_orders for client in self.clients])

        plants_by_name = {}
        for plant in self.plants:
            if plant.name not in plants_by_name:
                plants_by_name[plant.name] = 0
            plants_by_name[plant.name] += 1

        sorted_plants = sorted(plants_by_name.items(), key=lambda kv: (-kv[1], kv[0]))
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))

        result = []
        result.append("~Flower Shop Report~")
        result.append(f"Income: {self.income:.2f}")
        result.append(f"Count of orders: {count_of_all_orders}")
        result.append(f"~~Unsold plants: {len(self.plants)}~~")

        for name, count in sorted_plants:
            result.append(f"{name}: {count}")

        result.append(f"~~Clients number: {len(self.clients)}~~")

        for client in sorted_clients:
            result.append(client.client_details())
        return "\n".join(result)