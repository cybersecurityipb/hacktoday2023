#include <bits/stdc++.h>
using namespace std;


const string FLAG = "hacktoday{l3tS_gO0ooO!!!_CoNr4tu1aTiOn_nOw_y0u_KnoW_wH4t_LCA_Re4L1y_1s(^_^)}";

const int MAX_FOLDER = 9;
const int MAX_FILE   = 5; 

const string CLIENT_NAME = "ln y";
const string USER_NAME   = "you";

const string BRACKET1_ANSI = "\x1b[38;2;93;11;166m";
const string LABEL1_ANSI = "\x1b[38;2;255;150;0m";
const string BRACKET2_ANSI = "\x1b[38;2;17;30;92m";
const string LABEL2_ANSI = "\x1b[38;2;1;255;250m";
const string BRACKET3_ANSI = "\x1b[38;2;220;0;255m";
const string LABEL3_ANSI = "\x1b[38;2;4;255;0m";

const string PROGRESS_BAR_FILL_ANSI = "\x1b[48;2;215;13;255m";
const string PROGRESS_BAR_UNFILL_ANSI = "\x1b[48;2;40;40;40m";
const int PROGRESS_BAR_SIZE = 50;
const int PROGRESS_BAR_MID  = 10;

int query_left = 1e4;
int folder_left = 1e4;


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

vector<string> filenames_v;

vector<string> subnames
{
    "Peninggalan-Mas-Denu",
    "ln-ehe-y",
    "tutor",
    "dekkk",
    "sepuh",
    "puh-ajarin-puh",
    "keuangan",
    "asasi",
    "rapat",
    "bpjs",
    "IPB-University",
    "kampus-IPB",
    "IPB",
    "digdaya",
    "hutang",
    "ITTODAY",
    "kunjungan",
    "ngopi",
    "nyantai",
    "skripsi",
    "skripsiii-finalll",
    "hacktoday2023",
    "hektod",
    "cicilan",
    "tugas",
    "rumah",
    "taman",
    "jungkir",
    "tuntutan",
    "kebijakan",
    "hukum",
    "sekolah",
    "vokasi",
    "biologi",
    "fisika",
    "sejarah",
    "sarjana",
    "ngampus",
    "turu",
    "mbl",
    "teori",
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
    "pekan-ilkomerz",
    "angkatan59",
    "kating",
    "ilkom",
    "CPSC",
    "JOIN-CPSC"
    "ln-y",
    "yqroo",
    "linz",
    "encryptedscrpitss",
    "ghifar",
    "ardhani",
    "compe",
    "bims-kuy",
    "glitchgoo",
    "jedi",
    "kelapacuyy",
    "zantos",
    "luqman",
    "patsac",
    "ZafiN",
    "zran",
    "sooji",
    "arai",
    "kiaraa09",
    "CryLyx",
    "anro128",
    "TLE",
    "TLEverse",
    "TLE-aloevera"
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
    "exe",
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
#pragma region Drawer

void chat(const string& sender, const string& message="")
{
    cout << "\x1b[48;2;85;85;85m  " + sender + "  \x1b[0m" << '\n';
    if (!message.empty())
        cout << message << "\n\n";
}

void option(const string& label, const string& content, const string& bracket_ansi, const string& label_ansi)
{
    cout << bracket_ansi + "[" + label_ansi + label + bracket_ansi + "]" + "\x1b[0m " + content << '\n';
}

string progress_bar(int cur1, int max1, int size=50)
{
    int prg = size * cur1 / max1;
    string result = PROGRESS_BAR_FILL_ANSI + string(prg, ' ') + PROGRESS_BAR_UNFILL_ANSI + string(size - prg, ' ');
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
        chat(name);

        for (int i = 0; i < folders.size(); i++)
        {
            const int num = i + 1;
            string key = to_string(num);

            option(key, folders[i]->name, BRACKET2_ANSI, LABEL2_ANSI);
        }

        for (int i = 0; i < files.size(); i++)
            option("+", files[i]->name, BRACKET3_ANSI, LABEL3_ANSI);

        if (parent == NULL)
            option("0", "RETURN TO MAIN MENU", BRACKET2_ANSI, LABEL2_ANSI);
        else
            option("0", "BACK", BRACKET2_ANSI, LABEL2_ANSI);
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

string client_chat, user_input;

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
            active = active->folders[o - 1];
        else
            cout << "folder not found\n\n";
    }
}

