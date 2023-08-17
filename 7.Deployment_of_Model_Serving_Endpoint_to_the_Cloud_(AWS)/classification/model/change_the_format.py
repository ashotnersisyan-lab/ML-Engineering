import tarfile

with tarfile.open('pipeline.tar.gz', 'w:gz') as tar:
    tar.add('pipeline.pkl')
