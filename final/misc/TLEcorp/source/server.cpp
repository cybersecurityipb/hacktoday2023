#include <bits/stdc++.h>
using namespace std;


string flag = "hacktoday{hAd3uh_kErJ4_CAp3_juGA_yAahHhHhhhH4h_UnTUn6_4dA_Lc4_h3h3}";

const int MAX_FOLDER = 9;
const int MAX_FILE   = 15; 

int query_left = 1e5;
int folder_left = 1e5;

string client_name = "ln y";
string user_name   = "you";


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
    sparse_table()
    {}

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
#pragma region Name

set<string> foldernames;
set<string> filenames;

vector<string> foldernames_v;
vector<string> filenames_v;

vector<string> subnames
{
    "keuangan",
    "rapat",
    "bpjs",
    "IPB_University",
    "kampus_IPB",
    "ITTODAY",
    "hacktoday2023",
    "hektod",
    "cicilan",
    "tugas",
    "rumah",
    "taman",
    "kebijakan",
    "hukum",
    "sekolah",
    "vokasi",
    "biologi",
    "fisika",
    "sejarah",
    "mbl",
    "teori"
    "kalkulus2",
    "matematika",
    "hak",
    "martabat",
    "uang",
    "harga",
    "biaya",
    "bunga",
    "pajak",
    "rapat",
    "konvensional",
    "FMIPA",
    "angkatan59",
    "ln_y",
    "yqroo",
    "linz",
    "encrypted",
    "bimskuy",
    "ghifar",
    "ghifar",
    "compe_",
    "glitchgoo",
    "jedi",
    "kelapacuyy",
    "zantos",
    "luqman",
    "patsac",
    "ZafiN",
    "zran",
    "sooji",
    "araii",
    "Kiaraa",
    "CryLyx",
    "anro",
    "Burhanez",
    "Subhanez",
    "japran",
    "TLE",
    "TLEverse"
};
vector<string> extensions
{
    "jpg",
    "png",
    "pdf",
    "doc",
    "docx",
    "pptx",
    "zip",
    "html",
    "xml"
};

string get_random_name()
{
    string result = subnames[rand() % subnames.size()];

    const int n = rand() % 4;
    for (int i = 0; i < n; i++)
        result += "_" + subnames[rand() % subnames.size()];
    string add = to_string(rand() % 10000);
    add = "_" + string(4 - add.size(), '0') + add;
    result += add;

    return result;
}

string get_random_name(set<string>& _holder, string _extension="")
{
    if (_extension.empty())
    {
        string result = get_random_name();
        while (_holder.count(result))
            result = get_random_name();
        _holder.insert(result);
        
        return result;
    }

    string result = get_random_name() + "." + _extension;
    while (_holder.count(result))
        result = get_random_name() + "." + _extension;
    _holder.insert(result);
    
    return result;
}

string get_random_extension()
{
    string result = extensions[rand() % extensions.size()];

    return result;
}

#pragma endregion
#pragma region Structure

class folder;
class file;

class file
{
public:
    string name;
    folder* parent;

public:

public:
    file(string _name)
        : name(move(_name))
    {}
};

class folder
{
public:
    string name;
    folder* parent = NULL;
    vector<folder*> folders;
    vector<file*> files;

public:
    void add(folder* _folder)
    {
        _folder->parent = this;
        folders.push_back(_folder);
    }

    void add(file* _file)
    {
        _file->parent = this;
        files.push_back(_file);
    }

    void generate_random(int& _folder_left)
    {   
        const int n = min(_folder_left, 1 + rand() % min(MAX_FOLDER, 1 + _folder_left));
        const int m = rand() % (MAX_FILE + 1);

        for (int i = 0; i < n; i++)
            add(new folder(get_random_name(foldernames)));
        for (int i = 0; i < m; i++)
        {
            string extension = get_random_extension();
            add(new file(get_random_name(filenames, extension)));
        }

        _folder_left -= n;
    }

    void draw()
    {
        cout << "\x1b[48;2;85;85;85m  " + name + "  \x1b[0m" << '\n';

        for (int i = 0; i < folders.size(); i++)
        {
            const int num = i + 1;
            string key = to_string(num);

            cout << "\x1b[38;2;17;30;92m[\x1b[38;2;1;255;250m" + key + "\x1b[38;2;17;30;92m]\x1b[0m ";
            cout << folders[i]->name << '\n';
        }
        for (int i = 0; i < files.size(); i++)
        {
            cout << "\x1b[38;2;220;0;255m[\x1b[38;2;4;255;0m+\x1b[38;2;220;0;255m]\x1b[0m ";
            cout << files[i]->name << '\n';
        }
        if (parent == NULL)
        {
            cout << "\x1b[38;2;17;30;92m[\x1b[38;2;1;255;250m0\x1b[38;2;17;30;92m]\x1b[0m RETURN TO MAIN MENU\n";
        }
        else
        {
            cout << "\x1b[38;2;17;30;92m[\x1b[38;2;1;255;250m0\x1b[38;2;17;30;92m]\x1b[0m BACK\n";
        }
    }

public:
    folder(string _name)
        : name(move(_name))
    {}
};

