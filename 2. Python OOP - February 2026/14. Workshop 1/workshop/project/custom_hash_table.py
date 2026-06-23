class HashTable:
    def __init__(self):
        self.array = [[] for _ in range(4)]
        self.count = 0

    def hash(self, key: str) -> int:
        return sum(ord(ch) for ch in key) % len(self.array)

    def add(self, key: str, value):
        index = self.hash(key)
        bucket = self.array[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

        if self.count / len(self.array) > 0.7:
            self._resize()

    def get(self, key: str):
        index = self.hash(key)
        bucket = self.array[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError("Key not found")

    def _resize(self):
        old_data = []
        for bucket in self.array:
            for item in bucket:
                old_data.append(item)

        self.array = [[] for _ in range(len(self.array) * 2)]
        self.count = 0

        for key, value in old_data:
            self.add(key, value)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)