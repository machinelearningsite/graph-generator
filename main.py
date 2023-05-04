import pandas as pd

class GraphGenerator:
    def __init__(self, data) -> None:
        self.data = pd.read_csv(data)

    def get_columns(self):
        print(self.data.columns)

def main():
    data = input("Enter data name: ")
    gg = GraphGenerator(data)
    gg.get_columns()

if __name__=="__main__":
    main()