# Docker SSH Authentication Lab Instructions

## Project Overview
This is a Docker-based security lab demonstrating SSH authentication methods (password and host-based authentication) in an isolated network environment. The lab consists of two Alpine Linux containers: an SSH server and an SSH client.

## Architecture

### Network Design
- **Internal isolated network**: `auth-network` (10.0.103.0/24)
- **SSH Server**: 10.0.103.2 (ssh-server)
- **SSH Client**: 10.0.103.3 (ssh-client)
- Network is `internal: true` - no external internet access, isolated lab environment

### Components

#### SSH Server (`ssh_server/`)
- **Base**: Alpine Linux with OpenSSH server
- **Entrypoint**: `/entrypoint.sh` - generates host keys and starts sshd in foreground mode (-D -e)
- **Users**: root, student (password: "password"), instructor (password: "password")
- **SSH Config**: 
  - PermitRootLogin enabled
  - Host-based authentication enabled (`HostbasedAuthentication yes`)
  - Trusted hosts defined in `/etc/ssh/shosts.equiv` (ssh-client, 10.0.103.3)
  - `IgnoreRhosts no` - allows .rhosts/.shosts files
  - `HostbasedUsesNameFromPacketOnly yes` - uses packet hostname for auth

#### SSH Client (`ssh_client/`)
- **Base**: Alpine Linux with OpenSSH client
- **Users**: root, student (no password), instructor (no password)
- **SSH Config**:
  - Host-based authentication enabled
  - `EnableSSHKeysign yes` - required for host-based auth

### Key Files
- `docker-compose.yml`: Defines services, network, and IP assignments
- `ssh_server/Dockerfile`: Server configuration with SSH settings embedded in RUN commands
- `ssh_client/Dockerfile`: Client configuration with host-based auth setup
- `ssh_server/rootfs/entrypoint.sh`: Server startup script
- `pub_keys/`: Directories for storing SSH public keys (currently empty placeholders)

## Development Patterns

### Configuration Approach
- **Inline configuration**: SSH settings modified via `sed` commands in Dockerfiles (not separate config files)
- **Pre-baked users**: Users and passwords created during image build, not at runtime
- **Privileged containers**: Both containers run as `privileged: true` for SSH key signing operations

### SSH Setup Pattern
```dockerfile
sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config
```
- All SSH configuration changes use in-place `sed` editing
- Echo commands append additional config lines when sed replacement isn't suitable

### User Management
- All users get bash shell (`-s /bin/bash`)
- Custom PS1 prompts set in `.bashrc` and `/etc/profile` for consistent shell experience
- Student users have unlocked passwords (`passwd -u`)

## Workflows

### Build and Run
```bash
docker-compose up --build
```
Builds both images and starts the lab environment.

### Access Containers
```bash
docker exec -it ssh-client /bin/bash
docker exec -it ssh-server /bin/bash
```

### Testing SSH from Client
```bash
# From ssh-client container
ssh student@ssh-server  # Password authentication
ssh student@10.0.103.2  # Using IP
```

### Debugging SSH
- Server logs: `docker logs ssh-server` (sshd runs with `-e` flag for stderr logging)
- Check SSH config: `docker exec ssh-server cat /etc/ssh/sshd_config`
- Verify host keys: `docker exec ssh-server ls -la /etc/ssh/`

## Important Conventions

1. **No external dependencies**: Lab is completely self-contained and isolated
2. **Commented volumes**: Volume mounts in docker-compose.yml are commented out - enable when working with key distribution
3. **Fixed IP addresses**: Services use static IPs for predictable networking in security demonstrations
4. **Alpine Linux**: Lightweight base, uses `apk` for packages and `ash` shell for scripts
5. **Educational focus**: Configurations prioritize demonstration of security concepts over production hardening (e.g., root login enabled, simple passwords)

## Modification Guidelines

- **Adding users**: Update both Dockerfiles with matching usernames for authentication testing
- **Changing network**: Update subnet in docker-compose.yml AND hardcoded IPs in ssh_server's shosts.equiv
- **Adding SSH keys**: Uncomment volume mounts and place keys in respective `pub_keys/` directories
- **SSH config changes**: Modify `sed` commands in Dockerfiles or add new `echo` commands for additional options
