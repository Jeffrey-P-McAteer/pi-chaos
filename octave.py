
import os
import sys
import subprocess

def main(args=sys.argv):
  octave_install_folder = os.path.join(os.path.dirname(__file__), 'octave-cache')
  os.makedirs(octave_install_folder, exist_ok=True)

  octave_install_folder_var = os.path.join(octave_install_folder, 'var')
  if not os.path.exists(octave_install_folder_var):
    subprocess.run([
      'ln', '-s', '/var', octave_install_folder
    ], check=True)

  octave_bin = os.path.join(octave_install_folder, 'usr', 'bin', 'octave')
  if not os.path.exists(octave_bin):
    subprocess.run([
      'sudo', 'pacman', '-r', octave_install_folder, '-S', 'octave'
    ], check=True)

  subp_env = dict(os.environ)

  sys_path_l = subp_env.get('PATH', '').split(os.pathsep)
  octave_root_path_l = [os.path.join(octave_install_folder, p.lstrip(os.sep) ) for p in sys_path_l]

  subp_env['PATH'] = os.pathsep.join(sys_path_l + octave_root_path_l)

  subp_cmd = [
    #octave_bin
    os.path.join(octave_install_folder, 'usr/lib/octave/9.1.0/exec/x86_64-pc-linux-gnu/octave-gui'),
  ] + args[1:]

  subp_env['LD_LIBRARY_PATH'] = os.environ.get('LD_LIBRARY_PATH', '')+os.pathsep+os.pathsep.join(sys_path_l + octave_root_path_l)

  print(f'> {" ".join(subp_cmd)}')

  # subp_env['LD_DEBUG'] = 'all'

  subprocess.run(subp_cmd, env=subp_env)


if __name__ == '__main__':
  main()
