# !/usr/bin/env python
import os
import sys
import json
import toml
import click
import datetime
import subprocess
import pandas as pd
from pathlib import Path


def run_cmd(args_list):
        """
        run linux commands
        """
        # import subprocess
        print('Running system command: {0}'.format(' '.join(args_list)))
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_output, s_err = proc.communicate()
        s_return =  proc.returncode
        return s_return, s_output, s_err

@click.command()
@click.option('--hdfs_path', default=None, help='Input origin_hdfs_path for path rename')
def main(hdfs_path):
    current_ts = int(datetime.datetime.now().timestamp())
    origin_hdfs_path = hdfs_path
    check = hdfs_path.split("/")[-1].split("-")
    myenv = os.environ.copy()
    print("++++++++++++++++++++++")
    (ret, out, err)= run_cmd(['hdfs', 'dfs', '-ls', origin_hdfs_path])
    print(out.decode("utf-8"))
    print(err.decode("utf-8"))
    print("----------------------")
    sys.exit(1)
    if check[0] in ["train", "score", "download"] and type(int(check[1])) is int:
        hdfs_mv_cmd = f"hdfs dfs -mv {origin_hdfs_path} {origin_hdfs_path}_{current_ts}"
        print(hdfs_mv_cmd)
        r = subprocess.getstatusoutput(hdfs_mv_cmd)
        print(r)
    else:
        print(f"{hdfs_path} not allow to rename")

if __name__ == '__main__':
    main()
