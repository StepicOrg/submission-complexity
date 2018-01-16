#include <iostream>
using namespace std;
int main() {
  int n, m, x, y;
    cin >> m >> n >> x >> y;
    if (m >= n && y < m/2 && x < n/2 && y < x ||   m>=n && y < m/2 && x > n/2 && y < (n - x) || m <= n && y < n/2 && x < m/2 && y < x ||  m <= n && y < n/2 && x > m/2 && y < (m - x) || y==0 ) {
        cout << y;
        }
     else if (m >= n && y> m/2 && x < n/2 &&  (m-y) < x || m>=n && y > m/2 && x > n/2 && (m - y)< (n - x) ) {
        cout << m - y;
    }
    else if (m <= n && y > n/2 && x < m/2 && (n-y) < x || m <=n && y > n/2 && x > m/2 && (n - y) < (m - x) ) {
        cout << n - y;

    }
        else if (m>=n && y > m/2 && x > n/2 && (m - y) > (n - x) || m>=n && y < m/2 && x > n/2 && y >(n - x) ) {
            cout << n - x;
                    }
    else if (m <= n && y < n/2 && x > m/2 && y > (m - x)|| m <=n && y > n/2 && x > m/2 && (n - y) >(m - x) ){
        cout << m - x;
    }
    else {
        cout << x;
        }
  return 0;
}
