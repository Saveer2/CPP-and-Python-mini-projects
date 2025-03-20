#include <iostream>
#include <cmath>

using namespace std;

class graph {
public:
    void formula(double Hc) {
        double t;
        double Tc = 9.2;
        double Ho = 150 * 1000;

        double value = 1 - (Hc / Ho);
        if (value < 0) {  
            cout << "Error: sqrt() of a negative number is not possible!" << endl;
            return;
        } else {
            t = Tc * sqrt(value);
            cout << "Hc: " << Hc << " -> T: " << t << endl;
            plot(Hc, t);
        }
    }

    void loop() {
        int num;
        cout << "Enter number of readings: ";
        cin >> num;

        double *Hc = new double[num];  
        for (int i = 0; i < num; i++) {
            cout << "Enter value " << (i + 1) << " for Hc: ";
            cin >> Hc[i];
        }
        cout << endl;

        for (int i = 0; i < num; i++) {
            formula(Hc[i]);
        }

        delete[] Hc;  
    }

    void plot(double Hc, double T) {
        int scale = 10;  
        int pos = static_cast<int>(T * scale);  

        cout << Hc << " | ";
        for (int i = 0; i < pos; i++) {
            cout << "*";
        }
        cout << endl;
    }
};

int main() {
    graph g1;
    g1.loop();
    return 0;
}