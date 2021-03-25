#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

int main() {
	float a = .0f;
	float b = .0f;
	float c = .0f;

	std::cin >> a >> b >> c;

	const float D = (pow(b, 2) - (4 * a * c));

	if (D < 0) {
		std::cout << "no roots" << std::endl;
	}
	else if (D > 0) {
		const float x1 = (-b + std::sqrt(D)) / (2 * a);
		const float x2 = (-b - std::sqrt(D)) / (2 * a);
		std::cout << x1 << " " << x2 << std::endl;
	}
	else {
		const float x = -b / (2 * a);
		std::cout << x << std::endl;
	}

	return 0;
}