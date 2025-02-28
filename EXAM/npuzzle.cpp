#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int main() {
    map<char, pair<int, int>> locations = {
        {'A', {0, 0}}, {'B', {0, 1}}, {'C', {0, 2}}, {'D', {0, 3}},
        {'E', {1, 0}}, {'F', {1, 1}}, {'G', {1, 2}}, {'H', {1, 3}},
        {'I', {2, 0}}, {'J', {2, 1}}, {'K', {2, 2}}, {'L', {2, 3}},
        {'M', {3, 0}}, {'N', {3, 1}}, {'O', {3, 2}}
    };

    vector<string> board(4);
    for (auto &row : board) {
        cin >> row;
    }

    int total = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            char ch = board[i][j];
            if (ch != '.') {
                auto [row, col] = locations[ch];
                total += abs(i - row) + abs(j - col);
            }
        }
    }

    cout << total << "\n";
    return 0;
}
