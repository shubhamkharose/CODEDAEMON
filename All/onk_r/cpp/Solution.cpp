#include<bits/stdc++.h>
using namespace std;
int main() {
   int key = 66;
   char cipher[] = "%!')!6$$.#%9ztvwpsqpsq?";
   for(int i=0;i<24;i++){
       printf("%c",(int)cipher[i]^key);
   }
   
}
