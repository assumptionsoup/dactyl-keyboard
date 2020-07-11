import os
import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class PythonExecutorEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self._last_event_time = -1

    def on_modified(self, event):
        # Because of https://github.com/gorakhargosh/watchdog/issues/346
        # Add a small wait
        if time.time() - self._last_event_time < 0.01:
            return
        self._last_event_time = time.time()
        logging.info("Change detected in %s, reloading dactyl:", event.src_path)
        p = subprocess.Popen(
            '{} "{}"'.format(sys.executable, os.path.abspath('dactyl.py')),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        # Kinda annoying this blocks
        out, err = p.communicate()
        print(out.decode('ascii'))
        print(err.decode('ascii'))



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = PythonExecutorEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
