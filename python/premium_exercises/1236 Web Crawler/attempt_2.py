class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        visited = set()
        visited.add(startUrl)
        stack = [startUrl]
        start_host_name = startUrl.split("//")[1].split("/")[0]

        while stack:
            current_url = stack.pop()
            url_list = htmlParser.getUrls(current_url)

            for url in url_list:
                new_host_name = url.split("//")[1].split("/")[0]
                if url not in visited and new_host_name == start_host_name:
                    visited.add(url)
                    stack.append(url)

        result_list = list(visited)
        return result_list
