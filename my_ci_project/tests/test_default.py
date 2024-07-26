def test_foo(host):
    file = host.file('/etc/foo.conf')
    assert file.exists
    assert file.contains("bar")
