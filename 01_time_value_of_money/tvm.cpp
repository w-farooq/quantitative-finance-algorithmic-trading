#include <iostream>
#include <cmath>


// Discrete Methods
constexpr double future_value_discrete (const double present_value, const double r, const double n) {
    return present_value * std::pow(1+r, n);
}

constexpr double present_value_discrete (const double future_value, const double r, const double n) {
    return future_value / std::pow(1+r, n);
}


// Continuous Methods
constexpr double future_value_continuous (const double present_value, const double r, const double t) {
    return present_value * std::exp(r*t);
}

constexpr double present_value_continuous (const double future_value, const double r, const double t) {
    return future_value * std::exp(-r*t);
}

int main() {

    constexpr double present_value {1000.00};
    constexpr double r {0.05};
    constexpr double n {10.0};
    constexpr double t {10.0};



    std::cout << "================================= DISCRETE METHODS =======================================\n";
    const double future_value_result {future_value_discrete(present_value, r, n)};
    const double present_value_result {present_value_discrete(future_value_result, r, n)};
    std::cout << "Future Value of " << present_value << " at " << r << " for " << n << " years is " << future_value_result << "\n";
    std::cout << "Present Value of " << future_value_result << " at " << r << " for " << n << " years is " << present_value_result << "\n";


    std::cout << "================================= CONTINUOUS METHODS =======================================\n";
    const double future_value_continuous_result {future_value_continuous(present_value, r, t)};
    const double present_value_continuous_result {present_value_continuous(future_value_continuous_result, r, t)};
    std::cout << "Future Value of " << present_value << " at " << r << " for " << n << " years is " << future_value_continuous_result << "\n";
    std::cout << "Present Value of " << future_value_continuous_result << " at " << r << " for " << n << " years is " << present_value_continuous_result << "\n";

    return 0;
}
