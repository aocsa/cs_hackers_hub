#include <iostream>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <set>

//dynamic programing
// memoization + guessing

using edges = std::map<int, double>;

struct graph : public std::map<int, edges> {
    void add_node(int id){
        insert(std::make_pair(id, edges{}));
    }
};


const int White = 0;
const int Gray = 1;
const int Black = 2;

void dfs_visit(graph& graph, int u, std::vector<int> &pred, std::vector<int> &color) {
    color[u] = Gray;
    for (auto [v, w] : graph[u]) {
        if (color[v] == White) {
            pred[v] = u;
            dfs_visit(graph, v, pred, color);
        }
    }
    color[u] = Black;
}

bool contains( std::vector<int> &path, int key) {
    return std::find(std::begin(path), std::end(path), key) != std::end(path);
}

void dfs(graph& g, int u, int target,  std::vector<int> path, std::vector<int>& global_path) {
    for(auto [v, w] : g[u]) {
        std::cout << u << " -> " << v << std::endl;
        if (v == target) {
            global_path = path;
        }
        if (contains(path, v)) {
            path.push_back(v);
            dfs(g, v, target, path, global_path);
        }
    }
}

std::vector<int> dfs_search(graph& g, int source, int target){
    std::vector<int> global_path;
    std::vector<int> path;
    path.push_back(source);
    dfs(g, source, target, path, global_path);
    return global_path;
}



int rec(const std::vector<int> &arr, int total, int i) {
    if (total == 0) {
        return 1;
    }
    else if (total < 0) {
        return 0;
    }
    else if (i < 0) {
        return 0;
    }
    else if (total < arr[i]){
        return rec(arr, total, i -1);
    } else {
        return rec(arr, total - arr[i], i -1) +
               rec(arr, total, i -1);
    }
    return 0;
}

int count_sets(const std::vector<int>& arr, int total){
    // no negative numbers
    // no duplicates

    // empty set sum is 0 => 1


    return rec(arr, total, arr.size() - 1);
}


int main() {
    graph g;
    for (int i = 0; i <= 8; ++i) {
        g.add_node(i);
    }
    g[1][0] = g[0][1] = 1;
    g[2][1] = g[1][2] = 1;
    g[6][2] = g[2][6] = 1;
    g[4][0] = g[0][4] = 1;
    g[5][4] = g[4][5] = 1;
    g[2][3] = g[3][2] = 1;
    g[8][7] = g[7][8] = 1;
    for(auto [u, e] : g){
        std::cout << u << ":\n";
        for (auto [v, w] : e) {
            std::cout <<"\t->" << v << "\n";
        }
    }

    std::vector<int> path = dfs_search(g, 0, 6);

    for (int i = 0 ; i < path.size(); i++){

        std::cout << path[i] << "-> ";

    }
    return 0;
}