
import pytest
from common.session import session
from parsing.table import table


@pytest.fixture (scope='session')
def web_session(request):
    web_session = session()

    def closeSession():
        print ('Close browser session')
        web_session.close_web_driver()
    request.addfinalizer(closeSession)
    return web_session


def test_1_instance(web_session):

    t = table(web_session)

    print "List of middleware datasources: ", t.get_middleware_datasources_table(), "\n"
    print "List of middleware providers: ", t.get_middleware_providers_table(), "\n"
    print "List of middleware deployments: ", t.get_middleware_deployments_table(), "\n"

    servers_list = t.get_middleware_servers_table()
    print "Full servers list: ", servers_list, "\n"

    """

    # In case of 2 present entities:
        print "Feed 1: ", servers_list[0]["Feed"]
        print "Feed 2: ", servers_list[1]["Feed"]

    """


def test_multi_instances(web_session):

    print "List of middleware datasources: ", table(web_session).get_middleware_datasources_table(), "\n"
    print "List of middleware providers: ",   table(web_session).get_middleware_providers_table(), "\n"
    print "List of middleware deployments: ", table(web_session).get_middleware_deployments_table(), "\n"
    print "Middleware servers list: ",        table(web_session).get_middleware_servers_table(), "\n"

