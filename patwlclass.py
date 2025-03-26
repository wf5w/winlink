#!/usr/bin/env python

import subprocess
import platform

class PatWL:
    def __init__(self):
        self.executable = 'pat'
        if platform.system() == 'Windows':
            self.executable = 'pat.exe'
        self._mailbox_path()

    def _mailbox_path(self):
        result = subprocess.run([self.executable, 'env'], capture_output=True, text=True)
        output = result.stdout.strip().splitlines()
        
        self.mailbox_path= ''
        self.callsign = ''
        for i in enumerate(output):
            s = i[1]
            n = s.find("PAT_MYCALL")
            if n != -1:
                k, v = s[n:-1].split('=')
                self.callsign = v[1:]
            n = s.find("PAT_MAILBOX_PATH")
            if n != -1:
                k, v = s[n:-1].split('=')
                mbpath = v[1:]

        self.mailbox_path = mbpath + '/' + self.callsign

    def save(self, to, subject, message):
        recipients = []
        if to.find(';') != -1:
            recipients = to.split(';')
        elif to.find(',') != -1:
            recipients = to.split(',')
        else:
            recipients.append(to)

        for t in recipients:
            sendto = t.strip()
            self._save(sendto, subject, message)

    def _save(self, to, subject, message):
        command = [self.executable, 'compose', to, '-s', subject]
        #print(command)
        process = subprocess.Popen(command,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   text=True)

        stdout, stderr = process.communicate(input=message)
        #print(stdout)        
        #print(stderr)

if __name__ == '__main__':

    pwl = PatWL()
    print(pwl.mailbox_path)
    print(pwl.callsign)
    pwl.save('wf5w@arrl.net', "test message", "Hello\nthere\n")

