import os
import fnmatch
from pathlib import Path
import subprocess

class ElasticModule:
    def __init__(self):
        # setup commands just in case
        os.system("git clone https://github.com/armysick/sliver")
        os.environ['PATH'] += os.pathsep + os.path.expanduser('~/go/bin')
        self.install_go_tools()
        
        # replaces
        self.ignore_list = {".git", ".github", "docs", "vendor"}
        self.rename_paths = True
        self.replace_pairs = [
            ("IfconfigReq", "PeppermintButler"),
            ("ImpersonateReq", "LumpySpacePrincess"),
            ("InvokeMigrateReq", "Gunter"),
            ("RevToSelfReq", "Marcelline"),
            ("ScreenshotReq", "JakeTheDoggy"),
            ("SideloadReq", "BeemoBoss"),
            ("InvokeSpawnDllReq", "PrincessFlame"),
            ("NetstatReq", "FinTheRomanian"),
            ("httpSessionInit", "PacoPartys"),
            ("screenshotRequested", "Esquilichi"),
            ("RegistryReadReq", "Forrof"),
            ("RequestResend", "Gioser"),
            ("GetPrivInfo", "Lurxeh"),
            ("-NoExit", "-nOExIt"),
            ("sliver", "golder"),
			("Sliver", "Golder"),
			("SLIVER", "GOLDER"),
			("beacon", "kraken"),
			("Beacon", "Kraken"),
			("BEACON", "KRAKEN"),
			("bishopfox", "esquilando"),
			("BishopFox", "EsquiLando")
        ]

    def name(self):
        return "Elastic"

    def install_go_tools(self):
        tools = [
            {
                'name': 'protoc-gen-go',
                'version': 'v1.31.0',
                'install_command': ['go', 'install', 'google.golang.org/protobuf/cmd/protoc-gen-go@v1.31.0'],
                'check_command': ['protoc-gen-go', '--version'],
            },
            {
                'name': 'protoc-gen-go-grpc',
                'version': 'v1.3.0',
                'install_command': ['go', 'install', 'google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.3.0'],
                'check_command': ['protoc-gen-go-grpc', '--version'],
            }
        ]
        for tool in tools:
            subprocess.run(tool['install_command'], check=True)

    def run(self, config):
        start_path = Path(config.run_dir) / "sliver"
        
        for search, replace in self.replace_pairs:
            try:
                self.search_and_replace(start_path, search, replace)
                self.search_and_rename_files(start_path, search, replace)
                self.search_and_rename_directories(start_path, search, replace)
            except Exception as e:
                print(f"[Elastic] Error during execution: {e}")

    def should_ignore(self, path):
        return any(ignored in path.parts for ignored in self.ignore_list)

    def search_and_replace(self, start_path, search, replace):
        print(f"Buscando '{search}' en {start_path}")
        for root, _, files in os.walk(start_path):
            if self.should_ignore(Path(root)):
                continue         
            for file in files:
                file_path = Path(root) / file
                if self.should_ignore(file_path):
                    continue    
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    if search in content:
                        new_content = content.replace(search, replace)
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        print(f"[+] Replacing '{search}' for '{replace}' in {file_path}")
                    else:
                       continue
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    def search_and_rename_files(self, start_path, search, replace):
        for root, _, files in os.walk(start_path):
            if self.should_ignore(Path(root)):
                continue
            
            for file in files:
                if search in file:
                    old_path = Path(root) / file
                    new_path = Path(root) / file.replace(search, replace)
                    os.rename(old_path, new_path)

    def search_and_rename_directories(self, start_path, search, replace):
        for root, dirs, _ in os.walk(start_path, topdown=False):
            for dir_name in dirs:
                if search in dir_name:
                    old_path = Path(root) / dir_name
                    new_path = Path(root) / dir_name.replace(search, replace)
                    os.rename(old_path, new_path)


class Builder:
    def __init__(self, config, verbose=False):
        self.config = config
        self.verbose = verbose

    def run_make(self):
        make_dir = os.path.join(self.config['RunDir'], 'sliver')
        if not os.path.exists(make_dir):
            raise FileNotFoundError(f"Make directory not found: {make_dir}")

        # First run 'make pb'
        cmd = ['make', 'pb']
        self._run_command(cmd, make_dir)

        # Then run 'make'
        cmd = ['make']
        self._run_command(cmd, make_dir)

    def _run_command(self, cmd, cwd):
        result = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            error_message = result.stderr.decode('utf-8')
            raise RuntimeError(f"Command failed with error: {error_message}")
        if self.verbose:
            print(result.stdout.decode('utf-8'))

if __name__ == "__main__":
    class Config:
        def __init__(self, run_dir):
            self.run_dir = run_dir
            
    current_dir = os.path.dirname(os.path.realpath(__file__))
    config = Config(current_dir) 
    module = ElasticModule()
    module.run(config)
    config = {'RunDir' : current_dir}
    builder = Builder(config, verbose=True)
    builder.run_make()
