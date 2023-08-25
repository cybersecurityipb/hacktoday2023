#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <seccomp.h>

char* TICKET[16];
const size_t MALLOC_SIZE = 0x20;
const char* prompt = "Seat Number : ";

void init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void seccomp_rules(){
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_KILL);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit), 0);
    seccomp_load(ctx);
}

void menu(){
    printf("\n[+] 1. Order Ticket\n");
    printf("[+] 2. Verify Ticket\n");
    printf("[+] 3. Refund\n");
}

unsigned long ticketid(const char* prompt) {
  unsigned long idx;
  printf("%s", prompt);
  scanf("%lu%*c", &idx);
  if (idx < 0 || idx >= 16) {
    _exit(-1);
  }
  return idx;
}

void order(unsigned long idx){
    TICKET[idx] = malloc(MALLOC_SIZE);
    printf("Name : ");
    read(STDIN_FILENO, TICKET[idx], MALLOC_SIZE + 0x10);
}

void verify(unsigned long idx){
    char confirmation[MALLOC_SIZE];
    
    if (TICKET[idx] == NULL){
        printf("This seat is available, you are free to order this one\n");
    } else {
        printf("Please Confirm !\n");
        printf("Your seat %lu\n", idx);
        printf("please say your name for confirmation : ");
        read(STDIN_FILENO, confirmation, MALLOC_SIZE);
        if (strcmp(TICKET[idx],confirmation) == 0){
            printf("This ticket has been verified, for your own safety please change the ticket name\n");
            printf("New name : ");
            read(STDIN_FILENO, TICKET[idx], MALLOC_SIZE);
        } else {
            printf("Sorry sir this ticket belongs to %s", TICKET[idx]);
            TICKET[idx] = NULL;
        }
    }
}

void refund(unsigned long idx){
    if (TICKET[idx] == NULL){
        printf("This seat is available, you are free to order this one\n");
    } else {
        free(TICKET[idx]);
        printf("ok\n");
    }
}

int main(int argc, char** argv){

    int input;
    unsigned long idx;

    init();
    seccomp_rules();
    printf("===============================\n");
    printf("== WELCOME TO HACKTODAY 2023 ==\n");
    printf("===============================\n");
    printf("can u secure ticket for final??\n");
    while(1){
        menu();
        printf("> ");
        scanf("%d%*c", &input);
        
        switch (input){
            case 1:
                idx = ticketid(prompt);
                order(idx);
                break;
            case 2:
                idx = ticketid(prompt);
                verify(idx);
                break;
            case 3:
                idx = ticketid(prompt);
                refund(idx);
                break;
            default:
                puts("Invalid choice!");
                _exit(0);
        }
    }
}

// gcc spirit.c -o spirit -lseccomp