import subprocess

profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

profiles_list = [i.split(':') for i in profiles if "All User Profiles" in i]

