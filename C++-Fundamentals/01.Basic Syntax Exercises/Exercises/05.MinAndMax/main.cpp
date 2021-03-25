#include <iostream>
#include <cstdlib>

int main() {
	int n;
	std::cin >> n;

	int min, max;
	max = INT_MIN;
	min = INT_MAX;
	int number;

	for (int i = 0; i < n; i++)
	{
		std::cin >> number;

		if (number >= max) max = number;
		if (number <= min) min = number;
	}
	std::cout << min << " " << max << std::endl;
	return 0;
}