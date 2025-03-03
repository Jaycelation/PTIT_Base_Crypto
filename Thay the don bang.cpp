#include<bits/stdc++.h>
using namespace std;

char encrypt(char c, string s){
	if(!isalpha(c)) return c;
	c = toupper(c);
	int index = c - 'A';
	return s[index];
}

char decrypt(char c, string s){
	if(!isalpha(c)) return c;
	c = toupper(c);
	size_t pos = s.find(c);
	return char(pos + 'A');
}

string encryptText(string s, string key){
	string res = "";
	for(char c: s){
		res += encrypt(c, key);
	}
	return res;
}

string decryptText(string s, string key){
	string res = "";
	for(char c: s){
		res += decrypt(c, key);
	}
	return res;
}

int main(){
	string key = "ZPBYJRSKFLXQNWVDHMGUTOIAEC";
	string plaintext;
	cin >> plaintext;
	cout << encryptText(plaintext, key) << endl;
	return 0;
}
