class Vendor:
    def __init__(self,inventory = None):
        if inventory is not None:
            self.inventory = inventory
        else:
            self.inventory = []

#add new item and return inventory list
    def add(self,add_item):
        self.inventory.append(add_item)
        return add_item

#remove duplicates from inventory list if any, else return None
    def remove(self,check_item):
        if check_item in self.inventory:
            self.inventory.remove(check_item)
            return check_item
        else:
            return None

#check id in inventory,return id. if not, return None
    def get_by_id(self,id):
        for item in self.inventory:
            if id == item.id:
                return item
        else:
            return None