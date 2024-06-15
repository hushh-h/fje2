import json
import argparse
import Strategy
import StyleFactory
import IconFactory

class generate_fje:
    def __init__(self,args):
        self.file = args.file
        self.style = args.style
        self.icon = args.icon

    def create(self):
        with open(self.file, 'r') as f:
            data = json.load(f)
        strategy = Strategy.strategy(data,self.icon,self.style)
        strategy.display()


if __name__ == "__main__":
    parameter = argparse.ArgumentParser(description='FJE')
    parameter.add_argument('-f', '--file', required=True, help='file path')
    parameter.add_argument('-s', '--style', required=True, help='style')
    parameter.add_argument('-i', '--icon', required=True, help='icon')
    args = parameter.parse_args()

    generator = generate_fje(args)
    generator.create()