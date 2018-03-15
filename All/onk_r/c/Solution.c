#include<bits/stdc++.h>
#define ll long long
#define vll vector<ll>
#define sll set<ll>
#define mll map<ll,ll>
#define MOD 1000000007
#define fo(i,m,n) for(i=m;i<n;i++)
#define fore(i,m,n) for(i=m;i>=n;i--)
 
using namespace std;
ll getMid(ll s, ll e) {  return s + (e -s)/2;  }
ll cnt = 0;
ll getXorUtil(ll *st, ll ss, ll se, ll qs, ll qe, ll si,ll x)
{
    if (qs <= ss && qe >= se)
        return st[si];
    if (se < qs || ss > qe)
        return 0;
    ll mid = getMid(ss, se);
    ll one = getXorUtil(st, ss, mid, qs, qe, 2*si+1,x);
    ll two = getXorUtil(st, mid+1, se, qs, qe, 2*si+2,x);
    cnt+=one==x;
    cnt+=two==x;
    return one^two;
}
void updateValueUtil(ll *st, ll ss, ll se, ll i, ll diff, ll si)
{
    if (i < ss || i > se)
        return;
    st[si] = st[si] + diff;
    if (se != ss)
    {
        ll mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i, diff, 2*si + 1);
        updateValueUtil(st, mid+1, se, i, diff, 2*si + 2);
    }
}
  
void updateValue(ll arr[], ll *st, ll n, ll i, ll new_val)
{
    if (i < 0 || i > n-1)
    {
        return;
    }
  
    ll diff = new_val - arr[i];
  
    arr[i] = new_val;
  
    updateValueUtil(st, 0, n-1, i, diff, 0);
}
  
ll getXor(ll *st, ll n, ll qs, ll qe,ll x)
{
    if (qs < 0 || qe > n-1 || qs > qe)
    {
        return -1;
    }
    cnt=0;
    return getXorUtil(st, 0, n-1, qs, qe, 0,x);
}
  

ll constructSTUtil(ll arr[], ll ss, ll se, ll *st, ll si)
{
    if (ss == se)
    {
        st[si] = arr[ss];
        return arr[ss];
    }
  
    ll mid = getMid(ss, se);
    st[si] =  constructSTUtil(arr, ss, mid, st, si*2+1) ^
              constructSTUtil(arr, mid+1, se, st, si*2+2);
    return st[si];
}
  
ll *constructST(ll arr[], ll n)
{
    ll x = (ll)(ceil(log2(n))); 
    ll max_size = 2*(ll)pow(2, x) - 1; 
    ll *st =  (ll *)malloc(sizeof(ll)*max_size);
    constructSTUtil(arr, 0, n-1, st, 0);
    return st;
}
  
int main()
{
    ll i,n,q,qeri;
    scanf("%Ld %Ld",&n,&q);
    ll a[n];
    fo(i,0,n){
    	scanf("%Ld",&a[i]);
	}
    ll *st = constructST(a, n);
    fo(qeri,0,q)
    {
    	ll mode,index,x;
    	scanf("%Ld %Ld %Ld",&mode,&index,&x);
		if(mode==1){
    	      updateValue(a, st, n, index-1, x);
		}
    	else{
    	    getXor(st, n, 0, i,x);
    		printf("%Ld\n",cnt);
		}
	}
    return 0;
}