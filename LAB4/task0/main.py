
import sys
import os

sys.path.append("..")


import task0.mychl as chl
import task0.myyaml as yaml


def parse(string):
    return chl.dump(yaml.loads(string))


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__), "in.yaml")
    output_file = os.path.join(os.path.dirname(__file__), "out.hcl")

    string = open(input_file, "r", encoding='UTF-8').read()
    open(output_file, "w", encoding='UTF-8').write(parse(string))
    print("Complete!")
