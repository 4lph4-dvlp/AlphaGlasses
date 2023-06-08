#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char baseURL[3000] = "http://localhost:3000";
char cmd[3000];

int main() {

  while(1) {
    printf("dd\n");
    sprintf(cmd, "wget -q -r -np -R  \"index.html*\" %s/static/list -O ./list", baseURL);
    printf("%s", cmd);
    system(cmd);

    FILE *fp = fopen("./list", "r");

    char userName[1000];
    while(fscanf(fp, "%s", userName) != EOF) {
      sprintf(cmd, "mkdir ./user/%s", userName);
      system(cmd);
      
      sprintf(cmd, "mkdir ./user/%s/img", userName);
      system(cmd);
      printf("[*] Made Directories : %s\n", userName);
      
      sprintf(cmd, "wget -q -r -np -R \"index.html*\" %s/static/%s/info.txt -O ./user/%s/info.txt"
      , baseURL, userName, userName);
      system(cmd);
      printf("[*] Getting infoText\n");

      for(int i=1 ; i<=100 ; i++) {
        sprintf(cmd, "wget -q -r -np -R \"index.html*\" %s/static/%s/img/%d.jpg -O ./user/%s/img/%d.jpg"
        , baseURL, userName, i, userName, i);
        system(cmd);
      }
      printf("[*] Getting Imgs\n");
    }
    
    usleep(10 * 60 * 1000 * 1000);
  }
}