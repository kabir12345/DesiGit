from typing import Dict, List

class GitCommands:
    """
    A class containing all git commands and their Hinglish equivalents.
    Also provides helper methods for command lookup and validation.
    """
    
    COMMANDS: Dict[str, str] = {
        # Basic Commands
        'van': 'git',
        
        # Setup and Config
        'setting': 'config',
        'madad': 'help',
        'kharabi': 'bugreport',
        'vishwas': 'credential-helper',
        
        # Getting and Creating Projects
        'ped': 'init',
        'nakal': 'clone',
        
        # Basic Snapshotting
        'jodo': 'add',
        'haalat': 'status',
        'farak': 'diff',
        'zimma': 'commit',
        'tippani': 'notes',
        'wapas': 'restore',
        'reset': 'reset',
        'hatao': 'rm',
        'khisko': 'mv',
        
        # Branching and Merging
        'tehni': 'branch',
        'dekho': 'checkout',
        'badlo': 'switch',
        'milao': 'merge',
        'milap-yantra': 'mergetool',
        'dekhrek': 'log',
        'kuda': 'stash',
        'nishani': 'tag',
        'kaam-ped': 'worktree',
        
        # Sharing and Updating Projects
        'lao': 'fetch',
        'kheech': 'pull',
        'dhaka': 'push',
        'door': 'remote',
        'upshakha': 'submodule',
        
        # Inspection and Comparison
        'dikhao': 'show',
        'farak-yantra': 'difftool',
        'seema-farak': 'range-diff',
        'kitna': 'shortlog',
        'batao': 'describe',
        
        # Patching
        'lagao': 'apply',
        'chun-lo': 'cherry-pick',
        'nayi-neev': 'rebase',
        'ultao': 'revert',
        
        # Debugging
        'do-tukda': 'bisect',
        'dosh': 'blame',
        'khojo': 'grep',
        
        # Email
        'daakiya': 'am',
        'prarup': 'format-patch',
        'bhejo': 'send-email',
        'maang': 'request-pull',
        
        # External Systems
        'svn': 'svn',
        'jaldi-ghusao': 'fast-import',
        
        # Administration
        'saaf': 'clean',
        'raddi': 'gc',
        'jaanch': 'fsck',
        'ref-log': 'reflog',
        'chhanno': 'filter-branch',
        'web-dikho': 'instaweb',
        'sanrakshan': 'archive',
        'gathri': 'bundle',
        
        # Server Admin
        'sewak': 'daemon',
        'server-update': 'update-server-info',
        
        # Plumbing Commands
        'file-dekho': 'cat-file',
        'ignore-jaanch': 'check-ignore',
        'checkout-suchi': 'checkout-index',
        'zimma-ped': 'commit-tree',
        'ginti': 'count-objects',
        'farak-suchi': 'diff-index',
        'har-ek-ke-liye': 'for-each-ref',
        'hash-cheez': 'hash-object',
        'file-suchi': 'ls-files',
        'ped-suchi': 'ls-tree',
        'milao-adhaar': 'merge-base',
        'ped-padho': 'read-tree',
        'rev-suchi': 'rev-list',
        'rev-samjho': 'rev-parse',
        'dikho-ref': 'show-ref',
        'sanket-ref': 'symbolic-ref',
        'suchi-update': 'update-index',
        'ref-update': 'update-ref',
        'pack-jaanch': 'verify-pack',
        'ped-likho': 'write-tree',
        
        # Common Combined Commands
        'abhi-jodo': 'add .',
        'sab-saaf': 'clean -fd',
        'branch-saaf': 'remote prune origin',
        'nayi-tehni': 'checkout -b',
        'vapas-jao': 'checkout -',
        'stash-lagao': 'stash apply',
        'zimma-vapas': 'commit --amend',
        'setting-dekho': 'config --list',
        'door-dekho': 'remote -v',
    }

    # Reverse mapping for validation
    REVERSE_COMMANDS = {v: k for k, v in COMMANDS.items()}

    @classmethod
    def get_git_command(cls, hinglish_command: str) -> str:
        """
        Get the git command for a given Hinglish command.
        
        Args:
            hinglish_command (str): The Hinglish version of the command
            
        Returns:
            str: The corresponding git command or the original if not found
        """
        return cls.COMMANDS.get(hinglish_command, hinglish_command)

    @classmethod
    def get_hinglish_command(cls, git_command: str) -> str:
        """
        Get the Hinglish command for a given git command.
        
        Args:
            git_command (str): The original git command
            
        Returns:
            str: The corresponding Hinglish command or the original if not found
        """
        return cls.REVERSE_COMMANDS.get(git_command, git_command)

    @classmethod
    def is_valid_command(cls, command: str) -> bool:
        """
        Check if a given command is a valid Hinglish command.
        
        Args:
            command (str): The command to validate
            
        Returns:
            bool: True if the command exists in the mapping
        """
        return command in cls.COMMANDS

    @classmethod
    def get_command_category(cls, command: str) -> str:
        """
        Get the category of a command based on its functionality.
        
        Args:
            command (str): The Hinglish command
            
        Returns:
            str: The category of the command
        """
        categories = {
            'setup': ['setting', 'madad', 'kharabi', 'vishwas'],
            'create': ['ped', 'nakal'],
            'snapshot': ['jodo', 'haalat', 'farak', 'zimma', 'tippani', 'wapas', 'reset', 'hatao', 'khisko'],
            'branch': ['tehni', 'dekho', 'badlo', 'milao', 'kuda', 'nishani'],
            'remote': ['lao', 'kheech', 'dhaka', 'door', 'upshakha'],
            'inspect': ['dikhao', 'dekhrek', 'kitna', 'batao'],
            'patch': ['lagao', 'chun-lo', 'nayi-neev', 'ultao'],
            'debug': ['do-tukda', 'dosh', 'khojo'],
            'admin': ['saaf', 'raddi', 'jaanch', 'ref-log', 'sanrakshan', 'gathri'],
            'plumbing': ['file-dekho', 'ginti', 'hash-cheez', 'file-suchi', 'ped-suchi']
        }
        
        for category, commands in categories.items():
            if command in commands:
                return category
        return 'other'

    @classmethod
    def get_command_help(cls, command: str) -> str:
        """
        Get help text for a specific command.
        
        Args:
            command (str): The Hinglish command
            
        Returns:
            str: Help text explaining the command's usage
        """
        help_text = {
            'ped': 'Initialize a new git repository (git init)',
            'jodo': 'Add file contents to the index (git add)',
            'haalat': 'Show the working tree status (git status)',
            'zimma': 'Record changes to the repository (git commit)',
            'dhaka': 'Update remote refs along with associated objects (git push)',
            'kheech': 'Fetch from and integrate with another repository or local branch (git pull)',
            'tehni': 'List, create, or delete branches (git branch)',
            'dekho': 'Switch branches or restore working tree files (git checkout)',
            'milao': 'Join two or more development histories together (git merge)',
            'kuda': 'Stash the changes in a dirty working directory away (git stash)',
            # Add more help text for other commands as needed
        }
        return help_text.get(command, f'No help available for {command}')

    @classmethod
    def list_all_commands(cls) -> List[Dict[str, str]]:
        """
        Get a list of all commands with their git equivalents.
        
        Returns:
            List[Dict[str, str]]: List of dictionaries containing command mappings
        """
        return [{'hinglish': k, 'git': v} for k, v in cls.COMMANDS.items()]

# Example usage strings for common operations
USAGE_EXAMPLES = {
    'initialize': 'desigit ped',
    'add_files': 'desigit jodo .',
    'commit': 'desigit zimma -m "your message"',
    'push': 'desigit dhaka origin master',
    'pull': 'desigit kheech origin master',
    'new_branch': 'desigit tehni feature-branch',
    'checkout': 'desigit dekho branch-name',
    'status': 'desigit haalat',
}

# Command categories for help organization
COMMAND_CATEGORIES = {
    'Basic Commands': ['ped', 'jodo', 'haalat', 'zimma', 'dhaka', 'kheech'],
    'Branch Operations': ['tehni', 'dekho', 'milao', 'kuda'],
    'Inspection': ['dikhao', 'dekhrek', 'farak', 'kitna'],
    'Advanced': ['nayi-neev', 'chun-lo', 'ultao', 'do-tukda'],
}