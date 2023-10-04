class MyHashMap:
    def __init__(self):
        self.l=[-1 for i in range(1000001)]
        
    def put(self, key: int, value: int) -> None:
        self.l[key]=value

    def get(self, key: int) -> int:
        return self.l[key]

    def remove(self, key: int) -> None:
        self.l[key]=-1
