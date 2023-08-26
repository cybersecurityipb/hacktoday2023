#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct strukturpointer
{
	int size;
	uint64_t *ptr;
} sp;

sp SP[3];

void winner()
{
	puts("Welcome Hacker");
	system("/bin/sh");
}

void setup()
{

	setvbuf(stdout, NULL, _IONBF, 0);
}

void removee()
{
	int idx;
	printf("idx : ");
	fflush(stdout);
	scanf("%d",&idx);
	if(idx > 2 || idx < 0)
	{
		puts("No Out Of Bound Okay");
		return;
	}

	if(!SP[idx].ptr)
	{
		puts("Not Allocated Yet");
		return;
	}

	free(SP[idx].ptr);
	SP[idx].ptr = NULL;
	puts("Removing Page Done");
}

void request()
{
	int idx,size;
	printf("idx : ");
	fflush(stdout);
	scanf("%d",&idx);
	if(idx > 2 || idx < 0)
	{
		puts("No Out Of Bound Okay");
		return;
	}

	if(SP[idx].ptr)
	{
		puts("Allocated Yet");
		return;
	}
	printf("size : ");
	fflush(stdout);
	scanf("%d",&size);
	if(size > 0x420 || size < 0)
	{
		puts("Size Only between 0x and 0x420");
		return;
	}
	SP[idx].size = size;
	SP[idx].ptr = (uint64_t *)malloc(size);
	puts("Allocation Done");	
}

void fill()
{
	int idx;
	printf("idx : ");
	fflush(stdout);
	scanf("%d",&idx);
	if(idx > 2 || idx < 0)
	{
		puts("No Out Of Bound Okay");
		return;
	}

	if(!SP[idx].ptr)
	{
		puts("Not Allocated Yet");
		return;
	}

	printf("content : ");
	fflush(stdout);
	read(0,SP[idx].ptr, SP[idx].size + 0x10);
	puts("Thank You");
}

void show()
{
	int idx;
	printf("idx : ");
	fflush(stdout);
	scanf("%d",&idx);
	if(idx > 2 || idx < 0)
	{
		puts("No Out Of Bound Okay");
		return;
	}

	if(!SP[idx].ptr)
	{
		puts("Not Allocated Yet");
		return;
	}

	printf("content : %s\n",(char *)SP[idx].ptr);
}



void menu()
{
	puts("Welcome To My Note");
	puts("1. Request Page");
	puts("2. Fill Page");
	puts("3. Show Page");
	puts("4. Remove Page");
	puts("5. Exit");
}

int main(int argc, char **argv)
{
	int choice;
	while(1)
	{
		menu();
		printf("choice : ");
		fflush(stdout);
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
				request();
				break;
			case 2:
				fill();
				break;
			case 3:
				show();
				break;
			case 4:
				removee();
				break;
			case 5:
				exit(0);
				break;
			default:
				puts("choice the right number!");
				break;
		}
	}
	return 0;
}