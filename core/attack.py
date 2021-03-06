#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from core.alert import info
from core.alert import error
from core.alert import messages


def start_attack(target, num, total, scan_method, users, passwds, timeout_sec, thread_number, ports, log_in_file,
                 time_sleep, language, verbose_level, show_version, check_update, socks_proxy, retries, ping_flag, methods_args):
    info(messages(language, 45).format(str(target), str(num), str(total)))
    # Calling Engines
    # BruteForce Engines
    if scan_method[-6:] == '_brute':
        try:
            start = getattr(
                __import__('lib.brute.%s.engine' % (scan_method.rsplit('_brute')[0]),
                           fromlist=['start']),
                'start')
        except:
            error(messages(language, 46).format(scan_method))
            from core.color import finish
            finish()
            sys.exit(1)
        start(target, users, passwds, ports, timeout_sec, thread_number, num, total, log_in_file, time_sleep, language,
              verbose_level, show_version, check_update, socks_proxy, retries, ping_flag, methods_args)
    # Scanners Engines
    if scan_method[-5:] == '_scan':
        try:
            start = getattr(
                __import__('lib.scan.%s.engine' % (scan_method.rsplit('_scan')[0]),
                           fromlist=['start']),
                'start')
        except:
            error(messages(language, 46).format(scan_method))
            from core.color import finish
            finish()
            sys.exit(1)
        start(target, users, passwds, ports, timeout_sec, thread_number, num, total, log_in_file, time_sleep, language,
              verbose_level, show_version, check_update, socks_proxy, retries, ping_flag, methods_args)
