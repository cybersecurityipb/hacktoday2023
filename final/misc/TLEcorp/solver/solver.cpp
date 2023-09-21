#include <bits/stdc++.h>
using namespace std;

#pragma region Sparse Table

#ifndef _SPARSE_TABLE
#define _SPARSE_TABLE 1

template <typename _Tp>
class sparse_table
{
    using _Func = function<_Tp(_Tp, _Tp)>;

public:
    const int           size, height;
    const _Func         func;
    const bool          overlap_func;
    vector<vector<_Tp>> data;

public:
    const _Tp get(const int& _idx) const
    {
        return data[0][_idx];
    }

    const _Tp get(const int& _lidx, const int& _ridx) const
    {
        const int n = _ridx - _lidx + 1;
        const int p = 32 - (__builtin_clz(n) + 1);
        const int k = 1 << p;

        if (!overlap_func)
            return func(data[p][_lidx], data[p][_ridx - k + 1]);
        if (__builtin_popcount(n) == 1)
            return data[p][_lidx];
        return func(data[p][_lidx], (*this).get(_lidx + k, _ridx));
    }


    const auto operator[] (const int &_idx) const
    {
        return data[_idx];
    }

public:
    template <typename _Iter>
    sparse_table(_Iter _begin, _Iter _end, const _Func& _func=[](_Tp _lval, _Tp _rval){ return min(_lval, _rval); }, const bool& _overlap_func=false)
        : size(_end - _begin), height(32 - __builtin_clz(size)), func(_func), overlap_func(_overlap_func)
    {
        data.resize(height);

        data[0].reserve(size);
        for (auto it = _begin; it != _end; ++it)
            data[0].emplace_back(*it);
            
        for (int i = 1, n = size - 1; n > 0; n -= 1 << i++)
        {
            data[i].reserve(n);
            for (int j = 0; j < n; ++j)
                data[i].emplace_back(func(data[i - 1][j], data[i - 1][j + (1 << (i - 1))]));
        }
    }

    template <typename _Sequence>
    sparse_table(const _Sequence& _sequence, const _Func& _func=[](_Tp _lval, _Tp _rval){ return min(_lval, _rval); }, const bool& _overlap_func=false)
        : sparse_table(_sequence.begin(), _sequence.end(), _func, _overlap_func)
    {}

    template <typename _Sequence, size_t _Size>
    sparse_table(const _Sequence (&_sequence)[_Size], const _Func& _func=[](_Tp _lval, _Tp _rval){ return min(_lval, _rval); }, const bool& _overlap_func=false)
        : sparse_table(_sequence, _sequence + _Size, _func, _overlap_func)
    {}
};

#endif /* _SPARSE_TABLE */

#pragma endregion


int n, m;

map<string, vector<string>> graph;
map<string, string> grp;

vector<string> tbl;
vector<int> dpt;
vector<map<int, string>> idx;
map<string, int> re;

void dfs(const string& u, const string& p, int d)
{
    while (idx.size() < d)
        idx.push_back({});

    tbl.push_back(u);
    dpt.push_back(d);
    idx[d][tbl.size() - 1] = u;
    re[u] = tbl.size() - 1;

    for (string& v : graph[u])
    {
        if (v == p)
            continue;
        
        dfs(v, u, d + 1);
        tbl.push_back(u);
        dpt.push_back(d);
        idx[d][tbl.size() - 1] = u;
    }
}

int main()
{
    cin >> n;
    while (n--)
    {
        string u, v;
        cin >> u >> v;

        graph[u].push_back(v);
    }

    cin >> n;
    while (n--)
    {
        string u, v;
        cin >> m >> v;

        while (m--)
        {
            cin >> u;
            grp[u] = v;
        }
    }

    sparse_table<string> stable(tbl);

    while (true)
    {
        string u, v;
        cin >> u >> v;

        u = grp[u];
        v = grp[v];

        int l = re[u];
        int r = re[v];
        if (l > r) swap(l, r);

        int d = dpt[re[stable.get(l, r)]];
        string result = idx[d].lower_bound(l)->second;

        cout << result << '\n';
    }
}