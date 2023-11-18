#include <iostream>
using namespace std;
int main() {
  float kmh;
  cout << "Enter the speed in kilometers per hour: ";
  cin >> kmh;
  // 1 kilometer is equal to 0.621371 miles.
  float mph = kmh * 0.621371;
  cout << "The speed in miles per hour is: " << mph << endl;
  return 0;
}