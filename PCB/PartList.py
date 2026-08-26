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
        f = i
        n = f[0].split(',')[0]
        q = f[-2]
        # name.append(n)
        # quantity.append(f[-2])
        val = f[-1]
        if(len(val) > 13):
            val = val[:13]
        value.append(val)
        out += n.rjust(pad, " ")
        out += val.rjust(pad, " ")
        out += str(q).rjust(pad, " ")
        out += "\n"
    print(out)
    return

def main():
    ExtractFields()
    return

if __name__ == '__main__':
    main()

