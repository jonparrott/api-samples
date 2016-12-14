import os

import search


search.DEVELOPER_KEY = os.environ['DEVELOPER_KEY']


def test_youtube_search(capsys):
    search.youtube_search('Google', 25)

    out, _ = capsys.readouterr()

    assert 'Google' in out
