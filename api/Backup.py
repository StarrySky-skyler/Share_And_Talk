"""
=================================================
@Project -> File    ：Share_And_Talk -> Backup.py
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 9:32
@用途               ：备份数据库
@email              ：65846869+Skyler-Sun@users.noreply.github.com
==================================================
"""
import subprocess
from time import strftime

import pysnooper
from pathlib import Path
from ShareAndTalk.settings import BASE_DIR


class Backuper:
    def __backupDB(self):
        """Backup share and talk database"""
        # Export database as backup.json
        date = strftime('%Y%m%d_%H%M%S')
        filePath = Path(BASE_DIR) / f'backup/backup_{date}.json'
        args = ['py', '-Xutf8', 'manage.py', 'dumpdata', '-o',
                filePath.absolute().resolve()]
        # py -Xutf8 manage.py dumpdata -o backup_2023_06_06.json
        subprocess.check_call(args, creationflags=subprocess.CREATE_NO_WINDOW)

    @pysnooper.snoop('info.log')
    def backup(self):
        """Main backup function"""
        try:
            self.__backupDB()
            return 'ok'
        except Exception as e:
            return str(e)
