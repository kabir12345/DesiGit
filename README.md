# Desigit

Desigit (Desi + Git) is a command-line tool that provides Hinglish (Hindi + English) aliases for git commands. It allows you to use familiar Hindi words to perform git operations.

## Installation

```bash
pip install desigit
```

## Usage

Instead of using `git`, you can use `desigit` with Hinglish commands:

```bash
# Initialize a repository
desigit ped

# Add files
desigit jodo .

# Check status
desigit haalat

# Commit changes
desigit zimma -m "Initial commit"

# Push to remote
desigit dhaka origin master

# Pull from remote
desigit kheech origin master

# Create a new branch
desigit tehni feature-branch

# Switch branches
desigit dekho main
```

## Command Reference

### Basic Commands
- `ped` - Initialize repository (git init)
- `haalat` - Check status (git status)
- `jodo` - Add files (git add)
- `zimma` - Commit changes (git commit)
- `dhaka` - Push changes (git push)
- `kheech` - Pull changes (git pull)

### Branch Operations
- `tehni` - Create/list branches (git branch)
- `dekho` - Checkout branch (git checkout)
- `milao` - Merge branches (git merge)
- `kuda` - Stash changes (git stash)

[Full command reference available in documentation]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.