def generate_pod_table(pod_list):
    pod_table = {}

    for item in pod_list:
        pod_name, node_name = item.split(' ', 1)
        if node_name in pod_table:
            pod_table[node_name].append(pod_name)
        else:
            pod_table[node_name] = [pod_name]

    return pod_table

# Example usage
input_list = [
    "Pod1 Node1",
    "Pod2 Node2",
    "Pod3 Node1",
    "Pod4 Node3",
    "Pod5 Node2",
    "Pod6 Node3"
]

table = generate_pod_table(input_list)

# Printing the generated table
for node_name, pod_list in table.items():
    print("Node:", node_name)
    print("Pods:", ", ".join(pod_list))
    print()
