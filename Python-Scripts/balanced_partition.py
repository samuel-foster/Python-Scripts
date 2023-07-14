import math
from collections import defaultdict

def balanced_partition(table, num_groups):
    # Step 2: Calculate the total number of pods and nodes in the table
    total_pods = len(table)
    total_nodes = len(set(node for _, nodes in table for node in nodes))

    # Step 3: Adjust the number of groups if there are fewer nodes than the specified number of groups
    if total_nodes < num_groups:
        num_groups = total_nodes

    # Step 4: Calculate the target number of nodes per group
    target_nodes_per_group = math.ceil(total_nodes / num_groups)

    # Step 5: Initialize empty lists for each group and a dictionary to store the count of nodes in each group
    groups = [[] for _ in range(num_groups)]
    node_counts = defaultdict(int)

    # Step 6: Sort the table based on the number of nodes in each row
    sorted_table = sorted(table, key=lambda row: len(row[1]))

    # Steps 7-9: Assign pods to groups while maintaining balance
    for pod, nodes in sorted_table:
        assigned_group = None
        for i in range(num_groups):
            if node_counts[i] < target_nodes_per_group:
                groups[i].append((pod, nodes))
                node_counts[i] += 1
                assigned_group = i
                break
        if assigned_group is None:
            min_group = min(range(num_groups), key=lambda i: node_counts[i])
            groups[min_group].append((pod, nodes))
            node_counts[min_group] += 1

    # Step 10: Generate a summary of each group
    group_summary = []
    for i, group in enumerate(groups):
        group_summary.append({
            'Group': i + 1,
            'Number of Pods': len(group),
            'Node Counts': defaultdict(int)
        })
        for pod, nodes in group:
            for node in nodes:
                group_summary[i]['Node Counts'][node] += 1

    return groups, group_summary

# Example usage
table = []  # Insert the table of pods and assigned nodes here

num_groups = 3
groups, group_summary = balanced_partition(table, num_groups)

# Output the groups and summaries
for i, group in enumerate(groups):
    print(f"Group {i + 1}:")
    for pod, nodes in group:
        print(f"  Node: {pod}, Pods: {', '.join(nodes)}")
    print()

for summary in group_summary:
    print(f"Group {summary['Group']} Summary:")
    print(f"  Number of Nodes: {summary['Number of Pods']}")
    print("  Pod Counts:")
    for node, count in summary['Node Counts'].items():
        print(f"    {node}: {count}")
    print()
