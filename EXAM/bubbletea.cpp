#include <iostream>
#include <vector>
#include <limits>

int main() {
    int n, m, budget;
    std::cin >> n;

    std::vector<int> basePrices(n);
    for (int &price : basePrices) {
        std::cin >> price;
    }

    std::cin >> m;
    std::vector<int> toppingPrices(m);
    for (int &price : toppingPrices) {
        std::cin >> price;
    }

    int minCost = std::numeric_limits<int>::max();

    for (int i = 0; i < n; ++i) {
        int numToppings;
        std::cin >> numToppings;

        while (numToppings--) {
            int toppingIndex;
            std::cin >> toppingIndex;
            minCost = std::min(minCost, basePrices[i] + toppingPrices[toppingIndex - 1]);
        }
    }

    std::cin >> budget;
    int maxStudents = (budget / minCost) - 1;
    std::cout << std::max(0, maxStudents) << std::endl;

    return 0;
}
