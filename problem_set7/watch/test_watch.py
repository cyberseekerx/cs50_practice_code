from watch import parse


def test_link():
    assert (
        parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
        == "https://youtu.be/xvFZjo5PgG0"
    )
