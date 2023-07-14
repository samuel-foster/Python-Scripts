def generate_pod_table(pod_list):
    pod_table = {}

    for item in pod_list:
        pod_name, node_name = item.split(' ', 1)
        if node_name in pod_table:
            pod_table[node_name].append(pod_name)
        else:
            pod_table[node_name] = [pod_name]

    table = [(node_name, pod_list) for node_name, pod_list in pod_table.items()]
    return table

# Example usage
input_list = [
]

table = generate_pod_table(input_list)

# Printing the generated table
for node_name, pod_list in table:
    print(f'("{node_name}", {pod_list}),')
