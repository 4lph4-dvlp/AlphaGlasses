#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char baseURL[1000] = "http://greencafe.kro.kr:80";
char cmd[1000];

int main() {

  while(1) {
    printf("dd\n");
    sprintf(cmd, "wget -q -r -np -R  \"index.html*\" %s/static/list -O ./list", baseURL);
    printf("%s", cmd);
    system(cmd);

    FILE *fp = fopen("./list", "r");

    char userName[1000];
    while(fscanf(fp, "%s", userName) != EOF) {
      printf("%s\n", userName);
      sprintf(cmd, "mkdir ./user/%s", userName);
      system(cmd);
      
      sprintf(cmd, "mkdir ./user/%s/img", userName);
      system(cmd);
      
      sprintf(cmd, "wget -q -r -np -R \"index.html*\" %s/static/%s/info.txt -O ./user/%s/info.txt"
      , baseURL, userName, userName);
      system(cmd);

      for(int i=1 ; i<=100 ; i++) {
        sprintf(cmd, "wget -q -r -np -R \"index.html*\" %s/static/%s/img/%d.png -O ./user/%s/img/%d.png"
        , baseURL, userName, i, userName, i);
        system(cmd);
      }
    }
    
    usleep(10 * 60 * 1000 * 1000 / 10);
  }
}
