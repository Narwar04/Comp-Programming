#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int itemCount, tempItem;
    long long discount = 0;
	
    std::cin >> itemCount;
    std::vector<int> cart(itemCount);

    for (int i = 0; i < itemCount; i++) {
        std::cin >> cart[i];
    }

    std::sort(cart.begin(), cart.end(), std::greater<int>());

    for (int i = 2; i < itemCount; i += 3) {
        discount += cart[i];
    }

    std::cout << discount;
    return 0;
}
