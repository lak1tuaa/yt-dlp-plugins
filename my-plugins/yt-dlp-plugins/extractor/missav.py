# coding: utf-8
from __future__ import unicode_literals

from yt_dlp.extractor.common import InfoExtractor


class MissAVIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?missav\.ws/.*/.*/(?P<id>[\w-]+)'
    _TEST = {
        'url': 'https://missav.ws/dm28/en/mvsd-232-uncensored-leak',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': '42',
            'ext': 'mp4',
            'title': 'MVSD-232 De S and de M hedonist, Emma Kisaki is back! Breast Milk Injection Semen Cum Swallowing Thick Double Hole Fisting play Making Continuous Creampie Fuck! ! NozomiSaki Emma - Nozomi Saki Emma (Haruki, Haruki Kato)',
            'thumbnail': r're:^https?://.*\.jpg$',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')

        return {
            'id': video_id,
            'title': title,
            'description': self._og_search_description(webpage),
            'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see youtube_dl/extractor/common.py)
        }