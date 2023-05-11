def test_init_db_command(cli_runner, monkeypatch):
    class Recorder:
        called = False

    def fake_init_db():
        Recorder.called = True

    init_db_path = 'virtual_bookshelf.extensions.database.init_db'
    monkeypatch.setattr(init_db_path, fake_init_db)
    result = cli_runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
