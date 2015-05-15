import shutil
import glob
import os.path
import botocore.session

session = botocore.session.Session(session_vars={'profile': (None, None, 'tsid-test')})
s3 = session.create_client('s3', region_name='eu-west-1')
archive = open('dist/extract_script-0.1.tar.gz', 'rb')
s3.create_bucket(Bucket='extract_script')
s3.put_object(Bucket='extract_script', ACL='public-read', Key='app.tar.gz', Body=archive)
