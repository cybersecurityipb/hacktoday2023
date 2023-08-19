#include <cstdio>
using namespace std;

void get_input(char* buff, int n);

class Note {
    public:
        char* public_note;
        char* private_note;

    void virtual print_public(){
        printf("echo %s > /dev/null\n", public_note);
        printf("saved :0\n");
    }

    void virtual get_private(){
        printf("private note: ");
        get_input(private_note, 512);
        printf("edit public note: ");
        get_input(public_note, 96);
    }
};

void get_input(char* buff, int n){
    char c;
    while ((c = getchar()) != '\n' && n >= 0){
        *buff = c;
        buff++;
        n--;
    }
}

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

Note *pn;
char private_buffer[512] = {0};

int main(void){
    init();

    Note n;
    pn = &n;
    char buffer[32] = {0};

    printf("Enter your note: ");
    get_input(buffer, 32);

    pn->public_note = buffer;
    pn->private_note = private_buffer;
    pn->print_public();

    return 0;
}
