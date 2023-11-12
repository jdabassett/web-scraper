import pytest
from scraper.scraper import get_citations_needed_report, get_citations_needed_count


# @pytest.mark.skip('TODO')
def test_report_function_exists():
    assert get_citations_needed_report

# @pytest.mark.skip('TODO')
def test_count_function_exists():
    assert get_citations_needed_count

# @pytest.mark.skip("TODO")
def test_count_return_0():
    int_count = get_citations_needed_count("https://en.wikipedia.org/wiki/Main_Page")
    assert int_count == 0

# @pytest.mark.skip("TODO")
def test_report_return_0():
    list_count = get_citations_needed_report("https://en.wikipedia.org/wiki/Main_Page")
    assert isinstance(list_count,list) and list_count==[]


# @pytest.mark.skip("TODO")
def test_count_return_1():
    int_count = get_citations_needed_count("https://en.wikipedia.org/wiki/Vodka")
    assert int_count == 1

# @pytest.mark.skip("TODO")
def test_report_return_1():
    list_count = get_citations_needed_report("https://en.wikipedia.org/wiki/Vodka")
    assert isinstance(list_count,list) and len(list_count)==1