#include <stdio.h>
#include <unistd.h>

int main() {
  char *cmd = "/bin/sh";
  char *argv[] = { cmd, NULL };
  char *envp[] = { NULL };

  execve("/bin/sh", argv, envp);
  return 0;
}