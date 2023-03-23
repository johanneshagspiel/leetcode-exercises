class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        def rec_crawl(url, htmlParser, url_set, host_name):

            url_list = htmlParser.getUrls(url)
            for new_url in url_list:
                new_host_name = new_url.split("//")[1].split("/")[0]
                if new_url not in url_set and host_name == new_host_name:
                    url_set.add(new_url)
                    url_set = rec_crawl(new_url, htmlParser, url_set, host_name)

            return url_set

        host_name = startUrl.split("//")[1].split("/")[0]
        url_set = set()
        url_set.add(startUrl)
        result_url_set = rec_crawl(startUrl, htmlParser, url_set, host_name)
        result_list = list(result_url_set)
        return result_list