folder* const root = new folder("Drive_C");

#pragma endregion
#pragma region Checker

map<folder*, vector<folder*>> graph;
map<string, folder*> grp;

vector<int> dpt;
vector<map<int, folder*>> idx;
map<folder*, int> re;

sparse_table<int>* stable;

void dfs(folder* u, folder* p, int d=0)
{
    while (idx.size() <= d)
        idx.push_back({});

    dpt.push_back(d);
    idx[d][dpt.size() - 1] = u;
    re[u] = dpt.size() - 1;

    for (folder* v : graph[u])
    {
        if (v == p)
            continue;
        
        dfs(v, u, d + 1);
        dpt.push_back(d);
        idx[d][dpt.size() - 1] = u;
    }
}

string get_lca(string& u, const string& v)
{
    int l = re[grp[u]];
    int r = re[grp[v]];

    if (l > r) swap(l, r);

    int d = stable->get(l, r);
    string result = idx[d].lower_bound(l)->second->name;

    return result;
}

#pragma endregion
#pragma region Main

void chat(const string& sender, const string& message="")
{
    cout << "\x1b[48;2;85;85;85m  " + sender + "  \x1b[0m" << '\n';
    if (!message.empty())
        cout << message << "\n\n";
}


void folder_room()
{
    folder* active = root;

    while (true)
    {
        active->draw();
        int o; cin >> o;
        cout << '\n';
        
        if (!o)
        {
            if (active->parent == NULL)
            {
                break;
            }
            else
            {
                active = active->parent;
            }
        }
        else if (o <= active->folders.size())
        {
            active = active->folders[o - 1];
        }
        else
        {
            cout << "command not found\n";
        }
    }
}

void chat_room()
{
    if (!query_left)
    {
        chat(client_name, "Terima kasih banyak dik, nih hadiah :)\n" + flag);

        exit(0);
    }

    cout << "\x1b[38;2;17;30;92m[\x1b[38;2;1;255;250m1\x1b[38;2;17;30;92m]\x1b[0m CHAT\n";
    cout << "\x1b[38;2;17;30;92m[\x1b[38;2;1;255;250m0\x1b[38;2;17;30;92m]\x1b[0m RETURN TO MAIN MENU\n";

    int o; cin >> o;
    cout << '\n';

    string client_req_item1, client_req_item2, client_chat, user_input;
    switch (o)
    {
    case 0:
        return;
        break;
    case 1:
        client_req_item1 = filenames_v[rand() % filenames_v.size()];
        client_req_item2 = filenames_v[rand() % filenames_v.size()];

        client_chat = client_req_item1 + " dan " + client_req_item2;

        chat(client_name, client_chat);

        chat(user_name);

        cin >> user_input;
        cout << '\n';

        if (user_input != get_lca(client_req_item1, client_req_item2))
        {
            chat(client_name, "aduhhh perusahaan jadi bangkrut gara-gara kesalahan kamu doang dekk!!!\nkecewa...");
            
            exit(0);
        }

        --query_left;
        chat_room();
        break;
    default:
        break;
    }
}

void main_room()
{
    cout << "\x1b[38;2;93;11;166m[\x1b[38;2;255;150;0m1\x1b[38;2;93;11;166m]\x1b[0m FOLDER ROOM\n";
    cout << "\x1b[38;2;93;11;166m[\x1b[38;2;255;150;0m2\x1b[38;2;93;11;166m]\x1b[0m CHAT ROOM\n";
    cout << "\x1b[38;2;93;11;166m[\x1b[38;2;255;150;0m0\x1b[38;2;93;11;166m]\x1b[0m EXIT\n";

    int o; cin >> o;
    cout << '\n';
    switch (o)
    {
    case 0:
        exit(0);
        break;
    case 1:
        folder_room();
        break;
    case 2:
        chat_room();
        break;
    default:
        cout << "hmm, minimal input yg bener dulu dik :(~\n";
        break;
    }
}

#pragma endregion


int main()
{
    // GENERATE RANDOM FILES
    srand(time(0));

    queue<folder*> que;
    que.push(root);
    while (!que.empty())
    {
        folder* const tmp = que.front();
        que.pop();

        tmp->generate_random(folder_left);
        for (auto& fld : tmp->folders)
        {
            graph[tmp].push_back(fld);
            que.push(fld);
        }
        for (auto& fil : tmp->files)
            grp[fil->name] = tmp;
    }

    foldernames_v = vector(foldernames.begin(), foldernames.end());
    filenames_v = vector(filenames.begin(), filenames.end());
    
    dfs(root, NULL);
    stable = new sparse_table<int>(dpt);

    // SIMULATE
    while (true)
        main_room();
    
    return 0;
}