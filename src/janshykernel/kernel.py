#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
from pexpect import replwrap

notallowed = ["(quit)", "(exit)"]

hywrapper = replwrap.REPLWrapper("hy", "=> ", None, continuation_prompt="... ")

class janshykernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.11.0'
    language = 'hy'
    language_version = '1.0a4'
    language_info = {
        'name': 'hy',
        'mimetype': 'application/hy',
        'file_extension': '.hy',
    }
    banner = "Hy Kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            if code in notallowed:
                solution = f'"{code}" is not allowed in the hy kernel'
            else:
                code = code.replace("\n", " ")
                try:
                    solution = hywrapper.run_command(code)
                except:
                    solution = "The command was incomplete!"
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }