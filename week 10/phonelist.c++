#include <iostream>
#include <string>
#include <vector>
#include <queue>

void experiment() {
    std::priority_queue<std::string, std::vector<std::string>, std::greater<>> pq;
    int wordCount;
    std::cin >> wordCount;
    while (wordCount-- > 0) {
        std::string word;
        std::cin >> word;
        pq.push(word);
    }
    std::string previous = pq.top();
    pq.pop();
    while (!pq.empty()) {
        std::string current = pq.top();
        pq.pop();
        if (current.compare(0, previous.length(), previous) == 0) {
            std::cout << "No\n";
            return;
        }
        previous = current;
    }
    std::cout << "Yes\n";
}

int main() {
    int testCases;
    std::cin >> testCases;
    while (testCases-- > 0) {
        experiment();
    }
    return 0;
}
