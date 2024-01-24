class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key, value, timestamp):
        pair = [value, timestamp]
        
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(pair)

    def get(self, key: str, timestamp) -> str:
        ans = ""
        values = self.data.get(key, [])

        l = 0
        r = len(values) - 1

        while l <= r:
            m = (l + r) // 2
        
            if timestamp == values[m][1]:
                return values[m][0]
            elif timestamp < values[m][1]:
                r = m - 1
            else:
                ans = values[m][0]
                l = m + 1
        
        return ans

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo","bar",1)
    param_2 = obj.get("foo",1)
    param_3 = obj.get("foo",3)
    obj.set("foo","bar2",4)
    param_4 = obj.get("foo",4)
    param_5 = obj.get("foo",5)
    params = [param_2, param_3, param_4, param_5]

    expected = ["bar", "bar", "bar2", "bar2"]
    for i, exp in enumerate(params):
        assert(exp == expected[i])
    print('ok')