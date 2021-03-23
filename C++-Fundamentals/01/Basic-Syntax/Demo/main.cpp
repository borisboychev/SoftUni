#include <iostream>

const int secondsInMinute = 60;

const int minutesInHour = 60;

const int hoursInDay = 24;

const int secondsInHour = secondsInMinute * minutesInHour;


int main() {

    int days = 3;

    double a = 2.504;

    float pi = 3.14f;

    int totalSeconds = days * hoursInDay * secondsInHour;
    std::cout << "days have " << totalSeconds << " seconds" << std::endl;
    return 0;
}