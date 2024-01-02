def get_resource_demand(task):
    return task['resource_demand']

def divide_and_conquer_resource_allocation(tasks, start, end):
    if start == end:
        return {'max_task': tasks[start], 'min_task': tasks[start]}

    mid = (start + end) // 2

    left_result = divide_and_conquer_resource_allocation(tasks, start, mid)
    right_result = divide_and_conquer_resource_allocation(tasks, mid + 1, end)

    # combine results from subproblems using the named function
    max_task = max(left_result['max_task'], right_result['max_task'], key=get_resource_demand)
    min_task = min(left_result['min_task'], right_result['min_task'], key=get_resource_demand)

    return {'max_task': max_task, 'min_task': min_task}

# example usage
tasks = [{'task_name': 'Task1', 'resource_demand': 10},
         {'task_name': 'Task2', 'resource_demand': 5},
         {'task_name': 'Task3', 'resource_demand': 8}]

result = divide_and_conquer_resource_allocation(tasks, 0, len(tasks) - 1)

print("Task demanding maximum resources")
print(f"{result['max_task']['task_name']} with demand {result['max_task']['resource_demand']}")

print("\nTask demanding minimum resources")
print(f"{result['min_task']['task_name']} with demand {result['min_task']['resource_demand']}")
