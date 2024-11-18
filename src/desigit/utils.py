import os
import subprocess
from typing import List, Tuple, Optional
import click
from difflib import get_close_matches
from .commands import GitCommands

def execute_git_command(command: List[str]) -> Tuple[int, str, str]:
    """
    Execute a git command and return the result.
    
    Args:
        command: List of command arguments
        
    Returns:
        Tuple of (return_code, stdout, stderr)
    """
    try:
        process = subprocess.Popen(
            ['git'] + command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            cwd=os.getcwd()
        )
        stdout, stderr = process.communicate()
        return process.returncode, stdout, stderr
    except FileNotFoundError:
        return 1, '', 'Error: Git is not installed or not in PATH'
    except Exception as e:
        return 1, '', str(e)

def format_output(text: str, error: bool = False) -> str:
    """
    Format command output with colors.
    
    Args:
        text: Text to format
        error: Whether this is error output
        
    Returns:
        Formatted text
    """
    if error:
        # Color error messages in red
        return click.style(text, fg='red')
    
    # Add colors to specific git output patterns
    lines = []
    for line in text.splitlines(True):  # Keep line endings
        if line.startswith('+'):
            line = click.style(line, fg='green')
        elif line.startswith('-'):
            line = click.style(line, fg='red')
        elif line.startswith('modified:'):
            line = click.style(line, fg='yellow')
        elif 'branch' in line.lower():
            line = click.style(line, fg='bright_blue')
        lines.append(line)
    
    return ''.join(lines)

def get_similar_commands(command: str, max_suggestions: int = 3) -> List[str]:
    """
    Get similar commands for typo suggestions.
    
    Args:
        command: The mistyped command
        max_suggestions: Maximum number of suggestions to return
        
    Returns:
        List of similar command suggestions
    """
    all_commands = list(GitCommands.COMMANDS.keys())
    return get_close_matches(command, all_commands, n=max_suggestions, cutoff=0.6)

def print_command_help(command: str):
    """
    Print help information for a specific command.
    
    Args:
        command: The command to show help for
    """
    if GitCommands.is_valid_command(command):
        git_cmd = GitCommands.get_git_command(command)
        help_text = GitCommands.get_command_help(command)
        category = GitCommands.get_command_category(command)
        
        click.echo(f"\n{click.style(command, fg='green')} ({click.style(f'git {git_cmd}', fg='yellow')})")
        click.echo(f"Category: {click.style(category, fg='blue')}")
        click.echo(f"\n{help_text}")
        
        # Show examples if available
        if command in USAGE_EXAMPLES:
            click.echo(f"\nExample: {USAGE_EXAMPLES[command]}")
    else:
        click.echo(f"No help available for unknown command: {command}", err=True)

def print_version():
    """Print version information."""
    import pkg_resources
    try:
        version = pkg_resources.get_distribution('desigit').version
        click.echo(f"desigit version {version}")
        
        # Get git version
        returncode, stdout, stderr = execute_git_command(['--version'])
        if returncode == 0:
            click.echo(stdout.strip())
    except Exception:
        click.echo("desigit version unknown")

def is_git_repository() -> bool:
    """
    Check if the current directory is a git repository.
    
    Returns:
        bool: True if current directory is a git repository
    """
    returncode, _, _ = execute_git_command(['rev-parse', '--git-dir'])
    return returncode == 0

def get_current_branch() -> Optional[str]:
    """
    Get the name of the current git branch.
    
    Returns:
        str: Current branch name or None if not in a git repository
    """
    if not is_git_repository():
        return None
        
    returncode, stdout, stderr = execute_git_command(['branch', '--show-current'])
    if returncode == 0 and stdout:
        return stdout.strip()
    return None