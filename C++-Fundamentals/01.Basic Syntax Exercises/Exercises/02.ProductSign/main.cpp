#include <iostream>

int main() {

	int a, b, c;

	std::cin >> a >> b >> c;

	int res = a * b * c;

	if (res >= 0) std::cout << '+' << std::endl;
	else std::cout << '-' << std::endl;

	return 0;
}