def read_input():
    return [i[:-1] for i in open("day6_input.txt", "r")]


def build_graph(data):
    mp = {}
    for row in data:
        a, b = row.split(")")
        mp[b] = a
    return mp


def build_bidirec_graph(data):
    mp = {}
    for row in data:
        a, b = row.split(")")
        if a not in mp:
            mp[a] = [b]
        else:
            mp[a].append(b)
        if b not in mp:
            mp[b] = [a]
        else:
            mp[b].append(a)
    return mp


def count_path_length(graph, start, end="COM"):
    if start == end:
        return 0

    return 1 + count_path_length(graph, graph[start], end)


def count_path_length_bidrec(graph, start, end, visited, path):
    visited.add(start)
    if start == end:
        global answer
        answer = path
        return

    for i in graph[start]:
        if i not in visited:
            count_path_length_bidrec(graph, i, end, visited, list(path) + [i])


_graph = build_bidirec_graph(read_input())
answer = 0
print(count_path_length_bidrec(_graph, "YOU", "SAN", set(), []))
print(len(answer) - 2)

exit(0)
main_graph = build_graph(read_input())
print(sum([count_path_length(main_graph, i) for i in main_graph.keys()]))


