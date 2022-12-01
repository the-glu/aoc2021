points = []
links = {}

with open("input") as f:
    for l in f.readlines():
        fr, to = l.strip().split("-")

        if fr not in points:
            points.append(fr)
            links[fr] = []

        if to not in points:
            points.append(to)
            links[to] = []

        links[fr].append(to)
        links[to].append(fr)

all_paths = []

def find_all_paths(cpos='start', visited=None, visited2=None, path=None):

    if not visited:
        visited = []
        visited2 = []

    if not path:
        path = []

    path = path[::]
    visited = visited[::]
    visited2 = visited2[::]

    if cpos.islower():
        if cpos not in visited:
            visited.append(cpos)
        else:
            visited2.append(cpos)

    path.append(cpos)

    if cpos == 'end':
        all_paths.append(path)
        return

    for dest in links[cpos]:
        if dest != "start" and (dest not in visited or len(visited2) < 1) and dest not in visited2:
            find_all_paths(dest, visited, visited2, path)




print(points, links)
find_all_paths()
print(len(all_paths))
# for p in all_paths:
#     print(p)
