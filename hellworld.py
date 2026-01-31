import subprocess
import time
import sys

def get_cpu_temp_line():
    try:
        output = subprocess.check_output(['sensors']).decode()
        for line in output.split('\n'):
            if 'Package id 0:' in line or 'Tdie:' in line or 'Core 0:' in line:
                return line.strip()
        return "CPU temperature not found"
    except Exception as e:
        return f"Could not read CPU temperature: {e}"

def main():
    print("Live CPU Temperature (press Ctrl+C to stop):")
    print("test git")
    print("test git to revert please delete this")
    
    try:
        while True:
            temp_line = get_cpu_temp_line()
            sys.stdout.write('\r' + temp_line + ' ' * 20)
            sys.stdout.flush()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()