def read_data(path:str):
    data=[]
    with open(path, "r+") as f:
        for line in f:
            data.append(line.replace("\n", "").split(","))
    return data
