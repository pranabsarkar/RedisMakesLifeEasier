class processData:
    def __init__(self):
        self.result = None

    def handle(self, data):
        self.result = []
        for key in range(len(data)):
            self.result.append(
                {
                    "id": data[key][0],
                    "zipcode": data[key][1],
                    "name": data[key][2],
                    "email": data[key][3],
                    "contact": data[key][4],
                }
            )
        return self.result