void chat_room()
{
    if (!query_left)
    {
        chat(CLIENT_NAME, "boleh juga kamu dik... selamat bekerja di TLEcorp :)\nsilahkan dinikmati hidangan pembukanya...\n" + FLAG);

        exit(0);
    }

    string client_req_item1, client_req_item2;
    if (client_chat.empty())
    {
        client_req_item1 = filenames_v[rand() % filenames_v.size()];
        client_req_item2 = filenames_v[rand() % filenames_v.size()];
        
        client_chat = client_req_item1 + " dan " + client_req_item2;
    }

    chat(CLIENT_NAME, client_chat);

    option("1", "ANSWER CHAT", BRACKET2_ANSI, LABEL2_ANSI);
    option("0", "RETURN TO MAIN MENU", BRACKET2_ANSI, LABEL2_ANSI);

    int o = 1; cin >> o;
    cout << '\n';

    switch (o)
    {
    case 0:
        return;
        break;
    case 1:
        chat(USER_NAME);

        cin >> user_input;
        cout << '\n';

        if (user_input != get_lca(client_req_item1, client_req_item2))
        {
            chat(CLIENT_NAME, "aduhhh kayaknya kamu orangnya tidak bisa berpikir cepat dan tidak cekatan ya dekk!!!\nkecewa...\ncoba lagi taun depan :)");
            
            exit(0);
        }

        --query_left;
        client_chat.clear();
        chat_room();
        break;
    default:
        break;
    }
}

void help_room()
{
    chat("How to Navigate");
    cout << "- [x] where x is an integer means that you can choose that option to navigate\n";
    cout << '\n';

    chat("Constraints");
    cout << "- There are 10000 folders in total\n";
    cout << "- Each folder only contains up to 9 folders\n";
    cout << "- Each folder only contains up to 5 files\n";
    cout << "- You need to answer ln y correctly 10000 times\n";
    cout << '\n';

    option("0", "RETURN TO MAIN MENU", BRACKET2_ANSI, LABEL2_ANSI);

    int o; cin >> o;
    cout << '\n';
    switch (o)
    {
    case 0:
        return;
        break;
    default:
        cout << "hmm, minimal input yg bener dulu dik :(\n\n";
        help_room();
        break;
    }
}

void main_room()
{
    chat("Main Menu");
    option("1", "OPEN FOLDER", BRACKET1_ANSI, LABEL1_ANSI);
    option("2", "OPEN CHAT", BRACKET1_ANSI, LABEL1_ANSI);
    option("3", "HELP", BRACKET1_ANSI, LABEL1_ANSI);
    option("0", "EXIT", BRACKET1_ANSI, LABEL1_ANSI);

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
    case 3:
        help_room();
        break;
    default:
        cout << "hmm, minimal input yg bener dulu dik :(\n\n";
        break;
    }
}

#pragma endregion
#pragma region Initialization

void generate_random_folders()
{
    chat("LOADING DATA");

    int MAXN = folder_left;
    int MAXM = 0;

    srand(time(0));

    queue<folder*> que;
    que.push(root);
    while (!que.empty())
    {
        folder* const tmp = que.front();
        que.pop();


        if (folder_left)
        {
            
            cout << progress_bar(MAXN - folder_left, MAXN, PROGRESS_BAR_MID) + string(PROGRESS_BAR_SIZE - PROGRESS_BAR_MID, ' ') << '\r';
            MAXM = que.size();
        }
        else
            cout << PROGRESS_BAR_FILL_ANSI + string(PROGRESS_BAR_MID, ' ') + progress_bar(MAXM - que.size(), MAXM, PROGRESS_BAR_SIZE - PROGRESS_BAR_MID) << '\r';
        cout << "\x1b[0m";
        
        tmp->generate_random(folder_left);
        for (auto& fld : tmp->folders)
        {
            graph[tmp].push_back(fld);
            que.push(fld);
        }
        for (auto& fil : tmp->files)
            grp[fil->name] = tmp;
    }
    cout << "LOADING FINISHED" + string(PROGRESS_BAR_SIZE - 16, ' ');

    filenames_v = vector(filenames.begin(), filenames.end());

    cout << "\n\n";
}

void generate_sparse_table()
{
    dfs(root, NULL);
    stable = new sparse_table<int>(dpt);
}

#pragma endregion

int main()
{
    // INITIALIZE
    generate_random_folders();
    generate_sparse_table();

    // SIMULATE
    while (true) main_room();
    
    return 0;
}