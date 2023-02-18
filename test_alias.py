from openalea.core.pkgmanager import PackageManager

def test_catalog():
    """test_catalog: test init catalog in PackageManager"""
    pkgman = PackageManager()
    pkgman.init(verbose=False)
    assert (pkgman["catalog.data"]["int"] ==
        pkgman["openalea.data structure"]["int"])


