import sys
import click
from typing import List, Optional
from .commands import GitCommands, USAGE_EXAMPLES, COMMAND_CATEGORIES
from .utils import (
    execute_git_command,
    get_similar_commands,
    format_output,
    print_command_help,
    print_version
)

def print_categories():
    """Print all available command categories and their commands."""
    click.echo("\nAvailable Command Categories:")
    for category, commands in COMMAND_CATEGORIES.items():
        click.echo(f"\n{category}:")
        for cmd in commands:
            git_cmd = GitCommands.get_git_command(cmd)
            click.echo(f"  {cmd:<15} -> git {git_cmd}")

def print_examples():
    """Print usage examples."""
    click.echo("\nCommon Usage Examples:")
    for description, example in USAGE_EXAMPLES.items():
        click.echo(f"  {description.replace('_', ' ').title():<20} : {example}")

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--version', is_flag=True, help='Show version information.')
@click.option('--list', 'list_commands', is_flag=True, help='List all available commands.')
@click.option('--examples', is_flag=True, help='Show usage examples.')
def cli(ctx, version: bool, list_commands: bool, examples: bool):
    """
    Desigit - Git with Hinglish commands
    
    Use Hindi-English (Hinglish) words to run git commands.
    """
    if version:
        print_version()
        sys.exit(0)
    
    if list_commands:
        print_categories()
        sys.exit(0)
        
    if examples:
        print_examples()
        sys.exit(0)
        
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        sys.exit(0)

@cli.command(context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.argument('args', nargs=-1)
@click.option('--help', '-h', is_flag=True, help='Show help for a command.')
def run(args: tuple, help: bool):
    """Execute a git command using Hinglish aliases."""
    if not args:
        click.echo("Usage: desigit <command> [options]")
        return

    command = args[0]
    
    # Show help for specific command
    if help:
        print_command_help(command)
        return

    if GitCommands.is_valid_command(command):
        git_command = [GitCommands.get_git_command(command)] + list(args[1:])
        returncode, stdout, stderr = execute_git_command(git_command)
        
        if stdout:
            click.echo(format_output(stdout), nl=False)
        if stderr:
            click.echo(format_output(stderr, error=True), nl=False, err=True)
        
        sys.exit(returncode)
    else:
        # Show similar commands if the command is not found
        similar = get_similar_commands(command)
        click.echo(f"Unknown command: {command}", err=True)
        if similar:
            click.echo("\nDid you mean one of these?", err=True)
            for cmd in similar:
                click.echo(f"  {cmd} (git {GitCommands.get_git_command(cmd)})", err=True)
        click.echo("\nUse --list to see all available commands.", err=True)
        sys.exit(1)

def main():
    """Main entry point for the CLI."""
    try:
        cli(prog_name='desigit')
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()