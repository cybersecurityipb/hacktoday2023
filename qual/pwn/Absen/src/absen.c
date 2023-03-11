# include <stdio.h>
# include <stdlib.h>

char large_buffer[512];

void init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void win(){
	FILE *f = fopen("flag.txt","r");
	  if (f == NULL) {
	    printf("%s", "flag.txt not found");
	    exit(0);
	  }
	    
	char flag[50];
	fgets(flag,50,f);
  	printf("kamu berhasil absen\n%s\n", flag);
  	exit(0); 
}

int main(int argc, char** argv){
    init();
    char buffer[8];
    printf("Nama : ");
    fgets(buffer, 8, stdin);
    printf(buffer);
    printf("NIM : ");
    fgets(large_buffer, 512, stdin);
    printf(large_buffer);
    printf("Asal Univ: ");
    fgets(large_buffer, 512, stdin);
    printf(large_buffer);
    puts("ga boleh nitip absen ya");
    return 0;
}

// compiled with gcc -no-pie -Wl,-z,relro,-z,now -o absen absen.c