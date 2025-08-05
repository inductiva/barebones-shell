import sys
import runpy
import shlex
from pathlib import Path
from prompt_toolkit import PromptSession

import inductiva
import inductiva._cli as cli_pkg

# Command to build exe
# pyinstaller barebones_shell.py --name barebones_shell --icon=favicon.ico --additional-hooks-dir=. --onefile

def run_python_file(filepath: str, args: list[str]):
    """
    Runs a Python script with the provided arguments in a simulated __main__ environment.
    """
    original_argv = sys.argv
    try:
        sys.argv = [filepath] + args
        runpy.run_path(filepath, run_name="__main__")
    finally:
        sys.argv = original_argv


def run_inductiva_cli(args: list[str]):
    """
    Runs the Inductiva CLI with the provided arguments, handling SystemExit cleanly.
    """
    original_argv = sys.argv
    try:
        sys.argv = ["inductiva"] + args
        cli_pkg.main()
    except SystemExit as e:
        if e.code != 0:
            print(f"inductiva CLI exited with code {e.code}")
    except Exception as ex:
        print(f"Error running inductiva CLI: {ex}")
    finally:
        sys.argv = original_argv


def main():
    """
    Launches the interactive command loop for running Python files or Inductiva CLI commands.
    """
    print("Inductiva Runner. Type 'exit' or Ctrl+C to quit.")
    session = PromptSession()

    while True:
        try:
            command = session.prompt("> ").strip()
            if command.lower() in {"exit", "quit"}:
                break

            parts = shlex.split(command, posix=sys.platform != "win32")
            if not parts:
                continue

            cmd, *args = parts

            if cmd == "python" and args:
                file_to_run = Path(args[0])
                script_args = args[1:]

                if not file_to_run.is_file():
                    print(f"File not found: {file_to_run}")
                    continue

                print(f"Running {file_to_run}...")
                run_python_file(str(file_to_run), script_args)

            elif cmd == "inductiva":
                print(f"Running inductiva CLI: {' '.join(parts)}")
                run_inductiva_cli(args)

            else:
                print("Unknown command. Try:")
                print("  python script.py")
                print("  inductiva auth login")

        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
