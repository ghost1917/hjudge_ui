class HdfsDownloader(object):
    """Downloads files and dirs from hdfs
            :param local_dir name of local dir where data will be stored
            :type  local_dir: string
            :param remote_dir name of remote dir where data is stored now
            :type  remote_dir: string
            :param hdfs_urls: first webhdfs endpoint
            :type  hdfs_urls: list
    """
    def __init__(self, local_dir, remote_dir, hdfs_urls):
        self.client = self.build_client(hdfs_urls)
        self.local_dir = local_dir
        self.remote_dir = remote_dir
        if not os.path.exists(self.local_dir):
            os.makedirs(self.local_dir)

    def build_client(self, hdfs_urls, test_path='/user/hive/warehouse/'):
        """
        :param hdfs_urls: something like this `http://lga-grid106.contextweb.prod:50070`
        :type  hdfs_urls: list
        :param test_path: path to test, is endpoint active or not
        :type  test_path: string
        :return: hdfs_client
        """
        problem = True
        test_folder = test_path.rsplit('/', 1)[0]
        for hdfs_url in hdfs_urls:
            client = Client(hdfs_url)
            res = client.status(test_folder, strict=False)
            if res is not None:
                problem = False
                break
        if problem:
            raise ValueError("{} does not contain active hdfs node OR {} does not exist!".format(repr(hdfs_urls),
                                                                                                 test_folder))
        else:
            LOG.warn("{} is used as active node.".format(hdfs_url))
        return client

    def download(self, hdfs_path):
        LOG.info("Downloading {} into {}".format(hdfs_path, self.local_dir))
        return self.client.download(os.path.join(self.remote_dir, hdfs_path),
                                    os.path.join(self.local_dir,  hdfs_path),
                                    overwrite=True)


def download_from_hdfs(downloader, hdfs_path):
    """Download files and dirs from hdfs.
        :param downloader: hdfs file downloader
        :type  downloader: HdfsDownloader
        :param hdfs_path: file or directory to download to local
        :type  hdfs_path: string
        :return: local path of downloaded item
        :rtype: string
    """
    return downloader.download(hdfs_path)
