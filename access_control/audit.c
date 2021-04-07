#define _GNU_SOURCE
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    char *v[3];
    if(argc < 2) {
        printf("Please type a file name.\n");
        return 1;
        }

    v[0] = "/bin/cat"; v[1] = argv[1]; v[2] = 0;

    /*
        Set q = 0 for questions related to system(),
        and q = 1 for related to execve()
    */
    int q = 0;

    if (q == 0){
        char *command = malloc(strlen(v[0]) + strlen(v[1]) + 2);
        sprintf(command, "%s %s", v[0], v[1]);
        system(command);
        }
    else
        execve(v[0], v, 0);

    return 0 ;
}