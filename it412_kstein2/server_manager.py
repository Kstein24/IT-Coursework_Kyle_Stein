# Kyle Stein 
# Walsh College
# IT 412
# 1/22/2026
# Week 2 & 3 Files And Exceptions

"""
Server configuration manager.

Stores multiple server configurations as a list of dictionaries
in server_configs.json and handles backups automatically.
"""

from pathlib import Path
from typing import Dict, List

from functions.cli import prompt_choice, prompt_nonempty, prompt_yes_no, print_header
from functions.json_store import load_json, save_json


class ServerManager:
    """
    Encapsulates all server configuration logic.
    """

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.server_configs_path = base_dir / "server_configs.json"
        self.servers: List[Dict[str, str]] = self.load_servers()

    def load_servers(self) -> List[Dict[str, str]]:
        """
        Load server configurations from disk.
        """
        data = load_json(self.server_configs_path, default=[])
        return [dict(item) for item in data if isinstance(item, dict)]

    def has_servers(self) -> bool:
        """
        Return True if at least one server exists.
        """
        return bool(self.servers)

    def save_servers(self) -> None:
        """
        Save server configurations and back up the file.
        """
        save_json(self.server_configs_path, self.servers, make_backup_on_overwrite=True)

    def add_server(self, primary: Dict[str, str]) -> None:
        """
        Add a new server using the primary configuration as a base.
        """
        print_header("Add New Server")

        server = dict(primary)
        server["Server Name"] = prompt_nonempty("Server name: ")

        if prompt_yes_no("Modify values for this server?"):
            for key in list(server.keys()):
                if prompt_yes_no(f"Change '{key}'?"):
                    server[key] = prompt_nonempty("New value: ")

        self.servers.append(server)
        self.save_servers()

    def modify_server(self) -> None:
        """
        Modify a single key/value in an existing server.
        """
        if not self.servers:
            return

        for i, server in enumerate(self.servers, 1):
            print(f"{i}. {server.get('Server Name', 'Unnamed')}")

        idx = int(prompt_choice("Choose server: ",
                                [str(i) for i in range(1, len(self.servers) + 1)])) - 1

        key = prompt_nonempty("Key to modify: ")
        if key in self.servers[idx]:
            self.servers[idx][key] = prompt_nonempty("New value: ")

    def delete_server(self) -> None:
        """
        Delete a server and all associated data.
        """
        for i, server in enumerate(self.servers, 1):
            print(f"{i}. {server.get('Server Name', 'Unnamed')}")

        idx = int(prompt_choice("Choose server: ",
                                [str(i) for i in range(1, len(self.servers) + 1)])) - 1

        if prompt_yes_no("Confirm delete?"):
            del self.servers[idx]
