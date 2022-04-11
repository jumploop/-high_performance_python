import json

import pylab as py

if __name__ == "__main__":
    raw_data = json.load(open("metric_data.json"))

    for name, values in raw_data.items():
        print(name)
        py.figure()
        py.title(f"Call timeline for {name}")
        min_t = values[0]["start"]
        for i, data in enumerate(values):
            py.plot([data["start"] - min_t, data["end"] - min_t], [i, i])
        py.xlabel("Time")
        py.ylabel("Request Number")
        py.savefig(f"images/{name}.png")
