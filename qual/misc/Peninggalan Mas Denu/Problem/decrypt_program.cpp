#include <iostream>
#include <string>

int main() {
    std::string enc = "Wv'\nDHkOoxs:`ry.";
    std::cout << "key:";
    std::string key; std::cin >> key;
    
    std::string res = "";
    for (int i = 0; i < enc.size(); i++) {
        int a = (i * 2) % key.size();
        int b = (i * 2 + 1) % key.size();
        int x = (key[a] - '0') + (key[b] - '0') * 10;
        res += enc[i] ^ x;
    }
    std::cout << res << '\n';

    return 0;
}