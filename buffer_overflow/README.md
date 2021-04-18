# Buffer Overflow Attacks

# To start the container instance
docker compose build
# docker-compose build
sudo docker run -it --privileged --name eureka-lab --hostname buffer sec-linux bash




# Compile Commands
gcc -z execstack -m32 -o call_shellcode call_shellcode.c
# or gcc -z execstack -m32 -fno-pic -o call_shellcode call_shellcode.c

As root,
gcc -z execstack -fno-stack-protector -m32 -o stack stack.c
chmod 4755 stack

As non-root,
gcc -m32 -o exploit exploit-modified.c
./exploit
./stack