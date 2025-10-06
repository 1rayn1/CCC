def extract_links(line):
    links = []
    i = 0
    while i < len(line):
        if line[i:i+9] == '<A HREF="':
            i += 9
            url = ""
            while i < len(line) and line[i] != '"':
                url += line[i]
                i += 1
            links.append(url)
        else:
            i += 1
    return links

def dfs(graph, start, target, visited):
    if start == target:
        return True
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False


n = int(input())
graph = {}
link_log = []


for _ in range(n):
    url = input().strip()
    graph[url] = []
    while True:
        line = input()
        if line.strip() == "</HTML>":
            break
        links = extract_links(line)
        for link in links:
            graph[url].append(link)
            link_log.append(f"Link from {url} to {link}")


for entry in link_log:
    print(entry)


while True:
    src = input().strip()
    if src == "The End":
        break
    dst = input().strip()
    visited = set()
    if dfs(graph, src, dst, visited):
        print(f"Can surf from {src} to {dst}.")
    else:
        print(f"Can't surf from {src} to {dst}.")


'''
3
http://ccc.uwaterloo.ca
<HTML> <TITLE>This is the CCC page</TITLE>
Hello there boys
and girls.  <B>Let's</B> try <A HREF="http://abc.def/ghi"> a
little
problem </A>
</HTML>
http://abc.def/ghi
<HTML> Now is the <TITLE>time</TITLE> for all good people to program.
<A HREF="http://www.www.www.com">hello</A><A HREF="http://xxx">bye</A>
</HTML>
http://www.www.www.com
<HTML>
<TITLE>Weird and Wonderful World</TITLE>
</HTML>
http://ccc.uwaterloo.ca
http://www.www.www.com
http://www.www.www.com
http://ccc.uwaterloo.ca
The End
'''
