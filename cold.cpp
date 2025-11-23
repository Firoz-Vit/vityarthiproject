#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; cin >> t;
	while(t--){
		long long po = 0 , pe = 0 , qo = 0 , qe = 0; 
		long long n; cin >> n;

		vector<long long> wow(n);
		for(long long i = 0; i < n; i++){
			cin >> wow[i];
			if(wow[i] % 2 == 0) pe++;
			else if(wow[i] % 2 != 0) po++;
		}
		long long m; cin >> m;
		vector<long long> owo(m);
		
		for(long long i = 0; i < m; i++){
			cin >> owo[i];
			if(owo[i] % 2 == 0) qe++;
			else if(owo[i] % 2 != 0) qo++;
		}
		cout << ((po * qo) + (pe * qe)) << "\n";
	}
}
