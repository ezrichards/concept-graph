# Parse notional machine data stored in markdown from https://github.com/notionalmachines/notionalmachines.github.io
import os

data_files = os.listdir('nm-data')

all_notional_machines = {}

for data_file in data_files:
    title = data_file.split(".md")[0]
    notional_machine_dict = {}

    with open('nm-data/' + data_file) as file:
        for line in file:
            if "---" not in line:
                key = line.split(": ")[0].strip().replace("\"", "")
                if len(line.split(": ")) > 1: # some keys don't have values
                    val = line.split(": ")[1].strip().replace("\n", "").replace("\"", "")

                notional_machine_dict.update({ key: val })

        file.close()

    all_notional_machines.update({ title: notional_machine_dict })

print(all_notional_machines)
