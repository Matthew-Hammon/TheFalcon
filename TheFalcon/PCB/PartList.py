import numpy as np
import pandas as pd

def ExtractFields():
    df = pd.read_csv("TheFalcon[Left].csv")
    df = np.array(df)
    value = []
    quantity = []
    name = []
    pad = 20
    out = "Name".rjust(pad, " ")
    out += "#".rjust(pad, " ")
    out += "Val".rjust(pad, " ")
    out += "\n"

    for i in df:
        f = i[0].split(',')
        name.append(f[0])
        quantity.append(f[-2])
        val = f[-1]
        if(len(val) > 13):
            val = val[:13]
        value.append(val)
        out += f[0].rjust(pad, " ")
        out += val.rjust(pad, " ")
        out += f[-2].rjust(pad, " ")
        out += "\n"
    print(out)
    return

def main():
    ExtractFields()
    return

if __name__ == '__main__':
    main()

