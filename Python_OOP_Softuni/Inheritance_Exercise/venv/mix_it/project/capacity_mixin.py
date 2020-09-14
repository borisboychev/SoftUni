class CapacityMixin:

    @staticmethod
    def get_capacity(capacity, amount):
        if amount > capacity:
            raise Exception("Capacity Reached!")
        return capacity - amount