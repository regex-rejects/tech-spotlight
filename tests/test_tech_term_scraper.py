import pytest
import csv
from tech_spotlight.tech_term_search import open_text, open_terms, get_terms, write_data


@pytest.mark.skip("TODO")
def test_open_text_content_exists():
    read_file = './test-raw-data/sample_read.txt'
    text_content = open_text(read_file)
    assert text_content


@pytest.mark.skip("TODO")
def test_open_tech_terms_exists():
    terms_file = './datasets/tech_list.txt'
    tech_terms = open_terms(terms_file)
    assert tech_terms


@pytest.mark.skip("TODO")
def test_get_terms_data_list_exists():
    read_file = './test-raw-data/sample_read.txt'
    terms_file = './datasets/tech_list.txt'
    data_list = get_terms(read_file, terms_file)
    assert data_list


@pytest.mark.skip("TODO")
def test_write_data_content_exists():
    read_file = './test-raw-data/sample_read.txt'
    terms_file = './datasets/tech_list.txt'
    write_file = './test-raw-data/sample_write.csv'
    write_data(read_file, terms_file, write_file)
    file = open(write_file)
    written_content = csv.reader(file)
    assert written_content
    file.close()


# # @pytest.mark.skip("TODO")
# def test_written_data_contains_python():
#     read_file = './test-raw-data/sample_read.txt'
#     terms_file = './datasets/tech_list.txt'
#     write_file = './test-raw-data/sample_write.csv'
#     write_data(read_file, terms_file, write_file)
#     with open(write_file, )